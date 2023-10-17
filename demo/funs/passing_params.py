def zero(n):
    print(id(n))
    n = 0
    print(id(n))


def prepend(lst, v):
    print(id(lst))
    lst.insert(0, v)
    print(id(lst))


a = 100
print(id(a))
zero(a)
print(a)

l = [1, 2, 3]
print(id(l))
prepend(l, 100)
print(l)
