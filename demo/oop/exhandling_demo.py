try:
    num = int(input("Enter number :"))
    print(100 // num)
except ValueError:
    print("Invalid Number!")
else:
    print("Success")
finally:
    print("Finally!")

print("The End")
