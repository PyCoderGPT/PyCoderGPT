from case_MBPP_342 import text_match_wordz_middle


def check(candidate):
    assert candidate("pythonzabc.")==True
    assert candidate("zxyabc.")==False
    assert candidate("  lang  .")==False

if __name__ == '__main__':
    check(text_match_wordz_middle)