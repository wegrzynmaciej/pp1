class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'P({self.x},{self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(5, 6)
p3 = Point(1, 2)
print(p1 == p3)
