values = ["abc123", "pqr456", "aaa999", "xyz111"]


def last3(s):
    return s[-3:]


for v in sorted(values, key=last3):
    print(v)

for v in sorted(values, key=lambda n: n[-3:]):
    print(v)
