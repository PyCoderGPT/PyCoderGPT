from case_MBPP_297 import swap_List


def check(candidate):
    assert candidate([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
    assert candidate([1, 2, 3]) == [3, 2, 1]
    assert candidate([4, 5, 6]) == [6, 5, 4]
    assert candidate([10, 33, 7, 61, 27]) == [27, 33, 7, 61, 10]
    assert candidate([13, 30, 9, 54, 25]) == [25, 30, 9, 54, 13]
    assert candidate([9, 38, 8, 60, 24]) == [24, 38, 8, 60, 9]
    assert candidate([12, 36, 9, 56, 25]) == [25, 36, 9, 56, 12]
    assert candidate([10, 38, 9, 60, 25]) == [25, 38, 9, 60, 10]
    assert candidate([14, 33, 4, 51, 26]) == [26, 33, 4, 51, 14]
    assert candidate([11, 31, 6, 57, 19]) == [19, 31, 6, 57, 11]
    assert candidate([8, 35, 6, 56, 19]) == [19, 35, 6, 56, 8]
    assert candidate([11, 34, 8, 56, 28]) == [28, 34, 8, 56, 11]
    assert candidate([13, 30, 6, 56, 28]) == [28, 30, 6, 56, 13]
    assert candidate([17, 37, 6, 60, 28]) == [28, 37, 6, 60, 17]
    assert candidate([15, 40, 10, 57, 28]) == [28, 40, 10, 57, 15]
    assert candidate([9, 30, 12, 58, 23]) == [23, 30, 12, 58, 9]
    assert candidate([9, 40, 12, 56, 24]) == [24, 40, 12, 56, 9]
    assert candidate([11, 36, 10, 54, 20]) == [20, 36, 10, 54, 11]
    assert candidate([17, 31, 8, 56, 24]) == [24, 31, 8, 56, 17]
    assert candidate([10, 39, 14, 56, 28]) == [28, 39, 14, 56, 10]
    assert candidate([7, 38, 7, 52, 23]) == [23, 38, 7, 52, 7]
    assert candidate([15, 30, 4, 58, 25]) == [25, 30, 4, 58, 15]
    assert candidate([7, 40, 11, 51, 26]) == [26, 40, 11, 51, 7]
    assert candidate([13, 40, 13, 53, 23]) == [23, 40, 13, 53, 13]
    assert candidate([8, 39, 9, 56, 19]) == [19, 39, 9, 56, 8]
    assert candidate([14, 40, 5, 55, 19]) == [19, 40, 5, 55, 14]
    assert candidate([15, 37, 9, 60, 29]) == [29, 37, 9, 60, 15]
    assert candidate([14, 36, 4, 58, 19]) == [19, 36, 4, 58, 14]
    assert candidate([11, 31, 11, 54, 20]) == [20, 31, 11, 54, 11]
    assert candidate([17, 38, 4, 57, 23]) == [23, 38, 4, 57, 17]
    assert candidate([13, 39, 14, 53, 22]) == [22, 39, 14, 53, 13]
    assert candidate([9, 36, 6, 59, 26]) == [26, 36, 6, 59, 9]
    assert candidate([15, 33, 4, 52, 22]) == [22, 33, 4, 52, 15]
    assert candidate([17, 35, 10, 59, 26]) == [26, 35, 10, 59, 17]
    assert candidate([7, 39, 5, 56, 27]) == [27, 39, 5, 56, 7]
    assert candidate([9, 30, 10, 56, 29]) == [29, 30, 10, 56, 9]
    assert candidate([4, 5, 5]) == [5, 5, 4]
    assert candidate([5, 3, 4]) == [4, 3, 5]
    assert candidate([5, 1, 1]) == [1, 1, 5]
    assert candidate([1, 7, 4]) == [4, 7, 1]
    assert candidate([5, 3, 3]) == [3, 3, 5]
    assert candidate([4, 7, 6]) == [6, 7, 4]
    assert candidate([6, 2, 1]) == [1, 2, 6]
    assert candidate([3, 3, 8]) == [8, 3, 3]
    assert candidate([4, 6, 6]) == [6, 6, 4]
    assert candidate([6, 2, 4]) == [4, 2, 6]
    assert candidate([2, 1, 5]) == [5, 1, 2]
    assert candidate([4, 7, 4]) == [4, 7, 4]
    assert candidate([2, 7, 2]) == [2, 7, 2]
    assert candidate([4, 2, 4]) == [4, 2, 4]
    assert candidate([2, 4, 5]) == [5, 4, 2]
    assert candidate([1, 1, 1]) == [1, 1, 1]
    assert candidate([4, 7, 4]) == [4, 7, 4]
    assert candidate([1, 5, 3]) == [3, 5, 1]
    assert candidate([2, 7, 4]) == [4, 7, 2]
    assert candidate([1, 5, 8]) == [8, 5, 1]
    assert candidate([5, 4, 4]) == [4, 4, 5]
    assert candidate([5, 5, 2]) == [2, 5, 5]
    assert candidate([5, 5, 6]) == [6, 5, 5]
    assert candidate([2, 4, 1]) == [1, 4, 2]
    assert candidate([4, 6, 2]) == [2, 6, 4]
    assert candidate([6, 5, 2]) == [2, 5, 6]
    assert candidate([6, 1, 6]) == [6, 1, 6]
    assert candidate([3, 7, 3]) == [3, 7, 3]
    assert candidate([6, 4, 6]) == [6, 4, 6]
    assert candidate([6, 1, 8]) == [8, 1, 6]
    assert candidate([2, 5, 1]) == [1, 5, 2]
    assert candidate([5, 7, 7]) == [7, 7, 5]
    assert candidate([1, 5, 2]) == [2, 5, 1]
    assert candidate([9, 10, 7]) == [7, 10, 9]
    assert candidate([7, 10, 10]) == [10, 10, 7]
    assert candidate([6, 7, 7]) == [7, 7, 6]
    assert candidate([5, 9, 9]) == [9, 9, 5]
    assert candidate([2, 5, 8]) == [8, 5, 2]
    assert candidate([2, 7, 5]) == [5, 7, 2]
    assert candidate([2, 8, 8]) == [8, 8, 2]
    assert candidate([5, 2, 5]) == [5, 2, 5]
    assert candidate([4, 7, 1]) == [1, 7, 4]
    assert candidate([3, 4, 7]) == [7, 4, 3]
    assert candidate([3, 6, 5]) == [5, 6, 3]
    assert candidate([8, 5, 1]) == [1, 5, 8]
    assert candidate([3, 6, 7]) == [7, 6, 3]
    assert candidate([5, 9, 1]) == [1, 9, 5]
    assert candidate([3, 2, 8]) == [8, 2, 3]
    assert candidate([8, 3, 3]) == [3, 3, 8]
    assert candidate([5, 10, 5]) == [5, 10, 5]
    assert candidate([5, 6, 10]) == [10, 6, 5]
    assert candidate([8, 6, 7]) == [7, 6, 8]
    assert candidate([5, 1, 8]) == [8, 1, 5]
    assert candidate([5, 10, 11]) == [11, 10, 5]
    assert candidate([4, 8, 11]) == [11, 8, 4]
    assert candidate([8, 5, 7]) == [7, 5, 8]
    assert candidate([9, 2, 3]) == [3, 2, 9]
    assert candidate([1, 8, 4]) == [4, 8, 1]
    assert candidate([8, 8, 6]) == [6, 8, 8]
    assert candidate([1, 9, 5]) == [5, 9, 1]
    assert candidate([6, 4, 9]) == [9, 4, 6]
    assert candidate([6, 7, 2]) == [2, 7, 6]
    assert candidate([6, 4, 6]) == [6, 4, 6]
    assert candidate([6, 1, 9]) == [9, 1, 6]
    assert candidate([7, 4, 11]) == [11, 4, 7]
    assert candidate([5, 2, 7]) == [7, 2, 5]

if __name__ == '__main__':
    check(swap_List)