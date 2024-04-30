from case_MBPP_162 import find


def check(candidate):
    assert candidate(10,3) == 3
    assert candidate(4,2) == 2
    assert candidate(20,5) == 4
    assert candidate(9, 4) == 2
    assert candidate(15, 1) == 15
    assert candidate(11, 4) == 2
    assert candidate(7, 8) == 0
    assert candidate(14, 6) == 2
    assert candidate(11, 7) == 1
    assert candidate(12, 3) == 4
    assert candidate(7, 7) == 1
    assert candidate(15, 2) == 7
    assert candidate(10, 5) == 2
    assert candidate(13, 1) == 13
    assert candidate(14, 6) == 2
    assert candidate(11, 7) == 1
    assert candidate(13, 5) == 2
    assert candidate(6, 1) == 6
    assert candidate(11, 1) == 11
    assert candidate(6, 1) == 6
    assert candidate(10, 2) == 5
    assert candidate(8, 8) == 1
    assert candidate(15, 7) == 2
    assert candidate(14, 1) == 14
    assert candidate(11, 3) == 3
    assert candidate(7, 2) == 3
    assert candidate(14, 6) == 2
    assert candidate(5, 2) == 2
    assert candidate(15, 2) == 7
    assert candidate(14, 5) == 2
    assert candidate(11, 6) == 1
    assert candidate(6, 5) == 1
    assert candidate(9, 3) == 3
    assert candidate(5, 1) == 5
    assert candidate(9, 1) == 9
    assert candidate(9, 6) == 1
    assert candidate(7, 1) == 7
    assert candidate(4, 7) == 0
    assert candidate(4, 4) == 1
    assert candidate(1, 5) == 0
    assert candidate(9, 2) == 4
    assert candidate(2, 1) == 2
    assert candidate(3, 3) == 1
    assert candidate(1, 2) == 0
    assert candidate(6, 1) == 6
    assert candidate(1, 7) == 0
    assert candidate(4, 2) == 2
    assert candidate(2, 6) == 0
    assert candidate(1, 6) == 0
    assert candidate(5, 2) == 2
    assert candidate(9, 4) == 2
    assert candidate(5, 5) == 1
    assert candidate(6, 5) == 1
    assert candidate(2, 1) == 2
    assert candidate(3, 4) == 0
    assert candidate(4, 4) == 1
    assert candidate(1, 3) == 0
    assert candidate(7, 4) == 1
    assert candidate(4, 6) == 0
    assert candidate(6, 3) == 2
    assert candidate(8, 7) == 1
    assert candidate(8, 5) == 1
    assert candidate(2, 2) == 1
    assert candidate(3, 1) == 3
    assert candidate(6, 6) == 1
    assert candidate(1, 4) == 0
    assert candidate(3, 2) == 1
    assert candidate(9, 7) == 1
    assert candidate(7, 2) == 3
    assert candidate(15, 5) == 3
    assert candidate(18, 7) == 2
    assert candidate(25, 4) == 6
    assert candidate(24, 10) == 2
    assert candidate(24, 5) == 4
    assert candidate(25, 8) == 3
    assert candidate(15, 9) == 1
    assert candidate(25, 10) == 2
    assert candidate(19, 3) == 6
    assert candidate(17, 6) == 2
    assert candidate(21, 6) == 3
    assert candidate(16, 8) == 2
    assert candidate(25, 4) == 6
    assert candidate(17, 5) == 3
    assert candidate(16, 9) == 1
    assert candidate(21, 1) == 21
    assert candidate(17, 9) == 1
    assert candidate(18, 9) == 2
    assert candidate(21, 2) == 10
    assert candidate(20, 2) == 10
    assert candidate(22, 2) == 11
    assert candidate(21, 10) == 2
    assert candidate(22, 6) == 3
    assert candidate(21, 8) == 2
    assert candidate(23, 10) == 2
    assert candidate(18, 2) == 9
    assert candidate(18, 7) == 2
    assert candidate(20, 4) == 5
    assert candidate(21, 4) == 5
    assert candidate(17, 4) == 4
    assert candidate(18, 7) == 2
    assert candidate(25, 2) == 12
    assert candidate(18, 5) == 3

if __name__ == '__main__':
    check(find)