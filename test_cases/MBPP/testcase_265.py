from case_MBPP_265 import difference


def check(candidate):
    assert candidate(3) == 30
    assert candidate(5) == 210
    assert candidate(2) == 6

if __name__ == '__main__':
    check(difference)