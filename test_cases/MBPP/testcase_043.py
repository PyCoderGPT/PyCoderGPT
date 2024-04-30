from case_MBPP_043 import closest_num


def check(candidate):
    assert candidate(11) == 10
    assert candidate(7) == 6
    assert candidate(12) == 11

if __name__ == '__main__':
    check(closest_num)