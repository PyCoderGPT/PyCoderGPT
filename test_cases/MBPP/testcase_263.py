from case_MBPP_263 import first_Digit


def check(candidate):
    assert candidate(123) == 1
    assert candidate(456) == 4
    assert candidate(12) == 1

if __name__ == '__main__':
    check(first_Digit)