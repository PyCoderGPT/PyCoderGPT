from case_MBPP_412 import text_starta_endb


def check(candidate):
    assert candidate("aabbbb")
    assert not candidate("aabAbbbc")
    assert not candidate("accddbbjjj")

if __name__ == '__main__':
    check(text_starta_endb)