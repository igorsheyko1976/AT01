def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a / b

def check(number):
    return number % 2 == 0

def mod(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a % b