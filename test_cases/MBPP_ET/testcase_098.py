from case_MBPP_098 import next_Power_Of_2


def check(candidate):
    assert candidate(0) == 1
    assert candidate(5) == 8
    assert candidate(17) == 32
    assert candidate(2) == 2
    assert candidate(2) == 2
    assert candidate(5) == 8
    assert candidate(2) == 2
    assert candidate(1) == 1
    assert candidate(5) == 8
    assert candidate(2) == 2
    assert candidate(5) == 8
    assert candidate(3) == 4
    assert candidate(3) == 4
    assert candidate(1) == 1
    assert candidate(2) == 2
    assert candidate(4) == 4
    assert candidate(2) == 2
    assert candidate(2) == 2
    assert candidate(5) == 8
    assert candidate(4) == 4
    assert candidate(1) == 1
    assert candidate(4) == 4
    assert candidate(4) == 4
    assert candidate(3) == 4
    assert candidate(4) == 4
    assert candidate(3) == 4
    assert candidate(3) == 4
    assert candidate(5) == 8
    assert candidate(5) == 8
    assert candidate(4) == 4
    assert candidate(2) == 2
    assert candidate(2) == 2
    assert candidate(2) == 2
    assert candidate(5) == 8
    assert candidate(3) == 4
    assert candidate(2) == 2
    assert candidate(5) == 8
    assert candidate(10) == 16
    assert candidate(4) == 4
    assert candidate(1) == 1
    assert candidate(9) == 16
    assert candidate(2) == 2
    assert candidate(4) == 4
    assert candidate(2) == 2
    assert candidate(4) == 4
    assert candidate(4) == 4
    assert candidate(6) == 8
    assert candidate(8) == 8
    assert candidate(8) == 8
    assert candidate(1) == 1
    assert candidate(9) == 16
    assert candidate(1) == 1
    assert candidate(3) == 4
    assert candidate(9) == 16
    assert candidate(9) == 16
    assert candidate(1) == 1
    assert candidate(1) == 1
    assert candidate(1) == 1
    assert candidate(7) == 8
    assert candidate(2) == 2
    assert candidate(4) == 4
    assert candidate(7) == 8
    assert candidate(10) == 16
    assert candidate(8) == 8
    assert candidate(8) == 8
    assert candidate(5) == 8
    assert candidate(10) == 16
    assert candidate(5) == 8
    assert candidate(4) == 4
    assert candidate(13) == 16
    assert candidate(14) == 16
    assert candidate(17) == 32
    assert candidate(19) == 32
    assert candidate(17) == 32
    assert candidate(13) == 16
    assert candidate(17) == 32
    assert candidate(17) == 32
    assert candidate(17) == 32
    assert candidate(18) == 32
    assert candidate(15) == 16
    assert candidate(22) == 32
    assert candidate(12) == 16
    assert candidate(14) == 16
    assert candidate(14) == 16
    assert candidate(15) == 16
    assert candidate(12) == 16
    assert candidate(20) == 32
    assert candidate(21) == 32
    assert candidate(16) == 16
    assert candidate(20) == 32
    assert candidate(20) == 32
    assert candidate(19) == 32
    assert candidate(12) == 16
    assert candidate(17) == 32
    assert candidate(17) == 32
    assert candidate(19) == 32
    assert candidate(16) == 16
    assert candidate(18) == 32
    assert candidate(13) == 16
    assert candidate(22) == 32
    assert candidate(18) == 32
    assert candidate(21) == 32

if __name__ == '__main__':
    check(next_Power_Of_2)