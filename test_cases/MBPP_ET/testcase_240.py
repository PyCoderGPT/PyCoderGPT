from case_MBPP_240 import sumofFactors


def check(candidate):
    assert candidate(18) == 26
    assert candidate(30) == 48
    assert candidate(6) == 8
    assert candidate(20) == 36
    assert candidate(14) == 16
    assert candidate(13) == 0
    assert candidate(21) == 0
    assert candidate(21) == 0
    assert candidate(17) == 0
    assert candidate(16) == 30
    assert candidate(21) == 0
    assert candidate(21) == 0
    assert candidate(18) == 26
    assert candidate(17) == 0
    assert candidate(16) == 30
    assert candidate(23) == 0
    assert candidate(14) == 16
    assert candidate(14) == 16
    assert candidate(14) == 16
    assert candidate(17) == 0
    assert candidate(17) == 0
    assert candidate(19) == 0
    assert candidate(23) == 0
    assert candidate(16) == 30
    assert candidate(22) == 24
    assert candidate(13) == 0
    assert candidate(15) == 0
    assert candidate(20) == 36
    assert candidate(19) == 0
    assert candidate(15) == 0
    assert candidate(22) == 24
    assert candidate(21) == 0
    assert candidate(18) == 26
    assert candidate(16) == 30
    assert candidate(21) == 0
    assert candidate(18) == 26
    assert candidate(32) == 62
    assert candidate(28) == 48
    assert candidate(28) == 48
    assert candidate(32) == 62
    assert candidate(33) == 0
    assert candidate(31) == 0
    assert candidate(35) == 0
    assert candidate(35) == 0
    assert candidate(34) == 36
    assert candidate(25) == 0
    assert candidate(34) == 36
    assert candidate(29) == 0
    assert candidate(25) == 0
    assert candidate(32) == 62
    assert candidate(32) == 62
    assert candidate(31) == 0
    assert candidate(34) == 36
    assert candidate(28) == 48
    assert candidate(33) == 0
    assert candidate(35) == 0
    assert candidate(27) == 0
    assert candidate(34) == 36
    assert candidate(32) == 62
    assert candidate(34) == 36
    assert candidate(26) == 28
    assert candidate(33) == 0
    assert candidate(29) == 0
    assert candidate(35) == 0
    assert candidate(33) == 0
    assert candidate(26) == 28
    assert candidate(25) == 0
    assert candidate(35) == 0
    assert candidate(26) == 28
    assert candidate(11) == 0
    assert candidate(1) == 0
    assert candidate(4) == 6
    assert candidate(2) == 3
    assert candidate(4) == 6
    assert candidate(6) == 8
    assert candidate(11) == 0
    assert candidate(9) == 0
    assert candidate(10) == 12
    assert candidate(5) == 0
    assert candidate(1) == 0
    assert candidate(9) == 0
    assert candidate(9) == 0
    assert candidate(2) == 3
    assert candidate(8) == 14
    assert candidate(1) == 0
    assert candidate(7) == 0
    assert candidate(2) == 3
    assert candidate(10) == 12
    assert candidate(5) == 0
    assert candidate(7) == 0
    assert candidate(10) == 12
    assert candidate(8) == 14
    assert candidate(4) == 6
    assert candidate(1) == 0
    assert candidate(11) == 0
    assert candidate(8) == 14
    assert candidate(4) == 6
    assert candidate(3) == 0
    assert candidate(11) == 0
    assert candidate(5) == 0
    assert candidate(8) == 14
    assert candidate(8) == 14

if __name__ == '__main__':
    check(sumofFactors)