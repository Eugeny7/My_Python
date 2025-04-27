import pytest

from Otus.hw_1.src.rectangle import Rectangle
from Otus.hw_1.src.square import Square
from Otus.hw_1.src.triangle import Triangle
from Otus.hw_1.src.сircle import Circle


@pytest.mark.parametrize('side_a, side_b, side_c, area, perimeter, name',
                         [(13, 14, 15, 84, 42, "Triangle")])
def test_triangle_ar_per_name(side_a, side_b, side_c, area, perimeter, name):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.name == name
    assert triangle.area() == area
    assert triangle.perimeter() == perimeter


@pytest.mark.parametrize('radius, side_a, side_b, side_c',
                         [(13, 32, 23, 123),
                          (531231, 8312, 9321, 1123)])
def test_triangle_add_area(radius, side_a, side_b, side_c):
    circle = Circle(radius)
    triangle = Triangle(side_a, side_b, side_c)
    square = Square(side_a)
    rectangle = Rectangle(side_a, side_b)
    assert triangle.add_area(circle) == triangle.area() + circle.area()
    assert triangle.add_area(square) == triangle.area() + square.area()
    assert triangle.add_area(rectangle) == triangle.area() + rectangle.area()


@pytest.mark.parametrize('radius, side_a, side_b, side_c',
                         [(-11, 32, 23, 12),
                          (0, 83, 77, 111)])
def test_triangle_add_area(radius, side_a, side_b, side_c):
    with pytest.raises(ValueError):
        circle = Circle(radius)
        triangle = Triangle(side_a, side_b, side_c)
        square = Square(side_a)
        rectangle = Rectangle(side_a, side_b)
        assert triangle.add_area(circle) == triangle.area() + circle.area()
        assert triangle.add_area(square) == triangle.area() + square.area()
        assert triangle.add_area(rectangle) == triangle.area() + rectangle.area()
