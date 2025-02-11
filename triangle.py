import  math

class Triangle():
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <=0:
            raise ValueError(f'Creating a figure: '"Triangle"' impossible')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = "Triangle"

    def area(self):
        p = self.side_a + self.side_b + self.side_c / 2
        return math.sqrt(p(p - self.side_a)(p - self.side_b)(p - self.side_c))

    def perimiter(self):
        return self.side_a + self.side_b +self.side_c
def triangle():
    my_triangle = Triangle(10, 20, 20)
    return my_triangle.area()
triangle()