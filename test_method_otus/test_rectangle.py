from src.сircle import *
from src.square import *
from src.rectangle import *
from src.triangle import *
import pytest


@pytest.mark.parametrize('side_a, side_b, area, perimeter, name',
                         [(5, 10, 50, 30, 'Rectangle')])
def test_rectangle_ar_per_name(side_a, side_b, area, perimeter, name):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.name == name
    assert rectangle.area() == area
    assert rectangle.perimeter() == perimeter


@pytest.mark.parametrize('radius, side_a, side_b, side_c',
                         [(10, 13, 14, 15),
                          (777, 888, 999, 1000)])
def test_rectangle_add_area(radius, side_a, side_b, side_c):
    circle = Circle(radius)
    triangle = Triangle(side_a, side_b, side_c)
    square = Square(side_a)
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.add_area(circle) == rectangle.area() + circle.area()
    assert rectangle.add_area(square) == rectangle.area() + square.area()
    assert rectangle.add_area(triangle) == rectangle.area() + triangle.area()


@pytest.mark.parametrize('radius, side_a, side_b, side_c',
                         [(-10, 13, 14, 15),
                          (1, 1, 1, 0)])
def test_rectangle_add_area(radius, side_a, side_b, side_c):
    with pytest.raises(ValueError):
        circle = Circle(radius)
        triangle = Triangle(side_a, side_b, side_c)
        square = Square(side_a)
        rectangle = Rectangle(side_a, side_b)
        assert rectangle.add_area(circle) == rectangle.area() + circle.area()
        assert rectangle.add_area(square) == rectangle.area() + square.area()
        assert rectangle.add_area(triangle) == rectangle.area() + triangle.area()
