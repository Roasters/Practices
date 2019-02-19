import sys
sys_stdout_orig = sys.stdout
sys.stdout = open("result.txt",'w')
sys_stdin_orig = sys.stdin
sys.stdin = open("input.txt", 'r')

def add(x):
    return x + 3

def x2f(infile, f):
    for line in infile:
        x = float(line)
        y = f(x)
        print("%g\n"%y)

infile = input()
x2f(infile, add)

