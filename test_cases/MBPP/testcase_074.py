from case_MBPP_074 import sum


def check(candidate):
    assert candidate(10,15) == 6
    assert candidate(100,150) == 93
    assert candidate(4,6) == 3

if __name__ == '__main__':
    check(sum)