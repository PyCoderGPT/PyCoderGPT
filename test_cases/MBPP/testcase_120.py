from case_MBPP_120 import next_Perfect_Square


def check(candidate):
    assert candidate(35) == 36
    assert candidate(6) == 9
    assert candidate(9) == 16

if __name__ == '__main__':
    check(next_Perfect_Square)