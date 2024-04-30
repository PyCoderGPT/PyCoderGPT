from case_MBPP_057 import eulerian_num


def check(candidate):
    assert candidate(3, 1) == 4
    assert candidate(4, 1) == 11
    assert candidate(5, 3) == 26

if __name__ == '__main__':
    check(eulerian_num)