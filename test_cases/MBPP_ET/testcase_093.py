from case_MBPP_093 import sum_series


def check(candidate):
    assert candidate(6)==12
    assert candidate(10)==30
    assert candidate(9)==25
    assert candidate(5) == 9
    assert candidate(6) == 12
    assert candidate(3) == 4
    assert candidate(5) == 9
    assert candidate(7) == 16
    assert candidate(8) == 20
    assert candidate(8) == 20
    assert candidate(11) == 36
    assert candidate(1) == 1
    assert candidate(4) == 6
    assert candidate(4) == 6
    assert candidate(8) == 20
    assert candidate(10) == 30
    assert candidate(10) == 30
    assert candidate(11) == 36
    assert candidate(10) == 30
    assert candidate(6) == 12
    assert candidate(6) == 12
    assert candidate(3) == 4
    assert candidate(8) == 20
    assert candidate(9) == 25
    assert candidate(10) == 30
    assert candidate(5) == 9
    assert candidate(3) == 4
    assert candidate(1) == 1
    assert candidate(11) == 36
    assert candidate(3) == 4
    assert candidate(10) == 30
    assert candidate(8) == 20
    assert candidate(10) == 30
    assert candidate(9) == 25
    assert candidate(3) == 4
    assert candidate(6) == 12
    assert candidate(12) == 42
    assert candidate(8) == 20
    assert candidate(5) == 9
    assert candidate(13) == 49
    assert candidate(6) == 12
    assert candidate(11) == 36
    assert candidate(13) == 49
    assert candidate(12) == 42
    assert candidate(8) == 20
    assert candidate(8) == 20
    assert candidate(15) == 64
    assert candidate(13) == 49
    assert candidate(12) == 42
    assert candidate(6) == 12
    assert candidate(13) == 49
    assert candidate(15) == 64
    assert candidate(15) == 64
    assert candidate(12) == 42
    assert candidate(11) == 36
    assert candidate(11) == 36
    assert candidate(15) == 64
    assert candidate(11) == 36
    assert candidate(7) == 16
    assert candidate(11) == 36
    assert candidate(7) == 16
    assert candidate(5) == 9
    assert candidate(10) == 30
    assert candidate(12) == 42
    assert candidate(7) == 16
    assert candidate(15) == 64
    assert candidate(9) == 25
    assert candidate(14) == 56
    assert candidate(7) == 16
    assert candidate(13) == 49
    assert candidate(4) == 6
    assert candidate(7) == 16
    assert candidate(7) == 16
    assert candidate(7) == 16
    assert candidate(7) == 16
    assert candidate(8) == 20
    assert candidate(5) == 9
    assert candidate(8) == 20
    assert candidate(11) == 36
    assert candidate(6) == 12
    assert candidate(11) == 36
    assert candidate(12) == 42
    assert candidate(4) == 6
    assert candidate(11) == 36
    assert candidate(10) == 30
    assert candidate(8) == 20
    assert candidate(5) == 9
    assert candidate(12) == 42
    assert candidate(10) == 30
    assert candidate(4) == 6
    assert candidate(6) == 12
    assert candidate(13) == 49
    assert candidate(4) == 6
    assert candidate(9) == 25
    assert candidate(12) == 42
    assert candidate(5) == 9
    assert candidate(7) == 16
    assert candidate(11) == 36
    assert candidate(13) == 49
    assert candidate(13) == 49
    assert candidate(8) == 20
    assert candidate(9) == 25

if __name__ == '__main__':
    check(sum_series)