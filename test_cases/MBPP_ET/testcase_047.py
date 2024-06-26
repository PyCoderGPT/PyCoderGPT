from case_MBPP_047 import power


def check(candidate):
    assert candidate(3,4) == 81
    assert candidate(2,3) == 8
    assert candidate(5,5) == 3125
    assert candidate(1, 5) == 1
    assert candidate(8, 5) == 32768
    assert candidate(3, 9) == 19683
    assert candidate(6, 2) == 36
    assert candidate(8, 5) == 32768
    assert candidate(1, 6) == 1
    assert candidate(2, 9) == 512
    assert candidate(4, 3) == 64
    assert candidate(3, 9) == 19683
    assert candidate(7, 3) == 343
    assert candidate(2, 2) == 4
    assert candidate(7, 5) == 16807
    assert candidate(5, 7) == 78125
    assert candidate(4, 3) == 64
    assert candidate(3, 2) == 9
    assert candidate(8, 7) == 2097152
    assert candidate(1, 2) == 1
    assert candidate(8, 7) == 2097152
    assert candidate(1, 6) == 1
    assert candidate(6, 9) == 10077696
    assert candidate(4, 5) == 1024
    assert candidate(6, 2) == 36
    assert candidate(2, 8) == 256
    assert candidate(6, 9) == 10077696
    assert candidate(8, 4) == 4096
    assert candidate(7, 3) == 343
    assert candidate(3, 7) == 2187
    assert candidate(4, 2) == 16
    assert candidate(6, 1) == 6
    assert candidate(4, 4) == 256
    assert candidate(8, 4) == 4096
    assert candidate(3, 7) == 2187
    assert candidate(3, 6) == 729
    assert candidate(3, 2) == 9
    assert candidate(7, 4) == 2401
    assert candidate(4, 4) == 256
    assert candidate(4, 6) == 4096
    assert candidate(6, 8) == 1679616
    assert candidate(2, 4) == 16
    assert candidate(2, 3) == 8
    assert candidate(7, 8) == 5764801
    assert candidate(4, 4) == 256
    assert candidate(4, 2) == 16
    assert candidate(6, 1) == 6
    assert candidate(4, 8) == 65536
    assert candidate(2, 7) == 128
    assert candidate(5, 6) == 15625
    assert candidate(2, 8) == 256
    assert candidate(2, 6) == 64
    assert candidate(2, 6) == 64
    assert candidate(1, 5) == 1
    assert candidate(2, 4) == 16
    assert candidate(6, 1) == 6
    assert candidate(3, 5) == 243
    assert candidate(4, 4) == 256
    assert candidate(7, 2) == 49
    assert candidate(3, 2) == 9
    assert candidate(7, 8) == 5764801
    assert candidate(4, 7) == 16384
    assert candidate(3, 3) == 27
    assert candidate(7, 7) == 823543
    assert candidate(5, 5) == 3125
    assert candidate(6, 2) == 36
    assert candidate(4, 7) == 16384
    assert candidate(3, 4) == 81
    assert candidate(2, 6) == 64
    assert candidate(4, 4) == 256
    assert candidate(6, 10) == 60466176
    assert candidate(1, 6) == 1
    assert candidate(3, 2) == 9
    assert candidate(2, 3) == 8
    assert candidate(10, 5) == 100000
    assert candidate(4, 5) == 1024
    assert candidate(4, 6) == 4096
    assert candidate(8, 10) == 1073741824
    assert candidate(5, 10) == 9765625
    assert candidate(4, 7) == 16384
    assert candidate(10, 1) == 10
    assert candidate(5, 1) == 5
    assert candidate(2, 10) == 1024
    assert candidate(4, 7) == 16384
    assert candidate(10, 9) == 1000000000
    assert candidate(10, 9) == 1000000000
    assert candidate(3, 9) == 19683
    assert candidate(6, 10) == 60466176
    assert candidate(9, 5) == 59049
    assert candidate(5, 6) == 15625
    assert candidate(10, 8) == 100000000
    assert candidate(7, 6) == 117649
    assert candidate(6, 4) == 1296
    assert candidate(7, 7) == 823543
    assert candidate(3, 7) == 2187
    assert candidate(6, 7) == 279936
    assert candidate(6, 6) == 46656
    assert candidate(2, 9) == 512
    assert candidate(8, 1) == 8
    assert candidate(5, 9) == 1953125
    assert candidate(5, 4) == 625
    assert candidate(3, 8) == 6561

if __name__ == '__main__':
    check(power)