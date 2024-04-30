from case_MBPP_093 import sum_series


def check(candidate):
    assert candidate(6) == 12
    assert candidate(10) == 30
    assert candidate(9) == 25

if __name__ == '__main__':
    check(sum_series)