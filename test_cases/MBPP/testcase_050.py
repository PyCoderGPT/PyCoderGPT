from case_MBPP_050 import divisor


def check(candidate):
    assert candidate(15) == 4
    assert candidate(12) == 6
    assert candidate(9) == 3

if __name__ == '__main__':
    check(divisor)