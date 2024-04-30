from case_MBPP_017 import opposite_Signs


def check(candidate):
    assert candidate(1,-2) == True
    assert candidate(3,2) == False
    assert candidate(-10,-10) == False
    assert candidate(-2,2) == True

if __name__ == '__main__':
    check(opposite_Signs)