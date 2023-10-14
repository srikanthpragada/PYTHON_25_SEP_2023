# Functional programming

def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def domath(a, b, operation):
    print(operation(a, b))


domath(10, 20, add)
domath(10, 20, mul)
