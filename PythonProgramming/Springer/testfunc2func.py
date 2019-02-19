def test_halve():
    assert halve(5) == 2.5

def halve(n):
    return n*0.5

def test_add():
    assert add(1, 2) == 3

    tol = 1E-14
    a = 0.1; b = 0.2
    computed = add(a, b)
    expected = 0.3
    assert abs(expected - computed) < tol

    assert add([1,4], [4,7]) == [1,4,4,7]

    assert add('hello, ', 'world') == 'hello, world'

def add(n, m):
    return n + m

def test_equal():
    assert equal('abc', 'abc') == (True, 'abc')
    assert equal('abc', 'aBc') == (False, 'ab|Bc')
    assert equal('abc', 'aBcd') == (False, 'ab|Bc*|d')
    assert equal('Hello, World!', 'hello world') == \
            (False, 'H|hello,| |wW|oo|rr|ll|dd|*!|*')

def equal(a, b):
    out = ""
    if a == b:
        return True, a
    elif len(a) == len(b):  
        for i in range(len(a)):
            if a[i] == b[i]:
                out += a[i]
            else:
                out += a[i] + "|" + b[i]
        return False, out             
    elif len(a) > len(b):
        for i in range(len(b)):
            if a[i] == b[i]:
                out += a[i]
            else:                   
                out += a[i] + "|" + b[i]
        for i in range(len(a)-len(b), 0, -1):
            out += a[-i] + "|" + "*"
        return False, out
    elif len(a) < len(b):
        for i in range(len(a)):
            if a[i] == b[i]:
                out += a[i]
            else:                   
                out += a[i] + "|" + b[i]
        for i in range(len(b)-len(a), 0, -1):
            out +=   "*" + "|" + b[-i]
        return False, out          
                    


