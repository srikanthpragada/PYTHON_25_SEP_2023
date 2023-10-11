data = [(1, 20), (3, 40), (5, 60), (2, 50), (1, 40), (2, 50), (1, 60)]

students = {}
for entry in data:
    rollno, marks = entry
    total = students.get(rollno, 0)
    students[rollno] = total + marks

print(students)


