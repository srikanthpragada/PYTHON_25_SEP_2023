names = ["abc", "Xyz", "Pqr", "def"]


def has_upper(st) -> bool:
    for c in st:
        if c.isupper():
            return True

    return False


for n in filter(has_upper, names):
    print(n)
