from tz3_main import min_in_file, max_in_file, proizv_of_file, sum_of_file, square_root_of_sum

def test_min():
    test_list = [1, 2, 3, 4, 5]
    assert min_in_file(test_list) == 1


def test_max():
    test_list = [1, 2, 3, 4, 5]
    assert max_in_file(test_list) == 5


def test_add():
    test_list = [1, 2, 3, 4, 5]
    assert sum_of_file(test_list) == 15


def test_multiply():
    test_list = [1, 2, 3, 4, 5]
    assert proizv_of_file(test_list) == 120


def test_root():
    test_list = [1, 2, 3, 4, 5, 1]
    assert square_root_of_sum(test_list) == 4

