from case_MBPP_020 import smallest_num


def check(candidate):
    assert candidate([10, 20, 1, 45, 99]) == 1
    assert candidate([1, 2, 3]) == 1
    assert candidate([45, 46, 50, 60]) == 45

if __name__ == '__main__':
    check(smallest_num)