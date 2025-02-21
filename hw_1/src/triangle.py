import math

from hw_1.src.figure import *


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(f'Creating a figure: "triangle" impossible')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = "Triangle"

    def area(self):
        if (self.side_a + self.side_b <= self.side_c) or \
        (self.side_b + self.side_c <= self.side_a) or \
        (self.side_a + self.side_c <= self.side_b):
            raise ValueError(f'It is impossible to comb the square root from a negative number')
        p = (self.side_a + self.side_b + self.side_c) / 2
        return int(math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c