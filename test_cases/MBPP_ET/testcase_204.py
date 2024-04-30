from case_MBPP_204 import overlapping


def check(candidate):
    assert candidate([1,2,3,4,5],[6,7,8,9]) == False
    assert candidate([1,2,3],[4,5,6]) == False
    assert candidate([1,4,5],[1,4,5]) == True
    assert candidate([1, 3, 7, 9, 1], [6, 11, 4, 12]) == 0
    assert candidate([2, 2, 5, 3, 2], [1, 9, 12, 6]) == 0
    assert candidate([3, 6, 3, 3, 9], [1, 6, 11, 14]) == 1
    assert candidate([3, 6, 5, 9, 6], [10, 3, 12, 13]) == 1
    assert candidate([2, 5, 2, 2, 5], [1, 8, 12, 13]) == 0
    assert candidate([1, 7, 8, 2, 7], [4, 6, 13, 8]) == 1
    assert candidate([1, 5, 1, 1, 7], [2, 11, 7, 4]) == 1
    assert candidate([3, 2, 7, 7, 4], [3, 11, 5, 14]) == 1
    assert candidate([3, 7, 1, 6, 7], [3, 2, 6, 13]) == 1
    assert candidate([5, 6, 8, 4, 4], [7, 3, 8, 11]) == 1
    assert candidate([3, 4, 5, 2, 3], [10, 11, 9, 6]) == 0
    assert candidate([5, 4, 4, 2, 5], [8, 6, 13, 12]) == 0
    assert candidate([3, 3, 3, 3, 9], [2, 3, 12, 7]) == 1
    assert candidate([6, 1, 3, 5, 5], [2, 7, 3, 13]) == 1
    assert candidate([4, 5, 4, 7, 1], [6, 8, 6, 14]) == 0
    assert candidate([6, 1, 1, 5, 2], [6, 5, 10, 8]) == 1
    assert candidate([5, 1, 4, 3, 10], [9, 10, 6, 12]) == 1
    assert candidate([2, 5, 7, 9, 1], [6, 10, 11, 4]) == 0
    assert candidate([1, 7, 8, 3, 1], [9, 11, 12, 12]) == 0
    assert candidate([6, 4, 4, 5, 2], [7, 8, 3, 4]) == 1
    assert candidate([4, 1, 5, 6, 8], [1, 4, 9, 14]) == 1
    assert candidate([5, 2, 4, 4, 2], [4, 7, 9, 6]) == 1
    assert candidate([2, 1, 3, 8, 9], [9, 4, 6, 4]) == 1
    assert candidate([5, 2, 5, 8, 3], [6, 7, 5, 14]) == 1
    assert candidate([5, 3, 2, 6, 10], [4, 9, 9, 11]) == 0
    assert candidate([6, 7, 7, 8, 10], [7, 6, 10, 12]) == 1
    assert candidate([3, 6, 4, 3, 2], [1, 7, 11, 11]) == 0
    assert candidate([6, 5, 8, 4, 5], [2, 4, 12, 12]) == 1
    assert candidate([5, 7, 5, 9, 5], [2, 3, 12, 12]) == 0
    assert candidate([1, 7, 4, 7, 9], [7, 11, 8, 12]) == 1
    assert candidate([6, 4, 1, 1, 10], [2, 5, 5, 10]) == 1
    assert candidate([3, 7, 6, 8, 8], [10, 11, 6, 10]) == 1
    assert candidate([3, 1, 3, 9, 5], [9, 3, 10, 6]) == 1
    assert candidate([6, 7, 5], [6, 10, 2]) == 1
    assert candidate([6, 1, 5], [7, 8, 2]) == 0
    assert candidate([2, 3, 2], [6, 10, 3]) == 1
    assert candidate([4, 7, 1], [4, 1, 8]) == 1
    assert candidate([4, 5, 3], [9, 5, 8]) == 1
    assert candidate([3, 5, 3], [7, 2, 1]) == 0
    assert candidate([6, 5, 6], [6, 10, 4]) == 1
    assert candidate([5, 4, 2], [9, 6, 4]) == 1
    assert candidate([4, 7, 2], [6, 4, 3]) == 1
    assert candidate([3, 3, 2], [7, 6, 3]) == 1
    assert candidate([1, 7, 6], [6, 6, 2]) == 1
    assert candidate([2, 1, 3], [9, 1, 1]) == 1
    assert candidate([2, 5, 1], [8, 2, 8]) == 1
    assert candidate([1, 1, 8], [9, 3, 4]) == 0
    assert candidate([6, 2, 7], [6, 5, 7]) == 1
    assert candidate([2, 1, 2], [2, 8, 7]) == 1
    assert candidate([5, 6, 1], [2, 2, 3]) == 0
    assert candidate([6, 2, 2], [8, 10, 2]) == 1
    assert candidate([3, 7, 6], [4, 4, 3]) == 1
    assert candidate([5, 4, 6], [8, 3, 6]) == 1
    assert candidate([6, 1, 1], [3, 3, 3]) == 0
    assert candidate([1, 5, 5], [6, 6, 2]) == 0
    assert candidate([5, 3, 5], [6, 5, 10]) == 1
    assert candidate([3, 4, 2], [5, 2, 7]) == 1
    assert candidate([1, 2, 3], [7, 8, 6]) == 0
    assert candidate([5, 3, 5], [8, 8, 3]) == 1
    assert candidate([2, 3, 2], [8, 3, 8]) == 1
    assert candidate([2, 7, 5], [9, 9, 8]) == 0
    assert candidate([5, 7, 2], [3, 7, 11]) == 1
    assert candidate([1, 4, 8], [2, 10, 10]) == 0
    assert candidate([1, 1, 1], [9, 2, 3]) == 0
    assert candidate([1, 3, 5], [6, 9, 7]) == 0
    assert candidate([4, 2, 4], [9, 7, 5]) == 0
    assert candidate([4, 6, 6], [1, 6, 10]) == 1
    assert candidate([3, 2, 7], [2, 7, 1]) == 1
    assert candidate([6, 3, 1], [5, 5, 3]) == 1
    assert candidate([6, 4, 3], [5, 3, 1]) == 1
    assert candidate([3, 8, 1], [6, 3, 10]) == 1
    assert candidate([6, 2, 4], [2, 6, 8]) == 1
    assert candidate([6, 4, 5], [3, 8, 4]) == 1
    assert candidate([3, 6, 6], [2, 2, 7]) == 0
    assert candidate([4, 8, 10], [1, 6, 4]) == 1
    assert candidate([1, 9, 7], [1, 9, 6]) == 1
    assert candidate([1, 3, 7], [5, 6, 3]) == 1
    assert candidate([1, 6, 10], [5, 3, 7]) == 0
    assert candidate([5, 4, 10], [4, 1, 1]) == 1
    assert candidate([2, 7, 2], [4, 2, 10]) == 1
    assert candidate([6, 1, 3], [5, 4, 1]) == 1
    assert candidate([3, 1, 8], [4, 7, 10]) == 0
    assert candidate([2, 6, 10], [2, 8, 3]) == 1
    assert candidate([5, 1, 2], [2, 1, 8]) == 1
    assert candidate([3, 4, 2], [6, 4, 4]) == 1
    assert candidate([3, 3, 1], [1, 7, 7]) == 1
    assert candidate([3, 7, 1], [4, 5, 5]) == 0
    assert candidate([1, 1, 9], [5, 1, 1]) == 1
    assert candidate([4, 6, 9], [5, 6, 10]) == 1
    assert candidate([2, 1, 6], [4, 4, 7]) == 0
    assert candidate([4, 7, 7], [3, 8, 6]) == 0
    assert candidate([5, 8, 1], [3, 9, 4]) == 0
    assert candidate([2, 9, 1], [3, 4, 5]) == 0
    assert candidate([4, 4, 9], [3, 1, 4]) == 1
    assert candidate([3, 5, 9], [2, 1, 9]) == 1
    assert candidate([5, 2, 1], [1, 8, 2]) == 1
    assert candidate([1, 9, 4], [1, 1, 4]) == 1
    assert candidate([5, 3, 9], [3, 7, 5]) == 1
    assert candidate([5, 4, 4], [4, 4, 7]) == 1

if __name__ == '__main__':
    check(overlapping)