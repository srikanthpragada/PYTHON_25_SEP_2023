data = [(1, 20), (3, 40), (5, 60), (2, 50), (1, 40), (2, 50), (1, 60)]

students = {}
for entry in data:
    rollno, marks = entry
    if rollno in students:
        students[rollno] = students[rollno] + marks
    else:
        students[rollno] = marks

print(students)


