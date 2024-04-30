from case_MBPP_015 import check


def check(candidate):
    assert candidate(70) == False
    assert candidate(23) == False
    assert candidate(73) == True

if __name__ == '__main__':
    check(check)