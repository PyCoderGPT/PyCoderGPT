from case_MBPP_189 import median_numbers


def check(candidate):
    assert candidate(25,55,65)==55.0
    assert candidate(20,10,30)==20.0
    assert candidate(15,45,75)==45.0
    assert candidate(22, 54, 68) == 54
    assert candidate(22, 57, 66) == 57
    assert candidate(22, 54, 61) == 54
    assert candidate(30, 53, 63) == 53
    assert candidate(22, 55, 61) == 55
    assert candidate(25, 60, 61) == 60
    assert candidate(22, 56, 68) == 56
    assert candidate(29, 53, 70) == 53
    assert candidate(23, 53, 66) == 53
    assert candidate(29, 58, 67) == 58
    assert candidate(27, 52, 64) == 52
    assert candidate(29, 60, 61) == 60
    assert candidate(25, 57, 61) == 57
    assert candidate(20, 50, 66) == 50
    assert candidate(21, 51, 65) == 51
    assert candidate(29, 51, 67) == 51
    assert candidate(26, 55, 69) == 55
    assert candidate(24, 53, 64) == 53
    assert candidate(28, 55, 65) == 55
    assert candidate(27, 57, 66) == 57
    assert candidate(20, 58, 70) == 58
    assert candidate(23, 56, 67) == 56
    assert candidate(28, 55, 69) == 55
    assert candidate(23, 58, 70) == 58
    assert candidate(26, 54, 62) == 54
    assert candidate(27, 51, 64) == 51
    assert candidate(28, 50, 65) == 50
    assert candidate(29, 55, 69) == 55
    assert candidate(22, 57, 70) == 57
    assert candidate(27, 52, 69) == 52
    assert candidate(30, 58, 61) == 58
    assert candidate(20, 58, 63) == 58
    assert candidate(27, 51, 69) == 51
    assert candidate(21, 12, 26) == 21
    assert candidate(18, 6, 28) == 18
    assert candidate(19, 7, 27) == 19
    assert candidate(21, 14, 25) == 21
    assert candidate(20, 7, 29) == 20
    assert candidate(15, 7, 31) == 15
    assert candidate(15, 8, 32) == 15
    assert candidate(20, 6, 34) == 20
    assert candidate(20, 7, 28) == 20
    assert candidate(21, 8, 31) == 21
    assert candidate(23, 6, 31) == 23
    assert candidate(20, 10, 34) == 20
    assert candidate(16, 14, 29) == 16
    assert candidate(16, 7, 30) == 16
    assert candidate(23, 9, 32) == 23
    assert candidate(15, 7, 28) == 15
    assert candidate(18, 5, 26) == 18
    assert candidate(22, 8, 26) == 22
    assert candidate(19, 6, 26) == 19
    assert candidate(15, 11, 30) == 15
    assert candidate(18, 5, 31) == 18
    assert candidate(19, 6, 32) == 19
    assert candidate(20, 5, 31) == 20
    assert candidate(21, 13, 26) == 21
    assert candidate(19, 5, 33) == 19
    assert candidate(24, 8, 25) == 24
    assert candidate(21, 15, 34) == 21
    assert candidate(17, 14, 31) == 17
    assert candidate(17, 8, 30) == 17
    assert candidate(21, 13, 34) == 21
    assert candidate(19, 5, 34) == 19
    assert candidate(15, 8, 30) == 15
    assert candidate(21, 12, 31) == 21
    assert candidate(19, 40, 78) == 40
    assert candidate(19, 50, 78) == 50
    assert candidate(11, 44, 73) == 44
    assert candidate(18, 42, 70) == 42
    assert candidate(11, 48, 72) == 48
    assert candidate(10, 48, 79) == 48
    assert candidate(17, 48, 79) == 48
    assert candidate(17, 46, 74) == 46
    assert candidate(20, 49, 78) == 49
    assert candidate(12, 40, 71) == 40
    assert candidate(16, 40, 79) == 40
    assert candidate(17, 40, 80) == 40
    assert candidate(15, 50, 78) == 50
    assert candidate(11, 41, 76) == 41
    assert candidate(20, 47, 73) == 47
    assert candidate(19, 50, 71) == 50
    assert candidate(10, 42, 77) == 42
    assert candidate(20, 44, 70) == 44
    assert candidate(16, 41, 78) == 41
    assert candidate(20, 49, 70) == 49
    assert candidate(11, 50, 75) == 50
    assert candidate(20, 42, 72) == 42
    assert candidate(15, 48, 74) == 48
    assert candidate(15, 49, 72) == 49
    assert candidate(10, 42, 80) == 42
    assert candidate(17, 43, 78) == 43
    assert candidate(18, 44, 73) == 44
    assert candidate(13, 50, 80) == 50
    assert candidate(14, 40, 75) == 40
    assert candidate(11, 48, 72) == 48
    assert candidate(10, 42, 75) == 42
    assert candidate(10, 42, 74) == 42
    assert candidate(15, 41, 74) == 41

if __name__ == '__main__':
    check(median_numbers)