from case_MBPP_230 import positive_count


def check(candidate):
    assert candidate([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
    assert candidate([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.69
    assert candidate([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.56

if __name__ == '__main__':
    check(positive_count)