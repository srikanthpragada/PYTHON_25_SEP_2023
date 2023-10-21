import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def __str__(self):
        return f"{self.x}, {self.y}, {self.r}"

    def __gt__(self, other):
        return self.r > other.r

    def __eq__(self, other):
        return self.r == other.r and self.x == other.x and self.y == other.y


c1 = Circle(10, 10, 20)
print(f"{c1.area():8.2f}")

c2 = Circle(10, 10, 10)
print(c1 > c2)  # c1.__gt__(c2)
print(c1 < c2)  # c1.__gt__(c2)

print(c1)
print(str(c1))  # c.__str__()
print(c1.__str__())

cl = [Circle(10, 10, 5), Circle(10, 20, 10),
      Circle(10, 10, 15), Circle(5, 5, 3)]

for c in sorted(cl):
    print(c)
