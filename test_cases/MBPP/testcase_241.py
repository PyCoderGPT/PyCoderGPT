from case_MBPP_241 import text_match_wordz


def check(candidate):
    assert candidate("pythonz.")==True
    assert candidate("xyz.")==True
    assert candidate("  lang  .")==False

if __name__ == '__main__':
    check(text_match_wordz)