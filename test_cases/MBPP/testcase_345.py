from case_MBPP_345 import maxAverageOfPath


def check(candidate):
    assert candidate([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert candidate([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert candidate([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert candidate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

if __name__ == '__main__':
    check(maxAverageOfPath)