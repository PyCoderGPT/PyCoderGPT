from case_MBPP_366 import check_none


def check(candidate):
    assert candidate((10, 4, 5, 6, None)) == True
    assert candidate((7, 8, 9, 11, 14)) == False
    assert candidate((1, 2, 3, 4, None)) == True

if __name__ == '__main__':
    check(check_none)