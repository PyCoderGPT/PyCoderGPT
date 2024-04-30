from case_MBPP_308 import get_ludic


def check(candidate):
    assert candidate(10) == [1, 2, 3, 5, 7]
    assert candidate(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert candidate(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]

if __name__ == '__main__':
    check(get_ludic)