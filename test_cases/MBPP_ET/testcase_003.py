from case_MBPP_003 import differ_At_One_Bit_Pos


def check(candidate):
    assert candidate(13,9) == True
    assert candidate(15,8) == False
    assert candidate(2,4) == False
    assert candidate(14, 9) == False
    assert candidate(17, 9) == False
    assert candidate(15, 7) == True
    assert candidate(8, 7) == False
    assert candidate(13, 13) == 0
    assert candidate(16, 5) == False
    assert candidate(17, 10) == False
    assert candidate(17, 10) == False
    assert candidate(9, 14) == False
    assert candidate(17, 14) == False
    assert candidate(11, 9) == True
    assert candidate(18, 7) == False
    assert candidate(18, 6) == False
    assert candidate(9, 10) == False
    assert candidate(12, 6) == False
    assert candidate(12, 12) == 0
    assert candidate(13, 10) == False
    assert candidate(15, 7) == True
    assert candidate(12, 11) == False
    assert candidate(15, 10) == False
    assert candidate(8, 12) == True
    assert candidate(9, 13) == True
    assert candidate(10, 5) == False
    assert candidate(15, 11) == True
    assert candidate(14, 11) == False
    assert candidate(9, 10) == False
    assert candidate(16, 11) == False
    assert candidate(18, 10) == False
    assert candidate(15, 11) == True
    assert candidate(14, 7) == False
    assert candidate(12, 8) == True
    assert candidate(10, 4) == False
    assert candidate(16, 12) == False
    assert candidate(11, 9) == True
    assert candidate(13, 4) == False
    assert candidate(18, 12) == False
    assert candidate(13, 13) == 0
    assert candidate(19, 7) == False
    assert candidate(16, 9) == False
    assert candidate(13, 5) == True
    assert candidate(20, 8) == False
    assert candidate(16, 12) == False
    assert candidate(16, 12) == False
    assert candidate(14, 13) == False
    assert candidate(20, 6) == False
    assert candidate(12, 3) == False
    assert candidate(13, 4) == False
    assert candidate(19, 12) == False
    assert candidate(19, 9) == False
    assert candidate(11, 10) == True
    assert candidate(16, 13) == False
    assert candidate(14, 7) == False
    assert candidate(14, 10) == True
    assert candidate(14, 7) == False
    assert candidate(13, 11) == False
    assert candidate(10, 12) == False
    assert candidate(17, 11) == False
    assert candidate(14, 3) == False
    assert candidate(15, 12) == False
    assert candidate(19, 9) == False
    assert candidate(19, 4) == False
    assert candidate(14, 12) == True
    assert candidate(17, 3) == False
    assert candidate(14, 9) == False
    assert candidate(20, 5) == False
    assert candidate(11, 10) == True
    assert candidate(4, 1) == False
    assert candidate(4, 3) == False
    assert candidate(4, 6) == True
    assert candidate(4, 5) == True
    assert candidate(1, 4) == False
    assert candidate(7, 9) == False
    assert candidate(4, 1) == False
    assert candidate(2, 4) == False
    assert candidate(4, 6) == True
    assert candidate(5, 6) == False
    assert candidate(7, 9) == False
    assert candidate(3, 8) == False
    assert candidate(7, 2) == False
    assert candidate(5, 7) == True
    assert candidate(6, 1) == False
    assert candidate(6, 9) == False
    assert candidate(2, 4) == False
    assert candidate(4, 2) == False
    assert candidate(2, 6) == True
    assert candidate(2, 3) == True
    assert candidate(6, 8) == False
    assert candidate(3, 8) == False
    assert candidate(5, 7) == True
    assert candidate(1, 1) == 0
    assert candidate(1, 2) == False
    assert candidate(5, 5) == 0
    assert candidate(4, 3) == False
    assert candidate(6, 3) == False
    assert candidate(3, 1) == True
    assert candidate(1, 1) == 0
    assert candidate(5, 1) == True
    assert candidate(4, 4) == 0
    assert candidate(1, 9) == True

if __name__ == '__main__':
    check(differ_At_One_Bit_Pos)