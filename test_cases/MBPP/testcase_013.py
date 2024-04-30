from case_MBPP_013 import test_duplicate


def check(candidate):
    assert candidate(([1,2,3,4,5]))==False
    assert candidate(([1,2,3,4, 4]))==True
    assert candidate([1,1,2,2,3,3,4,4,5])==True

if __name__ == '__main__':
    check(test_duplicate)