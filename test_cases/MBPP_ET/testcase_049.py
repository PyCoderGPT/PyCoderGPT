from case_MBPP_049 import Find_Min_Length


def check(candidate):
    assert candidate([[1],[1,2]]) == 1
    assert candidate([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert candidate([[3,3,3],[4,4,4,4]]) == 3
    assert candidate([[3], [6, 5]]) == 1
    assert candidate([[6], [1, 4]]) == 1
    assert candidate([[5], [3, 4]]) == 1
    assert candidate([[4], [1, 7]]) == 1
    assert candidate([[6], [2, 2]]) == 1
    assert candidate([[2], [4, 1]]) == 1
    assert candidate([[6], [1, 5]]) == 1
    assert candidate([[5], [4, 5]]) == 1
    assert candidate([[6], [2, 7]]) == 1
    assert candidate([[3], [6, 6]]) == 1
    assert candidate([[4], [5, 7]]) == 1
    assert candidate([[1], [4, 1]]) == 1
    assert candidate([[3], [3, 5]]) == 1
    assert candidate([[6], [4, 1]]) == 1
    assert candidate([[1], [5, 4]]) == 1
    assert candidate([[1], [3, 7]]) == 1
    assert candidate([[6], [1, 1]]) == 1
    assert candidate([[4], [6, 6]]) == 1
    assert candidate([[6], [3, 1]]) == 1
    assert candidate([[5], [4, 4]]) == 1
    assert candidate([[3], [4, 6]]) == 1
    assert candidate([[1], [1, 2]]) == 1
    assert candidate([[4], [6, 7]]) == 1
    assert candidate([[2], [6, 2]]) == 1
    assert candidate([[3], [4, 6]]) == 1
    assert candidate([[6], [3, 2]]) == 1
    assert candidate([[5], [2, 6]]) == 1
    assert candidate([[6], [4, 1]]) == 1
    assert candidate([[6], [5, 7]]) == 1
    assert candidate([[5], [3, 1]]) == 1
    assert candidate([[2], [1, 7]]) == 1
    assert candidate([[6], [4, 4]]) == 1
    assert candidate([[4], [3, 5]]) == 1
    assert candidate([[5, 7], [2, 1, 7], [2, 4, 8, 4]]) == 2
    assert candidate([[3, 5], [3, 1, 7], [3, 5, 5, 2]]) == 2
    assert candidate([[1, 1], [1, 7, 1], [1, 5, 8, 9]]) == 2
    assert candidate([[6, 2], [6, 3, 7], [1, 2, 4, 9]]) == 2
    assert candidate([[6, 7], [2, 1, 2], [1, 1, 2, 6]]) == 2
    assert candidate([[1, 1], [1, 1, 2], [3, 1, 6, 9]]) == 2
    assert candidate([[2, 6], [5, 4, 8], [1, 3, 7, 5]]) == 2
    assert candidate([[5, 7], [3, 2, 5], [5, 7, 6, 2]]) == 2
    assert candidate([[2, 1], [1, 7, 2], [5, 2, 7, 1]]) == 2
    assert candidate([[5, 3], [6, 5, 7], [3, 1, 1, 9]]) == 2
    assert candidate([[5, 2], [1, 1, 2], [6, 5, 1, 8]]) == 2
    assert candidate([[4, 7], [3, 7, 3], [4, 3, 2, 5]]) == 2
    assert candidate([[5, 7], [1, 4, 4], [2, 1, 5, 2]]) == 2
    assert candidate([[4, 3], [5, 1, 1], [4, 4, 1, 7]]) == 2
    assert candidate([[1, 6], [1, 2, 6], [2, 1, 5, 5]]) == 2
    assert candidate([[2, 6], [1, 5, 3], [2, 4, 4, 1]]) == 2
    assert candidate([[2, 5], [1, 6, 6], [5, 5, 7, 4]]) == 2
    assert candidate([[4, 2], [4, 2, 5], [5, 2, 7, 1]]) == 2
    assert candidate([[1, 1], [3, 5, 4], [3, 3, 4, 7]]) == 2
    assert candidate([[5, 7], [2, 2, 2], [3, 7, 1, 9]]) == 2
    assert candidate([[4, 6], [2, 7, 3], [4, 7, 8, 4]]) == 2
    assert candidate([[6, 7], [2, 7, 3], [6, 3, 2, 9]]) == 2
    assert candidate([[1, 5], [3, 3, 7], [6, 5, 2, 3]]) == 2
    assert candidate([[2, 2], [4, 7, 7], [2, 7, 7, 5]]) == 2
    assert candidate([[6, 4], [3, 2, 5], [5, 3, 7, 7]]) == 2
    assert candidate([[6, 1], [2, 5, 3], [3, 6, 8, 8]]) == 2
    assert candidate([[6, 4], [5, 3, 2], [5, 5, 5, 5]]) == 2
    assert candidate([[4, 6], [1, 5, 3], [4, 3, 3, 6]]) == 2
    assert candidate([[1, 6], [6, 1, 5], [2, 3, 3, 8]]) == 2
    assert candidate([[6, 6], [6, 3, 8], [2, 7, 2, 6]]) == 2
    assert candidate([[4, 4], [3, 1, 4], [1, 3, 2, 1]]) == 2
    assert candidate([[1, 7], [3, 3, 3], [5, 2, 7, 9]]) == 2
    assert candidate([[2, 3], [3, 3, 5], [4, 2, 4, 4]]) == 2
    assert candidate([[1, 6, 5], [7, 9, 1, 8]]) == 3
    assert candidate([[6, 1, 2], [4, 8, 2, 8]]) == 3
    assert candidate([[7, 2, 6], [4, 1, 9, 8]]) == 3
    assert candidate([[7, 5, 6], [2, 9, 6, 6]]) == 3
    assert candidate([[1, 2, 4], [1, 9, 2, 6]]) == 3
    assert candidate([[4, 6, 6], [5, 6, 3, 2]]) == 3
    assert candidate([[4, 2, 2], [1, 2, 3, 4]]) == 3
    assert candidate([[8, 1, 4], [6, 9, 1, 3]]) == 3
    assert candidate([[5, 5, 2], [1, 5, 4, 2]]) == 3
    assert candidate([[7, 6, 2], [5, 6, 5, 4]]) == 3
    assert candidate([[2, 2, 1], [5, 9, 6, 9]]) == 3
    assert candidate([[4, 6, 7], [1, 6, 7, 1]]) == 3
    assert candidate([[2, 7, 8], [3, 4, 4, 2]]) == 3
    assert candidate([[6, 4, 4], [3, 2, 8, 5]]) == 3
    assert candidate([[6, 7, 1], [2, 5, 8, 2]]) == 3
    assert candidate([[6, 6, 1], [4, 5, 2, 2]]) == 3
    assert candidate([[2, 4, 2], [4, 4, 3, 9]]) == 3
    assert candidate([[8, 7, 5], [8, 7, 8, 9]]) == 3
    assert candidate([[4, 3, 5], [8, 9, 6, 8]]) == 3
    assert candidate([[6, 4, 7], [9, 6, 2, 5]]) == 3
    assert candidate([[3, 8, 7], [9, 4, 6, 5]]) == 3
    assert candidate([[2, 1, 4], [9, 3, 6, 7]]) == 3
    assert candidate([[4, 2, 4], [9, 4, 9, 8]]) == 3
    assert candidate([[2, 7, 6], [4, 1, 9, 8]]) == 3
    assert candidate([[5, 4, 7], [6, 2, 2, 2]]) == 3
    assert candidate([[3, 6, 5], [7, 3, 8, 7]]) == 3
    assert candidate([[8, 2, 1], [9, 9, 6, 6]]) == 3
    assert candidate([[5, 6, 2], [5, 8, 9, 5]]) == 3
    assert candidate([[5, 5, 2], [8, 6, 7, 3]]) == 3
    assert candidate([[2, 5, 3], [9, 8, 6, 8]]) == 3
    assert candidate([[1, 6, 4], [4, 3, 2, 4]]) == 3
    assert candidate([[4, 4, 3], [6, 5, 2, 4]]) == 3
    assert candidate([[7, 5, 6], [1, 1, 8, 8]]) == 3

if __name__ == '__main__':
    check(Find_Min_Length)