from case_MBPP_260 import big_sum


def check(candidate):
    assert candidate([1,2,3]) == 4
    assert candidate([-1,2,3,4]) == 3
    assert candidate([2,3,6]) == 8

if __name__ == '__main__':
    check(big_sum)