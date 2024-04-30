from case_MBPP_018 import is_octagonal


def check(candidate):
    assert candidate(5) == 65
    assert candidate(10) == 280
    assert candidate(15) == 645

if __name__ == '__main__':
    check(is_octagonal)