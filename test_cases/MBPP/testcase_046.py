from case_MBPP_046 import is_undulating


def check(candidate):
    assert candidate(1212121) == True
    assert candidate(1991) == False
    assert candidate(121) == True

if __name__ == '__main__':
    check(is_undulating)