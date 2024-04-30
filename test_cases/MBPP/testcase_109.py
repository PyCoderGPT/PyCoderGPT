from case_MBPP_109 import re_arrange_array


def check(candidate):
    assert candidate([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
    assert candidate([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
    assert candidate([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]

if __name__ == '__main__':
    check(re_arrange_array)