from case_MBPP_360 import geometric_sum


def check(candidate):
    assert candidate(7) == 1.9921875
    assert candidate(4) == 1.9375
    assert candidate(8) == 1.99609375

if __name__ == '__main__':
    check(geometric_sum)