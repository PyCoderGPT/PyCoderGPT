from case_MBPP_142 import ascii_value


def check(candidate):
    assert candidate('A')==65
    assert candidate('R')==82
    assert candidate('S')==83

if __name__ == '__main__':
    check(ascii_value)