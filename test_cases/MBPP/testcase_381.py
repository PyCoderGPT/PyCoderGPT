from case_MBPP_381 import is_decimal


def check(candidate):
    assert candidate('123.11')==True
    assert candidate('e666.86')==False
    assert candidate('3.124587')==False
    assert candidate('1.11')==True
    assert candidate('1.1.11')==False

if __name__ == '__main__':
    check(is_decimal)