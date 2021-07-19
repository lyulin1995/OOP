class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        """we are passing another point object
        built in method"""
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        """we are passing another point object"""
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        """return a scalar"""
        return self.x * p.x + self.y * p.y

    def length(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __len__(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        """sometimes decimal number can mess up in python and they don't get the same percison"""
        return self.x == p.x and self.y == p.y

    def __str__(self):
        """every time we try to convert our point object into a string
        return a string value"""
        return "(" + str(self.x) + ',' + str(self.y) + ')'


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
p5 = p1 + p2  # p1 is self, p2 is p
p6 = p4 - p1
p7 = p2 * p3
len(p1)
print(p5, p6, p7)
print(p1 == p2)
print(p1 > p2)
print(p4 <= p3)
