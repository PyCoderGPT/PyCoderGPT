from case_MBPP_327 import swap_List


def check(candidate):
    assert candidate([1,2,3]) == [3,2,1]
    assert candidate([1,2,3,4,4]) == [4,2,3,4,1]
    assert candidate([4,5,6]) == [6,5,4]

if __name__ == '__main__':
    check(swap_List)