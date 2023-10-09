names = ['Larry', 'Mark', 'Bill']
ages = [43, 38, 63, 93]

for name, age in zip(names, ages, strict=True):
    print(name, age)
