
num = int(input("Enter a number :"))

while True:
    sum = 0
    while num > 0:
       sum += num % 10
       num //= 10

    if sum > 9:
        num = sum
    else:
        print(sum)
        break




