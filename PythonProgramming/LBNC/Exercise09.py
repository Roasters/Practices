"""
============
|Exercise 1|
============
"""
import os
os.chdir(r"C:\Users\SJH\Documents\PythonScripts\LB&C")

with open('06_data.txt', 'r') as f:
    data = f.readlines()

# 1
dataDict = {}
for line in data:
    tmp = line.split()
    dataDict[tmp[0]] = float(tmp[-1])

#2-1(with key)
keyList = list(dataDict.keys())
keyList.sort()
for k in keyList:
    print(k, '\t', dataDict[k])
#2-2(with item)
itemList = list(dataDict.items())
itemList.sort()
for k, v in itemList:
    print(k, '\t', v)