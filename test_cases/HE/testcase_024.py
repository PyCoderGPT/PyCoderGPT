from case_HE_024 import largest_divisor


def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7

if __name__ == '__main__':
    check(largest_divisor)