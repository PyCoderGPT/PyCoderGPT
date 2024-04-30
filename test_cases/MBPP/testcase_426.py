from case_MBPP_426 import check_smaller


def check(candidate):
    assert candidate((1, 2, 3), (2, 3, 4)) == False
    assert candidate((4, 5, 6), (3, 4, 5)) == True
    assert candidate((11, 12, 13), (10, 11, 12)) == True

if __name__ == '__main__':
    check(check_smaller)