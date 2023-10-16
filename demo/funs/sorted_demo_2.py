names = [' Joe', 'bill', ' Larry', 'Mark', 'Li']


def normalize(s):
    return s.strip().upper()


for n in sorted(names, key=normalize):
    print(n)
