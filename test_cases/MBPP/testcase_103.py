from case_MBPP_103 import check_type


def check(candidate):
    assert candidate((5, 6, 7, 3, 5, 6) ) == True
    assert candidate((1, 2, "4") ) == False
    assert candidate((3, 2, 1, 4, 5) ) == True

if __name__ == '__main__':
    check(check_type)