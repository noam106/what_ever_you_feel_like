import shapes.calc


def test_float_num():
    test_list = [6,8.2584,6,8.2584]
    assert shapes.calc.rectangle_perimeter(test_list) == 28.52


def test_non_num():
    test_list = [4,4,4,'s']
    assert shapes.calc.square_area(test_list) is None
    assert shapes.calc.square_perimeter(test_list) is None


def test_non_triangle():
    test_list = [1,2,1]
    assert shapes.calc.rectangle_area(test_list) is None
    assert shapes.calc.rectangle_perimeter(test_list) is None
