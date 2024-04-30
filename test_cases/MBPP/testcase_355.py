from case_MBPP_355 import find_first_occurrence


def check(candidate):
    assert candidate([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
    assert candidate([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
    assert candidate([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4

if __name__ == '__main__':
    check(find_first_occurrence)