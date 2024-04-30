from case_MBPP_386 import is_polite


def check(candidate):
    assert candidate(7) == 11
    assert candidate(4) == 7
    assert candidate(9) == 13

if __name__ == '__main__':
    check(is_polite)