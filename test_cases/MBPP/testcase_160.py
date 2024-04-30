from case_MBPP_160 import max_length


def check(candidate):
    assert candidate([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
    assert candidate([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])
    assert candidate([[5], [15,20,25]])==(3, [15,20,25])

if __name__ == '__main__':
    check(max_length)