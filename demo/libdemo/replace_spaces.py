import re

with open("test.txt", "rt") as f:
    contents = f.read()


result = re.sub(r' +', ' ', contents)
#result = re.sub(r'\n+', '\n', result)

print(result)
with open("test.txt", "wt") as f:
    f.write(result)







