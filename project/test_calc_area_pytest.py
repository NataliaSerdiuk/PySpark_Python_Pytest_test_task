import math
import pytest
from areacalc import *


def test_circle_area():
    radius = 5
    assert math.isclose(Circle.calc_cirсle_area(radius), math.pi * (radius ** 2), rel_tol=1e-9)

def test_triangle_area():
    x = 5
    y = 3
    z = 4
    assert math.isclose(Triangle.calc_triangle_area(x,y,z), 6.0, rel_tol=1e-9)

def test_true_check_right_triangle_3_4_5():
    assert Triangle.check_right_triangle(3,4,5)==True

def test_true_check_right_triangle_5_12_13():
    assert Triangle.check_right_triangle(5, 12, 13) == True

def test_false_check_right_triangle_3_5_5():
    assert Triangle.check_right_triangle(3, 5, 5) == False

def test_false_check_right_triangle_1_2_3():
    assert Triangle.check_right_triangle(1,2,3) == False

def test_calc_rectangle_area():
    x = 4
    y = 5
    assert math.isclose(Rectangle.calc_rectangle_area(x,y),20.0, rel_tol=1e-9)

def test_invalid_shape():
    with pytest.raises(NotImplementedError):
        calc_selection('овал', 5, 7, 9)
