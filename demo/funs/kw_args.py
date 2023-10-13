def fun(**kwargs):
    print(type(kwargs))


def fun2(*args, **kwargs):
    pass


fun(a=10, b=20, n="Abc")
fun(x=1, y=10)
fun2(10, 20, a=10, b=20)
