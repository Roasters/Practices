# Exercise 1 - 'for'
a = 'abcdef'

out = ""
for alph in a:
    out += alph
    print(out)

# Exercise 1 - 'slicing'

i = 0
for _ in a:
    print(a[:i+1])
    i += 1 

i = 0
while i <= len(a):
    print(a[:i])
    i += 1

# Exercise 2 - 1
a = 'abcdef'

s = input("Enter a letter: ")
out = ""
for alph in a:
    out += alph + s
    print(out)    

# Exercise 2 - 2
a = 'abcdef'

n = input('Enter an integer: ')
print(a * int(n))

# Exercise 3
a = 'abcdef'
b = ['c', 'e', 'g']

for alph in b:
    if alph in a:
        print(alph)

# Exercise 4
s = 'i like programming'

for alph in s:
    print(alph, s.count(alph))


# Exercise 5
import os
os.chdir(r'C:\Users\sjhon\Documents\PythonScripts\LB&C')

text = open('02_sample.txt', 'r')
result = open('no_space.txt', 'w')

out = ''
result.write(''.join(text.read().split(' ')))

text.close()
result.close()

