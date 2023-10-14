# Overloading
def add(a, b):
    pass

add2 = add

def add(a, b, c):
    pass


add2(10, 20)
add(10, 20, 30)
