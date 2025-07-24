import math

class Circle:

    pi = math.pi # class variable

    def __init__(self, radius):
        self._radius = radius
        self._type = 'circle' # instance variable

    def calculate_area(self):
        return Circle.pi * self._radius * self._radius

    def calculate_circumference(self):
        return 2 * self.pi * self._radius

    def show(self):
        print(f'Area: {self.calculate_area()}, Circumference: {self.calculate_circumference()}')

circle = Circle(5)
print(f'Area of circle: {circle.calculate_area()}')
print(f'Circumference of circle: {circle.calculate_circumference()}')
circle.show()