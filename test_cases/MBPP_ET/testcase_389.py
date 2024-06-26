from case_MBPP_389 import Diff


def check(candidate):
    assert (candidate([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
    assert (candidate([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
    assert (candidate([1,2,3], [6,7,1])) == [2,3,6,7]
    assert candidate([9, 13, 16, 21, 35, 37, 36], [22, 43, 40]) == [35, 36, 37, 9, 13, 16, 21, 40, 43, 22]
    assert candidate([5, 10, 19, 24, 27, 40, 41], [30, 41, 30]) == [5, 40, 10, 19, 24, 27, 30]
    assert candidate([8, 18, 21, 25, 26, 36, 35], [27, 44, 33]) == [35, 36, 8, 18, 21, 25, 26, 33, 27, 44]
    assert candidate([9, 18, 15, 27, 32, 30, 36], [29, 42, 35]) == [32, 36, 9, 15, 18, 27, 30, 42, 35, 29]
    assert candidate([5, 17, 25, 21, 28, 36, 42], [21, 42, 35]) == [36, 5, 17, 25, 28, 35]
    assert candidate([5, 13, 22, 29, 31, 35, 37], [30, 45, 36]) == [35, 37, 5, 13, 22, 29, 31, 36, 45, 30]
    assert candidate([8, 19, 22, 29, 33, 37, 36], [29, 37, 31]) == [33, 36, 8, 19, 22, 31]
    assert candidate([13, 20, 25, 20, 33, 40, 39], [27, 35, 38]) == [33, 39, 40, 13, 20, 25, 27, 35, 38]
    assert candidate([12, 16, 18, 30, 35, 36, 37], [22, 45, 33]) == [35, 36, 37, 12, 16, 18, 30, 33, 45, 22]
    assert candidate([10, 10, 16, 29, 31, 37, 43], [26, 38, 34]) == [37, 10, 43, 16, 29, 31, 26, 34, 38]
    assert candidate([10, 17, 17, 26, 29, 34, 44], [21, 35, 40]) == [34, 10, 44, 17, 26, 29, 40, 35, 21]
    assert candidate([15, 14, 20, 23, 25, 40, 38], [27, 38, 33]) == [40, 14, 15, 20, 23, 25, 33, 27]
    assert candidate([15, 17, 19, 28, 26, 39, 40], [29, 38, 38]) == [39, 40, 15, 17, 19, 26, 28, 29, 38]
    assert candidate([11, 18, 20, 26, 34, 32, 35], [29, 41, 40]) == [32, 34, 35, 11, 18, 20, 26, 40, 41, 29]
    assert candidate([9, 20, 19, 25, 30, 34, 37], [21, 41, 33]) == [34, 37, 9, 19, 20, 25, 30, 41, 21, 33]
    assert candidate([13, 14, 25, 28, 29, 40, 41], [29, 43, 36]) == [40, 41, 13, 14, 25, 28, 43, 36]
    assert candidate([13, 14, 25, 21, 30, 35, 40], [24, 36, 36]) == [35, 40, 13, 14, 21, 25, 30, 24, 36]
    assert candidate([6, 17, 18, 24, 27, 31, 42], [23, 41, 38]) == [6, 42, 17, 18, 24, 27, 31, 41, 38, 23]
    assert candidate([13, 11, 17, 26, 35, 31, 35], [30, 45, 32]) == [35, 11, 13, 17, 26, 31, 32, 45, 30]
    assert candidate([7, 11, 19, 27, 35, 40, 36], [22, 37, 38]) == [35, 36, 7, 40, 11, 19, 27, 37, 38, 22]
    assert candidate([12, 11, 25, 20, 32, 36, 44], [20, 38, 40]) == [32, 36, 11, 12, 44, 25, 40, 38]
    assert candidate([13, 14, 19, 27, 26, 38, 35], [20, 42, 37]) == [35, 38, 13, 14, 19, 26, 27, 42, 20, 37]
    assert candidate([10, 15, 21, 23, 28, 34, 39], [22, 38, 35]) == [34, 39, 10, 15, 21, 23, 28, 35, 38, 22]
    assert candidate([13, 13, 23, 23, 28, 31, 39], [27, 41, 32]) == [39, 13, 23, 28, 31, 32, 41, 27]
    assert candidate([12, 17, 23, 27, 32, 36, 43], [26, 44, 32]) == [36, 43, 12, 17, 23, 27, 26, 44]
    assert candidate([6, 10, 24, 22, 25, 40, 42], [27, 42, 36]) == [6, 40, 10, 22, 24, 25, 27, 36]
    assert candidate([6, 15, 16, 26, 33, 37, 37], [25, 39, 38]) == [33, 37, 6, 15, 16, 26, 25, 38, 39]
    assert candidate([7, 16, 20, 23, 31, 30, 36], [20, 44, 30]) == [36, 7, 16, 23, 31, 44]
    assert candidate([5, 15, 25, 21, 29, 30, 39], [22, 35, 31]) == [5, 39, 15, 21, 25, 29, 30, 35, 22, 31]
    assert candidate([14, 11, 16, 28, 30, 34, 44], [23, 43, 34]) == [11, 44, 14, 16, 28, 30, 43, 23]
    assert candidate([14, 14, 25, 28, 26, 32, 40], [28, 35, 33]) == [32, 40, 14, 25, 26, 33, 35]
    assert candidate([5, 18, 15, 23, 32, 32, 40], [24, 40, 31]) == [32, 5, 15, 18, 23, 24, 31]
    assert candidate([11, 14, 16, 25, 32, 33, 43], [27, 43, 32]) == [33, 11, 14, 16, 25, 27]
    assert candidate([2, 1, 2, 2, 6], [3, 9, 5]) == [1, 2, 6, 9, 3, 5]
    assert candidate([5, 6, 2, 2, 10], [8, 7, 3]) == [2, 10, 5, 6, 8, 3, 7]
    assert candidate([2, 3, 4, 8, 2], [3, 2, 6]) == [8, 4, 6]
    assert candidate([2, 2, 3, 4, 10], [7, 7, 5]) == [3, 10, 2, 4, 5, 7]
    assert candidate([1, 1, 4, 8, 6], [5, 12, 1]) == [8, 4, 6, 12, 5]
    assert candidate([6, 1, 8, 7, 6], [4, 5, 5]) == [8, 1, 6, 7, 4, 5]
    assert candidate([4, 4, 8, 2, 4], [8, 9, 6]) == [2, 4, 9, 6]
    assert candidate([3, 2, 8, 2, 9], [11, 10, 6]) == [8, 9, 2, 3, 10, 11, 6]
    assert candidate([2, 2, 8, 7, 7], [1, 8, 1]) == [2, 7, 1]
    assert candidate([4, 6, 4, 7, 5], [9, 10, 4]) == [5, 6, 7, 9, 10]
    assert candidate([1, 1, 8, 2, 10], [2, 4, 1]) == [8, 10, 4]
    assert candidate([1, 2, 7, 1, 6], [8, 8, 6]) == [1, 2, 7, 8]
    assert candidate([2, 3, 8, 1, 8], [4, 7, 6]) == [8, 1, 2, 3, 4, 6, 7]
    assert candidate([3, 3, 7, 8, 2], [9, 7, 6]) == [8, 2, 3, 9, 6]
    assert candidate([4, 2, 4, 8, 9], [3, 9, 2]) == [8, 4, 3]
    assert candidate([2, 2, 4, 9, 1], [9, 9, 1]) == [2, 4]
    assert candidate([3, 2, 2, 4, 3], [10, 5, 2]) == [3, 4, 10, 5]
    assert candidate([4, 1, 3, 5, 6], [4, 7, 6]) == [1, 3, 5, 7]
    assert candidate([4, 4, 8, 5, 4], [6, 3, 2]) == [8, 4, 5, 2, 3, 6]
    assert candidate([5, 3, 1, 8, 9], [1, 5, 2]) == [8, 9, 3, 2]
    assert candidate([5, 7, 2, 4, 5], [9, 12, 1]) == [2, 4, 5, 7, 9, 12, 1]
    assert candidate([1, 4, 8, 8, 5], [1, 12, 2]) == [8, 4, 5, 2, 12]
    assert candidate([1, 2, 2, 4, 9], [1, 5, 3]) == [9, 2, 4, 3, 5]
    assert candidate([2, 4, 6, 8, 4], [6, 9, 5]) == [8, 2, 4, 9, 5]
    assert candidate([3, 3, 5, 6, 3], [10, 6, 1]) == [3, 5, 1, 10]
    assert candidate([2, 3, 3, 4, 10], [6, 10, 6]) == [2, 3, 4, 6]
    assert candidate([4, 1, 2, 2, 1], [5, 9, 4]) == [1, 2, 9, 5]
    assert candidate([2, 7, 1, 5, 4], [7, 8, 5]) == [1, 2, 4, 8]
    assert candidate([4, 6, 4, 6, 9], [2, 7, 5]) == [9, 4, 6, 2, 5, 7]
    assert candidate([6, 6, 8, 6, 5], [6, 3, 3]) == [8, 5, 3]
    assert candidate([4, 7, 4, 7, 1], [11, 7, 6]) == [1, 4, 11, 6]
    assert candidate([1, 4, 6, 3, 7], [2, 5, 3]) == [1, 4, 6, 7, 2, 5]
    assert candidate([5, 7, 8, 2, 3], [7, 5, 2]) == [8, 3]
    assert candidate([4, 4, 8], [6, 5, 2]) == [8, 4, 2, 5, 6]
    assert candidate([4, 5, 2], [6, 3, 2]) == [4, 5, 3, 6]
    assert candidate([3, 1, 1], [4, 12, 5]) == [1, 3, 12, 4, 5]
    assert candidate([5, 7, 4], [10, 3, 1]) == [4, 5, 7, 1, 10, 3]
    assert candidate([4, 6, 8], [11, 9, 6]) == [8, 4, 9, 11]
    assert candidate([1, 5, 8], [2, 7, 4]) == [8, 1, 5, 2, 4, 7]
    assert candidate([3, 1, 7], [4, 9, 4]) == [1, 3, 7, 9, 4]
    assert candidate([5, 7, 5], [1, 2, 6]) == [5, 7, 1, 2, 6]
    assert candidate([4, 1, 1], [2, 5, 5]) == [1, 4, 2, 5]
    assert candidate([2, 2, 6], [1, 4, 3]) == [2, 6, 1, 3, 4]
    assert candidate([4, 2, 4], [9, 10, 4]) == [2, 9, 10]
    assert candidate([6, 6, 8], [9, 5, 2]) == [8, 6, 9, 2, 5]
    assert candidate([5, 1, 4], [3, 6, 5]) == [1, 4, 3, 6]
    assert candidate([3, 3, 5], [9, 10, 4]) == [3, 5, 9, 10, 4]
    assert candidate([2, 5, 3], [10, 6, 6]) == [2, 3, 5, 10, 6]
    assert candidate([4, 7, 6], [11, 12, 4]) == [6, 7, 11, 12]
    assert candidate([1, 2, 5], [6, 3, 3]) == [1, 2, 5, 3, 6]
    assert candidate([4, 5, 3], [10, 5, 2]) == [3, 4, 10, 2]
    assert candidate([3, 6, 3], [6, 4, 5]) == [3, 4, 5]
    assert candidate([6, 7, 4], [7, 3, 6]) == [4, 3]
    assert candidate([6, 2, 8], [9, 3, 5]) == [8, 2, 6, 9, 3, 5]
    assert candidate([1, 4, 4], [9, 3, 1]) == [4, 9, 3]
    assert candidate([3, 1, 2], [11, 3, 4]) == [1, 2, 11, 4]
    assert candidate([3, 5, 6], [6, 11, 2]) == [3, 5, 2, 11]
    assert candidate([2, 1, 7], [11, 7, 6]) == [1, 2, 11, 6]
    assert candidate([4, 7, 1], [9, 6, 3]) == [1, 4, 7, 9, 3, 6]
    assert candidate([5, 3, 4], [6, 7, 5]) == [3, 4, 6, 7]
    assert candidate([3, 3, 8], [4, 6, 3]) == [8, 4, 6]
    assert candidate([4, 5, 4], [3, 10, 6]) == [4, 5, 10, 3, 6]
    assert candidate([1, 2, 2], [8, 4, 6]) == [1, 2, 8, 4, 6]
    assert candidate([4, 4, 6], [8, 7, 3]) == [4, 6, 8, 3, 7]
    assert candidate([2, 2, 2], [6, 6, 2]) == [6]
    assert candidate([1, 2, 8], [2, 9, 1]) == [8, 9]

if __name__ == '__main__':
    check(Diff)