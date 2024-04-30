from case_MBPP_425 import check_K


def check(candidate):
    assert candidate((10, 4, 5, 6, 8), 6) == True
    assert candidate((1, 2, 3, 4, 5, 6), 7) == False
    assert candidate((7, 8, 9, 44, 11, 12), 11) == True

if __name__ == '__main__':
    check(check_K)