from case_MBPP_107 import min_of_three


def check(candidate):
    assert candidate(10,20,0)==0
    assert candidate(19,15,18)==15
    assert candidate(-10,-20,-30)==-30
    assert candidate(9, 25, 4) == 4
    assert candidate(11, 19, 5) == 5
    assert candidate(12, 17, 4) == 4
    assert candidate(13, 15, 5) == 5
    assert candidate(6, 24, 2) == 2
    assert candidate(15, 16, 4) == 4
    assert candidate(10, 18, 4) == 4
    assert candidate(7, 23, 5) == 5
    assert candidate(12, 15, 2) == 2
    assert candidate(11, 24, 4) == 4
    assert candidate(7, 25, 1) == 1
    assert candidate(10, 24, 3) == 3
    assert candidate(11, 22, 5) == 5
    assert candidate(12, 24, 3) == 3
    assert candidate(7, 17, 5) == 5
    assert candidate(10, 23, 5) == 5
    assert candidate(7, 18, 4) == 4
    assert candidate(8, 19, 4) == 4
    assert candidate(6, 23, 2) == 2
    assert candidate(9, 24, 3) == 3
    assert candidate(10, 22, 2) == 2
    assert candidate(9, 19, 2) == 2
    assert candidate(6, 16, 2) == 2
    assert candidate(15, 18, 5) == 5
    assert candidate(6, 15, 3) == 3
    assert candidate(5, 20, 5) == 5
    assert candidate(8, 21, 1) == 1
    assert candidate(7, 21, 2) == 2
    assert candidate(9, 16, 1) == 1
    assert candidate(5, 24, 3) == 3
    assert candidate(13, 21, 5) == 5
    assert candidate(15, 18, 3) == 3
    assert candidate(11, 17, 5) == 5
    assert candidate(20, 19, 18) == 18
    assert candidate(21, 11, 19) == 11
    assert candidate(14, 17, 17) == 14
    assert candidate(24, 15, 16) == 15
    assert candidate(18, 16, 13) == 13
    assert candidate(23, 19, 18) == 18
    assert candidate(20, 12, 21) == 12
    assert candidate(20, 17, 21) == 17
    assert candidate(17, 15, 13) == 13
    assert candidate(19, 12, 17) == 12
    assert candidate(20, 12, 17) == 12
    assert candidate(21, 13, 16) == 13
    assert candidate(18, 17, 18) == 17
    assert candidate(24, 18, 14) == 14
    assert candidate(20, 10, 17) == 10
    assert candidate(24, 20, 16) == 16
    assert candidate(17, 19, 19) == 17
    assert candidate(16, 11, 23) == 11
    assert candidate(20, 12, 15) == 12
    assert candidate(19, 17, 21) == 17
    assert candidate(21, 18, 22) == 18
    assert candidate(19, 12, 19) == 12
    assert candidate(20, 20, 20) == 20
    assert candidate(14, 17, 14) == 14
    assert candidate(23, 18, 21) == 18
    assert candidate(20, 19, 16) == 16
    assert candidate(14, 12, 23) == 12
    assert candidate(14, 14, 13) == 13
    assert candidate(19, 15, 17) == 15
    assert candidate(22, 12, 18) == 12
    assert candidate(24, 10, 22) == 10
    assert candidate(18, 10, 14) == 10
    assert candidate(24, 20, 23) == 20
    assert candidate(-14, -18, -32) == -32
    assert candidate(-14, -20, -34) == -34
    assert candidate(-6, -22, -32) == -32
    assert candidate(-13, -19, -32) == -32
    assert candidate(-8, -23, -31) == -31
    assert candidate(-10, -19, -33) == -33
    assert candidate(-13, -24, -27) == -27
    assert candidate(-14, -22, -31) == -31
    assert candidate(-8, -24, -26) == -26
    assert candidate(-13, -22, -25) == -25
    assert candidate(-5, -25, -35) == -35
    assert candidate(-8, -18, -26) == -26
    assert candidate(-13, -22, -28) == -28
    assert candidate(-15, -23, -28) == -28
    assert candidate(-8, -15, -34) == -34
    assert candidate(-12, -21, -34) == -34
    assert candidate(-8, -16, -27) == -27
    assert candidate(-6, -21, -27) == -27
    assert candidate(-7, -23, -34) == -34
    assert candidate(-5, -15, -33) == -33
    assert candidate(-6, -21, -26) == -26
    assert candidate(-6, -15, -33) == -33
    assert candidate(-11, -16, -30) == -30
    assert candidate(-8, -24, -35) == -35
    assert candidate(-10, -21, -31) == -31
    assert candidate(-5, -17, -30) == -30
    assert candidate(-13, -15, -32) == -32
    assert candidate(-15, -24, -31) == -31
    assert candidate(-12, -20, -28) == -28
    assert candidate(-14, -17, -30) == -30
    assert candidate(-6, -19, -31) == -31
    assert candidate(-14, -21, -25) == -25
    assert candidate(-13, -22, -35) == -35

if __name__ == '__main__':
    check(min_of_three)