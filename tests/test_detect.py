import shapes.detect
from shapes import *


def test_to_many_sides():
    test_list = [6,6,6,6,0]
    assert shapes.detect.is_triangle(test_list) is False
    assert shapes.detect.is_rectangle(test_list) is False
    assert shapes.detect.is_square(test_list) is False


def test_not_enough_sides():
    test_list = [8,5]
    assert shapes.detect.is_triangle(test_list) is False
    assert shapes.detect.is_rectangle(test_list) is False
    assert shapes.detect.is_square(test_list) is False


def negativ_num():
    test_list = [-1,3,5,7]
    test_list_2 = [2,6,-2]
    assert shapes.detect.is_triangle(test_list_2) is False
    assert shapes.detect.is_rectangle(test_list) is False
    assert shapes.detect.is_square(test_list) is False
