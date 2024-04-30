from case_HE_045 import triangle_area


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0


if __name__ == '__main__':
    check(triangle_area)