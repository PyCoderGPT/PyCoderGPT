from case_MBPP_180 import highest_Power_of_2


def check(candidate):
    assert candidate(10) == 8
    assert candidate(19) == 16
    assert candidate(32) == 32

if __name__ == '__main__':
    check(highest_Power_of_2)