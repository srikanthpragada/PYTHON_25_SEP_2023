from datetime import *

f = open("players.txt", "rt")
players = []

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) != 2:  # invalid line, so ignore
        continue

    name, dobstr = parts
    try:
        dob = datetime.strptime(dobstr, '%d-%m-%Y')
        time_delta = datetime.today() - dob
        age = time_delta.days // 365
        players.append((name, age))
    except:
        pass

f.close()

for name, age in sorted(players, key=lambda p: p[1]):
    print(f"{name:20}  {age:2}")
