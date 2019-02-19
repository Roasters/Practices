"""
=========================================
Dept. of Spanish Language and Literature
2012130730 Shim Jaeheon
LB&C Assignment #4
========================================
"""

import os, re
from collections import Counter as Cnt

def files(folder, fileName):
    fileList = os.listdir('./%s'%folder)
    outList = []
    for file in fileList:
        if fileName in file:
            outList.append(os.path.join(os.getcwd(), folder, file))
    return outList
#fileList = [os.path.join(os.getcwd(), folder, i for i) in os.listdir() if fileName in i)]

def tolower(s):
    tmp = []
    for i in s.split():
        i = i.split('/')
        i[0] = i[0].lower()
        tmp.append('/'.join(i))
    return ' '.join(tmp)

def alignment20_5(s):
    tmp = []
    for i in s.split():
        i = i.split('/')
        tmp.append('{:<20}{:>5}'.format(i[0], i[1]))
    return '\n'.join(tmp)

def intersect(folder, fileName, POS, outfile, fs):
    textList = []
    for file in files(folder, fileName):
        if file.endswith('.txt'):
            textList.append(open(file, 'r').read())
    for f in fs:
        textList[0] = f(textList[0])
        textList[1] = f(textList[1])

    wordList = []
    for text in textList:
        wordList.append(re.findall('.+?%s'%POS, text))

    # Using set intersection would be better

    tmpList = list(set(wordList[0])) + list(set(wordList[1]))
    wordCnt = list(Cnt(tmpList).most_common())
    wordCnt.sort()

    outfileW = open(outfile, 'w')
    for word in wordCnt:
        if word[1] == 2:
            outfileW.write(word[0]+'\n')
    outfileW.close()
