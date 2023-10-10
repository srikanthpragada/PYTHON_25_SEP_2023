l1 = [10, 20, 40, 50]
l2 = [100, 200]

for fi, fv in enumerate(l1):
    if fi < len(l2):
        print(fv, l2[fi])
    else:
        print(fv, 'Unknown')

