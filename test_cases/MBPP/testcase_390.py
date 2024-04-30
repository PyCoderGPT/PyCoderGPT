from case_MBPP_390 import odd_num_sum


def check(candidate):
    assert candidate(2) == 82
    assert candidate(3) == 707
    assert candidate(4) == 3108

if __name__ == '__main__':
    check(odd_num_sum)