from case_HE_076 import is_simple_power


def check(candidate):
    assert candidate(14, 7) == False
    assert candidate(26, 5) == False
    assert candidate(1, 1)==True
    assert candidate(32, 2) == True
    assert candidate(24, 4) == False
    assert candidate(21, 5) == False
    assert candidate(9, 3)==True
    assert candidate(125, 5) == True
    assert candidate(124, 7) == False
    assert candidate(21, 4) == False
    assert candidate(2, 2) == True
    assert candidate(27, 1) == False
    assert candidate(143322, 19) == False
    assert candidate(28, 5) == False
    assert candidate(20, 4) == False
    assert candidate(17, 10) == False
    assert candidate(16807, 7) == True
    assert candidate(17, 11) == False
    assert candidate(142683, 18) == False
    assert candidate(143173, 12) == False
    assert candidate(29, 2) == False
    assert candidate(124, 5) == False
    assert candidate(16, 4) == True
    assert candidate(4, 2)==True
    assert candidate(123, 6) == False
    assert candidate(7, 7) == True
    assert candidate(125, 1) == False
    assert candidate(243, 3) == True
    assert candidate(8, 8) == True
    assert candidate(12, 2) == False
    assert candidate(256, 4) == True
    assert candidate(143962, 11) == False
    assert candidate(16, 2)== True
    assert candidate(21, 6) == False
    assert candidate(143529, 19) == False
    assert candidate(144029, 13) == False
    assert candidate(3, 3) == True
    assert candidate(343, 7) == True
    assert candidate(3125, 5) == True
    assert candidate(1, 1) == True
    assert candidate(144014, 11) == False
    assert candidate(143958, 17) == False
    assert candidate(11, 3) == False
    assert candidate(28, 6) == False
    assert candidate(131, 3) == False
    assert candidate(216, 6) == True
    assert candidate(16, 2) == True
    assert candidate(13, 3) == False
    assert candidate(59049, 9) == True
    assert candidate(125, 9) == False
    assert candidate(126, 7) == False
    assert candidate(6, 6) == True
    assert candidate(8, 3) == False
    assert candidate(27, 3) == True
    assert candidate(625, 5) == True
    assert candidate(133, 8) == False
    assert candidate(49, 7) == True
    assert candidate(4, 4) == True
    assert candidate(142251, 16) == False
    assert candidate(142224, 12) == False
    assert candidate(2401, 7) == True
    assert candidate(9, 3) == True
    assert candidate(9, 2) == False
    assert candidate(1, 12)==True
    assert candidate(25, 5) == True
    assert candidate(512, 8) == True
    assert candidate(21, 1) == False
    assert candidate(28, 1) == False
    assert candidate(4, 2) == True
    assert candidate(7, 5) == False
    assert candidate(128, 4)==False
    assert candidate(12, 6)==False
    assert candidate(64, 4) == True
    assert candidate(1024, 4) == True
    assert candidate(133, 7) == False
    assert candidate(130, 7) == False
    assert candidate(81, 9) == True
    assert candidate(1296, 6) == True
    assert candidate(126, 5) == False
    assert candidate(24, 2)==False
    assert candidate(8, 2) == True
    assert candidate(27, 2) == False
    assert candidate(81, 3) == True
    assert candidate(142711, 20) == False
    assert candidate(143214, 16)== False
    assert candidate(142575, 18) == False
    assert candidate(16, 4)==True
    assert candidate(143844, 17) == False
    assert candidate(133, 6) == False
    assert candidate(17, 9) == False
    assert candidate(7776, 6) == True
    assert candidate(13, 9) == False

if __name__ == '__main__':
    check(is_simple_power)