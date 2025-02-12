import math

class Circle():
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f'It is impossible to create a figure: circle')
        self.radius = radius
        self.name = 'Circle'

    def area(self):
        return math.pi * pow(self.radius, 2)

    def perimeter(self):
        return math.pi * self.radius * 2



