
st = "90,34,abc,55,92,80,xy"

#print(st.split(","))

total = 0
for n in st.split(","):
    if n.isdigit():
        total += int(n)

print(total)
