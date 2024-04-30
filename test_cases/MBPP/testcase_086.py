from case_MBPP_086 import extract_singly


def check(candidate):
    assert set(candidate([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
    assert set(candidate([(1, 2, 3), (4, 2, 3), (7, 8)])) == set([1, 2, 3, 4, 7, 8])
    assert set(candidate([(7, 8, 9), (10, 11, 12), (10, 11)])) == set([7, 8, 9, 10, 11, 12])

if __name__ == '__main__':
    check(extract_singly)