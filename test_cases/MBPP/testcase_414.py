from case_MBPP_414 import sum_in_range


def check(candidate):
    assert candidate(2,5) == 8
    assert candidate(5,7) == 12
    assert candidate(7,13) == 40

if __name__ == '__main__':
    check(sum_in_range)