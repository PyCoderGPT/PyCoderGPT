from case_MBPP_077 import magic_square_test


def check(candidate):
    assert candidate([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert candidate([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert candidate([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

if __name__ == '__main__':
    check(magic_square_test)