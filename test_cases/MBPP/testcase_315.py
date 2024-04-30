from case_MBPP_315 import max_of_nth


def check(candidate):
    assert candidate([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    assert candidate([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
    assert candidate([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11

if __name__ == '__main__':
    check(max_of_nth)