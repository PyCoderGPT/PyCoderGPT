from case_MBPP_113 import volume_cube


def check(candidate):
    assert candidate(3)==27
    assert candidate(2)==8
    assert candidate(5)==125
    assert candidate(8) == 512
    assert candidate(5) == 125
    assert candidate(3) == 27
    assert candidate(5) == 125
    assert candidate(7) == 343
    assert candidate(1) == 1
    assert candidate(8) == 512
    assert candidate(2) == 8
    assert candidate(2) == 8
    assert candidate(8) == 512
    assert candidate(3) == 27
    assert candidate(2) == 8
    assert candidate(2) == 8
    assert candidate(7) == 343
    assert candidate(4) == 64
    assert candidate(8) == 512
    assert candidate(1) == 1
    assert candidate(5) == 125
    assert candidate(2) == 8
    assert candidate(4) == 64
    assert candidate(5) == 125
    assert candidate(3) == 27
    assert candidate(6) == 216
    assert candidate(8) == 512
    assert candidate(6) == 216
    assert candidate(3) == 27
    assert candidate(7) == 343
    assert candidate(4) == 64
    assert candidate(2) == 8
    assert candidate(3) == 27
    assert candidate(5) == 125
    assert candidate(3) == 27
    assert candidate(1) == 1
    assert candidate(1) == 1
    assert candidate(6) == 216
    assert candidate(7) == 343
    assert candidate(6) == 216
    assert candidate(6) == 216
    assert candidate(3) == 27
    assert candidate(6) == 216
    assert candidate(4) == 64
    assert candidate(7) == 343
    assert candidate(5) == 125
    assert candidate(5) == 125
    assert candidate(4) == 64
    assert candidate(5) == 125
    assert candidate(3) == 27
    assert candidate(3) == 27
    assert candidate(6) == 216
    assert candidate(6) == 216
    assert candidate(2) == 8
    assert candidate(1) == 1
    assert candidate(5) == 125
    assert candidate(5) == 125
    assert candidate(2) == 8
    assert candidate(7) == 343
    assert candidate(7) == 343
    assert candidate(4) == 64
    assert candidate(5) == 125
    assert candidate(4) == 64
    assert candidate(1) == 1
    assert candidate(7) == 343
    assert candidate(1) == 1
    assert candidate(4) == 64
    assert candidate(7) == 343
    assert candidate(4) == 64
    assert candidate(2) == 8
    assert candidate(8) == 512
    assert candidate(6) == 216
    assert candidate(3) == 27
    assert candidate(8) == 512
    assert candidate(10) == 1000
    assert candidate(9) == 729
    assert candidate(6) == 216
    assert candidate(3) == 27
    assert candidate(3) == 27
    assert candidate(6) == 216
    assert candidate(6) == 216
    assert candidate(9) == 729
    assert candidate(1) == 1
    assert candidate(5) == 125
    assert candidate(1) == 1
    assert candidate(7) == 343
    assert candidate(2) == 8
    assert candidate(4) == 64
    assert candidate(6) == 216
    assert candidate(3) == 27
    assert candidate(6) == 216
    assert candidate(9) == 729
    assert candidate(6) == 216
    assert candidate(1) == 1
    assert candidate(4) == 64
    assert candidate(4) == 64
    assert candidate(2) == 8
    assert candidate(3) == 27
    assert candidate(6) == 216
    assert candidate(1) == 1
    assert candidate(8) == 512
    assert candidate(4) == 64

if __name__ == '__main__':
    check(volume_cube)