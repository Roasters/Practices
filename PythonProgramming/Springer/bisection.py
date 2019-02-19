def bisection(f, a, b, eps=1E-6):
    fa = f(a)
    if fa*f(b) > 0:
        return None, 0
    i = 0
    while b-a > eps:
        i += 1
        m = (b+a)/2
        fm = f(m)
        if fa*fm <= 0:
            b = m
        else:
            a = m
            fa = fm
    return m, i

def test_bisection():
    f = lambda x: 2*x -3
    x_expected = 1.5
    x, iter = bisection(f, 0, 10, eps=1E-6)
    success = abs(x - x_expected) < eps
    assert success, 'found x=%g != %g'%(x, x_expected)

if __name__ == "__main__":
    test_bisection()    