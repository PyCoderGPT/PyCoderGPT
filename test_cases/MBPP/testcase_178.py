from case_MBPP_178 import set_left_most_unset_bit


def check(candidate):
    assert candidate(10) == 14
    assert candidate(12) == 14
    assert candidate(15) == 15

if __name__ == '__main__':
    check(set_left_most_unset_bit)