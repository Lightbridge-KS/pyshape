import pytest
from pyshape.shape import Shape, Circle, Square, Triangle

def test_circle_area():
    circle = Circle(color="red", radius=3)
    assert circle.area() == "The circle area = pi x 3^2 = 28.274333882308138"

def test_square_area():
    square = Square(color="blue", side=4)
    assert square.area() == "The square area = 16"

def test_triangle_area():
    triangle = Triangle(color="green", width=5, height=2)
    assert triangle.area() == "The triangle area = 5.0"

def test_shape_repr():
    circle = Circle(color="red", radius=3)
    assert repr(circle) == "Circle(color=red)"

def test_shape_str():
    square = Square(color="blue", side=4)
    assert str(square) == "Square with blue color"

@pytest.mark.parametrize(
    "shape_class, args, expected_area",
    [
        (Circle, {"color": "red", "radius": 1}, "The circle area = pi x 1^2 = 3.141592653589793"),
        (Square, {"color": "blue", "side": 2}, "The square area = 4"),
        (Triangle, {"color": "green", "width": 3, "height": 4}, "The triangle area = 6.0"),
    ]
)
def test_area_parametrize(shape_class, args, expected_area):
    shape = shape_class(**args)
    assert shape.area() == expected_area
