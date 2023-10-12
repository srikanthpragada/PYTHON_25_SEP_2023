
st = "how are you doing today"

freq = {}
for c in set(st):
    freq[c] = st.count(c)

freq = {c : st.count(c) for c in set(st)}

print(freq)



