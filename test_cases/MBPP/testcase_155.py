from case_MBPP_155 import validate


def check(candidate):
    assert candidate(1234) == True
    assert candidate(51241) == False
    assert candidate(321) == True

if __name__ == '__main__':
    check(validate)