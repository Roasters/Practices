# Exercise 1 - 1

s = 'i like programming and i like swimming'

for word in s.split():
    print(word, s.split().count(word))

out = {}
for word in s.split():
    if word not in out:
        out[word] = s.split().count(word)

# 1 - 2

for letter in s:
    print(letter, s.count(letter))

# 1 - 3 

wordList = s.split()
wordList.sort()
print(' '.join(wordList))   

# 1 - 4

letterList = list(s)
letterList.sort()
print(''.join(letterList))

# 2 - 1

a = [['one', 1], ['two', 2], ['three', 3]]
b = []
c = []

for i, j in a:
    b.append(i)
    c.append(j)

i = 0
b = a[:]
c = a[:]
while i != len(a):
    b[i] = a[i][0]
    c[i] = a[i][1]
    i += 1

# 2 - 2

b = ['one', 'two', 'three']; c = [1, 2, 3] 
a = b[:] 
for i in range(len(b)):
    a[i] = [b[i], c[i]]

for x in b:
    Idx = b.index(x)
    d.append([x, c[Idx]])    

i = 0
while i != len(b):
    d[i] = [b[i], c[i]]
    i += 1

while b != []:
    a.append([b.pop(0), c.pop(0)])    

for i in range(1, len(c)+1):
    Idx = c.index(i)
    d[Idx] = [b[Idx], c[Idx]]

# 3 - 1

import os
os.chdir(r"C:\Users\sjhon\Documents\PythonScripts\LB&C")

with open('06_data.txt', 'r') as f:
    data = f.readlines()

dataList = data[:]
for i in range(len(data)):
    dataList[i] = [data[i].split()[0], float(data[i].split()[1])]

dataList_sorted = dataList[:]
dataList_sorted.sort()
for name, score in dataList_sorted:
    print(name, '\t', score)

dataList_reversed = dataList[:]
dataList_reversed.sort(key = lambda x: x[1], reverse=True)
for name, score in dataList_reversed:
    print(name, '\t', score)