
st = "90,34,,55,92"

#print(st.split(","))

total = 0
for n in st.split(","):
    total += int(n)

print(total)
