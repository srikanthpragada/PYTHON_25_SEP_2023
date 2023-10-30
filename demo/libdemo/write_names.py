
names = ['Larry', 'Ellison', 'Elon', "Jeff", "Mark"]

f = open("names.txt", "wt")

for name in names:
    f.write(name + "\n")

f.close()
