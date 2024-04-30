from case_MBPP_240 import sumofFactors


def check(candidate):
    assert candidate(18) == 26
    assert candidate(30) == 48
    assert candidate(6) == 8

if __name__ == '__main__':
    check(sumofFactors)