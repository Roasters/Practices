# Exercise 1

def a(s):
    def inFunc(x):
        print("{:&^{}}".format(s, x))
    return inFunc

# ''.join(['(:&^', str(x), '}']).format(s)

# Exercise 2

n = 0

def add(x):
    global n
    n += x
    return n

a = lambda x: add(x)
