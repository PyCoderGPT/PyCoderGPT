from case_MBPP_324 import get_median


def check(candidate):
    assert candidate([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert candidate([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert candidate([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

if __name__ == '__main__':
    check(get_median)