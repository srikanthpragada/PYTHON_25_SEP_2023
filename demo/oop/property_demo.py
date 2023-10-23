class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def kind(self):
        if self.age <= 50:
            return "Young"
        else:
            return "Old"


p1 = Person("Mr. BIll", 65)
print(p1.kind)  # property
