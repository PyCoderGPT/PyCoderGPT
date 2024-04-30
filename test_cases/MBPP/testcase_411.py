from case_MBPP_411 import last


def check(candidate):
    assert candidate([1,2,3],1) == 0
    assert candidate([1,1,1,2,3,4],1) == 2
    assert candidate([2,3,2,3,6,8,9],3) == 3

if __name__ == '__main__':
    check(last)