from case_MBPP_178 import set_left_most_unset_bit


def check(candidate):
    assert candidate(10) == 14
    assert candidate(12) == 14
    assert candidate(15) == 15
    assert candidate(13) == 15
    assert candidate(13) == 15
    assert candidate(8) == 12
    assert candidate(15) == 15
    assert candidate(10) == 14
    assert candidate(13) == 15
    assert candidate(9) == 13
    assert candidate(13) == 15
    assert candidate(9) == 13
    assert candidate(13) == 15
    assert candidate(15) == 15
    assert candidate(11) == 15
    assert candidate(9) == 13
    assert candidate(7) == 7
    assert candidate(13) == 15
    assert candidate(5) == 7
    assert candidate(14) == 15
    assert candidate(7) == 7
    assert candidate(15) == 15
    assert candidate(6) == 7
    assert candidate(12) == 14
    assert candidate(12) == 14
    assert candidate(14) == 15
    assert candidate(12) == 14
    assert candidate(7) == 7
    assert candidate(12) == 14
    assert candidate(12) == 14
    assert candidate(12) == 14
    assert candidate(11) == 15
    assert candidate(15) == 15
    assert candidate(5) == 7
    assert candidate(5) == 7
    assert candidate(7) == 7
    assert candidate(17) == 25
    assert candidate(15) == 15
    assert candidate(10) == 14
    assert candidate(16) == 24
    assert candidate(12) == 14
    assert candidate(9) == 13
    assert candidate(15) == 15
    assert candidate(11) == 15
    assert candidate(16) == 24
    assert candidate(13) == 15
    assert candidate(16) == 24
    assert candidate(8) == 12
    assert candidate(16) == 24
    assert candidate(15) == 15
    assert candidate(9) == 13
    assert candidate(14) == 15
    assert candidate(14) == 15
    assert candidate(9) == 13
    assert candidate(10) == 14
    assert candidate(16) == 24
    assert candidate(8) == 12
    assert candidate(17) == 25
    assert candidate(14) == 15
    assert candidate(8) == 12
    assert candidate(12) == 14
    assert candidate(15) == 15
    assert candidate(15) == 15
    assert candidate(9) == 13
    assert candidate(8) == 12
    assert candidate(10) == 14
    assert candidate(9) == 13
    assert candidate(11) == 15
    assert candidate(15) == 15
    assert candidate(20) == 28
    assert candidate(19) == 27
    assert candidate(11) == 15
    assert candidate(16) == 24
    assert candidate(11) == 15
    assert candidate(20) == 28
    assert candidate(12) == 14
    assert candidate(10) == 14
    assert candidate(11) == 15
    assert candidate(15) == 15
    assert candidate(15) == 15
    assert candidate(17) == 25
    assert candidate(16) == 24
    assert candidate(12) == 14
    assert candidate(18) == 26
    assert candidate(16) == 24
    assert candidate(13) == 15
    assert candidate(14) == 15
    assert candidate(17) == 25
    assert candidate(20) == 28
    assert candidate(15) == 15
    assert candidate(15) == 15
    assert candidate(11) == 15
    assert candidate(15) == 15
    assert candidate(14) == 15
    assert candidate(10) == 14
    assert candidate(19) == 27
    assert candidate(17) == 25
    assert candidate(13) == 15
    assert candidate(17) == 25
    assert candidate(19) == 27
    assert candidate(16) == 24
    assert candidate(18) == 26

if __name__ == '__main__':
    check(set_left_most_unset_bit)