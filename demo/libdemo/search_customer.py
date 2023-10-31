f = open("customers.txt", "rt")

searchname = input("Enter customer name :")
found = False

while True:
    line = f.readline()
    if len(line) == 0:  # Empty line means EOF
        break

    parts = line.split(",")
    if len(parts) < 2:
        continue  # Ignore line as it doesn't required data

    name, email = parts
    if name.upper() == searchname.upper():
        print(email)
        found = True
        break

f.close()
if not found:
    print('Sorry! Name not found!')
