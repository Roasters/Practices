def L(x, n):
    s = 0
    for i in range(1, n+1):
        s += (1.0/i)*(x/(1.0+x))**i
    return s

def L2(x, n):
    s = 0
    for i in range(1, n+1):
        s += (1.0/i)*(x/(1.0+x))**i
    value_of_sum = s
    first_neglected_term = (1.0/(n+1))*(x/(1.0+x))**(n+1)
    from math import log
    exact_error = log(1+x) - value_of_sum
    return value_of_sum, first_neglected_term, exact_error

def L3(x, epsilon=1.0E-6):
    x = float(x)
    i = 1
    term = (1.0/i)*(x/(1+x))**i
    s = term
    while abs(term) > epsilon:
        i += 1
        term = (1.0/i)*(x/(1+x))**i
        s += term
    return s, i

def L4(x, n=None, epsilon=None, returnN=False):
    import sys
    if (n is None and epsilon is None) or (n is not None and epsilon is not None):
        print("Error: either 'n' or 'epsilon' must be given (not both of them)")
        sys.exit()
    term = x/(1+x)  
    s = term
    if n is not None:
        for i in range(2, n+1):
            term *= (i-1)/i*x/(1+x)
            s += term
        return (s, n) if returnN is True else s
    elif epsilon is not None:
        i = 1
        while abs(term) > epsilon:
            i += 1
            term *= (i-1)/i*x/(1+x)
            s += term
        return (s, i) if returnN is True else s             
