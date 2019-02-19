def extractWord(s):
    word_list = []
    for word in s.split():
        if len(word) >= 3:
            word_list.append(word)
    return word_list            

def makeTitle(s):
    return s.title()

def makeTitle2(s):
    out = []
    for word in s.split():
        out.append(word.capitalize())
    return ' '.join(out)

def initial(s):
    out = ''
    for word in s.split():
        out += word[0].upper()
    return out                  