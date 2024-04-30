from case_MBPP_268 import digit_distance_nums


def check(candidate):
    assert candidate(1,2) == 1
    assert candidate(23,56) == 6
    assert candidate(123,256) == 7

if __name__ == '__main__':
    check(digit_distance_nums)