from src.rectangle import *

class Square(Rectangle):
    def __init__(self, side):
        if side <0:
            raise ValueError('The creation of the figure "Square" is impossible')
        super().__init__(side,side)
        self.side = side
        self.name = 'Square'