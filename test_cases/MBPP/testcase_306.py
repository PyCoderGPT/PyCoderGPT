from case_MBPP_306 import is_Even


def check(candidate):
    assert candidate(1) == False
    assert candidate(2) == True
    assert candidate(3) == False

if __name__ == '__main__':
    check(is_Even)