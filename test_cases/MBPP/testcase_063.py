from case_MBPP_063 import common_in_nested_lists


def check(candidate):
    assert set(candidate([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
    assert set(candidate([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]))==set([5,23])
    assert set(candidate([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]))==set([4])

if __name__ == '__main__':
    check(common_in_nested_lists)