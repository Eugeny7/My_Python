import pytest


@pytest.mark.parametrize('side, area, perimeter, name',
                         [(10, 100, 40, 'Square')])
def test_square_ar_per_name(side, area, perimeter, name):
    square = Square(side)
    assert square.name == name
    assert square.area() == area
    assert square.perimeter() == perimeter


@pytest.mark.parametrize('radius, side_a, side_b, side_c',
                         [(10, 20, 30, 15)])
def test_square_add_area(radius, side_a, side_b, side_c):
    circle = Circle(radius)
    triangle = Triangle(side_a, side_b, side_c)
    square = Square(side_a)
    rectangle = Rectangle(side_a, side_b)
    assert square.add_area(circle) == square.area() + circle.area()
    assert square.add_area(triangle) == square.area() + triangle.area()
    assert square.add_area(rectangle) == square.area() + rectangle.area()


@pytest.mark.parametrize('radius, side_a, side_b, side_c',
                         [(10, 20, 30, -15),
                          (0, -1, 21, 7)])
def test_square_add_area_negative(radius, side_a, side_b, side_c):
    with pytest.raises(ValueError):
        circle = Circle(radius)
        triangle = Triangle(side_a, side_b, side_c)
        square = Square(side_a)
        rectangle = Rectangle(side_a, side_b)
        assert square.add_area(circle) == square.area() + circle.area()
        assert square.add_area(triangle) == square.area() + triangle.area()
        assert square.add_area(rectangle) == square.area() + rectangle.area()
