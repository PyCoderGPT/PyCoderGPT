from case_MBPP_415 import _sum


def check(candidate):
    assert candidate([1, 2, 3]) == 6
    assert candidate([15, 12, 13, 10]) == 50
    assert candidate([0, 1, 2]) == 3

if __name__ == '__main__':
    check(_sum)