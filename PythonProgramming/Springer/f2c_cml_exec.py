import sys

try:
    F = float(sys.argv[1])
except IndexError:
    print("A fahrenheit value must be given in the command line")
    sys.exit(1)

C = 5 / 9 * (F - 32)
print("%g Fahrenheit = %g Celsius" % (F, C))
