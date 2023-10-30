class InvalidSalaryError(Exception):
    def __init__(self, salary):
        self.salary = salary

    def __str__(self):
        return f"Invalid Salary : {self.salary}"



class Employee:
    # static attribute
    HRAPER = 30
    def __init__(self, name, desg=None, salary=0):
        self.name = name
        self.desg = desg
        self.salary = salary

    def setSalary(self, salary):
        if salary < 0:
            raise InvalidSalaryError(salary)

        self.salary = salary

    def setDesg(self, desg):
        self.desg = desg

    def getSalary(self):
        return self.salary + self.salary * Employee.HRAPER // 100


e1 = Employee(name="Mr. Scott", salary=100000)
e1.setSalary(-10000)
print(e1.getSalary())

e2 = Employee("Mr. Larry", "CTO")
