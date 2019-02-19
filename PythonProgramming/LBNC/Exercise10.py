# Exrcise 1

a = 'apple banana'
a = list(set(a))
a.sort()

for i in a:
    print(i)


# Exercise 2

import os
import re
os.chdir(r'C:\Users\SJH\Documents\PythonScripts\LB&C')

filenames = os.listdir('./08_ExampleText')

text = ''
for filename in filenames:
    text += open(os.path.join('./08_ExampleText', filename)).read()

text = text.lower()

textSet = set(re.findall('\w+', text))

textList = list(textSet)
textList.sort()

for i in textList:
    print(i)