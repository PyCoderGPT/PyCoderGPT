from case_MBPP_262 import remove_lowercase


def check(candidate):
    assert candidate("PYTHon")==('PYTH')
    assert candidate("FInD")==('FID')
    assert candidate("STRinG")==('STRG')

if __name__ == '__main__':
    check(remove_lowercase)