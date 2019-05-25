def gender_features(word):
    return {"last_letter": word[-1]}

def gender_features2(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

def gender_features3(word):
    return {"suffix1" : word[-1:],
            "suffix2" : word[-2:]}

from nltk.corpus import names
labeled_names = ([(name, "male") for name in names.words("male.txt")] + [(name, "female")
    for name in names.words("female.txt")])
import random
random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender) for n, gender in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
# in more compact version
from nltk.classify import apply_features
train_set = apply_features(gender_features, labeled_names[500:])
test_set = apply_features(gender_features, labeled_names[:500])

classifier = nltk.NaiveBayesClassifier.train(train_set)

# classifier methods
classifier.classify(gender_features)

# to test the classifier
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)

train_names = labeled_names[1500:]
devtest_names = labeled_names[500:1500]
test_names = labeled_names[:500]

train_set = [(gender_features(n), gender) for n, gender in train_names]
devtest_set = [(gender_features(n), gender) for n, gender in devtest_names]
test_set = [(gender_features(n), gender) for n, gender in test_names]

classifer = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, devtest_set))

# examine error cases
errors = []
for (feature, gender), (name, _) in zip(devtest_set, devtest_names):
    pred = classifier.classify(feature)
    if pred != gender:
        print("correct : {:<8} | guess : {:<8} | name : {:<30}".format(gender, pred, name))

from nltk.corpus import movie_reviews

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features["contains({})".format(word)] = (word in document_words)
    return features

documents = [(doc, tag) for tag in movie_reviews.categories() for doc in movie_reviews.words(categories=tag)]
featuresets = [(document_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

from nltk.corpus import brown
suffix_fdist = nltk.FreqDist()
for word in brown.words():
    if word.isalnum():
        word = word.lower()
        suffix_fdist[word[-1:]] += 1
        suffix_fdist[word[-2:]] += 1
        suffix_fdist[word[-3:]] += 1
common_suffixes = [suffix for suffix, count in suffix_fdist.most_common(100)]

def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features["endswith({})".format(suffix)] = word.lower().endswith(suffix)
    return features

tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n), g) for (n, g) in tagged_words if n.isalnum()]

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]

classifier = nltk.DecisionTreeClassifier.train(train_set)
nltk.classify.accuracy(classifier, test_set)

# including contextual information
def pos_features(sentence, i):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}

    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
    return features

tagged_sents = brown.tagged_sents(categories='news')
featuresets = []
for tagged_sent in tagged_sents:
    untagged_sent = nltk.tag.untag(tagged_sent)
    for i, (word, tag) in enumerate(tagged_sent):
        featuresets.append((pos_features(untagged_sent, i), tag))

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)

# including context of tag
def pos_features(sentence, i, history):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}

    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-tag"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
        features["prev_tag"] = history[i-1]
    return features

class ConsecutivePosTagger(nltk.TaggerI):
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = pos_features(untagged_sent, i, history)
                train_set.append((featureset, tag))
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = pos_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

tagged_sents = brown.tagged_sents(categories='news')
size = int(len(tagged_sents) * 0.1)
train_sents, test_sents = tagged_sents[size:] , tagged_sents[:size]
tagger = ConsecutivePosTagger(train_sents)
print(tagger.evaluate(test_sents))

sents = nltk.corpus.treebank_raw.sents()
tokens = []
boundaries = set()
offset = 0
for sent in sents:
    tokens.extend(sent)
    offset += len(sent)
    boundaries.add(offset-1)

def punct_features(tokens, i):
    return {'next-word-capitalized' : tokens[i+1][0].isupper(),
            'prev-word' : tokens[i-1].lower(),
            'punct' : tokens[i],
            'prev-word-is-one-char' : len(tokens[i-1]) == 1}

featuresets = [(punct_features(tokens, i), (i in boundaries))
                for i in range(1, len(tokens)-1)
                if tokens[i] in '.?!']

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)
nltk.classify.accuracy(classifier, test_set)

def segment_sentence(words):
    start = 0
    sents = []
    for i, word in enumerate(words):
        if word in ".?!" and classifier.classify(punct_features(words, i)) == True:
            print(i, word)
            sents.append(words[start:i+1])
            start = i + 1
    if start < len(words):
        sents.append(words[start:])
    return sents


posts = nltk.corpus.nps_chat.xml_posts()[:10000]

def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features["contains({})".format(word.lower())] = True
    return features

featuresets = [(dialogue_act_features(post.text), post.get('class'))
                for post in posts]

def rte_features(rtepair):
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    features['word_overlap'] = len(extractor.overlap('word'))
    features['word_hyp_extra'] = len(extractor.hyp_extra('word'))
    features['ne_overlap'] = len(extractor.overlap('word'))
    features['ne_hyp_extra'] = len(extractor.hyp_extra('ne'))
    return features

rtepair = nltk.corpus.rte.pairs(['rte3_dev.xml'])[33]

def tag_list(tagged_sents):
    return [tag for sent in tagged_sents for (word, tag) in sent]

def apply_tagger(tagger, corpus):
    return [tagger.tag(nltk.tag.untag(sent)) for sent in corpus]

tagged_sents = brown.tagged_sents(categories='fiction')
t0 = nltk.DefaultTagger("NN")
t1 = nltk.UnigramTagger(tagged_sents, backoff=t0)
t2 = nltk.BigramTagger(tagged_sents, backoff=t1)
gold = tag_list(brown.tagged_sents(categories='editorial'))
test = tag_list(apply_tagger(t2, brown.tagged_sents(categories='editorial')))
cm = nltk.ConfusionMatrix(gold, test)
print(cm.pretty_format(sort_by_count=True, show_percents=True, truncate=10))

import math
def entropy(labels):
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in freqdist]
    return -sum(p * math.log(p, 2) for p in probs)