from case_MBPP_334 import move_zero


def check(candidate):
    assert candidate([1,0,2,0,3,4]) == [1,2,3,4,0,0]
    assert candidate([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]
    assert candidate([0,1,0,1,1]) == [1,1,1,0,0]

if __name__ == '__main__':
    check(move_zero)