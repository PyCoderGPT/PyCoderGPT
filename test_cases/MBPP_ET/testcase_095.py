from case_MBPP_095 import areEquivalent


def check(candidate):
    assert candidate(36,57) == False
    assert candidate(2,4) == False
    assert candidate(23,47) == True
    assert candidate(37, 56) == False
    assert candidate(39, 59) == False
    assert candidate(33, 52) == False
    assert candidate(36, 54) == False
    assert candidate(32, 61) == False
    assert candidate(35, 62) == False
    assert candidate(38, 55) == False
    assert candidate(36, 60) == False
    assert candidate(32, 59) == False
    assert candidate(34, 54) == False
    assert candidate(32, 52) == False
    assert candidate(33, 59) == False
    assert candidate(31, 61) == True
    assert candidate(37, 62) == False
    assert candidate(41, 57) == False
    assert candidate(34, 60) == False
    assert candidate(34, 60) == False
    assert candidate(32, 55) == False
    assert candidate(36, 59) == False
    assert candidate(35, 54) == False
    assert candidate(35, 55) == False
    assert candidate(33, 62) == False
    assert candidate(32, 61) == False
    assert candidate(40, 53) == False
    assert candidate(35, 55) == False
    assert candidate(41, 52) == False
    assert candidate(33, 61) == False
    assert candidate(38, 53) == False
    assert candidate(41, 62) == False
    assert candidate(37, 62) == False
    assert candidate(37, 56) == False
    assert candidate(32, 56) == False
    assert candidate(32, 62) == False
    assert candidate(2, 6) == False
    assert candidate(4, 7) == False
    assert candidate(6, 1) == False
    assert candidate(1, 9) == False
    assert candidate(7, 2) == True
    assert candidate(4, 2) == False
    assert candidate(4, 2) == False
    assert candidate(7, 8) == False
    assert candidate(1, 1) == True
    assert candidate(4, 9) == False
    assert candidate(3, 6) == False
    assert candidate(3, 4) == False
    assert candidate(3, 1) == True
    assert candidate(1, 3) == True
    assert candidate(1, 8) == False
    assert candidate(2, 1) == True
    assert candidate(3, 3) == True
    assert candidate(5, 5) == True
    assert candidate(5, 5) == True
    assert candidate(3, 6) == False
    assert candidate(1, 2) == True
    assert candidate(7, 4) == False
    assert candidate(5, 4) == False
    assert candidate(2, 4) == False
    assert candidate(5, 3) == True
    assert candidate(7, 2) == True
    assert candidate(6, 9) == False
    assert candidate(7, 5) == True
    assert candidate(3, 4) == False
    assert candidate(7, 7) == True
    assert candidate(7, 3) == True
    assert candidate(5, 9) == False
    assert candidate(3, 2) == True
    assert candidate(21, 45) == False
    assert candidate(21, 45) == False
    assert candidate(22, 49) == False
    assert candidate(19, 46) == False
    assert candidate(20, 45) == False
    assert candidate(24, 46) == False
    assert candidate(18, 51) == True
    assert candidate(23, 51) == False
    assert candidate(19, 42) == False
    assert candidate(19, 45) == False
    assert candidate(28, 45) == False
    assert candidate(27, 46) == False
    assert candidate(26, 45) == False
    assert candidate(25, 43) == False
    assert candidate(27, 49) == False
    assert candidate(25, 42) == False
    assert candidate(20, 45) == False
    assert candidate(23, 42) == False
    assert candidate(27, 51) == False
    assert candidate(24, 48) == False
    assert candidate(26, 46) == False
    assert candidate(21, 48) == False
    assert candidate(22, 49) == False
    assert candidate(24, 51) == False
    assert candidate(19, 51) == False
    assert candidate(23, 43) == True
    assert candidate(26, 43) == False
    assert candidate(28, 47) == False
    assert candidate(19, 50) == False
    assert candidate(27, 52) == False
    assert candidate(27, 48) == False
    assert candidate(25, 46) == False
    assert candidate(24, 46) == False

if __name__ == '__main__':
    check(areEquivalent)