from case_MBPP_307 import first_repeated_char


def check(candidate):
    assert candidate("abcabc") == "a"
    assert candidate("abc") == None
    assert candidate("123123") == "1"

if __name__ == '__main__':
    check(first_repeated_char)