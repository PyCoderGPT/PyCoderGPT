from case_MBPP_001 import is_not_prime


def check(candidate):
    assert candidate(2) == False
    assert candidate(10) == True
    assert candidate(35) == True
    assert candidate(37) == False

if __name__ == '__main__':
    check(is_not_prime)