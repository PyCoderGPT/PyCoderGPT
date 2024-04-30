from case_MBPP_153 import all_unique


def check(candidate):
    assert candidate([1,2,3]) == True
    assert candidate([1,2,1,2]) == False
    assert candidate([1,2,3,4,5]) == True

if __name__ == '__main__':
    check(all_unique)