from case_MBPP_141 import find_star_num


def check(candidate):
    assert candidate(3) == 37
    assert candidate(4) == 73
    assert candidate(5) == 121

if __name__ == '__main__':
    check(find_star_num)