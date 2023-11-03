import re

f = open("cust.txt", "rt")

for line in f.readlines():
    m = re.search(r'\d{10}', line)
    if m is None:
        continue   # ignore line

    mobile = m.group()

    m = re.search(r"\w+@[a-zA-Z0-9.]+", line)
    if m is None:
        continue  # ignore line

    email = m.group()
    print(f"{email} - {mobile}")

f.close()
