from case_MBPP_275 import sum_digits


def check(candidate):
    assert candidate(345)==12
    assert candidate(12)==3
    assert candidate(97)==16

if __name__ == '__main__':
    check(sum_digits)