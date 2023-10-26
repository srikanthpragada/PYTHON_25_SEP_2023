import math
from abc import abstractmethod, ABC


# Abstract class
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def area(self):
        pass

    def show(self):
        print(self.x, self.y)


class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return math.pi * self.r * self.r


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def area(self):
        return self.side * self.side


c = Circle(10, 20, 15)
c.show()
s = Square(10, 10, 20)
print(c.area())
print(s.area())
