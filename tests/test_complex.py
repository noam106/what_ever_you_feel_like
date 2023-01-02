import shapes.complex
from shapes import complex


def test_empty_list():
    test_list = []
    assert shapes.complex.sort_function(test_list) == ({'triangles': [], 'square': [], 'rectangle': []}, [])


def test_list_with_nonint():
    test_list = [['testing']]
    assert shapes.complex.sort_function(test_list) == ({'triangles': [], 'square': [], 'rectangle': []}, ['testing'])



