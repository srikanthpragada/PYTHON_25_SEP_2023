# Positional only args
def fun(x, y, /):
    pass


fun(10, 20)
#fun(y=1, x=10)
