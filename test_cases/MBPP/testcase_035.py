from case_MBPP_035 import tetrahedral_number


def check(candidate):
    assert candidate(5) == 35
    assert candidate(6) == 56
    assert candidate(7) == 84

if __name__ == '__main__':
    check(tetrahedral_number)