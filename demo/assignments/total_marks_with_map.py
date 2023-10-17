data = "98,78,88,a,45"

marks = data.split(",")
valid_marks = filter(str.isdigit, marks)
print(sum(map(int, valid_marks)))
