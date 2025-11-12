# https://github.com/leonnaxie/lab11-LX-EC
# Partner 1: Leonna Xie
# Partner 2: Emily Chen

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError()
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError

    return b/a

def log(a,b):
    if a <= 0:
        raise ValueError

    if b <= 0 or b == 1:
        raise ValueError

    return math.log(a,b)

def exp(a,b):
    return a ** b


