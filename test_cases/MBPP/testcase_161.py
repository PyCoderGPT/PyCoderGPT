from case_MBPP_161 import count_no_of_ways


def check(candidate):
    assert candidate(2, 4) == 16
    assert candidate(3, 2) == 6
    assert candidate(4, 4) == 228

if __name__ == '__main__':
    check(count_no_of_ways)