from case_MBPP_242 import check_monthnumb_number


def check(candidate):
    assert candidate(5)==True
    assert candidate(2)==False
    assert candidate(6)==False

if __name__ == '__main__':
    check(check_monthnumb_number)