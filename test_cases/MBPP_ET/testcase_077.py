from case_MBPP_077 import magic_square_test


def check(candidate):
    assert candidate([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert candidate([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert candidate([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False
    assert candidate([[8, 9, 3, 14], [7, 10, 9, 11], [16, 6, 13, 6], [9, 11, 17, 2]]) == False
    assert candidate([[9, 10, 6, 17], [5, 8, 4, 11], [13, 1, 5, 9], [11, 10, 17, 8]]) == False
    assert candidate([[2, 8, 3, 9], [3, 16, 5, 7], [12, 7, 5, 2], [12, 11, 12, 6]]) == False
    assert candidate([[12, 12, 6, 10], [7, 10, 4, 9], [20, 8, 9, 8], [14, 8, 16, 3]]) == False
    assert candidate([[12, 10, 1, 13], [4, 12, 3, 6], [18, 7, 5, 1], [4, 2, 15, 7]]) == False
    assert candidate([[12, 17, 3, 9], [7, 9, 11, 8], [19, 1, 11, 1], [10, 9, 15, 7]]) == False
    assert candidate([[11, 7, 2, 16], [7, 18, 4, 12], [16, 7, 13, 6], [10, 1, 18, 6]]) == False
    assert candidate([[8, 7, 5, 15], [7, 13, 6, 8], [20, 2, 11, 9], [13, 6, 15, 4]]) == False
    assert candidate([[10, 8, 3, 10], [1, 9, 7, 13], [16, 7, 14, 4], [7, 10, 18, 1]]) == False
    assert candidate([[2, 17, 1, 10], [4, 15, 5, 11], [15, 6, 5, 7], [5, 1, 14, 8]]) == False
    assert candidate([[6, 13, 5, 14], [5, 15, 11, 14], [12, 4, 15, 2], [13, 9, 13, 5]]) == False
    assert candidate([[12, 14, 5, 9], [1, 11, 9, 14], [13, 5, 14, 8], [11, 7, 13, 4]]) == False
    assert candidate([[2, 9, 2, 16], [7, 15, 4, 11], [21, 2, 13, 4], [10, 9, 20, 9]]) == False
    assert candidate([[7, 11, 2, 16], [6, 10, 9, 8], [15, 4, 12, 6], [14, 10, 18, 9]]) == False
    assert candidate([[9, 8, 3, 12], [6, 14, 5, 7], [13, 3, 6, 10], [12, 11, 15, 6]]) == False
    assert candidate([[4, 10, 4, 17], [1, 14, 3, 12], [17, 6, 13, 1], [4, 8, 12, 8]]) == False
    assert candidate([[9, 7, 6, 9], [6, 10, 8, 10], [19, 3, 5, 1], [8, 7, 18, 5]]) == False
    assert candidate([[5, 13, 1, 12], [6, 16, 7, 10], [18, 4, 8, 5], [8, 5, 16, 4]]) == False
    assert candidate([[8, 12, 3, 13], [4, 13, 13, 8], [17, 7, 15, 9], [14, 5, 14, 7]]) == False
    assert candidate([[10, 9, 2, 18], [7, 9, 13, 13], [18, 7, 9, 4], [5, 9, 14, 8]]) == False
    assert candidate([[5, 8, 5, 16], [6, 14, 9, 15], [20, 2, 13, 5], [7, 4, 18, 1]]) == False
    assert candidate([[7, 14, 6, 9], [7, 14, 13, 8], [11, 6, 9, 5], [10, 3, 10, 6]]) == False
    assert candidate([[7, 15, 5, 9], [2, 17, 7, 8], [21, 8, 8, 1], [10, 11, 15, 8]]) == False
    assert candidate([[9, 14, 5, 19], [4, 15, 11, 16], [19, 6, 13, 7], [9, 7, 10, 1]]) == False
    assert candidate([[12, 11, 6, 15], [6, 16, 5, 13], [19, 8, 11, 1], [13, 10, 11, 2]]) == False
    assert candidate([[10, 11, 5, 11], [3, 18, 10, 15], [18, 6, 5, 3], [12, 5, 18, 3]]) == False
    assert candidate([[7, 11, 4, 17], [2, 15, 4, 11], [17, 5, 5, 3], [8, 2, 20, 7]]) == False
    assert candidate([[6, 16, 4, 15], [2, 15, 11, 8], [20, 6, 14, 3], [14, 3, 20, 7]]) == False
    assert candidate([[8, 11, 3, 11], [2, 12, 9, 7], [21, 5, 9, 10], [14, 7, 11, 1]]) == False
    assert candidate([[12, 17, 4, 14], [6, 9, 4, 16], [15, 5, 14, 5], [13, 3, 10, 7]]) == False
    assert candidate([[11, 14, 2, 17], [5, 17, 4, 10], [14, 1, 8, 6], [4, 7, 14, 2]]) == False
    assert candidate([[7, 16, 2, 10], [2, 17, 6, 13], [12, 5, 10, 5], [7, 1, 15, 1]]) == False
    assert candidate([[12, 7, 4, 14], [7, 18, 5, 9], [17, 4, 12, 1], [10, 7, 17, 4]]) == False
    assert candidate([[2, 2, 4], [5, 9, 5], [8, 2, 6]]) == False
    assert candidate([[7, 10, 8], [14, 9, 6], [1, 1, 13]]) == False
    assert candidate([[7, 2, 3], [4, 1, 1], [7, 2, 9]]) == False
    assert candidate([[4, 10, 11], [7, 5, 3], [5, 1, 4]]) == False
    assert candidate([[3, 7, 1], [12, 5, 3], [1, 7, 6]]) == False
    assert candidate([[6, 11, 4], [8, 1, 2], [9, 8, 11]]) == False
    assert candidate([[4, 3, 8], [4, 5, 6], [4, 4, 10]]) == False
    assert candidate([[5, 2, 11], [10, 4, 1], [3, 6, 4]]) == False
    assert candidate([[3, 7, 9], [5, 5, 6], [6, 2, 7]]) == False
    assert candidate([[2, 3, 7], [5, 1, 5], [6, 3, 8]]) == False
    assert candidate([[1, 11, 3], [11, 10, 3], [5, 8, 3]]) == False
    assert candidate([[4, 9, 4], [8, 8, 4], [2, 8, 10]]) == False
    assert candidate([[2, 11, 3], [9, 8, 3], [9, 5, 11]]) == False
    assert candidate([[5, 8, 3], [7, 10, 4], [3, 2, 11]]) == False
    assert candidate([[3, 9, 11], [13, 1, 3], [6, 3, 9]]) == False
    assert candidate([[6, 4, 2], [13, 2, 2], [6, 1, 12]]) == False
    assert candidate([[1, 2, 7], [13, 10, 3], [3, 6, 7]]) == False
    assert candidate([[7, 2, 9], [10, 8, 5], [2, 8, 13]]) == False
    assert candidate([[4, 8, 4], [14, 10, 3], [2, 1, 9]]) == False
    assert candidate([[4, 10, 10], [5, 6, 5], [1, 2, 11]]) == False
    assert candidate([[7, 3, 2], [6, 5, 4], [6, 1, 9]]) == False
    assert candidate([[6, 3, 2], [11, 2, 6], [2, 7, 11]]) == False
    assert candidate([[4, 8, 2], [6, 8, 5], [6, 6, 4]]) == False
    assert candidate([[1, 7, 4], [9, 2, 3], [5, 8, 9]]) == False
    assert candidate([[1, 8, 7], [4, 3, 4], [3, 1, 6]]) == False
    assert candidate([[2, 6, 5], [5, 3, 3], [5, 2, 4]]) == False
    assert candidate([[6, 5, 4], [6, 7, 1], [7, 1, 5]]) == False
    assert candidate([[1, 7, 2], [10, 4, 6], [6, 4, 6]]) == False
    assert candidate([[1, 12, 5], [7, 3, 1], [7, 3, 4]]) == False
    assert candidate([[1, 10, 1], [13, 4, 6], [4, 7, 12]]) == False
    assert candidate([[1, 7, 9], [7, 2, 2], [7, 5, 12]]) == False
    assert candidate([[1, 10, 3], [5, 2, 2], [7, 6, 4]]) == False
    assert candidate([[7, 5, 7], [6, 6, 2], [2, 1, 13]]) == False
    assert candidate([[5, 9, 3], [8, 8, 2], [7, 6, 3]]) == False
    assert candidate([[4, 2, 10], [10, 6, 4], [3, 4, 3]]) == False
    assert candidate([[4, 6, 10], [11, 4, 6], [3, 6, 2]]) == False
    assert candidate([[7, 11, 5], [5, 6, 2], [8, 4, 10]]) == False
    assert candidate([[7, 5, 4], [12, 10, 1], [1, 3, 6]]) == False
    assert candidate([[6, 7, 11], [7, 6, 5], [3, 8, 4]]) == False
    assert candidate([[6, 10, 11], [10, 5, 4], [2, 4, 4]]) == False
    assert candidate([[2, 5, 3], [4, 6, 1], [7, 1, 10]]) == False
    assert candidate([[4, 7, 4], [4, 8, 4], [7, 3, 2]]) == False
    assert candidate([[5, 2, 11], [12, 7, 4], [7, 2, 6]]) == False
    assert candidate([[7, 7, 6], [7, 2, 2], [6, 7, 11]]) == False
    assert candidate([[4, 8, 8], [7, 8, 3], [8, 3, 6]]) == False
    assert candidate([[6, 6, 2], [13, 9, 4], [6, 4, 4]]) == False
    assert candidate([[6, 11, 6], [8, 8, 4], [8, 7, 2]]) == False
    assert candidate([[5, 11, 2], [14, 5, 2], [7, 5, 5]]) == False
    assert candidate([[3, 12, 11], [13, 9, 2], [2, 8, 12]]) == False
    assert candidate([[5, 7, 1], [9, 7, 6], [4, 2, 2]]) == False
    assert candidate([[2, 3, 9], [14, 8, 5], [6, 1, 7]]) == False
    assert candidate([[3, 6, 7], [14, 5, 6], [8, 8, 5]]) == False
    assert candidate([[3, 8, 2], [9, 7, 3], [4, 8, 9]]) == False
    assert candidate([[7, 2, 6], [4, 3, 2], [9, 8, 7]]) == False
    assert candidate([[4, 10, 9], [11, 9, 3], [1, 3, 2]]) == False
    assert candidate([[4, 5, 7], [5, 6, 2], [8, 2, 5]]) == False
    assert candidate([[6, 8, 5], [10, 5, 3], [7, 6, 7]]) == False
    assert candidate([[4, 7, 11], [13, 8, 6], [8, 6, 3]]) == False
    assert candidate([[4, 5, 3], [11, 7, 5], [9, 1, 7]]) == False
    assert candidate([[1, 7, 1], [7, 9, 1], [2, 1, 11]]) == False
    assert candidate([[3, 7, 9], [13, 4, 3], [1, 3, 11]]) == False
    assert candidate([[5, 4, 9], [12, 4, 1], [4, 4, 9]]) == False
    assert candidate([[1, 4, 7], [9, 1, 3], [1, 8, 10]]) == False
    assert candidate([[2, 11, 2], [11, 4, 4], [3, 5, 2]]) == False
    assert candidate([[4, 2, 1], [14, 1, 3], [3, 4, 9]]) == False
    assert candidate([[7, 4, 8], [8, 2, 3], [1, 7, 11]]) == False

if __name__ == '__main__':
    check(magic_square_test)