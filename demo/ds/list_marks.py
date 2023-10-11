
data = "1,20:3,40:5,60:2,50:1,40"

students = {}
for entry in data.split(":"):
    rollno, marks = entry.split(",")
    students[rollno] = marks


for rollno, marks in sorted(students.items()):
    print(rollno, marks)

