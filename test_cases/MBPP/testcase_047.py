from case_MBPP_047 import power


def check(candidate):
    assert candidate(3,4) == 81
    assert candidate(2,3) == 8
    assert candidate(5,5) == 3125

if __name__ == '__main__':
    check(power)