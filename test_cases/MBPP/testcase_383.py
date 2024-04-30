from case_MBPP_383 import check_monthnumber_number


def check(candidate):
    assert candidate(6)==True
    assert candidate(2)==False
    assert candidate(12)==False

if __name__ == '__main__':
    check(check_monthnumber_number)