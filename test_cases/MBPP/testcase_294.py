from case_MBPP_294 import big_diff


def check(candidate):
    assert candidate([1,2,3,4]) == 3
    assert candidate([4,5,12]) == 8
    assert candidate([9,2,3]) == 7

if __name__ == '__main__':
    check(big_diff)