def isprime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False

    return True


if isprime(11):
    print("Prime")

