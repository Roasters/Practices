"""
========================================
Dept. of Spanish Language and Literature
2012130730 Shim Jaeheon
LB&C Assignment #1
========================================
"""

# 3. Extract english words

f = open(r'C:\Users\sjhon\Documents\PythonScripts\LB&C\04_sample01.txt', 'r', encoding='utf-8')
text = f.read().split()
f.close()

import re

out = open(r'C:\Users\sjhon\Documents\PythonScripts\LB&C\assignment1\out1.txt', 'w', encoding='utf-8')

p = re.compile('[a-zA-Z]+')
for word in text:
    if p.search(word):
        out.write(p.search(word).group()+'\n')

out.close()