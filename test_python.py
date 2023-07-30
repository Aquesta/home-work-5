import math


def test_python_filter():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'b', 10, 'a']
    filter_result = list(filter(lambda n: isinstance(n, int), numbers))
    assert filter_result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_python_map():
    numbers = [-1, -2, -3, 4, -6, 5, -7, 8, -9, 20]
    map_result = list(map(lambda n: abs(n), numbers))
    assert map_result == [1, 2, 3, 4, 6, 5, 7, 8, 9, 20]


def test_python_sorted():
    numbers = [2, 1, 5, 4, 3, 6, 9, 8, 7]
    sorted_result = list(sorted(numbers))
    assert sorted_result == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_python_pow():
    assert pow(2, 2) == 4
    assert pow(2, 3) == 8


def test_python_hypot():
    assert math.hypot(1, 2) == 2.23606797749979
    assert math.hypot(2, 3) == 3.605551275463989


def test_python_sqrt():
    assert math.sqrt(9) == 3
    assert math.sqrt(16) == 4


def test_python_pi():
    assert math.pi == 3.141592653589793
