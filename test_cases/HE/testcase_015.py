from case_HE_015 import string_sequence


def check(candidate):
    assert candidate(0) == '0'
    assert candidate(3) == '0 1 2 3'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'

if __name__ == '__main__':
    check(string_sequence)