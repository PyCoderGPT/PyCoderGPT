from case_MBPP_055 import kth_element


def check(candidate):
    assert candidate([12,3,5,7,19], 2) == 3
    assert candidate([17,24,8,23], 3) == 8
    assert candidate([16,21,25,36,4], 4) == 36

if __name__ == '__main__':
    check(kth_element)