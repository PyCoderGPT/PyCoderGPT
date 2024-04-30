from case_MBPP_176 import maximum


def check(candidate):
    assert candidate(5,10) == 10
    assert candidate(-1,-2) == -1
    assert candidate(9,7) == 9

if __name__ == '__main__':
    check(maximum)