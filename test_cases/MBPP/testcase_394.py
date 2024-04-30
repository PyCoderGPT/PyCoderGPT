from case_MBPP_394 import odd_position


def check(candidate):
    assert candidate([2,1,4,3,6,7,6,3]) == True
    assert candidate([4,1,2]) == True
    assert candidate([1,2,3]) == False

if __name__ == '__main__':
    check(odd_position)