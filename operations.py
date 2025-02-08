import math

def add(x, y): return x + y 

def mul(x, y): return x * y

def sub(x, y): return x - y

def factorial(x): 
    if x == 0:
        return 1
    return x * factorial(x - 1)


def exp(x, y): 
    if y == 1:
        return x
    return x * exp(x, y - 1)


def sum(xs):
    if len(xs) == 0:
        return 0
    return xs[0] + sum(xs[1:])


def mod(x, y):
    return x - ((x // y) * y)