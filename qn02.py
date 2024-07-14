import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_circumference(self):
        return self.get_perimeter()
    
circle1 = Circle(0, 0, 10)
print("Area:", circle1.get_area())
print("Perimeter:", circle1.get_perimeter())
print("Circumference:", circle1.get_circumference())