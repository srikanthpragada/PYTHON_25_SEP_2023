
names = []

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    names.append(name)

# names.sort()
# 
# for name in names[::-1]:  # reversed(names):
#     print(name)

for name in sorted(names, reverse=True):
    print(name)
