from case_MBPP_106 import odd_values_string


def check(candidate):
    assert candidate('abcdef') == 'ace'
    assert candidate('python') == 'pto'
    assert candidate('data') == 'dt'
    assert candidate('lambs') == 'lms'

if __name__ == '__main__':
    check(odd_values_string)