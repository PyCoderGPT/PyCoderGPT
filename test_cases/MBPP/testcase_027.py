from case_MBPP_027 import is_sublist


def check(candidate):
    assert candidate([2,4,3,5,7],[3,7])==False
    assert candidate([2,4,3,5,7],[4,3])==True
    assert candidate([2,4,3,5,7],[1,6])==False

if __name__ == '__main__':
    check(is_sublist)