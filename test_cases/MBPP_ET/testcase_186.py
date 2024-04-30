from case_MBPP_186 import check_distinct


def check(candidate):
    assert candidate((1, 4, 5, 6, 1, 4)) == False
    assert candidate((1, 4, 5, 6)) == True
    assert candidate((2, 3, 4, 5, 6)) == True
    assert candidate((2, 4, 3, 6, 5, 9)) == True
    assert candidate((4, 9, 3, 6, 4, 4)) == False
    assert candidate((4, 7, 6, 1, 2, 8)) == True
    assert candidate((6, 6, 3, 3, 3, 7)) == False
    assert candidate((1, 5, 2, 10, 5, 5)) == False
    assert candidate((1, 7, 10, 11, 4, 8)) == True
    assert candidate((5, 9, 1, 8, 4, 1)) == False
    assert candidate((2, 5, 10, 6, 4, 1)) == True
    assert candidate((2, 9, 9, 10, 6, 6)) == False
    assert candidate((6, 4, 1, 1, 3, 9)) == False
    assert candidate((6, 3, 8, 8, 2, 5)) == False
    assert candidate((1, 8, 3, 6, 2, 2)) == False
    assert candidate((2, 7, 10, 1, 1, 7)) == False
    assert candidate((4, 4, 7, 11, 5, 2)) == False
    assert candidate((5, 7, 10, 9, 1, 6)) == True
    assert candidate((5, 6, 4, 7, 4, 3)) == False
    assert candidate((4, 5, 9, 7, 6, 8)) == True
    assert candidate((1, 9, 9, 10, 6, 8)) == False
    assert candidate((3, 9, 1, 7, 5, 6)) == True
    assert candidate((3, 2, 2, 6, 5, 4)) == False
    assert candidate((6, 1, 9, 8, 4, 3)) == True
    assert candidate((3, 1, 2, 10, 5, 8)) == True
    assert candidate((6, 8, 9, 4, 1, 3)) == True
    assert candidate((4, 3, 6, 9, 1, 8)) == True
    assert candidate((4, 2, 8, 7, 3, 1)) == True
    assert candidate((4, 3, 9, 4, 1, 8)) == False
    assert candidate((2, 5, 6, 10, 2, 9)) == False
    assert candidate((6, 7, 3, 2, 1, 1)) == False
    assert candidate((1, 9, 8, 9, 6, 4)) == False
    assert candidate((4, 5, 10, 9, 1, 6)) == True
    assert candidate((2, 5, 5, 8, 4, 9)) == False
    assert candidate((5, 7, 4, 7, 6, 6)) == False
    assert candidate((6, 7, 6, 8, 1, 9)) == False
    assert candidate((2, 8, 6, 11)) == True
    assert candidate((3, 3, 7, 6)) == False
    assert candidate((5, 6, 10, 9)) == True
    assert candidate((6, 4, 7, 10)) == True
    assert candidate((6, 4, 4, 6)) == False
    assert candidate((5, 5, 6, 9)) == False
    assert candidate((2, 6, 4, 2)) == False
    assert candidate((4, 3, 3, 2)) == False
    assert candidate((6, 7, 5, 6)) == False
    assert candidate((2, 9, 5, 10)) == True
    assert candidate((3, 8, 3, 5)) == False
    assert candidate((6, 5, 8, 1)) == True
    assert candidate((1, 1, 9, 8)) == False
    assert candidate((3, 5, 10, 2)) == True
    assert candidate((3, 2, 9, 2)) == False
    assert candidate((3, 8, 4, 4)) == False
    assert candidate((3, 2, 5, 7)) == True
    assert candidate((6, 2, 7, 10)) == True
    assert candidate((6, 7, 6, 3)) == False
    assert candidate((5, 4, 4, 4)) == False
    assert candidate((6, 3, 10, 11)) == True
    assert candidate((4, 9, 3, 11)) == True
    assert candidate((5, 2, 5, 8)) == False
    assert candidate((2, 6, 10, 6)) == False
    assert candidate((2, 3, 8, 10)) == True
    assert candidate((1, 2, 7, 3)) == True
    assert candidate((3, 4, 2, 8)) == True
    assert candidate((5, 6, 7, 10)) == True
    assert candidate((3, 8, 3, 10)) == False
    assert candidate((2, 4, 10, 3)) == True
    assert candidate((3, 1, 9, 11)) == True
    assert candidate((1, 1, 4, 4)) == False
    assert candidate((3, 7, 4, 7)) == False
    assert candidate((4, 8, 7, 10, 9)) == True
    assert candidate((1, 2, 2, 3, 1)) == False
    assert candidate((6, 5, 8, 4, 6)) == False
    assert candidate((5, 4, 1, 7, 6)) == True
    assert candidate((2, 2, 1, 8, 5)) == False
    assert candidate((7, 6, 3, 8, 11)) == True
    assert candidate((1, 5, 4, 9, 7)) == True
    assert candidate((4, 2, 3, 4, 1)) == False
    assert candidate((4, 4, 1, 4, 11)) == False
    assert candidate((7, 8, 8, 1, 3)) == False
    assert candidate((5, 5, 1, 2, 1)) == False
    assert candidate((4, 5, 5, 2, 10)) == False
    assert candidate((6, 5, 2, 5, 9)) == False
    assert candidate((1, 7, 7, 1, 7)) == False
    assert candidate((1, 2, 5, 7, 4)) == True
    assert candidate((1, 1, 2, 2, 5)) == False
    assert candidate((2, 4, 4, 7, 9)) == False
    assert candidate((1, 1, 5, 9, 9)) == False
    assert candidate((6, 8, 3, 4, 7)) == True
    assert candidate((4, 6, 3, 5, 9)) == True
    assert candidate((4, 5, 5, 2, 2)) == False
    assert candidate((2, 8, 7, 3, 5)) == True
    assert candidate((5, 2, 5, 6, 1)) == False
    assert candidate((4, 7, 2, 9, 1)) == True
    assert candidate((7, 8, 2, 9, 3)) == True
    assert candidate((6, 7, 3, 1, 5)) == True
    assert candidate((4, 2, 6, 9, 5)) == True
    assert candidate((4, 8, 5, 8, 5)) == False
    assert candidate((5, 3, 7, 6, 3)) == False
    assert candidate((5, 3, 1, 10, 10)) == False
    assert candidate((2, 6, 8, 8, 5)) == False
    assert candidate((2, 7, 1, 5, 11)) == True
    assert candidate((6, 7, 1, 10, 6)) == False

if __name__ == '__main__':
    check(check_distinct)