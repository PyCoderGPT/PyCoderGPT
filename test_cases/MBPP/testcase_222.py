from case_MBPP_222 import text_match_one


def check(candidate):
    assert candidate("ac")==False
    assert candidate("dc")==False
    assert candidate("abba")==True

if __name__ == '__main__':
    check(text_match_one)