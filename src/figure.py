class Figure():
    def __init__(self):
        self.name = "Figure"

    def add_area(self,any_figure):
        return self.area + any_figure.area()