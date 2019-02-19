"""This module is for calculating temperatures.
You can convert Celsius, Fahrenheit and Kelvin to each other.

    C2k(C) requires input Celsius and returns output Kelvin.
"""
def C2F(C):
    return 9/5*C + 32

def F2C(F):
    return 9/5*C + 32

def C2K(C):
    return C + 273.15

def K2C(K):
    return K - 273.15            

def F2K(F):
    return (F + 459.67) * 5/9

def K2F(K):
    return 9/5*K - 459.67

