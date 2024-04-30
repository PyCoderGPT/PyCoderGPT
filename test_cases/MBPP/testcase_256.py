from case_MBPP_256 import check_Consecutive


def check(candidate):
    assert candidate([1,2,3,4,5]) == True
    assert candidate([1,2,3,5,6]) == False
    assert candidate([1,2,1]) == False

if __name__ == '__main__':
    check(check_Consecutive)