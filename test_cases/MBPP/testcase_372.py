from case_MBPP_372 import add_tuple


def check(candidate):
    assert candidate([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
    assert candidate([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]
    assert candidate([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]

if __name__ == '__main__':
    check(add_tuple)