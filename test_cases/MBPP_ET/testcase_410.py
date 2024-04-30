from case_MBPP_410 import count_list


def check(candidate):
    assert candidate([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
    assert candidate([[1,2],[2,3],[4,5]]) == 3
    assert candidate([[1,0],[2,0]]) == 2
    assert candidate([[5, 3], [8, 10], [6, 16], [10, 10, 20]]) == 4
    assert candidate([[3, 4], [4, 7], [4, 11], [9, 10, 15]]) == 4
    assert candidate([[6, 5], [8, 10], [11, 12], [12, 10, 17]]) == 4
    assert candidate([[4, 3], [9, 5], [14, 16], [15, 19, 21]]) == 4
    assert candidate([[4, 3], [6, 3], [7, 16], [12, 12, 16]]) == 4
    assert candidate([[3, 4], [6, 10], [10, 14], [11, 12, 22]]) == 4
    assert candidate([[2, 1], [3, 11], [8, 7], [15, 20, 21]]) == 4
    assert candidate([[5, 2], [9, 4], [14, 14], [12, 18, 15]]) == 4
    assert candidate([[6, 5], [9, 10], [12, 12], [15, 18, 22]]) == 4
    assert candidate([[5, 7], [9, 3], [14, 14], [13, 12, 18]]) == 4
    assert candidate([[2, 8], [10, 12], [12, 15], [17, 16, 20]]) == 4
    assert candidate([[5, 3], [4, 3], [4, 13], [16, 10, 18]]) == 4
    assert candidate([[4, 8], [4, 7], [8, 10], [18, 11, 21]]) == 4
    assert candidate([[4, 3], [9, 6], [11, 12], [9, 14, 13]]) == 4
    assert candidate([[4, 6], [10, 3], [11, 16], [18, 12, 12]]) == 4
    assert candidate([[6, 3], [2, 4], [13, 14], [16, 16, 14]]) == 4
    assert candidate([[2, 3], [6, 6], [7, 14], [11, 12, 13]]) == 4
    assert candidate([[3, 5], [3, 10], [11, 15], [17, 15, 17]]) == 4
    assert candidate([[3, 1], [1, 6], [11, 10], [15, 17, 22]]) == 4
    assert candidate([[5, 8], [6, 7], [4, 13], [13, 12, 18]]) == 4
    assert candidate([[1, 6], [3, 10], [4, 8], [18, 20, 14]]) == 4
    assert candidate([[1, 8], [2, 2], [6, 14], [14, 15, 18]]) == 4
    assert candidate([[4, 6], [9, 7], [7, 10], [18, 12, 16]]) == 4
    assert candidate([[4, 6], [7, 6], [6, 9], [8, 18, 20]]) == 4
    assert candidate([[3, 5], [1, 6], [6, 7], [8, 17, 14]]) == 4
    assert candidate([[1, 4], [3, 7], [5, 10], [15, 17, 17]]) == 4
    assert candidate([[5, 1], [3, 7], [13, 9], [8, 11, 22]]) == 4
    assert candidate([[3, 4], [5, 11], [11, 11], [17, 17, 22]]) == 4
    assert candidate([[5, 4], [4, 4], [10, 16], [16, 13, 15]]) == 4
    assert candidate([[6, 1], [2, 11], [11, 6], [16, 13, 12]]) == 4
    assert candidate([[3, 2], [5, 12], [6, 8], [10, 17, 13]]) == 4
    assert candidate([[4, 8], [5, 4], [12, 8], [8, 17, 12]]) == 4
    assert candidate([[6, 7], [7, 4], [12, 16], [13, 10, 14]]) == 4
    assert candidate([[4, 5], [3, 7], [6, 2]]) == 3
    assert candidate([[6, 7], [2, 2], [7, 9]]) == 3
    assert candidate([[5, 5], [6, 4], [6, 3]]) == 3
    assert candidate([[4, 7], [4, 1], [9, 1]]) == 3
    assert candidate([[4, 4], [5, 4], [9, 10]]) == 3
    assert candidate([[5, 7], [4, 3], [1, 9]]) == 3
    assert candidate([[1, 2], [3, 3], [8, 1]]) == 3
    assert candidate([[3, 4], [6, 7], [4, 9]]) == 3
    assert candidate([[3, 4], [5, 4], [7, 4]]) == 3
    assert candidate([[1, 1], [6, 6], [2, 9]]) == 3
    assert candidate([[5, 1], [1, 2], [3, 7]]) == 3
    assert candidate([[4, 4], [7, 2], [9, 7]]) == 3
    assert candidate([[5, 1], [2, 2], [8, 8]]) == 3
    assert candidate([[4, 5], [3, 5], [7, 9]]) == 3
    assert candidate([[2, 7], [4, 3], [6, 10]]) == 3
    assert candidate([[3, 1], [3, 2], [9, 10]]) == 3
    assert candidate([[6, 2], [2, 4], [1, 2]]) == 3
    assert candidate([[5, 2], [4, 7], [9, 6]]) == 3
    assert candidate([[3, 1], [1, 1], [1, 5]]) == 3
    assert candidate([[3, 4], [4, 6], [6, 5]]) == 3
    assert candidate([[2, 5], [4, 6], [3, 10]]) == 3
    assert candidate([[3, 4], [2, 7], [2, 6]]) == 3
    assert candidate([[2, 1], [7, 7], [5, 2]]) == 3
    assert candidate([[6, 1], [3, 7], [7, 10]]) == 3
    assert candidate([[4, 6], [2, 2], [9, 2]]) == 3
    assert candidate([[5, 7], [4, 3], [9, 5]]) == 3
    assert candidate([[6, 4], [1, 1], [2, 1]]) == 3
    assert candidate([[5, 1], [3, 4], [5, 1]]) == 3
    assert candidate([[3, 3], [2, 4], [5, 2]]) == 3
    assert candidate([[3, 2], [3, 5], [2, 9]]) == 3
    assert candidate([[2, 2], [7, 2], [2, 3]]) == 3
    assert candidate([[3, 7], [2, 8], [6, 8]]) == 3
    assert candidate([[2, 4], [2, 6], [1, 3]]) == 3
    assert candidate([[1, 1], [6, 1]]) == 2
    assert candidate([[5, 3], [1, 1]]) == 2
    assert candidate([[2, 2], [5, 1]]) == 2
    assert candidate([[4, 4], [1, 5]]) == 2
    assert candidate([[6, 4], [5, 5]]) == 2
    assert candidate([[5, 4], [6, 2]]) == 2
    assert candidate([[4, 5], [1, 1]]) == 2
    assert candidate([[2, 4], [4, 5]]) == 2
    assert candidate([[1, 2], [7, 4]]) == 2
    assert candidate([[6, 3], [4, 1]]) == 2
    assert candidate([[1, 1], [2, 2]]) == 2
    assert candidate([[5, 3], [7, 5]]) == 2
    assert candidate([[6, 4], [4, 2]]) == 2
    assert candidate([[6, 2], [7, 1]]) == 2
    assert candidate([[4, 2], [5, 3]]) == 2
    assert candidate([[5, 5], [2, 1]]) == 2
    assert candidate([[3, 2], [6, 3]]) == 2
    assert candidate([[1, 3], [2, 3]]) == 2
    assert candidate([[6, 1], [5, 3]]) == 2
    assert candidate([[5, 4], [7, 5]]) == 2
    assert candidate([[4, 4], [2, 4]]) == 2
    assert candidate([[5, 5], [5, 4]]) == 2
    assert candidate([[2, 4], [5, 4]]) == 2
    assert candidate([[4, 2], [3, 5]]) == 2
    assert candidate([[6, 3], [6, 3]]) == 2
    assert candidate([[1, 1], [1, 1]]) == 2
    assert candidate([[3, 5], [1, 5]]) == 2
    assert candidate([[4, 3], [2, 2]]) == 2
    assert candidate([[6, 2], [3, 1]]) == 2
    assert candidate([[1, 4], [7, 3]]) == 2
    assert candidate([[4, 3], [7, 3]]) == 2
    assert candidate([[1, 3], [3, 2]]) == 2
    assert candidate([[6, 1], [1, 2]]) == 2

if __name__ == '__main__':
    check(count_list)