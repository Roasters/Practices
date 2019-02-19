import os

# Exercise 1

inDirectory = os.listdir()

for i in inDirectory:
    tmp = os.path.splitext(i)
    if tmp[-1] == '':
        print(tmp[0])

for i in inDirectory:
    tmp = os.path.splitext(i)
    if tmp[-1]:
        print(i)

for i in inDirectory:
    tmp = os.path.splitext(i)
    if tmp[-1] == '.txt':
        print(i)


# Exercise 2

os.chdir(r'C:\Users\SJH\Documents\PythonScripts\LB&C')

textFiles = os.listdir('./08_ExampleText')

for textFile in textFiles:
    with open('./08_ExampleText/' + textFile, 'r') as fr:
        text = fr.read()
    with open('./08_ExampleText/total.txt', 'a', encoding='utf-8') as fw:
        fw.write(text)


result = []

for textFile in textFiles:
    fr = open('./08_ExampleText/' + textFile, 'r')
    text = fr.read()
    result.append(text)
    fr.close()

fw = open('./08_ExampleText/total.txt', 'w')
fw.writelines(result)
fw.close()    