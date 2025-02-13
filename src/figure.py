from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self):
        self.name = "Figure"

    @abstractmethod
    def area(self):
        pass

    def add_area(self, any_figure):
        if not isinstance(any_figure, Figure):
            raise ValueError(f'{any_figure}: this is not a figure, the calculation of the total area is impossible')
        return self.area() + any_figure.area()
