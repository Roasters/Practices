import sys
def readC():
    try:
        C = float(sys.argv[1])
    except IndexError:
        raise IndexError("Celsius degrees must be supplied on the command line")
    except ValueError:
        raise ValueError("Celsius degrees must be a pure number, not '%s'"%sys.argv[1])
    if C < -273.15:
        raise ValueError("C=%g is a non-physical value!"%C)
    return C

try: 
    C = readC()
except Exception as e:
    print(e)
    sys.exit(1)    
F = 9.0/5*C + 32
print("%gC is %.1fF"%(C,F))