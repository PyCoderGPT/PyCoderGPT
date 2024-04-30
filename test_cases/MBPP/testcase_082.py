from case_MBPP_082 import hexagonal_num


def check(candidate):
    assert candidate(10) == 190
    assert candidate(5) == 45
    assert candidate(7) == 91

if __name__ == '__main__':
    check(hexagonal_num)