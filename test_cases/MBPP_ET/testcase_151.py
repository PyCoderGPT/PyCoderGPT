from case_MBPP_151 import is_num_decagonal


def check(candidate):
    assert candidate(3) == 27
    assert candidate(7) == 175
    assert candidate(10) == 370
    assert candidate(5) == 85
    assert candidate(1) == 1
    assert candidate(3) == 27
    assert candidate(2) == 10
    assert candidate(3) == 27
    assert candidate(8) == 232
    assert candidate(7) == 175
    assert candidate(4) == 52
    assert candidate(1) == 1
    assert candidate(4) == 52
    assert candidate(5) == 85
    assert candidate(3) == 27
    assert candidate(7) == 175
    assert candidate(4) == 52
    assert candidate(4) == 52
    assert candidate(5) == 85
    assert candidate(2) == 10
    assert candidate(1) == 1
    assert candidate(1) == 1
    assert candidate(8) == 232
    assert candidate(7) == 175
    assert candidate(4) == 52
    assert candidate(2) == 10
    assert candidate(2) == 10
    assert candidate(3) == 27
    assert candidate(4) == 52
    assert candidate(3) == 27
    assert candidate(2) == 10
    assert candidate(1) == 1
    assert candidate(8) == 232
    assert candidate(3) == 27
    assert candidate(8) == 232
    assert candidate(2) == 10
    assert candidate(10) == 370
    assert candidate(11) == 451
    assert candidate(6) == 126
    assert candidate(5) == 85
    assert candidate(12) == 540
    assert candidate(8) == 232
    assert candidate(2) == 10
    assert candidate(7) == 175
    assert candidate(5) == 85
    assert candidate(4) == 52
    assert candidate(7) == 175
    assert candidate(7) == 175
    assert candidate(4) == 52
    assert candidate(8) == 232
    assert candidate(6) == 126
    assert candidate(3) == 27
    assert candidate(4) == 52
    assert candidate(2) == 10
    assert candidate(8) == 232
    assert candidate(3) == 27
    assert candidate(5) == 85
    assert candidate(5) == 85
    assert candidate(7) == 175
    assert candidate(2) == 10
    assert candidate(10) == 370
    assert candidate(3) == 27
    assert candidate(8) == 232
    assert candidate(11) == 451
    assert candidate(12) == 540
    assert candidate(4) == 52
    assert candidate(7) == 175
    assert candidate(3) == 27
    assert candidate(12) == 540
    assert candidate(6) == 126
    assert candidate(10) == 370
    assert candidate(8) == 232
    assert candidate(8) == 232
    assert candidate(7) == 175
    assert candidate(15) == 855
    assert candidate(12) == 540
    assert candidate(15) == 855
    assert candidate(8) == 232
    assert candidate(7) == 175
    assert candidate(14) == 742
    assert candidate(13) == 637
    assert candidate(6) == 126
    assert candidate(10) == 370
    assert candidate(8) == 232
    assert candidate(10) == 370
    assert candidate(15) == 855
    assert candidate(9) == 297
    assert candidate(8) == 232
    assert candidate(14) == 742
    assert candidate(6) == 126
    assert candidate(12) == 540
    assert candidate(11) == 451
    assert candidate(11) == 451
    assert candidate(11) == 451
    assert candidate(13) == 637
    assert candidate(10) == 370
    assert candidate(8) == 232
    assert candidate(15) == 855
    assert candidate(13) == 637
    assert candidate(13) == 637
    assert candidate(5) == 85
    assert candidate(10) == 370

if __name__ == '__main__':
    check(is_num_decagonal)