from case_MBPP_357 import toggle_middle_bits


def check(candidate):
    assert candidate(9) == 15
    assert candidate(10) == 12
    assert candidate(11) == 13
    assert candidate(0b1000001) == 0b1111111
    assert candidate(0b1001101) == 0b1110011

if __name__ == '__main__':
    check(toggle_middle_bits)