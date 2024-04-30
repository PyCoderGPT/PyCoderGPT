from case_MBPP_313 import bell_Number


def check(candidate):
    assert candidate(2) == 2
    assert candidate(3) == 5
    assert candidate(4) == 15

if __name__ == '__main__':
    check(bell_Number)