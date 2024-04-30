from case_MBPP_135 import division_elements


def check(candidate):
    assert candidate((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
    assert candidate((12, 6, 8, 16),(6, 3, 4, 4)) == (2, 2, 2, 4)
    assert candidate((20, 14, 36, 18),(5, 7, 6, 9)) == (4, 2, 6, 2)

if __name__ == '__main__':
    check(division_elements)