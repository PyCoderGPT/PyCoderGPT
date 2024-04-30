from case_HE_023 import strlen


def check(candidate):
    assert candidate('') == 0
    assert candidate('x') == 1
    assert candidate('asdasnakj') == 9

if __name__ == '__main__':
    check(strlen)