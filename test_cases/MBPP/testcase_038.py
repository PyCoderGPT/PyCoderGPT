from case_MBPP_038 import sequence


def check(candidate):
    assert candidate(10) == 6
    assert candidate(2) == 1
    assert candidate(3) == 2

if __name__ == '__main__':
    check(sequence)