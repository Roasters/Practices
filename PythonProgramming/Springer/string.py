# ----------------------------------------------- String convert techniques

infile = open('table.dat','r')
lines = infile.readlines()
infile.close()
data = {}
properties = lines[0].split()

for p in properties:
    data[p] = {}

for line in lines[1:]:
    words = line.split()
    i = int(words[0])
    values = words[1:]
    for p, v in zip(properties, values):
        if v == 'no':
            data[p][i] = None
        else:
            data[p][i] = float(v)      

for p in data:
    values = data[p].values()
    data[p]['mean'] = sum(values)/len(values)

for p in sorted(data):
    print('Mean value of property %s = %g'%(p, data[p]['mean']))    


infile = open('read_pairs1.dat', 'r')
words = infile.read().split()
infile.close()

pairs = []
for word in words:
    word = word[1:-1]
    n1, n2 = word.split(',')
    pairs.append((float(n1), float(n2)))


with open('read_pairs2.dat', 'r') as infile:
    lines = infile.readlines()

pairs = []
for line in lines:
    line = line.strip()
    line = line.replace(' ', '')
    words = line.split(')(')
    words[0] = words[0][1:]
    words[-1] = words[-1][:-1]
    for word in words:
        n1, n2 = word.split(',')
        pairs.append((float(n1), float(n2)))   

with open('read_pairs2.dat', 'r') as infile:
    text = infile.read()

text = text.replace(")", "),")
text = "[" + text + "]"
pairs = eval(text)


# ----------------------------------------------- (x,y,z)
infile = open('xyz.dat', 'r')
coor = []
for line in infile:
    x_start = line.find('x')
    y_start = line.find('y')
    z_start = line.find('z')
    # print(x_start, y_start, z_start)
    x = line[x_start+2:y_start]
    y = line[y_start+2:z_start]
    z = line[z_start+2:]
    coor.append((float(x), float(y), float(z)))
infile.close()

import numpy as np 
coor = np.array(coor)
print(coor.shape, coor)    
