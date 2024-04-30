from case_HE_024 import largest_divisor


def check(candidate):
    assert candidate(47) == 1
    assert candidate(98) == 49
    assert candidate(104) == 52
    assert candidate(51) == 17
    assert candidate(10) == 5
    assert candidate(53) == 1
    assert candidate(3) == 1
    assert candidate(95) == 19
    assert candidate(44) == 22
    assert candidate(8) == 4
    assert candidate(4) == 2
    assert candidate(103) == 1
    assert candidate(11) == 1
    assert candidate(46) == 23
    assert candidate(49) == 7
    assert candidate(13) == 1
    assert candidate(14) == 7
    assert candidate(54) == 27
    assert candidate(99) == 33
    assert candidate(45) == 15
    assert candidate(9) == 3
    assert candidate(7) == 1
    assert candidate(100) == 50
    assert candidate(6) == 3
    assert candidate(48) == 24
    assert candidate(15) == 5
    assert candidate(101) == 1
    assert candidate(97) == 1
    assert candidate(12) == 6
    assert candidate(105) == 35
    assert candidate(5) == 1
    assert candidate(2) == 1
    assert candidate(102) == 51

if __name__ == '__main__':
    check(largest_divisor)