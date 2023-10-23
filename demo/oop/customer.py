class Customer:
    # constructor
    def __init__(self, name, email=None):
        # Object attributes
        self.name = name
        self.email = email

    # Method
    def show(self):
        print(f'Name  : {self.name}')
        print(f'Email : {self.email}')

    def setemail(self, email):
        self.email = email

# Create an object of Customer
c1 = Customer("Mr. Bill", "bill@gmail.com")
# c1.email = "bill@microsoft.com"
c1.setemail("bill@microsoft.com")
#c1.show()

c2 = Customer("Jane")
c2.setemail("jane@google.com")
#c2.show()

customers = [c1, c2, Customer("James", "james@oracle.com")]

for c in customers:
    c.show()

