from case_MBPP_406 import text_match_three


def check(candidate):
    assert not candidate("ac")
    assert not candidate("dc")
    assert candidate("abbbba")
    assert candidate("caacabbbba")

if __name__ == '__main__':
    check(text_match_three)