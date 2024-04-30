from case_MBPP_099 import frequency


def check(candidate):
    assert candidate([1,2,3], 4) == 0
    assert candidate([1,2,2,3,3,3,4], 3) == 3
    assert candidate([0,1,2,3,1,2], 1) == 2

if __name__ == '__main__':
    check(frequency)