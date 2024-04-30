from case_MBPP_157 import text_match_two_three


def check(candidate):
    assert candidate("ac")==(False)
    assert candidate("dc")==(False)
    assert candidate("abbbba")==(True)

if __name__ == '__main__':
    check(text_match_two_three)