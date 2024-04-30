from case_MBPP_098 import next_power_of_2


def check(candidate):
    assert candidate(0) == 1
    assert candidate(5) == 8
    assert candidate(17) == 32

if __name__ == '__main__':
    check(next_power_of_2)