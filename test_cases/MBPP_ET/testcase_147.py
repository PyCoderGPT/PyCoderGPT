from case_MBPP_147 import even_binomial_Coeff_Sum


def check(candidate):
    assert candidate(4) == 8
    assert candidate(6) == 32
    assert candidate(2) == 2
    assert candidate(2) == 2
    assert candidate(1) == 1
    assert candidate(4) == 8
    assert candidate(5) == 16
    assert candidate(7) == 64
    assert candidate(4) == 8
    assert candidate(9) == 256
    assert candidate(1) == 1
    assert candidate(4) == 8
    assert candidate(7) == 64
    assert candidate(4) == 8
    assert candidate(1) == 1
    assert candidate(8) == 128
    assert candidate(5) == 16
    assert candidate(3) == 4
    assert candidate(3) == 4
    assert candidate(2) == 2
    assert candidate(1) == 1
    assert candidate(8) == 128
    assert candidate(9) == 256
    assert candidate(7) == 64
    assert candidate(4) == 8
    assert candidate(3) == 4
    assert candidate(5) == 16
    assert candidate(8) == 128
    assert candidate(8) == 128
    assert candidate(1) == 1
    assert candidate(2) == 2
    assert candidate(8) == 128
    assert candidate(1) == 1
    assert candidate(3) == 4
    assert candidate(2) == 2
    assert candidate(1) == 1
    assert candidate(4) == 8
    assert candidate(2) == 2
    assert candidate(11) == 1024
    assert candidate(3) == 4
    assert candidate(4) == 8
    assert candidate(10) == 512
    assert candidate(11) == 1024
    assert candidate(2) == 2
    assert candidate(3) == 4
    assert candidate(8) == 128
    assert candidate(5) == 16
    assert candidate(4) == 8
    assert candidate(1) == 1
    assert candidate(11) == 1024
    assert candidate(11) == 1024
    assert candidate(4) == 8
    assert candidate(1) == 1
    assert candidate(9) == 256
    assert candidate(5) == 16
    assert candidate(2) == 2
    assert candidate(6) == 32
    assert candidate(4) == 8
    assert candidate(5) == 16
    assert candidate(7) == 64
    assert candidate(3) == 4
    assert candidate(11) == 1024
    assert candidate(11) == 1024
    assert candidate(11) == 1024
    assert candidate(3) == 4
    assert candidate(4) == 8
    assert candidate(9) == 256
    assert candidate(1) == 1
    assert candidate(6) == 32
    assert candidate(1) == 1
    assert candidate(3) == 4
    assert candidate(1) == 1
    assert candidate(3) == 4
    assert candidate(5) == 16
    assert candidate(2) == 2
    assert candidate(7) == 64
    assert candidate(3) == 4
    assert candidate(5) == 16
    assert candidate(1) == 1
    assert candidate(6) == 32
    assert candidate(2) == 2
    assert candidate(3) == 4
    assert candidate(5) == 16
    assert candidate(6) == 32
    assert candidate(4) == 8
    assert candidate(3) == 4
    assert candidate(1) == 1
    assert candidate(3) == 4
    assert candidate(1) == 1
    assert candidate(7) == 64
    assert candidate(1) == 1
    assert candidate(6) == 32
    assert candidate(6) == 32
    assert candidate(5) == 16
    assert candidate(7) == 64
    assert candidate(2) == 2
    assert candidate(6) == 32
    assert candidate(2) == 2
    assert candidate(5) == 16
    assert candidate(3) == 4
    assert candidate(3) == 4
    assert candidate(4) == 8

if __name__ == '__main__':
    check(even_binomial_Coeff_Sum)