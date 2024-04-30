from case_MBPP_010 import text_lowercase_underscore


def check(candidate):
    assert candidate("aab_cbbbc")==(True)
    assert candidate("aab_Abbbc")==(False)
    assert candidate("Aaab_abbbc")==(False)

if __name__ == '__main__':
    check(text_lowercase_underscore)