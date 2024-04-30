from case_MBPP_385 import number_ctr


def check(candidate):
    assert candidate('program2bedone') == 1
    assert candidate('3wonders') == 1
    assert candidate('123') == 3
    assert candidate('3wond-1ers2') == 3

if __name__ == '__main__':
    check(number_ctr)