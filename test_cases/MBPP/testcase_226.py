from case_MBPP_226 import count_bidirectional


def check(candidate):
    assert candidate([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert candidate([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert candidate([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

if __name__ == '__main__':
    check(count_bidirectional)