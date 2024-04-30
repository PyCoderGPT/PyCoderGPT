from case_MBPP_408 import even_position


def check(candidate):
    assert candidate([3,2,1]) == False
    assert candidate([1,2,3]) == False
    assert candidate([2,1,4]) == True

if __name__ == '__main__':
    check(even_position)