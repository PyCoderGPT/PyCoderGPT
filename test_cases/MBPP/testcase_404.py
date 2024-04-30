from case_MBPP_404 import tuple_str_int


def check(candidate):
    assert candidate("(7, 8, 9)") == (7, 8, 9)
    assert candidate("(1, 2, 3)") == (1, 2, 3)
    assert candidate("(4, 5, 6)") == (4, 5, 6)
    assert candidate("(7, 81, 19)") == (7, 81, 19)

if __name__ == '__main__':
    check(tuple_str_int)