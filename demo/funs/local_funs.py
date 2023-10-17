a = 100  # Global


def f1():
    b = 10  # Enclosing variable
    global a
    a = a + 1

    # Local function
    def f2():
        nonlocal b
        b = 20
        c = 20  # Local variable
        print(a, b, c)

    f2()
    print(b)


f1()
