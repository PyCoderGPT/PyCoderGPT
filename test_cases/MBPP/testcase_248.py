from case_MBPP_248 import upper_ctr


def check(candidate):
    assert candidate('PYthon') == 1
    assert candidate('BigData') == 1
    assert candidate('program') == 0

if __name__ == '__main__':
    check(upper_ctr)