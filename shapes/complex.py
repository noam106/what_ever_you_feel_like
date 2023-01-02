import shapes.detect
from shapes import *
import shapes.calc


def sort_function(lists_of_sides: list[list]):
    # opening list of uniqe items
    uniqe_list_of_sides = []
    for i in lists_of_sides:
        if i not in uniqe_list_of_sides:
            uniqe_list_of_sides.append(i)
    shapes_dict = {
        "triangles": [],
        'square': [],
        'rectangle': []
    }

    list_of_improper = []
    for shape in uniqe_list_of_sides:
        temp_shape_dict = {}
        if shapes.detect.is_triangle(shape) is True:
            temp_shape_dict['sides'] = shape
            temp_shape_dict['area'] = shapes.calc.triangle_area(shape)
            temp_shape_dict['perimeter'] = shapes.calc.triangle_perimeter(shape)
            shapes_dict['triangles'].append(temp_shape_dict)
        elif shapes.detect.is_square(shape) is True:
            temp_shape_dict['sides'] = shape
            temp_shape_dict['area'] = shapes.calc.square_area(shape)
            temp_shape_dict['perimeter'] = shapes.calc.square_perimeter(shape)
            shapes_dict['square'].append(temp_shape_dict)
        elif shapes.detect.is_rectangle(shape) is True:
            temp_shape_dict['sides'] = shape
            temp_shape_dict['area'] = shapes.calc.rectangle_area(shape)
            temp_shape_dict['perimeter'] = shapes.calc.rectangle_perimeter(shape)
            shapes_dict['rectangle'].append(temp_shape_dict)
        else:
            list_of_improper.append(shape)
    return shapes_dict, list_of_improper
