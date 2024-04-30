from case_MBPP_014 import is_woodall


def check(candidate):
    assert candidate(383) == True
    assert candidate(254) == False
    assert candidate(200) == False

if __name__ == '__main__':
    check(is_woodall)