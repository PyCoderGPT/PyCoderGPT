from case_MBPP_223 import last_Digit


def check(candidate):
    assert candidate(123) == 3
    assert candidate(25) == 5
    assert candidate(30) == 0
    assert candidate(126) == 6
    assert candidate(119) == 9
    assert candidate(120) == 0
    assert candidate(126) == 6
    assert candidate(126) == 6
    assert candidate(120) == 0
    assert candidate(124) == 4
    assert candidate(120) == 0
    assert candidate(120) == 0
    assert candidate(118) == 8
    assert candidate(120) == 0
    assert candidate(128) == 8
    assert candidate(118) == 8
    assert candidate(124) == 4
    assert candidate(127) == 7
    assert candidate(126) == 6
    assert candidate(124) == 4
    assert candidate(128) == 8
    assert candidate(126) == 6
    assert candidate(121) == 1
    assert candidate(123) == 3
    assert candidate(127) == 7
    assert candidate(118) == 8
    assert candidate(126) == 6
    assert candidate(127) == 7
    assert candidate(124) == 4
    assert candidate(119) == 9
    assert candidate(123) == 3
    assert candidate(122) == 2
    assert candidate(124) == 4
    assert candidate(119) == 9
    assert candidate(125) == 5
    assert candidate(125) == 5
    assert candidate(21) == 1
    assert candidate(26) == 6
    assert candidate(24) == 4
    assert candidate(23) == 3
    assert candidate(26) == 6
    assert candidate(26) == 6
    assert candidate(27) == 7
    assert candidate(20) == 0
    assert candidate(21) == 1
    assert candidate(22) == 2
    assert candidate(28) == 8
    assert candidate(30) == 0
    assert candidate(27) == 7
    assert candidate(30) == 0
    assert candidate(28) == 8
    assert candidate(22) == 2
    assert candidate(29) == 9
    assert candidate(27) == 7
    assert candidate(30) == 0
    assert candidate(26) == 6
    assert candidate(27) == 7
    assert candidate(30) == 0
    assert candidate(22) == 2
    assert candidate(25) == 5
    assert candidate(23) == 3
    assert candidate(28) == 8
    assert candidate(27) == 7
    assert candidate(23) == 3
    assert candidate(26) == 6
    assert candidate(25) == 5
    assert candidate(24) == 4
    assert candidate(27) == 7
    assert candidate(25) == 5
    assert candidate(33) == 3
    assert candidate(31) == 1
    assert candidate(32) == 2
    assert candidate(31) == 1
    assert candidate(27) == 7
    assert candidate(25) == 5
    assert candidate(25) == 5
    assert candidate(29) == 9
    assert candidate(32) == 2
    assert candidate(26) == 6
    assert candidate(32) == 2
    assert candidate(33) == 3
    assert candidate(27) == 7
    assert candidate(33) == 3
    assert candidate(28) == 8
    assert candidate(34) == 4
    assert candidate(32) == 2
    assert candidate(26) == 6
    assert candidate(27) == 7
    assert candidate(31) == 1
    assert candidate(26) == 6
    assert candidate(30) == 0
    assert candidate(29) == 9
    assert candidate(25) == 5
    assert candidate(25) == 5
    assert candidate(30) == 0
    assert candidate(26) == 6
    assert candidate(35) == 5
    assert candidate(29) == 9
    assert candidate(31) == 1
    assert candidate(35) == 5
    assert candidate(32) == 2
    assert candidate(34) == 4

if __name__ == '__main__':
    check(last_Digit)