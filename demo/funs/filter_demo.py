nums = [10, 11, 30, 33, 55]


def iseven(n) -> bool:
    return n % 2 == 0


for n in filter(iseven, nums):
    print(n)


for c in filter(str.isupper, "How Do You DO?"):
    print(c)