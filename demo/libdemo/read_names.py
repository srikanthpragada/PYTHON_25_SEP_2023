
f = open("names.txt", "rt")

for line in f.readlines():
   # print(line, end = '')
   print(line.strip())

f.close()

