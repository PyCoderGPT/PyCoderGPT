from case_MBPP_236 import cal_sum


def check(candidate):
    assert candidate(9) == 49
    assert candidate(10) == 66
    assert candidate(11) == 88
    assert candidate(11) == 88
    assert candidate(10) == 66
    assert candidate(8) == 37
    assert candidate(14) == 207
    assert candidate(12) == 117
    assert candidate(11) == 88
    assert candidate(4) == 10
    assert candidate(9) == 49
    assert candidate(12) == 117
    assert candidate(4) == 10
    assert candidate(4) == 10
    assert candidate(13) == 156
    assert candidate(5) == 15
    assert candidate(6) == 20
    assert candidate(12) == 117
    assert candidate(7) == 27
    assert candidate(4) == 10
    assert candidate(7) == 27
    assert candidate(11) == 88
    assert candidate(7) == 27
    assert candidate(13) == 156
    assert candidate(9) == 49
    assert candidate(6) == 20
    assert candidate(14) == 207
    assert candidate(9) == 49
    assert candidate(8) == 37
    assert candidate(11) == 88
    assert candidate(11) == 88
    assert candidate(13) == 156
    assert candidate(10) == 66
    assert candidate(10) == 66
    assert candidate(4) == 10
    assert candidate(7) == 27
    assert candidate(11) == 88
    assert candidate(10) == 66
    assert candidate(15) == 275
    assert candidate(14) == 207
    assert candidate(7) == 27
    assert candidate(13) == 156
    assert candidate(12) == 117
    assert candidate(5) == 15
    assert candidate(14) == 207
    assert candidate(15) == 275
    assert candidate(6) == 20
    assert candidate(9) == 49
    assert candidate(14) == 207
    assert candidate(8) == 37
    assert candidate(12) == 117
    assert candidate(7) == 27
    assert candidate(5) == 15
    assert candidate(6) == 20
    assert candidate(14) == 207
    assert candidate(6) == 20
    assert candidate(9) == 49
    assert candidate(8) == 37
    assert candidate(6) == 20
    assert candidate(12) == 117
    assert candidate(13) == 156
    assert candidate(15) == 275
    assert candidate(9) == 49
    assert candidate(5) == 15
    assert candidate(8) == 37
    assert candidate(13) == 156
    assert candidate(7) == 27
    assert candidate(8) == 37
    assert candidate(10) == 66
    assert candidate(14) == 207
    assert candidate(13) == 156
    assert candidate(6) == 20
    assert candidate(15) == 275
    assert candidate(12) == 117
    assert candidate(10) == 66
    assert candidate(9) == 49
    assert candidate(8) == 37
    assert candidate(16) == 365
    assert candidate(7) == 27
    assert candidate(8) == 37
    assert candidate(11) == 88
    assert candidate(10) == 66
    assert candidate(13) == 156
    assert candidate(12) == 117
    assert candidate(16) == 365
    assert candidate(13) == 156
    assert candidate(9) == 49
    assert candidate(9) == 49
    assert candidate(6) == 20
    assert candidate(6) == 20
    assert candidate(11) == 88
    assert candidate(9) == 49
    assert candidate(14) == 207
    assert candidate(11) == 88
    assert candidate(10) == 66
    assert candidate(9) == 49
    assert candidate(8) == 37
    assert candidate(9) == 49
    assert candidate(8) == 37
    assert candidate(15) == 275
    assert candidate(11) == 88
    assert candidate(8) == 37

if __name__ == '__main__':
    check(cal_sum)