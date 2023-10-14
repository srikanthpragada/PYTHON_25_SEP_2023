def digitsum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10

    return total


print(digitsum(123), digitsum(393933))
