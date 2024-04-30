from case_MBPP_231 import largest_neg


def check(candidate):
    assert candidate([1,2,3,-4,-6]) == -6
    assert candidate([1,2,3,-8,-9]) == -9
    assert candidate([1,2,3,4,-1]) == -1

if __name__ == '__main__':
    check(largest_neg)