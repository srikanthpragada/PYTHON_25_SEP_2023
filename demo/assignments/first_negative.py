def negative(nums):
    for n in nums:
        if n < 0:
            return n

    return 0


print(negative([10, 20, -44, -55]))
print(negative([10, 20, 55]))
