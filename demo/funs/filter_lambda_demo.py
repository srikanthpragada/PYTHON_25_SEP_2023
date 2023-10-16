nums = [10, 11, 30, 33, 55]

for n in filter(lambda n: n % 2 != 0, nums):
    print(n)
