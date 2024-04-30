from case_MBPP_069 import search


def check(candidate):
    assert candidate([1,1,2,2,3]) == 3
    assert candidate([1,1,3,3,4,4,5,5,7,7,8]) == 8
    assert candidate([1,2,2,3,3,4,4]) == 1

if __name__ == '__main__':
    check(search)