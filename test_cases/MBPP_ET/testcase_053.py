from case_MBPP_053 import decimal_to_binary


def check(candidate):
    assert candidate(8) == '1000'
    assert candidate(18) == '10010'
    assert candidate(7) == '111' 
    assert candidate(4) == 100
    assert candidate(13) == 1101
    assert candidate(10) == 1010
    assert candidate(13) == 1101
    assert candidate(6) == 110
    assert candidate(9) == 1001
    assert candidate(3) == 11
    assert candidate(13) == 1101
    assert candidate(7) == 111
    assert candidate(9) == 1001
    assert candidate(5) == 101
    assert candidate(8) == 1000
    assert candidate(5) == 101
    assert candidate(13) == 1101
    assert candidate(9) == 1001
    assert candidate(6) == 110
    assert candidate(13) == 1101
    assert candidate(6) == 110
    assert candidate(11) == 1011
    assert candidate(5) == 101
    assert candidate(8) == 1000
    assert candidate(12) == 1100
    assert candidate(4) == 100
    assert candidate(6) == 110
    assert candidate(8) == 1000
    assert candidate(5) == 101
    assert candidate(13) == 1101
    assert candidate(8) == 1000
    assert candidate(3) == 11
    assert candidate(11) == 1011
    assert candidate(9) == 1001
    assert candidate(7) == 111
    assert candidate(6) == 110
    assert candidate(20) == 10100
    assert candidate(21) == 10101
    assert candidate(13) == 1101
    assert candidate(15) == 1111
    assert candidate(23) == 10111
    assert candidate(20) == 10100
    assert candidate(20) == 10100
    assert candidate(17) == 10001
    assert candidate(23) == 10111
    assert candidate(13) == 1101
    assert candidate(21) == 10101
    assert candidate(23) == 10111
    assert candidate(15) == 1111
    assert candidate(20) == 10100
    assert candidate(22) == 10110
    assert candidate(16) == 10000
    assert candidate(19) == 10011
    assert candidate(23) == 10111
    assert candidate(14) == 1110
    assert candidate(16) == 10000
    assert candidate(15) == 1111
    assert candidate(21) == 10101
    assert candidate(18) == 10010
    assert candidate(13) == 1101
    assert candidate(23) == 10111
    assert candidate(20) == 10100
    assert candidate(18) == 10010
    assert candidate(22) == 10110
    assert candidate(18) == 10010
    assert candidate(20) == 10100
    assert candidate(15) == 1111
    assert candidate(13) == 1101
    assert candidate(16) == 10000
    assert candidate(10) == 1010
    assert candidate(12) == 1100
    assert candidate(8) == 1000
    assert candidate(3) == 11
    assert candidate(11) == 1011
    assert candidate(8) == 1000
    assert candidate(4) == 100
    assert candidate(12) == 1100
    assert candidate(12) == 1100
    assert candidate(11) == 1011
    assert candidate(4) == 100
    assert candidate(10) == 1010
    assert candidate(7) == 111
    assert candidate(4) == 100
    assert candidate(11) == 1011
    assert candidate(9) == 1001
    assert candidate(3) == 11
    assert candidate(8) == 1000
    assert candidate(6) == 110
    assert candidate(12) == 1100
    assert candidate(11) == 1011
    assert candidate(10) == 1010
    assert candidate(4) == 100
    assert candidate(6) == 110
    assert candidate(6) == 110
    assert candidate(4) == 100
    assert candidate(3) == 11
    assert candidate(3) == 11
    assert candidate(8) == 1000
    assert candidate(7) == 111
    assert candidate(7) == 111
    assert candidate(7) == 111
    assert candidate(11) == 1011

if __name__ == '__main__':
    check(decimal_to_binary)