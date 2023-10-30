# Generator to generate prime numbers between the range
def primes(start=1, end=100):
    for n in range(start, end + 1):
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                break
        else:
            yield n


for n in primes(100, 200):
    print(n)

# nums = primes(100,200)
# print(next(nums))
# print(next(nums))
