from case_MBPP_103 import check_type


def check(candidate):
    assert candidate((5, 6, 7, 3, 5, 6) ) == True
    assert candidate((1, 2, "4") ) == False
    assert candidate((3, 2, 1, 4, 5) ) == True
    assert candidate((2, 1, 6, 2, 2, 3)) == True
    assert candidate((1, 7, 9, 8, 8, 1)) == True
    assert candidate((10, 11, 9, 2, 4, 3)) == True
    assert candidate((9, 1, 6, 7, 4, 4)) == True
    assert candidate((9, 9, 7, 4, 6, 3)) == True
    assert candidate((2, 10, 9, 4, 1, 7)) == True
    assert candidate((8, 9, 8, 2, 5, 5)) == True
    assert candidate((5, 10, 6, 8, 7, 9)) == True
    assert candidate((5, 5, 4, 1, 3, 6)) == True
    assert candidate((5, 8, 10, 4, 7, 1)) == True
    assert candidate((8, 9, 3, 5, 4, 1)) == True
    assert candidate((9, 8, 5, 6, 10, 1)) == True
    assert candidate((8, 5, 9, 8, 1, 5)) == True
    assert candidate((1, 2, 3, 2, 3, 3)) == True
    assert candidate((1, 2, 12, 7, 1, 10)) == True
    assert candidate((8, 11, 12, 1, 5, 4)) == True
    assert candidate((6, 1, 3, 2, 7, 8)) == True
    assert candidate((7, 3, 11, 3, 2, 11)) == True
    assert candidate((2, 1, 5, 5, 7, 3)) == True
    assert candidate((8, 7, 8, 2, 2, 4)) == True
    assert candidate((1, 3, 12, 8, 2, 3)) == True
    assert candidate((3, 3, 4, 5, 6, 11)) == True
    assert candidate((4, 3, 5, 6, 5, 9)) == True
    assert candidate((3, 7, 3, 1, 4, 10)) == True
    assert candidate((8, 10, 4, 2, 10, 1)) == True
    assert candidate((4, 9, 8, 3, 7, 6)) == True
    assert candidate((5, 2, 8, 8, 8, 2)) == True
    assert candidate((10, 2, 6, 8, 10, 3)) == True
    assert candidate((5, 6, 12, 7, 9, 11)) == True
    assert candidate((2, 4, 8, 3, 1, 7)) == True
    assert candidate((7, 3, 12, 4, 10, 6)) == True
    assert candidate((5, 6, 4, 6, 3, 1)) == True
    assert candidate((8, 3, 4, 7, 9, 4)) == True
    assert candidate((6, 5, '3')) == False
    assert candidate((6, 2, '0')) == False
    assert candidate((5, 4, '3')) == False
    assert candidate((3, 7, '5')) == False
    assert candidate((2, 6, '6')) == False
    assert candidate((4, 6, '0')) == False
    assert candidate((5, 4, '3')) == False
    assert candidate((5, 4, '1')) == False
    assert candidate((1, 7, '0')) == False
    assert candidate((3, 1, '5')) == False
    assert candidate((4, 5, '7')) == False
    assert candidate((6, 2, '3')) == False
    assert candidate((6, 3, '4')) == False
    assert candidate((4, 7, '3')) == False
    assert candidate((5, 2, '4')) == False
    assert candidate((2, 6, '3')) == False
    assert candidate((2, 2, '8')) == False
    assert candidate((3, 3, '4')) == False
    assert candidate((1, 6, '4')) == False
    assert candidate((4, 7, '3')) == False
    assert candidate((2, 1, '6')) == False
    assert candidate((3, 7, '3')) == False
    assert candidate((3, 2, '6')) == False
    assert candidate((4, 7, '7')) == False
    assert candidate((2, 4, '9')) == False
    assert candidate((3, 7, '0')) == False
    assert candidate((6, 4, '6')) == False
    assert candidate((2, 6, '5')) == False
    assert candidate((2, 5, '0')) == False
    assert candidate((3, 6, '9')) == False
    assert candidate((6, 6, '3')) == False
    assert candidate((4, 3, '3')) == False
    assert candidate((6, 7, '5')) == False
    assert candidate((1, 1, 3, 5, 7)) == True
    assert candidate((4, 7, 2, 3, 7)) == True
    assert candidate((1, 4, 2, 4, 6)) == True
    assert candidate((5, 1, 2, 3, 10)) == True
    assert candidate((1, 3, 2, 2, 2)) == True
    assert candidate((8, 1, 2, 2, 6)) == True
    assert candidate((3, 7, 1, 6, 5)) == True
    assert candidate((5, 6, 1, 9, 10)) == True
    assert candidate((5, 2, 1, 3, 6)) == True
    assert candidate((5, 2, 4, 2, 3)) == True
    assert candidate((3, 6, 4, 1, 5)) == True
    assert candidate((8, 2, 3, 4, 1)) == True
    assert candidate((8, 2, 1, 1, 9)) == True
    assert candidate((8, 1, 4, 8, 1)) == True
    assert candidate((5, 3, 2, 5, 7)) == True
    assert candidate((4, 6, 6, 5, 9)) == True
    assert candidate((6, 7, 2, 3, 1)) == True
    assert candidate((6, 3, 2, 4, 5)) == True
    assert candidate((7, 3, 2, 2, 1)) == True
    assert candidate((3, 1, 4, 1, 3)) == True
    assert candidate((2, 5, 6, 6, 8)) == True
    assert candidate((3, 2, 3, 3, 7)) == True
    assert candidate((3, 3, 5, 3, 3)) == True
    assert candidate((7, 4, 5, 8, 3)) == True
    assert candidate((3, 1, 5, 6, 7)) == True
    assert candidate((8, 7, 5, 8, 6)) == True
    assert candidate((4, 6, 5, 1, 10)) == True
    assert candidate((1, 6, 2, 8, 8)) == True
    assert candidate((8, 7, 4, 8, 6)) == True
    assert candidate((5, 2, 4, 1, 2)) == True
    assert candidate((4, 5, 6, 9, 4)) == True
    assert candidate((1, 2, 5, 7, 1)) == True
    assert candidate((7, 1, 5, 4, 6)) == True

if __name__ == '__main__':
    check(check_type)