from case_MBPP_424 import first_odd


def check(candidate):
    assert candidate([1,3,5]) == 1
    assert candidate([2,4,1,3]) == 1
    assert candidate ([8,9,1]) == 9

if __name__ == '__main__':
    check(first_odd)