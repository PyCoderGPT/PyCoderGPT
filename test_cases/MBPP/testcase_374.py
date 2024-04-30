from case_MBPP_374 import jacobsthal_num


def check(candidate):
    assert candidate(5) == 11
    assert candidate(2) == 1
    assert candidate(4) == 5
    assert candidate(13) == 2731

if __name__ == '__main__':
    check(jacobsthal_num)