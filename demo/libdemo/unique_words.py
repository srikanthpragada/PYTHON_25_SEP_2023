f = open('story.txt', "r")

contents = f.read()
words = contents.split(" ")

for w in sorted(set(words)):
    print(w)

f.close()
