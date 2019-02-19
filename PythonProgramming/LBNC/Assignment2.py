"""
=========================================
Dept. of Spanish Language and Literature
2012130730 Shim Jaeheon
LB&C Assignment #2
========================================
"""

s = 'I love you'

# 1

wordList = s.split()
wordList.reverse()
print(' '.join(wordList))

# 2

out = []
for word in s.split():
    strList = list(word)
    strList.reverse()
    out.append(''.join(strList))
print(' '.join(out))

# 3

out = []
for word in s.split():
    strList = list(word)
    strList.reverse()
    out.append(''.join(strList))
out.reverse()    
print(' '.join(out))

# 4

strList = s.split()
tmp = strList[:]
strList.reverse()
strList = tmp + strList
print(' '.join(strList))

# 5

out = []
for word in s.split():
    for _ in range(s.split().index(word)+1):
        out.append(word)
print(' '.join(out))

# 6

out = []
wordList = s.split()
while wordList != []:
    out.append(wordList.pop())
print(' '.join(out))    

# 7

out = []
wordList = s.split()
while wordList != []:
    strList = list(wordList.pop(0))
    strList.reverse()
    out.append(''.join(strList))
print(' '.join(out))

# 8 

out = []
wordList = s.split()
while wordList != []:
    strList = list(wordList.pop())
    strList.reverse()
    out.append(''.join(strList))
print(' '.join(out))     