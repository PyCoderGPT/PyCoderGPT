from case_MBPP_419 import count_rotation


def check(candidate):
    assert candidate([3,2,1]) == 1
    assert candidate([4,5,1,2,3]) == 2
    assert candidate([7,8,9,1,2,3]) == 3
    assert candidate([1,2,3]) == 0
    assert candidate([1,3,2]) == 2

if __name__ == '__main__':
    check(count_rotation)