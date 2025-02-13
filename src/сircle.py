import math
from src.figure import *


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError(f'It is impossible to create a figure: circle')
        self.radius = radius
        self.name = 'Circle'

    def area(self):
        return round(math.pi * pow(self.radius, 2), 2)

    def perimeter(self):
        return round(math.pi * self.radius * 2, 2)
