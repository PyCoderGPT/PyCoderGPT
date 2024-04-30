from case_MBPP_019 import count_Substrings


def check(candidate):
    assert candidate('112112') == 6
    assert candidate('111') == 6
    assert candidate('1101112') == 12

if __name__ == '__main__':
    check(count_Substrings)