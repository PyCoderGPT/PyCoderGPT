from case_MBPP_221 import check_greater


def check(candidate):
    assert candidate([1, 2, 3, 4, 5], 4) == False
    assert candidate([2, 3, 4, 5, 6], 8) == True
    assert candidate([9, 7, 4, 8, 6, 1], 11) == True

if __name__ == '__main__':
    check(check_greater)