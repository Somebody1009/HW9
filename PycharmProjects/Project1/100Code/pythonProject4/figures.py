import math

class Figure:
    def perimeter(self):
        raise NotImplementedError()

    def area(self):
        raise NotImplementedError()

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        if s > self.a and s > self.b and s > self.c:
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return 0.0

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        try:
            s = (self.a + self.b + self.c + self.d) / 2
            height = (math.sqrt((s - self.a) * (s - self.b) * (s - self.c) * (s - self.d)) * 2) / (self.a + self.b)
            return ((self.a + self.b) / 2) * height
        except (ValueError, ZeroDivisionError):
            return 0.0

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r * self.r
