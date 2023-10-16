data = [10, -20, 15, -50]

for n in sorted(data, key=abs):
    print(n)

names = ['Joe', 'Bill', 'Larry', 'Mark', 'Li']

for n in sorted(names, key=len):
    print(n)
