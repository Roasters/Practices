import math
def pathlength(x, y):
    L = 0
    for i in range(1, len(x)):
        L += math.sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
    return L

def test():
    nList = [2**k for k in range(2, 11)]
    for n in nList:
        x = [1/2 * math.cos(2*math.pi*i/n) for i in range(n+1)]
        y = [1/2 * math.sin(2*math.pi*i/n) for i in range(n+1)]
        approx = pathlength(x, y)
        print("For %4d points on the circle, pi approximates to %.8f \
giving and error of %.8f" \
            %(n, approx, abs(pi-approx)))


def polygonArea(x, y):
    A = 0
    for i in range(len(x)-1):
        A += x[i]*y[i+1]
        A -= y[i]*x[i+1]
    A += (x[-1]*y[0] - y[-1]*x[0])    
    A *= 1/2
    return A