from case_MBPP_329 import find_First_Missing


def check(candidate):
    assert candidate([0,1,2,3]) == 4
    assert candidate([0,1,2,6,9]) == 3
    assert candidate([2,3,5,8,9]) == 0

if __name__ == '__main__':
    check(find_First_Missing)