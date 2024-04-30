from case_MBPP_006 import find_Rotations


def check(candidate):
    assert candidate("aaaa") == 1
    assert candidate("ab") == 2
    assert candidate("abc") == 3

if __name__ == '__main__':
    check(find_Rotations)