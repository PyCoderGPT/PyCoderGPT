from case_MBPP_187 import first_non_repeating_character


def check(candidate):
    assert candidate("abcabc") == None
    assert candidate("abc") == "a"
    assert candidate("ababc") == "c"

if __name__ == '__main__':
    check(first_non_repeating_character)