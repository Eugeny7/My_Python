class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        if side < 0:
            raise ValueError('The creation of the figure "Square" is impossible')
        self.side = side
        self.name = 'Square'
