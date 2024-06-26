from case_HE_129 import minPath


def check(candidate):
    assert candidate([[13, 16, 6, 5], [2, 4, 15, 19], [3, 5, 1, 9], [2, 5, 10, 14]], 7) == [1, 5, 1, 5, 1, 5, 1]
    assert candidate([[6, 4], [3, 6]], 13) == [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]
    assert candidate([[8, 10, 9, 5], [9, 19, 19, 9], [7, 1, 11, 3], [9, 12, 13, 3]], 4) == [1, 7, 1, 7]
    assert candidate([[11, 12, 12, 6], [7, 12, 11, 1], [12, 2, 14, 11], [14, 15, 9, 5]], 9) == [1, 6, 1, 6, 1, 6, 1, 6, 1]
    assert candidate([[11, 16, 6, 1], [13, 8, 12, 11], [2, 18, 14, 1], [11, 5, 12, 4]], 7) == [1, 4, 1, 4, 1, 4, 1]
    assert candidate([[13, 11, 15, 5], [14, 2, 18, 3], [7, 19, 13, 3], [9, 6, 2, 3]], 8) == [1, 17, 1, 17, 1, 17, 1, 17]
    assert candidate([[1, 6, 8], [3, 4, 5], [4, 10, 13]], 5) == [1, 3, 1, 3, 1]
    assert candidate([[3, 6, 2, 8], [9, 1, 6, 8], [5, 7, 14, 7], [10, 19, 16, 21]], 3) == [1, 6, 1]
    assert candidate([[13, 10, 14, 3], [4, 3, 20, 8], [7, 20, 14, 1], [9, 4, 12, 3]], 13) == [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    assert candidate([[2, 8, 8], [3, 5, 5], [9, 10, 3]], 5) == [1, 10, 1, 10, 1]
    assert candidate([[8, 1, 8, 13], [5, 3, 8, 5], [4, 20, 6, 13], [7, 18, 11, 5]], 8) == [1, 3, 1, 3, 1, 3, 1, 3]
    assert candidate([[16, 12, 5, 7], [1, 18, 12, 4], [7, 4, 15, 11], [17, 16, 11, 4]], 10) == [1, 7, 1, 7, 1, 7, 1, 7, 1, 7]
    assert candidate([[5, 5, 3], [5, 13, 9], [2, 2, 8]], 4) == [1, 10, 1, 10]
    assert candidate([[4, 2, 7], [7, 2, 10], [5, 4, 7]], 4) == [1, 10, 1, 10]
    assert candidate([[9, 5, 6, 3], [2, 15, 11, 1], [7, 4, 15, 1], [8, 16, 6, 4]], 11) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate([[5, 6, 1], [3, 2, 6], [11, 7, 9]], 5) == [1, 6, 1, 6, 1]
    assert candidate([[2, 7], [4, 5]], 9) == [1, 5, 1, 5, 1, 5, 1, 5, 1]
    assert candidate([[8, 7, 1], [3, 2, 9], [4, 13, 6]], 2) == [1, 7]
    assert candidate([[5, 6, 5], [1, 1, 9], [7, 3, 5]], 2) == [1, 1]
    assert candidate([[4, 1, 2], [8, 9, 4], [9, 4, 7]], 7) == [1, 2, 1, 2, 1, 2, 1]
    assert candidate([[7, 8, 13, 3], [14, 3, 13, 2], [3, 16, 19, 6], [15, 4, 3, 3]], 13) == [1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1]
    assert candidate([[15, 17, 6, 2], [4, 6, 20, 10], [4, 15, 16, 9], [12, 13, 3, 4]], 12) == [1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17]
    assert candidate([[5, 5, 15, 11], [9, 2, 9, 5], [5, 18, 9, 15], [13, 19, 5, 7]], 3) == [1, 17, 1]
    assert candidate([[5, 3, 4], [6, 13, 11], [5, 11, 8]], 7) == [1, 10, 1, 10, 1, 10, 1]
    assert candidate([[10, 17, 8, 4], [2, 7, 17, 17], [3, 3, 1, 10], [1, 6, 7, 15]], 5) == [1, 3, 1, 3, 1]
    assert candidate([[3, 7], [8, 1]], 15) == [1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1]
    assert candidate([[3, 2, 1], [7, 6, 7], [3, 6, 9]], 7) == [1, 2, 1, 2, 1, 2, 1]
    assert candidate([[3, 6], [3, 1]], 14) == [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    assert candidate([[9, 13, 3], [8, 6, 10], [4, 6, 6]], 5) == [1, 10, 1, 10, 1]
    assert candidate([[6, 9, 2], [5, 4, 1], [11, 6, 3]], 5) == [1, 2, 1, 2, 1]
    assert candidate([[6, 4, 13, 10], [5, 7, 12, 1], [3, 16, 11, 15], [8, 14, 9, 2]], 7) == [1, 10, 1, 10, 1, 10, 1]
    assert candidate([[11, 10, 9, 4], [5, 6, 13, 14], [4, 10, 4, 14], [3, 14, 14, 15]], 1) == [1]
    assert candidate([[1, 2], [1, 1]], 8) == [1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate([[4, 4], [7, 6]], 5) == [1, 5, 1, 5, 1]
    assert candidate([[1, 6, 3], [7, 9, 10], [1, 4, 5]], 6) == [1, 4, 1, 4, 1, 4]
    assert candidate([[5, 6], [1, 3]], 10) == [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    assert candidate([[3, 2], [4, 2]], 14) == [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]
    assert candidate([[6, 6], [3, 4]], 5) == [1, 5, 1, 5, 1]
    assert candidate([[4, 6, 8], [8, 8, 4], [10, 5, 6]], 1) == [1]
    assert candidate([[12, 3, 8, 3], [8, 15, 11, 5], [8, 5, 14, 7], [12, 13, 8, 4]], 7) == [1, 17, 1, 17, 1, 17, 1]
    assert candidate([[5, 5, 8], [6, 3, 11], [2, 12, 11]], 8) == [1, 10, 1, 10, 1, 10, 1, 10]
    assert candidate([[3, 3, 13, 8], [10, 5, 14, 4], [7, 17, 15, 10], [11, 17, 6, 7]], 11) == [1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1]
    assert candidate([[6, 2], [3, 5]], 13) == [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]
    assert candidate([[6, 2, 3], [6, 4, 3], [6, 5, 7]], 3) == [1, 10, 1]
    assert candidate([[9, 9, 5, 4], [7, 8, 13, 18], [5, 9, 6, 14], [8, 15, 15, 17]], 6) == [1, 17, 1, 17, 1, 17]
    assert candidate([[11, 10, 14, 1], [2, 1, 9, 10], [6, 7, 4, 13], [6, 14, 14, 11]], 7) == [1, 2, 1, 2, 1, 2, 1]
    assert candidate([[6, 2], [8, 2]], 11) == [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]
    assert candidate([[1, 4, 8], [1, 1, 5], [9, 7, 7]], 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate([[3, 6, 8], [7, 7, 9], [11, 12, 9]], 1) == [1]
    assert candidate([[11, 4, 11, 5], [8, 3, 12, 1], [4, 16, 7, 17], [9, 12, 13, 4]], 11) == [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]
    assert candidate([[7, 17, 6, 6], [8, 4, 11, 1], [7, 13, 13, 3], [15, 6, 9, 6]], 13) == [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    assert candidate([[12, 13, 10, 1], [9, 3, 15, 6], [5, 16, 14, 4], [11, 8, 7, 2]], 12) == [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6]
    assert candidate([[2, 10, 2], [5, 2, 3], [8, 11, 4]], 3) == [1, 10, 1]
    assert candidate([[8, 12, 2], [6, 3, 1], [4, 9, 2]], 1) == [1]
    assert candidate([[2, 3, 6], [6, 4, 11], [7, 13, 8]], 6) == [1, 10, 1, 10, 1, 10]
    assert candidate([[1, 3, 4, 9], [9, 6, 10, 13], [6, 8, 15, 10], [8, 15, 19, 11]], 3) == [1, 3, 1]
    assert candidate([[5, 7], [2, 2]], 6) == [1, 5, 1, 5, 1, 5]
    assert candidate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4) == [1, 2, 1, 2]
    assert candidate([[1, 2, 9], [8, 6, 11], [7, 8, 4]], 3) == [1, 2, 1]
    assert candidate([[1, 6], [8, 6]], 8) == [1, 6, 1, 6, 1, 6, 1, 6]
    assert candidate([[7, 2, 15, 15], [2, 7, 13, 3], [1, 16, 11, 13], [11, 14, 14, 5]], 3) == [1, 2, 1]
    assert candidate([[4, 17, 12, 5], [2, 6, 9, 10], [1, 2, 6, 9], [7, 12, 13, 19]], 4) == [1, 2, 1, 2]
    assert candidate([[2, 4, 5, 3], [1, 10, 3, 4], [11, 12, 15, 17], [9, 17, 17, 19]], 5) == [1, 2, 1, 2, 1]
    assert candidate([[8, 12, 9, 1], [3, 21, 19, 5], [10, 1, 11, 3], [13, 12, 13, 6]], 13) == [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]
    assert candidate([[9, 8, 2, 2], [8, 13, 13, 8], [6, 3, 16, 9], [13, 17, 11, 3]], 8) == [1, 17, 1, 17, 1, 17, 1, 17]
    assert candidate([[2, 4, 1], [2, 13, 10], [3, 11, 7]], 6) == [1, 4, 1, 4, 1, 4]
    assert candidate([[2, 2, 1], [3, 6, 8], [6, 6, 13]], 7) == [1, 2, 1, 2, 1, 2, 1]
    assert candidate([[3, 7, 4, 1], [2, 3, 9, 3], [14, 13, 14, 8], [9, 12, 14, 18]], 9) == [1, 3, 1, 3, 1, 3, 1, 3, 1]
    assert candidate([[10, 9, 8], [6, 4, 4], [9, 12, 3]], 3) == [1, 10, 1]
    assert candidate([[8, 14, 7, 3], [9, 6, 12, 14], [3, 4, 4, 8], [5, 7, 8, 20]], 10) == [1, 17, 1, 17, 1, 17, 1, 17, 1, 17]
    assert candidate([[5, 4], [1, 2]], 14) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    assert candidate([[1, 12, 6], [3, 5, 9], [5, 9, 4]], 9) == [1, 3, 1, 3, 1, 3, 1, 3, 1]
    assert candidate([[4, 3, 9], [5, 7, 7], [7, 10, 2]], 6) == [1, 10, 1, 10, 1, 10]
    assert candidate([[1, 7], [4, 7]], 12) == [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4]
    assert candidate([[2, 7], [4, 4]], 10) == [1, 5, 1, 5, 1, 5, 1, 5, 1, 5]
    assert candidate([[6, 4], [7, 3]], 8) == [1, 5, 1, 5, 1, 5, 1, 5]
    assert candidate([[5, 7, 5, 9], [7, 7, 3, 6], [5, 14, 10, 12], [17, 18, 14, 21]], 7) == [1, 17, 1, 17, 1, 17, 1]
    assert candidate([[6, 4, 2], [2, 6, 6], [11, 10, 11]], 3) == [1, 10, 1]
    assert candidate([[1, 1, 4, 3], [9, 6, 9, 13], [6, 15, 13, 12], [16, 12, 16, 20]], 9) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate([[3, 6, 1], [6, 2, 8], [3, 11, 5]], 4) == [1, 6, 1, 6]
    assert candidate([[2, 4, 12, 8], [9, 9, 7, 2], [1, 14, 16, 10], [11, 15, 8, 1]], 9) == [1, 8, 1, 8, 1, 8, 1, 8, 1]
    assert candidate([[2, 4, 9], [7, 9, 4], [3, 10, 6]], 13) == [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]
    assert candidate([[8, 3, 11, 7], [4, 12, 7, 1], [7, 20, 8, 15], [11, 18, 9, 6]], 9) == [1, 7, 1, 7, 1, 7, 1, 7, 1]
    assert candidate([[7, 8, 7, 4], [12, 6, 11, 10], [10, 12, 18, 8], [9, 12, 9, 1]], 16) == [1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8]
    assert candidate([[1, 4, 9], [4, 6, 6], [3, 3, 5]], 8) == [1, 4, 1, 4, 1, 4, 1, 4]
    assert candidate([[4, 2, 4, 6], [10, 1, 7, 5], [9, 11, 7, 9], [8, 10, 10, 18]], 8) == [1, 2, 1, 2, 1, 2, 1, 2]
    assert candidate([[7, 11, 2], [7, 2, 5], [10, 13, 6]], 11) == [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]
    assert candidate([[3, 3, 5], [2, 1, 4], [1, 3, 8]], 10) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    assert candidate([[2, 2], [5, 7]], 14) == [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]
    assert candidate([[3, 7, 8, 8], [3, 8, 7, 6], [5, 6, 11, 7], [17, 12, 18, 17]], 4) == [1, 17, 1, 17]
    assert candidate([[6, 3, 6, 5], [3, 4, 10, 4], [8, 15, 7, 14], [10, 19, 10, 14]], 9) == [1, 17, 1, 17, 1, 17, 1, 17, 1]
    assert candidate([[3, 1, 2, 3], [9, 5, 11, 12], [10, 6, 10, 14], [11, 11, 18, 18]], 4) == [1, 2, 1, 2]
    assert candidate([[6, 7], [2, 2]], 14) == [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]
    assert candidate([[4, 7, 3, 2], [2, 1, 11, 13], [11, 7, 15, 11], [16, 15, 15, 17]], 3) == [1, 2, 1]
    assert candidate([[7, 10, 1], [8, 6, 9], [5, 13, 7]], 3) == [1, 9, 1]
    assert candidate([[8, 12, 12, 1], [2, 5, 13, 14], [6, 3, 2, 16], [2, 13, 11, 14]], 6) == [1, 12, 1, 12, 1, 12]
    assert candidate([[7, 7, 7], [9, 5, 6], [11, 7, 6]], 4) == [1, 10, 1, 10]
    assert candidate([[4, 9, 12, 8], [3, 5, 9, 3], [8, 11, 12, 20], [5, 16, 13, 7]], 4) == [1, 17, 1, 17]
    assert candidate([[13, 16, 10, 3], [7, 6, 9, 17], [2, 11, 5, 15], [8, 8, 7, 19]], 4) == [1, 17, 1, 17]
    assert candidate([[3, 13, 8], [5, 5, 3], [3, 9, 2]], 2) == [1, 10]
    assert candidate([[1, 12, 6], [6, 4, 4], [6, 5, 11]], 11) == [1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1]
    assert candidate([[11, 3, 9, 6], [8, 18, 13, 1], [10, 5, 15, 1], [15, 12, 11, 3]], 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate([[7, 12, 4], [6, 4, 1], [11, 5, 4]], 7) == [1, 4, 1, 4, 1, 4, 1]
    assert candidate([[8, 14, 9, 2], [6, 4, 13, 15], [5, 7, 1, 12], [3, 10, 11, 16]], 5) == [1, 7, 1, 7, 1]
    assert candidate([[4, 9, 9, 5], [7, 5, 18, 11], [1, 9, 5, 17], [2, 11, 12, 18]], 6) == [1, 2, 1, 2, 1, 2]
    assert candidate([[9, 6, 1], [1, 11, 14], [4, 8, 4]], 13) == [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1]
    assert candidate([[4, 2, 3], [2, 10, 4], [5, 2, 7]], 8) == [1, 10, 1, 10, 1, 10, 1, 10]
    assert candidate([[9, 3, 11, 8], [9, 3, 14, 3], [4, 12, 11, 15], [5, 19, 12, 2]], 12) == [1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17]
    assert candidate([[1, 8], [3, 5]], 14) == [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    assert candidate([[4, 3], [3, 9]], 11) == [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]
    assert candidate([[11, 3, 8, 5], [4, 20, 10, 5], [9, 3, 14, 5], [13, 10, 10, 3]], 12) == [1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17]
    assert candidate([[6, 3, 7], [5, 6, 4], [5, 8, 7]], 3) == [1, 10, 1]
    assert candidate([[6, 1, 5, 1], [4, 5, 7, 8], [6, 12, 12, 8], [11, 9, 17, 14]], 1) == [1]
    assert candidate([[5, 1], [6, 8]], 8) == [1, 5, 1, 5, 1, 5, 1, 5]
    assert candidate([[9, 3, 9, 12], [4, 10, 16, 6], [8, 15, 11, 17], [12, 10, 9, 7]], 7) == [1, 17, 1, 17, 1, 17, 1]
    assert candidate([[7, 12, 8, 3], [9, 3, 11, 15], [4, 6, 1, 7], [7, 11, 8, 11]], 4) == [1, 6, 1, 6]
    assert candidate([[16, 16, 5, 5], [13, 4, 13, 3], [4, 12, 9, 8], [8, 11, 3, 7]], 11) == [1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1]
    assert candidate([[2, 7, 4], [3, 1, 5], [6, 8, 9]], 8) == [1, 3, 1, 3, 1, 3, 1, 3]
    assert candidate([[4, 7, 2], [5, 9, 11], [7, 6, 13]], 5) == [1, 10, 1, 10, 1]
    assert candidate([[3, 7], [7, 9]], 10) == [1, 5, 1, 5, 1, 5, 1, 5, 1, 5]
    assert candidate([[1, 7, 2], [5, 3, 2], [2, 4, 6]], 1) == [1]
    assert candidate([[11, 8, 7, 2], [5, 16, 14, 4], [9, 3, 15, 6], [12, 13, 10, 1]], 9) == [1, 6, 1, 6, 1, 6, 1, 6, 1]
    assert candidate([[1, 1, 3], [4, 4, 3], [2, 10, 11]], 3) == [1, 1, 1]
    assert candidate([[8, 16, 10, 4], [14, 6, 18, 1], [5, 19, 12, 1], [9, 4, 3, 5]], 12) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1) == [1]
    assert candidate([[4, 8, 4], [5, 2, 7], [5, 5, 7]], 4) == [1, 10, 1, 10]
    assert candidate([[3, 17, 14, 2], [7, 2, 17, 11], [10, 11, 2, 14], [7, 13, 15, 20]], 8) == [1, 17, 1, 17, 1, 17, 1, 17]
    assert candidate([[15, 14, 14, 1], [7, 2, 17, 11], [9, 13, 16, 2], [9, 12, 11, 4]], 8) == [1, 11, 1, 11, 1, 11, 1, 11]
    assert candidate([[6, 1, 5], [3, 8, 9], [2, 7, 4]], 8) == [1, 5, 1, 5, 1, 5, 1, 5]

    # Check some edge cases that are easy to work out by hand.
    assert candidate([[10, 6, 14, 8], [1, 4, 9, 1], [8, 11, 13, 13], [10, 10, 7, 1]], 3) == [1, 7, 1]
    assert candidate([[16, 13, 11, 4], [5, 13, 9, 2], [13, 6, 11, 9], [14, 16, 5, 4]], 9) == [1, 17, 1, 17, 1, 17, 1, 17, 1]
    assert candidate([[8, 13, 11, 4], [10, 5, 13, 3], [4, 19, 17, 6], [12, 3, 6, 5]], 17) == [1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1]
    assert candidate([[13, 12, 5, 2], [13, 6, 15, 7], [2, 13, 10, 6], [15, 4, 3, 6]], 10) == [1, 17, 1, 17, 1, 17, 1, 17, 1, 17]
    assert candidate([[5, 6, 4], [5, 3, 7], [5, 3, 8]], 11) == [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]
    assert candidate([[9, 5, 14, 14], [1, 6, 11, 5], [6, 21, 9, 20], [8, 17, 14, 7]], 7) == [1, 6, 1, 6, 1, 6, 1]
    assert candidate([[14, 10, 2, 5], [10, 17, 11, 6], [14, 2, 11, 4], [13, 11, 12, 4]], 14) == [1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17]
    assert candidate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [1, 2, 1]
    assert candidate([[1, 2], [3, 4]], 10) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    assert candidate([[5, 3, 6], [1, 9, 4], [3, 7, 3]], 10) == [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    assert candidate([[1, 3], [3, 2]], 10) == [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    assert candidate([[10, 10, 12, 5], [4, 14, 15, 8], [9, 3, 18, 2], [16, 11, 10, 6]], 8) == [1, 17, 1, 17, 1, 17, 1, 17]
    assert candidate([[7, 9, 4], [5, 2, 4], [6, 11, 7]], 10) == [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]
    assert candidate([[5, 3], [5, 2]], 7) == [1, 5, 1, 5, 1, 5, 1]

if __name__ == '__main__':
    check(minPath)