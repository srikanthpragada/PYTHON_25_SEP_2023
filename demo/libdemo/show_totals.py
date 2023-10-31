f = open("marks.txt", "r")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 1:
        continue

    total = 0
    for m in parts:
        if m.isdigit():
            total += int(m)

    print(total)
    # print(sum(map(int, parts)))

f.close()
