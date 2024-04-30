from case_MBPP_028 import get_equal


def check(candidate):
    assert candidate([(11, 22, 33), (44, 55, 66)]) == True
    assert candidate([(1, 2, 3), (4, 5, 6, 7)]) == False
    assert candidate([(1, 2), (3, 4)]) == True

if __name__ == '__main__':
    check(get_equal)