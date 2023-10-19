
def has_digit(st):
    for c in st:
        if c.isdigit():
            return True

    return False


def has_whitespace(st):
    for c in st:
        if c.isspace():
            return True

    return False