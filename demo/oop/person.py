class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # private attribute

    def getage(self):
        return self.__age


p1 = Person("Mr. Larry", 40)
print(p1.__dict__)
print(p1.name)
#print(p1._Person__age)
