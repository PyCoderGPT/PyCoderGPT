from case_MBPP_060 import add_lists


def check(candidate):
    assert candidate([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
    assert candidate([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)
    assert candidate([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)

if __name__ == '__main__':
    check(add_lists)