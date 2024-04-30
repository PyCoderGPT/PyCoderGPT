from case_HE_097 import multiply


def check(candidate):
    assert candidate(22, 29) == 18
    assert candidate(2882, 1009) == 18
    assert candidate(2, 5) == 10
    assert candidate(2762, 813) == 6
    assert candidate(21, 29) == 9
    assert candidate(152, 409) == 18
    assert candidate(4, 5) == 20
    assert candidate(3, 4) == 12
    assert candidate(3, 2) == 6
    assert candidate(1656, 1840) == 0
    assert candidate(1468, 1899) == 72
    assert candidate(12, 26) == 12
    assert candidate(24, 24) == 16
    assert candidate(77, 69) == 63
    assert candidate(5, 4) == 20
    assert candidate(144, 412) == 8
    assert candidate(18, -17) == 24
    assert candidate(80, 63) == 0
    assert candidate(2020, 1851) == 0, "Third test error: " + str(candidate(2020, 1851))
    assert candidate(23, 23) == 9
    assert candidate(14, -15) == 20
    assert candidate(19, -19) == 9
    assert candidate(11, -16) == 4
    assert candidate(22, 23) == 6
    assert candidate(78, 70) == 0
    assert candidate(81, 69) == 9
    assert candidate(152, 407) == 14
    assert candidate(4, 4) == 16
    assert candidate(5, 2) == 10
    assert candidate(149, 407) == 63
    assert candidate(4, 2) == 8
    assert candidate(19, 26) == 54
    assert candidate(23, 30) == 0
    assert candidate(17, 27) == 49, "Sixth test error: " + str(candidate(17, 27))      


    # Check some edge cases that are easy to work out by hand.
    assert candidate(9, -20) == 0
    assert candidate(14,-15) == 20, "Fourth test error: " + str(candidate(14,-15))
    assert candidate(1839, 2786) == 54
    assert candidate(15, 23) == 15
    assert candidate(72, 67) == 14
    assert candidate(150, 409) == 0
    assert candidate(148, 414) == 32
    assert candidate(2896, 2735) == 30
    assert candidate(2909, 1405) == 45
    assert candidate(1, 5) == 5
    assert candidate(16, 33) == 18
    assert candidate(143, 410) == 0
    assert candidate(12, -19) == 2
    assert candidate(1460, 1196) == 0
    assert candidate(3, 3) == 9
    assert candidate(13, -16) == 12
    assert candidate(2, 1) == 2
    assert candidate(72, 65) == 10
    assert candidate(18, -11) == 72
    assert candidate(1, 2) == 2
    assert candidate(146, 415) == 30
    assert candidate(71, 71) == 1
    assert candidate(21, 28) == 8
    assert candidate(148, 412) == 16, "First test error: " + str(candidate(148, 412))
    assert candidate(77, 71) == 7
    assert candidate(18, 24) == 32
    assert candidate(76, 68) == 48
    assert candidate(15, 25) == 25
    assert candidate(73, 63) == 9
    assert candidate(19, -10) == 0
    assert candidate(17, 31) == 7
    assert candidate(76, 72) == 12
    assert candidate(0, 0) == 0, "2nd edge test error: " + str(candidate(0, 0))
    assert candidate(16, 25) == 30
    assert candidate(13, -12) == 24
    assert candidate(146, 412) == 12
    assert candidate(16, 26) == 36
    assert candidate(1208, 2631) == 8
    assert candidate(4, 1) == 4
    assert candidate(14, 24) == 16
    assert candidate(1, 3) == 3
    assert candidate(147, 411) == 7
    assert candidate(19, 28) == 72, "Second test error: " + str(candidate(19, 28))
    assert candidate(12, 30) == 0
    assert candidate(146, 411) == 6
    assert candidate(1058, 1869) == 72
    assert candidate(2308, 1634) == 32
    assert candidate(153, 407) == 21
    assert candidate(18, 29) == 72
    assert candidate(1, 4) == 4
    assert candidate(1095, 1248) == 40
    assert candidate(24, 23) == 12
    assert candidate(2163, 1596) == 18
    assert candidate(1241, 1987) == 7
    assert candidate(15, 26) == 30
    assert candidate(144, 409) == 36
    assert candidate(0, 1) == 0, "1st edge test error: " + str(candidate(0, 1))
    assert candidate(2, 4) == 8
    assert candidate(74, 62) == 8
    assert candidate(81, 64) == 4
    assert candidate(17, 28) == 56
    assert candidate(1155, 2042) == 10
    assert candidate(77, 62) == 14
    assert candidate(15, -13) == 35
    assert candidate(12, -13) == 14
    assert candidate(18, 30) == 0
    assert candidate(80, 71) == 0
    assert candidate(17, 29) == 63
    assert candidate(23, 24) == 12
    assert candidate(19, 32) == 18
    assert candidate(151, 409) == 9
    assert candidate(19, -18) == 18
    assert candidate(4, 3) == 12
    assert candidate(76, 67) == 42, "Fifth test error: " + str(candidate(76, 67))

if __name__ == '__main__':
    check(multiply)