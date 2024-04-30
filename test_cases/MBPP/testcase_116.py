from case_MBPP_116 import number_of_substrings


def check(candidate):
    assert candidate("abc") == 6
    assert candidate("abcd") == 10
    assert candidate("abcde") == 15

if __name__ == '__main__':
    check(number_of_substrings)