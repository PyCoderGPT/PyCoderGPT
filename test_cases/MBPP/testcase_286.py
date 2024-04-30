from case_MBPP_286 import extract_even


def check(candidate):
    assert candidate((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert candidate((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert candidate((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

if __name__ == '__main__':
    check(extract_even)