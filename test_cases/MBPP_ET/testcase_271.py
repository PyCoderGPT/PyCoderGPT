from case_MBPP_271 import Find_Max_Length


def check(candidate):
    assert candidate([[1],[1,4],[5,6,7,8]]) == 4
    assert candidate([[0,1],[2,2,],[3,2,1]]) == 3
    assert candidate([[7],[22,23],[13,14,15],[10,20,30,40,50]]) == 5
    assert candidate([[3], [1, 7], [2, 5, 11, 5]]) == 4
    assert candidate([[3], [6, 2], [7, 8, 3, 11]]) == 4
    assert candidate([[6], [1, 7], [3, 11, 10, 12]]) == 4
    assert candidate([[3], [2, 2], [1, 10, 12, 10]]) == 4
    assert candidate([[2], [1, 5], [2, 5, 3, 13]]) == 4
    assert candidate([[2], [4, 3], [5, 11, 9, 3]]) == 4
    assert candidate([[2], [6, 9], [5, 7, 12, 5]]) == 4
    assert candidate([[4], [5, 1], [3, 6, 4, 7]]) == 4
    assert candidate([[2], [2, 8], [5, 9, 8, 4]]) == 4
    assert candidate([[3], [3, 2], [4, 5, 9, 8]]) == 4
    assert candidate([[4], [4, 7], [5, 11, 10, 10]]) == 4
    assert candidate([[4], [6, 4], [1, 11, 7, 5]]) == 4
    assert candidate([[1], [1, 9], [9, 8, 12, 6]]) == 4
    assert candidate([[5], [6, 1], [10, 11, 7, 12]]) == 4
    assert candidate([[3], [4, 4], [9, 11, 4, 3]]) == 4
    assert candidate([[6], [5, 9], [9, 1, 8, 3]]) == 4
    assert candidate([[6], [1, 5], [4, 11, 10, 4]]) == 4
    assert candidate([[3], [5, 9], [8, 7, 7, 7]]) == 4
    assert candidate([[5], [6, 1], [3, 5, 9, 12]]) == 4
    assert candidate([[1], [5, 2], [1, 5, 7, 8]]) == 4
    assert candidate([[4], [4, 3], [10, 5, 11, 9]]) == 4
    assert candidate([[2], [5, 2], [10, 2, 11, 4]]) == 4
    assert candidate([[4], [3, 5], [9, 2, 8, 5]]) == 4
    assert candidate([[4], [1, 9], [6, 11, 11, 7]]) == 4
    assert candidate([[5], [5, 4], [8, 2, 11, 8]]) == 4
    assert candidate([[4], [2, 1], [3, 2, 9, 4]]) == 4
    assert candidate([[1], [2, 6], [8, 7, 9, 4]]) == 4
    assert candidate([[1], [4, 5], [3, 1, 8, 8]]) == 4
    assert candidate([[5], [4, 6], [6, 9, 3, 12]]) == 4
    assert candidate([[2], [4, 3], [4, 8, 9, 6]]) == 4
    assert candidate([[6], [1, 5], [1, 8, 12, 7]]) == 4
    assert candidate([[2], [6, 6], [3, 1, 5, 5]]) == 4
    assert candidate([[4], [2, 1], [4, 6, 5, 13]]) == 4
    assert candidate([[2, 2], [7, 6], [6, 5, 4]]) == 3
    assert candidate([[2, 3], [3, 6], [6, 1, 5]]) == 3
    assert candidate([[3, 6], [7, 3], [4, 5, 6]]) == 3
    assert candidate([[1, 6], [1, 7], [7, 7, 3]]) == 3
    assert candidate([[2, 6], [5, 1], [3, 4, 6]]) == 3
    assert candidate([[3, 2], [4, 7], [8, 1, 4]]) == 3
    assert candidate([[3, 6], [2, 7], [4, 5, 2]]) == 3
    assert candidate([[2, 3], [7, 2], [2, 4, 5]]) == 3
    assert candidate([[5, 4], [4, 1], [1, 2, 6]]) == 3
    assert candidate([[1, 6], [3, 3], [2, 2, 1]]) == 3
    assert candidate([[2, 6], [4, 7], [6, 4, 6]]) == 3
    assert candidate([[4, 1], [4, 7], [4, 4, 2]]) == 3
    assert candidate([[3, 6], [7, 7], [2, 1, 4]]) == 3
    assert candidate([[5, 4], [7, 2], [6, 7, 6]]) == 3
    assert candidate([[3, 6], [3, 3], [3, 2, 1]]) == 3
    assert candidate([[4, 2], [2, 6], [7, 2, 6]]) == 3
    assert candidate([[1, 1], [7, 4], [8, 1, 3]]) == 3
    assert candidate([[2, 3], [6, 7], [8, 6, 6]]) == 3
    assert candidate([[2, 6], [2, 3], [5, 5, 5]]) == 3
    assert candidate([[4, 1], [7, 3], [7, 3, 2]]) == 3
    assert candidate([[3, 4], [5, 7], [1, 2, 6]]) == 3
    assert candidate([[2, 5], [3, 2], [6, 2, 3]]) == 3
    assert candidate([[5, 5], [6, 7], [3, 3, 1]]) == 3
    assert candidate([[3, 2], [7, 3], [6, 6, 4]]) == 3
    assert candidate([[3, 3], [1, 5], [5, 4, 5]]) == 3
    assert candidate([[4, 1], [3, 6], [1, 4, 3]]) == 3
    assert candidate([[2, 4], [6, 7], [3, 3, 5]]) == 3
    assert candidate([[2, 2], [7, 3], [6, 1, 1]]) == 3
    assert candidate([[2, 2], [7, 2], [1, 4, 1]]) == 3
    assert candidate([[2, 5], [4, 7], [2, 1, 6]]) == 3
    assert candidate([[1, 6], [1, 1], [2, 6, 2]]) == 3
    assert candidate([[2, 4], [2, 3], [5, 5, 1]]) == 3
    assert candidate([[2, 6], [7, 2], [5, 7, 3]]) == 3
    assert candidate([[11], [24, 28], [13, 15, 18], [15, 18, 34, 40, 53]]) == 5
    assert candidate([[4], [19, 26], [12, 13, 19], [15, 24, 26, 44, 52]]) == 5
    assert candidate([[2], [26, 22], [12, 12, 17], [7, 22, 28, 44, 54]]) == 5
    assert candidate([[4], [19, 22], [18, 18, 16], [14, 15, 31, 40, 49]]) == 5
    assert candidate([[5], [27, 26], [13, 10, 14], [11, 22, 34, 41, 50]]) == 5
    assert candidate([[11], [24, 21], [14, 13, 19], [12, 19, 30, 40, 46]]) == 5
    assert candidate([[9], [21, 20], [9, 15, 11], [15, 21, 25, 43, 48]]) == 5
    assert candidate([[11], [20, 22], [12, 11, 11], [6, 20, 31, 37, 53]]) == 5
    assert candidate([[4], [18, 26], [11, 11, 12], [12, 20, 35, 44, 46]]) == 5
    assert candidate([[3], [20, 25], [12, 15, 13], [9, 19, 35, 35, 47]]) == 5
    assert candidate([[5], [26, 19], [12, 17, 17], [15, 17, 29, 44, 50]]) == 5
    assert candidate([[11], [24, 21], [11, 15, 14], [10, 20, 34, 45, 46]]) == 5
    assert candidate([[10], [25, 26], [8, 12, 14], [7, 18, 25, 39, 50]]) == 5
    assert candidate([[12], [21, 27], [9, 13, 20], [12, 24, 30, 44, 55]]) == 5
    assert candidate([[10], [23, 25], [12, 16, 11], [5, 25, 33, 42, 53]]) == 5
    assert candidate([[10], [19, 27], [9, 15, 11], [10, 16, 29, 43, 47]]) == 5
    assert candidate([[9], [24, 27], [15, 13, 15], [8, 20, 28, 43, 49]]) == 5
    assert candidate([[8], [17, 26], [15, 19, 14], [13, 17, 27, 36, 47]]) == 5
    assert candidate([[7], [27, 24], [9, 13, 12], [8, 21, 29, 36, 53]]) == 5
    assert candidate([[11], [27, 26], [15, 15, 15], [13, 19, 32, 40, 46]]) == 5
    assert candidate([[9], [24, 25], [10, 15, 16], [8, 18, 30, 41, 45]]) == 5
    assert candidate([[11], [19, 25], [16, 10, 13], [11, 16, 33, 39, 49]]) == 5
    assert candidate([[12], [21, 22], [14, 16, 11], [14, 19, 29, 35, 46]]) == 5
    assert candidate([[5], [26, 24], [16, 12, 19], [9, 22, 32, 36, 54]]) == 5
    assert candidate([[5], [27, 27], [9, 9, 18], [7, 17, 30, 43, 45]]) == 5
    assert candidate([[3], [20, 23], [18, 19, 14], [15, 22, 30, 38, 48]]) == 5
    assert candidate([[7], [26, 19], [12, 11, 16], [14, 25, 28, 45, 45]]) == 5
    assert candidate([[8], [27, 19], [18, 9, 15], [15, 18, 26, 42, 52]]) == 5
    assert candidate([[2], [19, 18], [18, 10, 10], [10, 19, 33, 36, 47]]) == 5
    assert candidate([[11], [24, 25], [10, 11, 15], [11, 21, 26, 41, 53]]) == 5
    assert candidate([[11], [18, 27], [16, 9, 11], [11, 24, 32, 36, 48]]) == 5
    assert candidate([[7], [26, 24], [12, 11, 11], [13, 19, 30, 43, 51]]) == 5
    assert candidate([[2], [21, 18], [8, 16, 13], [5, 18, 26, 42, 55]]) == 5

if __name__ == '__main__':
    check(Find_Max_Length)