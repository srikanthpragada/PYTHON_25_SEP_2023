import sys

if len(sys.argv) < 2:
    print("Number is missing")
    exit()

num = int(sys.argv[1])
total = 0
while num > 0:
    total += num % 10
    num //= 10

print(total)

