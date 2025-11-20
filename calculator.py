#https://roshnipadala1@github.com/roshnipadala1/lab11--RP---SS-
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    # raise ValueError if a < 0
    try:
        return math.sqrt(a)
    except ValueError:
        print("error: a < 0")
def hypotenuse(a, b):
    # can have negative nums
    return math.hypot(a, b)

# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # raise ZeroDivisionError if a == 0
    try:
        result = b/a
        return result
    except ZeroDivisionError:
        print("Division by zero error")
        return None

def log(a, b):
    # use math library + raise ValueError
    try:
        result = math.log(b,a)
        return result
    except ValueError:
        print("Log error")
        return None

def exp(a, b):
    return a**b



