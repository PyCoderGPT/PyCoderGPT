from case_MBPP_223 import last_Digit


def check(candidate):
    assert candidate(123) == 3
    assert candidate(25) == 5
    assert candidate(30) == 0

if __name__ == '__main__':
    check(last_Digit)