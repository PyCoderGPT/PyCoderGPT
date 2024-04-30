from case_MBPP_247 import Extract


def check(candidate):
    assert candidate([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
    assert candidate([[1,2,3],[4, 5]]) == [1,4]
    assert candidate([[9,8,1],[1,2]]) == [9,1]
    assert candidate([[5, 6], [6, 9, 9], [2, 6, 3, 13]]) == [5, 6, 2]
    assert candidate([[2, 5], [8, 6, 7], [2, 9, 12, 11]]) == [2, 8, 2]
    assert candidate([[2, 4], [1, 7, 10], [10, 9, 12, 4]]) == [2, 1, 10]
    assert candidate([[1, 1], [7, 8, 7], [6, 3, 7, 10]]) == [1, 7, 6]
    assert candidate([[5, 4], [8, 9, 5], [9, 2, 7, 8]]) == [5, 8, 9]
    assert candidate([[5, 2], [8, 2, 6], [7, 10, 3, 4]]) == [5, 8, 7]
    assert candidate([[6, 2], [8, 9, 1], [3, 4, 10, 13]]) == [6, 8, 3]
    assert candidate([[5, 4], [4, 8, 2], [2, 6, 6, 4]]) == [5, 4, 2]
    assert candidate([[6, 2], [4, 9, 9], [11, 3, 3, 4]]) == [6, 4, 11]
    assert candidate([[2, 2], [1, 3, 8], [10, 4, 4, 12]]) == [2, 1, 10]
    assert candidate([[5, 3], [4, 3, 9], [8, 3, 9, 8]]) == [5, 4, 8]
    assert candidate([[6, 3], [4, 8, 2], [6, 12, 9, 10]]) == [6, 4, 6]
    assert candidate([[6, 4], [8, 4, 3], [10, 8, 3, 13]]) == [6, 8, 10]
    assert candidate([[2, 3], [1, 7, 9], [2, 9, 3, 6]]) == [2, 1, 2]
    assert candidate([[1, 6], [2, 5, 4], [6, 12, 5, 10]]) == [1, 2, 6]
    assert candidate([[5, 7], [5, 8, 9], [10, 11, 11, 12]]) == [5, 5, 10]
    assert candidate([[6, 6], [4, 9, 9], [3, 8, 10, 4]]) == [6, 4, 3]
    assert candidate([[1, 5], [8, 9, 9], [9, 5, 10, 4]]) == [1, 8, 9]
    assert candidate([[6, 4], [2, 9, 3], [8, 10, 13, 12]]) == [6, 2, 8]
    assert candidate([[4, 7], [6, 2, 9], [4, 12, 10, 14]]) == [4, 6, 4]
    assert candidate([[3, 5], [5, 5, 3], [7, 8, 4, 14]]) == [3, 5, 7]
    assert candidate([[3, 6], [5, 6, 5], [11, 7, 3, 9]]) == [3, 5, 11]
    assert candidate([[4, 2], [7, 4, 8], [4, 10, 12, 9]]) == [4, 7, 4]
    assert candidate([[6, 1], [1, 3, 1], [6, 7, 9, 11]]) == [6, 1, 6]
    assert candidate([[3, 7], [5, 4, 6], [2, 3, 12, 6]]) == [3, 5, 2]
    assert candidate([[1, 4], [3, 2, 6], [6, 6, 10, 12]]) == [1, 3, 6]
    assert candidate([[4, 3], [3, 9, 10], [6, 4, 3, 12]]) == [4, 3, 6]
    assert candidate([[3, 2], [4, 9, 3], [6, 12, 6, 6]]) == [3, 4, 6]
    assert candidate([[4, 1], [7, 1, 7], [10, 6, 6, 14]]) == [4, 7, 10]
    assert candidate([[4, 1], [1, 2, 5], [4, 12, 7, 4]]) == [4, 1, 4]
    assert candidate([[3, 1], [6, 3, 7], [3, 12, 11, 9]]) == [3, 6, 3]
    assert candidate([[3, 6], [5, 1, 7], [2, 8, 3, 13]]) == [3, 5, 2]
    assert candidate([[2, 6], [6, 9, 10], [4, 5, 13, 5]]) == [2, 6, 4]
    assert candidate([[6, 1, 1], [3, 4]]) == [6, 3]
    assert candidate([[2, 1, 6], [8, 1]]) == [2, 8]
    assert candidate([[1, 7, 4], [5, 7]]) == [1, 5]
    assert candidate([[1, 7, 8], [7, 6]]) == [1, 7]
    assert candidate([[1, 6, 6], [9, 3]]) == [1, 9]
    assert candidate([[2, 5, 3], [1, 6]]) == [2, 1]
    assert candidate([[5, 1, 4], [1, 9]]) == [5, 1]
    assert candidate([[5, 3, 2], [1, 7]]) == [5, 1]
    assert candidate([[3, 1, 7], [3, 1]]) == [3, 3]
    assert candidate([[5, 6, 3], [7, 9]]) == [5, 7]
    assert candidate([[2, 1, 4], [9, 8]]) == [2, 9]
    assert candidate([[1, 5, 7], [1, 7]]) == [1, 1]
    assert candidate([[5, 3, 3], [9, 1]]) == [5, 9]
    assert candidate([[5, 3, 5], [3, 2]]) == [5, 3]
    assert candidate([[2, 3, 7], [4, 8]]) == [2, 4]
    assert candidate([[3, 5, 1], [5, 3]]) == [3, 5]
    assert candidate([[5, 7, 6], [8, 4]]) == [5, 8]
    assert candidate([[6, 1, 1], [6, 3]]) == [6, 6]
    assert candidate([[1, 7, 8], [6, 6]]) == [1, 6]
    assert candidate([[1, 2, 2], [6, 7]]) == [1, 6]
    assert candidate([[1, 2, 2], [6, 3]]) == [1, 6]
    assert candidate([[1, 3, 3], [9, 9]]) == [1, 9]
    assert candidate([[6, 7, 8], [7, 8]]) == [6, 7]
    assert candidate([[2, 5, 1], [2, 7]]) == [2, 2]
    assert candidate([[6, 3, 3], [1, 7]]) == [6, 1]
    assert candidate([[4, 3, 8], [8, 6]]) == [4, 8]
    assert candidate([[5, 4, 7], [1, 1]]) == [5, 1]
    assert candidate([[5, 4, 1], [3, 3]]) == [5, 3]
    assert candidate([[1, 2, 7], [9, 6]]) == [1, 9]
    assert candidate([[2, 1, 7], [8, 6]]) == [2, 8]
    assert candidate([[4, 2, 1], [5, 9]]) == [4, 5]
    assert candidate([[6, 5, 1], [6, 7]]) == [6, 6]
    assert candidate([[5, 4, 7], [9, 7]]) == [5, 9]
    assert candidate([[4, 12, 4], [5, 6]]) == [4, 5]
    assert candidate([[11, 7, 2], [5, 2]]) == [11, 5]
    assert candidate([[4, 11, 2], [4, 7]]) == [4, 4]
    assert candidate([[8, 4, 2], [5, 1]]) == [8, 5]
    assert candidate([[6, 7, 6], [6, 3]]) == [6, 6]
    assert candidate([[12, 6, 6], [4, 1]]) == [12, 4]
    assert candidate([[11, 11, 4], [2, 5]]) == [11, 2]
    assert candidate([[6, 10, 2], [4, 3]]) == [6, 4]
    assert candidate([[7, 10, 3], [1, 3]]) == [7, 1]
    assert candidate([[13, 5, 4], [3, 2]]) == [13, 3]
    assert candidate([[14, 13, 3], [5, 4]]) == [14, 5]
    assert candidate([[10, 12, 6], [6, 3]]) == [10, 6]
    assert candidate([[5, 8, 4], [2, 7]]) == [5, 2]
    assert candidate([[8, 13, 2], [6, 6]]) == [8, 6]
    assert candidate([[5, 8, 1], [3, 6]]) == [5, 3]
    assert candidate([[8, 7, 4], [4, 4]]) == [8, 4]
    assert candidate([[5, 4, 3], [2, 3]]) == [5, 2]
    assert candidate([[9, 9, 6], [1, 7]]) == [9, 1]
    assert candidate([[8, 5, 6], [5, 4]]) == [8, 5]
    assert candidate([[9, 9, 1], [5, 4]]) == [9, 5]
    assert candidate([[8, 7, 2], [4, 6]]) == [8, 4]
    assert candidate([[8, 6, 6], [5, 2]]) == [8, 5]
    assert candidate([[11, 5, 5], [3, 6]]) == [11, 3]
    assert candidate([[9, 10, 3], [5, 1]]) == [9, 5]
    assert candidate([[6, 12, 2], [1, 2]]) == [6, 1]
    assert candidate([[12, 11, 6], [5, 7]]) == [12, 5]
    assert candidate([[7, 12, 6], [4, 7]]) == [7, 4]
    assert candidate([[4, 5, 3], [5, 6]]) == [4, 5]
    assert candidate([[12, 10, 1], [6, 5]]) == [12, 6]
    assert candidate([[10, 3, 1], [3, 6]]) == [10, 3]
    assert candidate([[5, 5, 1], [4, 3]]) == [5, 4]
    assert candidate([[8, 13, 1], [5, 4]]) == [8, 5]
    assert candidate([[9, 3, 5], [3, 1]]) == [9, 3]

if __name__ == '__main__':
    check(Extract)