from case_MBPP_040 import centered_hexagonal_number


def check(candidate):
    assert candidate(10) == 271
    assert candidate(2) == 7
    assert candidate(9) == 217

if __name__ == '__main__':
    check(centered_hexagonal_number)