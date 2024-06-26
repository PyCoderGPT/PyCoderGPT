from case_MBPP_202 import remove_odd


def check(candidate):
    assert candidate([1,2,3]) == [2]
    assert candidate([2,4,6]) == [2,4,6]
    assert candidate([10,20,3]) == [10,20]
    assert candidate([6, 6, 6]) == [6, 6, 6]
    assert candidate([2, 4, 6]) == [2, 4, 6]
    assert candidate([1, 3, 2]) == [3, 2]
    assert candidate([3, 4, 8]) == [4, 8]
    assert candidate([1, 5, 5]) == [5]
    assert candidate([4, 2, 1]) == [4, 2]
    assert candidate([5, 3, 5]) == [3]
    assert candidate([4, 5, 8]) == [4, 8]
    assert candidate([2, 4, 4]) == [2, 4, 4]
    assert candidate([3, 1, 4]) == [1, 4]
    assert candidate([5, 5, 6]) == [5, 6]
    assert candidate([6, 5, 8]) == [6, 8]
    assert candidate([4, 3, 7]) == [4, 7]
    assert candidate([2, 4, 6]) == [2, 4, 6]
    assert candidate([2, 7, 7]) == [2, 7]
    assert candidate([2, 5, 6]) == [2, 6]
    assert candidate([5, 1, 3]) == [1]
    assert candidate([6, 1, 5]) == [6, 5]
    assert candidate([4, 1, 8]) == [4, 8]
    assert candidate([3, 4, 1]) == [4]
    assert candidate([6, 3, 1]) == [6, 1]
    assert candidate([4, 1, 4]) == [4, 4]
    assert candidate([5, 2, 7]) == [2]
    assert candidate([6, 7, 5]) == [6, 5]
    assert candidate([1, 3, 8]) == [3, 8]
    assert candidate([4, 7, 3]) == [4, 3]
    assert candidate([4, 5, 2]) == [4, 2]
    assert candidate([1, 1, 2]) == [1, 2]
    assert candidate([3, 3, 3]) == [3]
    assert candidate([2, 1, 8]) == [2, 8]
    assert candidate([6, 2, 8]) == [6, 2, 8]
    assert candidate([5, 2, 7]) == [2]
    assert candidate([4, 6, 3]) == [4, 6]
    assert candidate([6, 7, 10]) == [6, 10]
    assert candidate([3, 5, 2]) == [5, 2]
    assert candidate([6, 2, 6]) == [6, 2, 6]
    assert candidate([5, 2, 2]) == [2, 2]
    assert candidate([3, 3, 6]) == [3, 6]
    assert candidate([5, 8, 8]) == [8, 8]
    assert candidate([4, 5, 10]) == [4, 10]
    assert candidate([1, 3, 4]) == [3, 4]
    assert candidate([3, 4, 2]) == [4, 2]
    assert candidate([4, 8, 5]) == [4, 8]
    assert candidate([7, 1, 7]) == [1]
    assert candidate([4, 4, 1]) == [4, 4]
    assert candidate([4, 5, 4]) == [4, 4]
    assert candidate([4, 5, 8]) == [4, 8]
    assert candidate([4, 3, 5]) == [4, 5]
    assert candidate([4, 1, 4]) == [4, 4]
    assert candidate([7, 2, 4]) == [2, 4]
    assert candidate([3, 1, 5]) == [1]
    assert candidate([2, 9, 2]) == [2, 2]
    assert candidate([1, 5, 11]) == [5]
    assert candidate([1, 3, 7]) == [3]
    assert candidate([5, 1, 7]) == [1]
    assert candidate([2, 3, 9]) == [2, 9]
    assert candidate([1, 8, 2]) == [8, 2]
    assert candidate([2, 1, 2]) == [2, 2]
    assert candidate([5, 9, 8]) == [9, 8]
    assert candidate([4, 8, 1]) == [4, 8]
    assert candidate([5, 7, 11]) == [7]
    assert candidate([2, 8, 5]) == [2, 8]
    assert candidate([4, 3, 8]) == [4, 8]
    assert candidate([2, 1, 10]) == [2, 10]
    assert candidate([2, 3, 8]) == [2, 8]
    assert candidate([1, 7, 5]) == [7]
    assert candidate([11, 20, 7]) == [20]
    assert candidate([12, 19, 5]) == [12, 5]
    assert candidate([8, 24, 8]) == [8, 24, 8]
    assert candidate([5, 16, 7]) == [16]
    assert candidate([12, 20, 1]) == [12, 20]
    assert candidate([5, 22, 5]) == [22]
    assert candidate([9, 25, 8]) == [25, 8]
    assert candidate([9, 15, 5]) == [15]
    assert candidate([11, 19, 2]) == [19, 2]
    assert candidate([7, 17, 2]) == [17, 2]
    assert candidate([11, 23, 3]) == [23]
    assert candidate([14, 20, 5]) == [14, 20]
    assert candidate([12, 18, 7]) == [12, 18]
    assert candidate([10, 19, 7]) == [10, 7]
    assert candidate([14, 24, 5]) == [14, 24]
    assert candidate([6, 21, 7]) == [6, 7]
    assert candidate([5, 23, 2]) == [23, 2]
    assert candidate([13, 17, 4]) == [17, 4]
    assert candidate([6, 16, 4]) == [6, 16, 4]
    assert candidate([14, 15, 6]) == [14, 6]
    assert candidate([7, 23, 4]) == [23, 4]
    assert candidate([9, 20, 8]) == [20, 8]
    assert candidate([9, 21, 7]) == [21]
    assert candidate([8, 25, 1]) == [8, 1]
    assert candidate([10, 17, 2]) == [10, 2]
    assert candidate([15, 17, 7]) == [17]
    assert candidate([15, 24, 1]) == [24]
    assert candidate([9, 21, 5]) == [21]
    assert candidate([9, 22, 2]) == [22, 2]
    assert candidate([15, 15, 1]) == [15]
    assert candidate([13, 24, 8]) == [24, 8]
    assert candidate([14, 24, 5]) == [14, 24]
    assert candidate([14, 21, 5]) == [14, 5]

if __name__ == '__main__':
    check(remove_odd)