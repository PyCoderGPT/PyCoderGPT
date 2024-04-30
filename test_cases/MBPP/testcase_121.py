from case_MBPP_121 import max_sum


def check(candidate):
    assert candidate([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert candidate([80, 60, 30, 40, 20, 10]) == 210
    assert candidate([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

if __name__ == '__main__':
    check(max_sum)