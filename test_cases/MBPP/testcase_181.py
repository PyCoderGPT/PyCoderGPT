from case_MBPP_181 import find_lucas


def check(candidate):
    assert candidate(9) == 76
    assert candidate(4) == 7
    assert candidate(3) == 4

if __name__ == '__main__':
    check(find_lucas)