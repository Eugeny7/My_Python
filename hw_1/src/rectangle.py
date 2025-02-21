from hw_1.src.figure import *


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        if side_a <= 0 or side_b <= 0:
            raise ValueError('The creation of the figure "rectangle" is impossible')
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'Rectangle'

    def area(self):
        return self.side_a * self.side_b

    def perimeter(self):
        return (self.side_a + self.side_b) * 2
