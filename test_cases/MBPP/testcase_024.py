from case_MBPP_024 import pos_count


def check(candidate):
    assert candidate([1,-2,3,-4]) == 2
    assert candidate([3,4,5,-1]) == 3
    assert candidate([1,2,3,4]) == 4

if __name__ == '__main__':
    check(pos_count)