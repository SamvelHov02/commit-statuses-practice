import math

def add(x, y): return x + y 

def mul(x, y): return x * y

def sub(x, y): return x - y

def factorial(x): 
    if x == 0:
        return 1
    return x * factorial(x - 1)

