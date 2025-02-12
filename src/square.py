import math

class Square():
    def __init__(self, side):
        if side <0:
            raise ValueError('The creation of the figure "Square" is impossible')
        self.side = side
        self.name = 'Square'

    def area(self):
        return pow(self.side, 2)

    def perimeter(self):
        return self.side * 4