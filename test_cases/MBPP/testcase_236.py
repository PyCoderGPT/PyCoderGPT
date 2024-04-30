from case_MBPP_236 import cal_sum


def check(candidate):
    assert candidate(9) == 49
    assert candidate(10) == 66
    assert candidate(11) == 88

if __name__ == '__main__':
    check(cal_sum)