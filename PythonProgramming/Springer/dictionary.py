temps = dict(Oslo=13, London=15.4, Paris=17.5)
temps['Madrid'] = 26.0

for city in temps:
    print('The temperature in {0} is {1}'.format(city, temps[city]))

temps_copy = temps.copy()
del temps_copy['Paris'] 


# ----------------------------------------------- Polynomial

p = {0: -1, 2: 1, 7: 3}  # P(x) = -1 + x^2 + 3x^7, key: power, value: coefficient

def evalPolyDict(poly, x):
    sum = 0
    for power in poly:
        sum += poly[power]*x**power
    return sum

def evalPolyDict2(poly, x):
    return sum(poly[power]*x**power for power in poly)

# ----------------------------------------------- Dictionary comprehension

from math import factorial
d = {k: (-1)**k/factorial(k) for k in range(n+1)}

# ----------------------------------------------- Default value

p1 = {-3:2, -1:-1, 2:-2}
value = p1.get(key, 0)

from collections import defaultdict

def polynomial_coeff_default():
    return 0
p2 = defaultdict(polynomial_coeff_default)
p2.update(p1)

# or (because polynomial_coeff_default is non-argument function)
p2 = defaultdict(lambda: 0)
p2 = defaultdict(float)   # float() == 0

# ----------------------------------------------- Ordered dictionaries

p1 = {-3:2, -1:-1.5, 2:-2}

from collections import OrderedDict
p2 = OrderedDict(p1)

data = OrderedDict()

data['Jan 2'] = 33
data['Jan 16'] = 0.1
data['Feb 2'] = 2

for date in data:  
    print(date, data[date])

import datetime
data = {}
d = datetime.datetime.strptime
data[d('Feb 2, 2017', '%b %d, %Y')] = 2 
data[d('Jan 2, 2017', '%b %d, %Y')] = 33
data[d('Jan 16, 2017', '%b %d, %Y')] = 0.1



def read_densities(filename):
    import re
    p = re.compile('(.+)\\b\s+\\b(\S+)')
    data = {}
    file = open(filename, 'r')
    for line in file.readlines():
        m = p.match(line)
        data[m.group(1)] = float(m.group(2))
    file.close()
    # data_dict = {data[i][0]: data[i][1] for i in range(len(data))}
    return data


