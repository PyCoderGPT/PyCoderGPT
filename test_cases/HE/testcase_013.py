from case_HE_013 import greatest_common_divisor


def check(candidate):
    assert candidate(3, 7) == 1
    assert candidate(10, 15) == 5
    assert candidate(49, 14) == 7
    assert candidate(144, 60) == 12

if __name__ == '__main__':
    check(greatest_common_divisor)