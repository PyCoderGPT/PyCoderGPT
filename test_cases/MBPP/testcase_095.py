from case_MBPP_095 import are_equivalent


def check(candidate):
    assert candidate(36, 57) == False
    assert candidate(2, 4) == False
    assert candidate(23, 47) == True

if __name__ == '__main__':
    check(are_equivalent)