from case_MBPP_386 import is_polite


def check(candidate):
    assert candidate(7) == 11
    assert candidate(4) == 7
    assert candidate(9) == 13
    assert candidate(3) == 6
    assert candidate(5) == 9
    assert candidate(9) == 13
    assert candidate(6) == 10
    assert candidate(2) == 5
    assert candidate(7) == 11
    assert candidate(9) == 13
    assert candidate(2) == 5
    assert candidate(8) == 12
    assert candidate(8) == 12
    assert candidate(9) == 13
    assert candidate(3) == 6
    assert candidate(8) == 12
    assert candidate(9) == 13
    assert candidate(8) == 12
    assert candidate(11) == 15
    assert candidate(2) == 5
    assert candidate(7) == 11
    assert candidate(12) == 17
    assert candidate(5) == 9
    assert candidate(12) == 17
    assert candidate(6) == 10
    assert candidate(6) == 10
    assert candidate(9) == 13
    assert candidate(10) == 14
    assert candidate(9) == 13
    assert candidate(11) == 15
    assert candidate(7) == 11
    assert candidate(9) == 13
    assert candidate(8) == 12
    assert candidate(3) == 6
    assert candidate(2) == 5
    assert candidate(6) == 10
    assert candidate(3) == 6
    assert candidate(6) == 10
    assert candidate(4) == 7
    assert candidate(7) == 11
    assert candidate(2) == 5
    assert candidate(7) == 11
    assert candidate(6) == 10
    assert candidate(1) == 3
    assert candidate(9) == 13
    assert candidate(5) == 9
    assert candidate(2) == 5
    assert candidate(9) == 13
    assert candidate(5) == 9
    assert candidate(7) == 11
    assert candidate(6) == 10
    assert candidate(9) == 13
    assert candidate(7) == 11
    assert candidate(5) == 9
    assert candidate(4) == 7
    assert candidate(9) == 13
    assert candidate(5) == 9
    assert candidate(2) == 5
    assert candidate(5) == 9
    assert candidate(1) == 3
    assert candidate(1) == 3
    assert candidate(9) == 13
    assert candidate(7) == 11
    assert candidate(8) == 12
    assert candidate(1) == 3
    assert candidate(3) == 6
    assert candidate(1) == 3
    assert candidate(9) == 13
    assert candidate(2) == 5
    assert candidate(9) == 13
    assert candidate(8) == 12
    assert candidate(5) == 9
    assert candidate(12) == 17
    assert candidate(8) == 12
    assert candidate(12) == 17
    assert candidate(7) == 11
    assert candidate(12) == 17
    assert candidate(12) == 17
    assert candidate(4) == 7
    assert candidate(9) == 13
    assert candidate(6) == 10
    assert candidate(7) == 11
    assert candidate(9) == 13
    assert candidate(9) == 13
    assert candidate(9) == 13
    assert candidate(4) == 7
    assert candidate(10) == 14
    assert candidate(5) == 9
    assert candidate(5) == 9
    assert candidate(10) == 14
    assert candidate(7) == 11
    assert candidate(6) == 10
    assert candidate(8) == 12
    assert candidate(9) == 13
    assert candidate(5) == 9
    assert candidate(12) == 17
    assert candidate(13) == 18
    assert candidate(8) == 12
    assert candidate(14) == 19
    assert candidate(12) == 17
    assert candidate(14) == 19
    assert candidate(5) == 9

if __name__ == '__main__':
    check(is_polite)