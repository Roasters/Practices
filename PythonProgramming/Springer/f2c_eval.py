import sys

output = eval(%sys.argv[1])

print("%s is a Python %s object"%(output, type(output).__name__))