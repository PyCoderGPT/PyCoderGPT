from case_MBPP_151 import is_num_decagonal


def check(candidate):
    assert candidate(3) == 27
    assert candidate(7) == 175
    assert candidate(10) == 370

if __name__ == '__main__':
    check(is_num_decagonal)