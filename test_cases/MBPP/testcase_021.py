from case_MBPP_021 import max_difference


def check(candidate):
    assert candidate([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
    assert candidate([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
    assert candidate([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23

if __name__ == '__main__':
    check(max_difference)