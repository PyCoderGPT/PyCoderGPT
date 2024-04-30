from case_MBPP_188 import check_char


def check(candidate):
    assert candidate("abba") == "Valid"
    assert candidate("a") == "Valid"
    assert candidate("abcd") == "Invalid"

if __name__ == '__main__':
    check(check_char)