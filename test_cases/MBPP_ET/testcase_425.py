from case_MBPP_425 import check_K


def check(candidate):
    assert candidate((10, 4, 5, 6, 8), 6) == True
    assert candidate((1, 2, 3, 4, 5, 6), 7) == False
    assert candidate((7, 8, 9, 44, 11, 12), 11) == True
    assert candidate((13, 1, 8, 3, 3), 6) == False
    assert candidate((7, 2, 9, 3, 10), 9) == True
    assert candidate((6, 2, 9, 10, 10), 9) == True
    assert candidate((13, 4, 5, 7, 5), 1) == False
    assert candidate((9, 6, 8, 5, 13), 5) == True
    assert candidate((10, 7, 8, 9, 6), 4) == False
    assert candidate((9, 4, 4, 6, 10), 9) == True
    assert candidate((14, 9, 3, 11, 9), 6) == False
    assert candidate((8, 3, 10, 7, 12), 7) == True
    assert candidate((15, 9, 6, 7, 4), 9) == True
    assert candidate((7, 8, 10, 10, 11), 6) == False
    assert candidate((15, 3, 4, 1, 6), 3) == True
    assert candidate((12, 9, 1, 8, 3), 4) == False
    assert candidate((13, 1, 6, 10, 8), 7) == False
    assert candidate((9, 1, 2, 3, 10), 2) == True
    assert candidate((7, 5, 7, 2, 13), 1) == False
    assert candidate((12, 4, 2, 10, 8), 10) == True
    assert candidate((8, 4, 4, 3, 11), 3) == True
    assert candidate((7, 1, 1, 6, 4), 4) == True
    assert candidate((12, 4, 4, 7, 3), 7) == True
    assert candidate((7, 2, 2, 2, 10), 10) == True
    assert candidate((7, 8, 5, 8, 7), 2) == False
    assert candidate((7, 3, 3, 8, 6), 2) == False
    assert candidate((8, 9, 10, 5, 3), 1) == False
    assert candidate((15, 7, 8, 5, 8), 6) == False
    assert candidate((9, 3, 2, 6, 8), 7) == False
    assert candidate((15, 6, 3, 7, 8), 1) == False
    assert candidate((11, 5, 1, 3, 13), 5) == True
    assert candidate((14, 5, 8, 7, 7), 6) == False
    assert candidate((7, 9, 5, 8, 13), 6) == False
    assert candidate((5, 2, 10, 9, 12), 1) == False
    assert candidate((14, 3, 2, 6, 7), 2) == True
    assert candidate((8, 9, 10, 1, 12), 1) == True
    assert candidate((1, 1, 7, 1, 5, 7), 8) == False
    assert candidate((4, 7, 1, 9, 3, 1), 6) == False
    assert candidate((6, 2, 7, 9, 2, 2), 5) == False
    assert candidate((3, 2, 7, 6, 3, 11), 10) == False
    assert candidate((5, 1, 6, 5, 8, 11), 2) == False
    assert candidate((4, 6, 3, 4, 10, 4), 4) == True
    assert candidate((5, 2, 4, 9, 9, 5), 9) == True
    assert candidate((2, 1, 7, 8, 6, 9), 10) == False
    assert candidate((4, 6, 8, 5, 9, 3), 2) == False
    assert candidate((2, 2, 5, 7, 5, 8), 12) == False
    assert candidate((2, 3, 2, 7, 3, 3), 8) == False
    assert candidate((3, 5, 5, 1, 9, 2), 3) == True
    assert candidate((1, 3, 7, 4, 6, 11), 12) == False
    assert candidate((5, 6, 6, 6, 7, 7), 11) == False
    assert candidate((1, 3, 4, 3, 5, 1), 6) == False
    assert candidate((2, 5, 4, 8, 8, 11), 4) == True
    assert candidate((3, 7, 3, 1, 7, 9), 8) == False
    assert candidate((4, 1, 8, 4, 5, 8), 4) == True
    assert candidate((3, 3, 1, 9, 7, 7), 10) == False
    assert candidate((5, 3, 3, 6, 2, 5), 7) == False
    assert candidate((4, 2, 7, 7, 4, 6), 12) == False
    assert candidate((1, 5, 1, 6, 7, 5), 9) == False
    assert candidate((5, 1, 7, 3, 5, 11), 10) == False
    assert candidate((5, 5, 3, 1, 2, 9), 8) == False
    assert candidate((6, 6, 7, 5, 9, 3), 12) == False
    assert candidate((6, 1, 7, 2, 7, 5), 8) == False
    assert candidate((5, 3, 6, 7, 7, 5), 2) == False
    assert candidate((6, 7, 6, 8, 2, 6), 9) == False
    assert candidate((6, 1, 7, 8, 1, 11), 9) == False
    assert candidate((5, 5, 3, 7, 3, 2), 4) == False
    assert candidate((3, 3, 1, 7, 6, 8), 3) == True
    assert candidate((1, 6, 6, 8, 7, 5), 5) == True
    assert candidate((4, 1, 4, 7, 1, 3), 3) == True
    assert candidate((8, 3, 12, 45, 7, 10), 8) == True
    assert candidate((3, 5, 4, 48, 13, 7), 11) == False
    assert candidate((2, 12, 7, 45, 8, 15), 14) == False
    assert candidate((4, 13, 5, 43, 11, 13), 7) == False
    assert candidate((10, 13, 4, 48, 13, 7), 16) == False
    assert candidate((2, 6, 4, 47, 15, 17), 14) == False
    assert candidate((5, 5, 10, 43, 8, 15), 13) == False
    assert candidate((12, 13, 6, 39, 7, 7), 8) == False
    assert candidate((5, 11, 14, 46, 8, 17), 10) == False
    assert candidate((2, 6, 13, 39, 12, 17), 11) == False
    assert candidate((2, 8, 8, 45, 13, 16), 7) == False
    assert candidate((11, 12, 12, 44, 16, 9), 6) == False
    assert candidate((5, 3, 4, 49, 9, 8), 8) == True
    assert candidate((4, 4, 13, 48, 11, 9), 10) == False
    assert candidate((5, 4, 12, 45, 15, 14), 16) == False
    assert candidate((2, 11, 10, 43, 12, 9), 15) == False
    assert candidate((12, 8, 14, 48, 7, 16), 11) == False
    assert candidate((12, 8, 5, 42, 6, 7), 11) == False
    assert candidate((3, 9, 12, 49, 13, 7), 13) == True
    assert candidate((12, 7, 4, 47, 16, 8), 10) == False
    assert candidate((10, 8, 4, 45, 14, 7), 12) == False
    assert candidate((7, 12, 11, 44, 16, 12), 12) == True
    assert candidate((10, 6, 7, 43, 9, 14), 16) == False
    assert candidate((11, 4, 5, 44, 12, 15), 13) == False
    assert candidate((8, 11, 6, 49, 7, 14), 9) == False
    assert candidate((9, 12, 7, 39, 15, 13), 7) == True
    assert candidate((10, 11, 4, 40, 6, 17), 11) == True
    assert candidate((10, 6, 13, 40, 11, 12), 14) == False
    assert candidate((11, 5, 8, 40, 6, 12), 16) == False
    assert candidate((11, 10, 8, 48, 11, 12), 10) == True
    assert candidate((12, 7, 11, 42, 8, 17), 14) == False
    assert candidate((4, 3, 13, 40, 6, 16), 7) == False
    assert candidate((4, 12, 6, 48, 6, 14), 6) == True

if __name__ == '__main__':
    check(check_K)