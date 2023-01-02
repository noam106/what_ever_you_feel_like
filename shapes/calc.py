from shapes import detect
import math


def rectangle_perimeter(list_of_side: list[float]) -> float:
    if detect.is_rectangle(list_of_side) is True:
        perimeter = sum(list_of_side)
        return perimeter
    else:
        return None


def rectangle_area(list_of_side: list[float]) -> float:
    if detect.is_rectangle(list_of_side) is True:
        for i in list_of_side:
            if i != list_of_side[0]:
                perimeter = i * list_of_side[0]
                return perimeter
    else:
        return None


def triangle_perimeter(list_of_side: list[float]) -> float:
    if detect.is_triangle(list_of_side) is True:
        perimeter = sum(list_of_side)
        return perimeter
    else:
        return None


def triangle_area(list_of_side: list[float]) -> float:
    if detect.is_triangle(list_of_side) is True:
        s = sum(list_of_side) / 2
        perimeter = (s*(s-list_of_side[0])*(s-list_of_side[1])*(s-list_of_side[2]))**0.5
        perimeter_round = round(perimeter, 2)
        return perimeter_round
    else:
        return None


def square_perimeter(list_of_side: list[float]) -> float:
    if detect.is_square(list_of_side) is True:
        perimeter = sum(list_of_side)
        return perimeter
    else:
        return None


def square_area(list_of_side: list[float]) -> float:
    if detect.is_square(list_of_side) is True:
        perimeter = list_of_side[0]**2
        return perimeter
    else:
        return None





