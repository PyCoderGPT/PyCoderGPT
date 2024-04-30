from case_MBPP_378 import text_match_zero_one


def check(candidate):
    assert candidate("ac")==False
    assert candidate("dc")==False
    assert candidate("abbbba")==True
    assert candidate("dsabbbba")==True
    assert candidate("asbbbba")==False
    assert candidate("abaaa")==True

if __name__ == '__main__':
    check(text_match_zero_one)