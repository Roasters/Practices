def H(x):
    return (0 if x < 0 else 1)

import numpy as np
x = np.linspace(-1, 1, 5)

# Using a loop
def H_loop(x):
    r = np.zeros(len(x))
    for i in range(len(x)):
        r[i] = H(x[i])
    return r 

# Using vectorize
H_vec = np.vectorize(H)       

# Boolean and floating
def H(x):
    r = x >= 0
    if isinstance(x, (int, float)):
        return int(r)
    elif isinstance(x, np.ndarray):
        return np.asarray(r, dtype=np.int)

# Numpy.where
def Hv(x):
    return np.where(x<0, 0.0, 1.0)

# Boolean indexing
def Hv(x):
    r = np.zeros(len(x), dtype=np.int)
    r[x > 0] = 1
    return r
