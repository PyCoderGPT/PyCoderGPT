from case_MBPP_037 import get_Char


def check(candidate):
    assert candidate("abc") == "f"
    assert candidate("gfg") == "t"
    assert candidate("ab") == "c"

if __name__ == '__main__':
    check(get_Char)