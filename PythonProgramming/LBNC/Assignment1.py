"""
========================================
Dept. of Spanish Language and Literature
2012130730 Shim Jaeheon
LB&C Assignment #1
========================================
"""

# 1. Extract words that end with '은' or '는'

f = open(r'C:\Users\sjhon\Documents\PythonScripts\LB&C\04_sample01.txt', 'r', encoding='utf-8')
text = f.read().split()
f.close()

import re

out = open(r'C:\Users\sjhon\Documents\PythonScripts\LB&C\assignment1\은는.txt', 'w', encoding='utf-8')

p = re.compile('\\b\w*(은|는)\\b')
for word in text:
    if p.search(word):
        out.write(p.search(word).group()+'\n')
out.close()               


    





