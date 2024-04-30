from case_MBPP_418 import test_three_equal


def check(candidate):
    assert candidate(1,1,1) == 3
    assert candidate(-1,-2,-3) == 0
    assert candidate(1,2,2) == 2

if __name__ == '__main__':
    check(test_three_equal)