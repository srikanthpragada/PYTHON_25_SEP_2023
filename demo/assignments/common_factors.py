# Common factors
a = 33
b = 66

small = a if a < b else b
found = False
for i in range(2, small//2 + 1):
    if a % i == 0 and b % i == 0:
        print(i)
        found = True

if not found:
    print('No common factor found!')


