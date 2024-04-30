from case_MBPP_194 import minimum


def check(candidate):
    assert candidate(1,2) == 1
    assert candidate(-5,-4) == -5
    assert candidate(0,0) == 0

if __name__ == '__main__':
    check(minimum)