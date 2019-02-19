def midpointIntegration(f, a, b, n=100):
    h = (b-a)/n
    I = 0
    for i in range(n):
        I += f(a + i*h + 0.5*h)
    return h*i

from math import *
import sys
fFormula = sys.argv[1]
a = eval(sys.argv[2])
b = eval(sys.argv[3])
if len(sys.argv) >= 5:
    n = int(sys.argv[4])
else: n = 200

code = """
def g(x):
    return %s"""%fFormula
exec(code)

I = midpointIntegration(g, a, b, n)
print("Integral of %s on [%g, %g] with n=%d: %g"%(fFormula, a, b, n, I))    