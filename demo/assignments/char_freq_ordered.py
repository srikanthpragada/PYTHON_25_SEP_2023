
st = "how are you doing today"

chars = []
for c in st:
    if c not in chars:
        print(c, st.count(c))
        chars.append(c)


