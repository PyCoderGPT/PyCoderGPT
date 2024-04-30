from case_MBPP_303 import find_kth


def check(candidate):
    assert candidate([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert candidate([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert candidate([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8

if __name__ == '__main__':
    check(find_kth)