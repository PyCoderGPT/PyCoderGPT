from case_MBPP_264 import Split


def check(candidate):
    assert candidate([1,2,3,4,5,6]) == [1,3,5]
    assert candidate([10,11,12,13]) == [11,13]
    assert candidate([7,8,9,1]) == [7,9,1]
    assert candidate([5, 4, 1, 5, 8, 2]) == [5, 1, 5]
    assert candidate([5, 6, 1, 2, 2, 5]) == [5, 1, 5]
    assert candidate([2, 2, 8, 7, 3, 6]) == [7, 3]
    assert candidate([2, 3, 6, 4, 5, 5]) == [3, 5, 5]
    assert candidate([4, 4, 4, 7, 7, 1]) == [7, 7, 1]
    assert candidate([2, 4, 7, 6, 1, 3]) == [7, 1, 3]
    assert candidate([1, 5, 6, 7, 8, 8]) == [1, 5, 7]
    assert candidate([1, 1, 2, 3, 10, 2]) == [1, 1, 3]
    assert candidate([5, 1, 7, 9, 2, 10]) == [5, 1, 7, 9]
    assert candidate([6, 7, 6, 6, 2, 7]) == [7, 7]
    assert candidate([6, 2, 3, 9, 9, 6]) == [3, 9, 9]
    assert candidate([2, 6, 2, 3, 9, 5]) == [3, 9, 5]
    assert candidate([6, 5, 1, 6, 7, 1]) == [5, 1, 7, 1]
    assert candidate([4, 4, 3, 2, 3, 11]) == [3, 3, 11]
    assert candidate([4, 5, 7, 6, 10, 6]) == [5, 7]
    assert candidate([2, 5, 1, 1, 1, 1]) == [5, 1, 1, 1, 1]
    assert candidate([2, 5, 2, 3, 9, 1]) == [5, 3, 9, 1]
    assert candidate([3, 2, 7, 7, 9, 2]) == [3, 7, 7, 9]
    assert candidate([3, 7, 5, 4, 4, 9]) == [3, 7, 5, 9]
    assert candidate([6, 7, 5, 5, 2, 8]) == [7, 5, 5]
    assert candidate([2, 1, 8, 7, 6, 8]) == [1, 7]
    assert candidate([5, 5, 7, 3, 10, 9]) == [5, 5, 7, 3, 9]
    assert candidate([4, 5, 6, 4, 8, 6]) == [5]
    assert candidate([4, 2, 2, 7, 7, 2]) == [7, 7]
    assert candidate([5, 3, 5, 3, 8, 8]) == [5, 3, 5, 3]
    assert candidate([4, 2, 3, 9, 5, 1]) == [3, 9, 5, 1]
    assert candidate([2, 5, 2, 9, 5, 6]) == [5, 9, 5]
    assert candidate([6, 5, 4, 5, 1, 5]) == [5, 5, 1, 5]
    assert candidate([1, 4, 5, 7, 8, 2]) == [1, 5, 7]
    assert candidate([3, 4, 7, 4, 6, 3]) == [3, 7, 3]
    assert candidate([4, 7, 5, 8, 4, 3]) == [7, 5, 3]
    assert candidate([4, 4, 6, 2, 8, 11]) == [11]
    assert candidate([5, 5, 5, 9, 1, 7]) == [5, 5, 5, 9, 1, 7]
    assert candidate([12, 8, 16, 11]) == [11]
    assert candidate([11, 14, 12, 13]) == [11, 13]
    assert candidate([6, 8, 14, 17]) == [17]
    assert candidate([7, 7, 13, 16]) == [7, 7, 13]
    assert candidate([11, 11, 16, 8]) == [11, 11]
    assert candidate([7, 10, 10, 8]) == [7]
    assert candidate([11, 12, 9, 11]) == [11, 9, 11]
    assert candidate([13, 16, 9, 8]) == [13, 9]
    assert candidate([13, 13, 11, 15]) == [13, 13, 11, 15]
    assert candidate([15, 6, 16, 13]) == [15, 13]
    assert candidate([13, 10, 14, 10]) == [13]
    assert candidate([13, 14, 16, 9]) == [13, 9]
    assert candidate([13, 15, 14, 13]) == [13, 15, 13]
    assert candidate([8, 16, 7, 13]) == [7, 13]
    assert candidate([12, 9, 9, 12]) == [9, 9]
    assert candidate([10, 9, 9, 17]) == [9, 9, 17]
    assert candidate([5, 8, 13, 17]) == [5, 13, 17]
    assert candidate([5, 11, 15, 15]) == [5, 11, 15, 15]
    assert candidate([11, 7, 15, 17]) == [11, 7, 15, 17]
    assert candidate([5, 6, 10, 9]) == [5, 9]
    assert candidate([8, 13, 13, 11]) == [13, 13, 11]
    assert candidate([11, 14, 16, 10]) == [11]
    assert candidate([6, 7, 9, 16]) == [7, 9]
    assert candidate([9, 9, 7, 13]) == [9, 9, 7, 13]
    assert candidate([10, 10, 10, 16]) == []
    assert candidate([12, 6, 9, 9]) == [9, 9]
    assert candidate([15, 13, 15, 15]) == [15, 13, 15, 15]
    assert candidate([11, 6, 7, 8]) == [11, 7]
    assert candidate([14, 10, 9, 13]) == [9, 13]
    assert candidate([10, 10, 11, 16]) == [11]
    assert candidate([14, 15, 12, 8]) == [15]
    assert candidate([13, 6, 14, 15]) == [13, 15]
    assert candidate([10, 6, 12, 18]) == []
    assert candidate([2, 10, 5, 2]) == [5]
    assert candidate([5, 10, 14, 4]) == [5]
    assert candidate([12, 5, 8, 6]) == [5]
    assert candidate([7, 8, 11, 2]) == [7, 11]
    assert candidate([9, 4, 10, 4]) == [9]
    assert candidate([9, 8, 6, 5]) == [9, 5]
    assert candidate([7, 13, 10, 2]) == [7, 13]
    assert candidate([12, 8, 8, 6]) == []
    assert candidate([7, 11, 10, 3]) == [7, 11, 3]
    assert candidate([3, 4, 12, 1]) == [3, 1]
    assert candidate([7, 6, 12, 3]) == [7, 3]
    assert candidate([10, 3, 4, 3]) == [3, 3]
    assert candidate([7, 3, 8, 5]) == [7, 3, 5]
    assert candidate([3, 7, 6, 1]) == [3, 7, 1]
    assert candidate([7, 11, 6, 4]) == [7, 11]
    assert candidate([9, 7, 13, 2]) == [9, 7, 13]
    assert candidate([4, 10, 9, 3]) == [9, 3]
    assert candidate([3, 8, 8, 1]) == [3, 1]
    assert candidate([10, 6, 10, 4]) == []
    assert candidate([9, 3, 7, 4]) == [9, 3, 7]
    assert candidate([12, 3, 14, 4]) == [3]
    assert candidate([4, 3, 6, 2]) == [3]
    assert candidate([11, 4, 10, 1]) == [11, 1]
    assert candidate([3, 12, 12, 5]) == [3, 5]
    assert candidate([8, 6, 12, 2]) == []
    assert candidate([7, 7, 7, 4]) == [7, 7, 7]
    assert candidate([12, 9, 12, 3]) == [9, 3]
    assert candidate([12, 12, 6, 1]) == [1]
    assert candidate([5, 4, 5, 5]) == [5, 5, 5]
    assert candidate([11, 11, 12, 3]) == [11, 11, 3]
    assert candidate([8, 11, 12, 3]) == [11, 3]
    assert candidate([12, 4, 4, 2]) == []
    assert candidate([12, 8, 14, 2]) == []

if __name__ == '__main__':
    check(Split)