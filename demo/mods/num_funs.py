data = [10, 20, 30, 40]


def iseven(n):
    """
    Return true if number is even otherwise false
    N is an integer
    Returns bool
    """
    return n % 2 == 0


def isprime(n):
    """
    Checks whether a number is prime
    :param n: Number to check
    :return: True if number is prime otherwise false
    """
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True
