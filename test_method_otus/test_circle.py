from src.сircle import *
from src.square import *
from src.rectangle import *
from src.triangle import *
import pytest


@pytest.mark.parametrize('radius, area, perimeter, name',
                         [(10, 314.16, 62.83, 'Circle')])
def test_circle_ar_per_name(radius, area, perimeter, name):
    circle = Circle(radius)
    assert circle.area() == area
    assert circle.perimeter() == perimeter
    assert circle.name == name


@pytest.mark.parametrize('radius, side_a, side_b, side_c',
                         [(10, 13, 14, 15)])
def test_circle_add_area(radius, side_a, side_b, side_c):
    circle = Circle(radius)
    triangle = Triangle(side_a, side_b, side_c)
    square = Square(side_a)
    rectangle = Rectangle(side_a, side_b)
    assert circle.add_area(triangle) == circle.area() + triangle.area()
    assert circle.add_area(square) == circle.area() + square.area()
    assert circle.add_area(rectangle) == circle.area() + rectangle.area()


@pytest.mark.parametrize('radius, side_a, side_b, side_c',
                         [(-10, 13, 14, 15),
                          (0, 888, 999, 1000)])
def test_circle_add_area_negative(radius, side_a, side_b, side_c):
    with pytest.raises(ValueError):
        circle = Circle(radius)
        triangle = Triangle(side_a, side_b, side_c)
        square = Square(side_a)
        rectangle = Rectangle(side_a, side_b)
        assert circle.add_area(triangle) == circle.area() + triangle.area()
        assert circle.add_area(square) == circle.area() + square.area()
        assert circle.add_area(rectangle) == circle.area() + rectangle.area()
