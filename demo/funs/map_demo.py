nums = [10, -22, -45, 36]


def modby10(n):
    return n % 10


for n in map(abs, nums):
    print(n)

for n in map(modby10, nums):
    print(n)
