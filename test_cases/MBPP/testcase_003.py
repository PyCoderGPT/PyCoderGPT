from case_MBPP_003 import differ_At_One_Bit_Pos


def check(candidate):
    assert candidate(13,9) == True
    assert candidate(15,8) == False
    assert candidate(2,4) == False
    assert candidate(2, 3) == True
    assert candidate(5, 1) == True
    assert candidate(1, 5) == True

if __name__ == '__main__':
    check(differ_At_One_Bit_Pos)