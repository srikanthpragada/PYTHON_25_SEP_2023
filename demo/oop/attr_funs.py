class Point:
    def __init__(self, x):
        self.x = x


p1 = Point(10)
print(p1.__dict__)
print(getattr(p1, 'x'), getattr(p1, 'y', 0))
setattr(p1, 'y', 20)
print(hasattr(p1, 'y'))
delattr(p1, 'x')
p1.color = 'red'  # create an attribute color
print(p1.__dict__)
