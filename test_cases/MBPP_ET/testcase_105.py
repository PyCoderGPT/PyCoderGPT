from case_MBPP_105 import count_Set_Bits


def check(candidate):
    assert candidate(2) == 1
    assert candidate(4) == 1
    assert candidate(6) == 2
    assert candidate(7) == 3
    assert candidate(4) == 1
    assert candidate(7) == 3
    assert candidate(3) == 2
    assert candidate(7) == 3
    assert candidate(5) == 2
    assert candidate(5) == 2
    assert candidate(6) == 2
    assert candidate(5) == 2
    assert candidate(6) == 2
    assert candidate(3) == 2
    assert candidate(3) == 2
    assert candidate(5) == 2
    assert candidate(4) == 1
    assert candidate(1) == 1
    assert candidate(3) == 2
    assert candidate(7) == 3
    assert candidate(2) == 1
    assert candidate(6) == 2
    assert candidate(3) == 2
    assert candidate(6) == 2
    assert candidate(2) == 1
    assert candidate(2) == 1
    assert candidate(5) == 2
    assert candidate(4) == 1
    assert candidate(4) == 1
    assert candidate(2) == 1
    assert candidate(7) == 3
    assert candidate(6) == 2
    assert candidate(3) == 2
    assert candidate(2) == 1
    assert candidate(7) == 3
    assert candidate(5) == 2
    assert candidate(2) == 1
    assert candidate(5) == 2
    assert candidate(5) == 2
    assert candidate(8) == 1
    assert candidate(7) == 3
    assert candidate(1) == 1
    assert candidate(7) == 3
    assert candidate(5) == 2
    assert candidate(3) == 2
    assert candidate(6) == 2
    assert candidate(3) == 2
    assert candidate(6) == 2
    assert candidate(4) == 1
    assert candidate(1) == 1
    assert candidate(6) == 2
    assert candidate(9) == 2
    assert candidate(7) == 3
    assert candidate(4) == 1
    assert candidate(2) == 1
    assert candidate(5) == 2
    assert candidate(3) == 2
    assert candidate(5) == 2
    assert candidate(8) == 1
    assert candidate(1) == 1
    assert candidate(7) == 3
    assert candidate(2) == 1
    assert candidate(4) == 1
    assert candidate(6) == 2
    assert candidate(1) == 1
    assert candidate(7) == 3
    assert candidate(3) == 2
    assert candidate(1) == 1
    assert candidate(9) == 2
    assert candidate(9) == 2
    assert candidate(6) == 2
    assert candidate(6) == 2
    assert candidate(2) == 1
    assert candidate(10) == 2
    assert candidate(4) == 1
    assert candidate(11) == 3
    assert candidate(10) == 2
    assert candidate(6) == 2
    assert candidate(5) == 2
    assert candidate(3) == 2
    assert candidate(8) == 1
    assert candidate(1) == 1
    assert candidate(8) == 1
    assert candidate(4) == 1
    assert candidate(4) == 1
    assert candidate(2) == 1
    assert candidate(8) == 1
    assert candidate(3) == 2
    assert candidate(1) == 1
    assert candidate(2) == 1
    assert candidate(10) == 2
    assert candidate(9) == 2
    assert candidate(9) == 2
    assert candidate(11) == 3
    assert candidate(5) == 2
    assert candidate(11) == 3
    assert candidate(6) == 2
    assert candidate(11) == 3
    assert candidate(8) == 1
    assert candidate(5) == 2
    assert candidate(10) == 2
    assert candidate(5) == 2

if __name__ == '__main__':
    check(count_Set_Bits)