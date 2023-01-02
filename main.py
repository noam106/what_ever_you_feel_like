import tests.test_detect
import tests.test_calc
import tests.test_complex


if __name__ == '__main__':
    tests.test_detect.negativ_num()
    tests.test_detect.test_to_many_sides()
    tests.test_detect.test_not_enough_sides()
    tests.test_calc.test_non_triangle()
    tests.test_calc.test_float_num()
    tests.test_calc.test_non_num()
    tests.test_complex.test_empty_list()
    tests.test_complex.test_list_with_nonint()


