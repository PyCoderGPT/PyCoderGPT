from case_MBPP_341 import is_nonagonal


def check(candidate):
    assert candidate(10) == 325
    assert candidate(15) == 750
    assert candidate(18) == 1089

if __name__ == '__main__':
    check(is_nonagonal)