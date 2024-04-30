from case_MBPP_033 import is_Diff


def check(candidate):
    assert candidate (12345) == False
    assert candidate(1212112) == True
    assert candidate(1212) == False

if __name__ == '__main__':
    check(is_Diff)