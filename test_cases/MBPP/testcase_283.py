from case_MBPP_283 import last_Digit_Factorial


def check(candidate):
    assert candidate(4) == 4
    assert candidate(21) == 0
    assert candidate(30) == 0

if __name__ == '__main__':
    check(last_Digit_Factorial)