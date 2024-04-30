from case_HE_063 import fibfib


def check(candidate):
    assert candidate(4) == 2
    assert candidate(27) == 2555757
    assert candidate(15) == 1705
    assert candidate(14) == 927
    assert candidate(13) == 504
    assert candidate(12) == 274
    assert candidate(28) == 4700770
    assert candidate(8) == 24
    assert candidate(17) == 5768
    assert candidate(25) == 755476
    assert candidate(26) == 1389537
    assert candidate(29) == 8646064
    assert candidate(19) == 19513
    assert candidate(5) == 4
    assert candidate(6) == 7
    assert candidate(18) == 10609
    assert candidate(9) == 44
    assert candidate(1) == 0
    assert candidate(16) == 3136
    assert candidate(10) == 81
    assert candidate(20) == 35890
    assert candidate(0) == 0
    assert candidate(21) == 66012
    assert candidate(30) == 15902591
    assert candidate(11) == 149
    assert candidate(7) == 13
    assert candidate(2) == 1
    assert candidate(22) == 121415
    assert candidate(24) == 410744
    assert candidate(3) == 1

if __name__ == '__main__':
    check(fibfib)