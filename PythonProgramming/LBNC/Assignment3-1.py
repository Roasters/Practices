"""
========================================
Dept. of Spanish Language and Literature
2012130730 Shim Jaeheon
LB&C Assignment #3
========================================
"""

# 3-1

a = """The/AT grand/JJ jury/NN commented/VB
on/In a/AT number/NN of/In other/AP topics/NNS ,/,
AMONG/In them/PRO the/AT Atlanta/NP and/CC"""

strDict = {}

for i in a.split():
    i = i.split('/')
    strDict[i[-1]] = []

for i in a.split():
    i = i.split('/')
    if i[0].lower() not in strDict[i[-1]]:
        strDict[i[-1]].append(i[0].lower())

print(strDict)


