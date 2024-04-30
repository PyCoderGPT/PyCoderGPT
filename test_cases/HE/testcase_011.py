from case_HE_011 import string_xor


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

if __name__ == '__main__':
    check(string_xor)