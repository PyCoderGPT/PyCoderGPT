from case_MBPP_152 import sequential_search


def check(candidate):
    assert candidate([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
    assert candidate([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)
    assert candidate([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6)

if __name__ == '__main__':
    check(sequential_search)