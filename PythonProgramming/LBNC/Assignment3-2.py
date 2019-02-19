"""
========================================
Dept. of Spanish Language and Literature
2012130730 Shim Jaeheon
LB&C Assignment #3
========================================
"""

# 3-2

import os
import re
from collections import Counter as Cnt

filenames = os.listdir('./09_예제텍스트')

text = ''
for filename in filenames:
    text += open('./09_예제텍스트/' + filename, 'r').read()

p = re.compile('<\w+ (type|pos).+?>(.+?)</\w+?>')  # re.sub("<.+?>, "", text)
matchList = p.findall(text)

cntDict = Cnt()
for i in matchList:
    cntDict[i[-1].lower()] += 1

mostCnt = cntDict.most_common()
mostCnt.sort()
mostCnt.sort(key = lambda x: x[1], reverse=True)

outfile = open('total.txt', 'w')

rank = 1
for k, v in mostCnt:
    outfile.write(str(rank) + '\t' + k + '\t' + str(v) + '\n')
    rank += 1

outfile.close()