from case_MBPP_424 import first_odd


def check(candidate):
    assert candidate([1,3,5]) == 1
    assert candidate([2,4,1,3]) == 1
    assert candidate ([8,9,1]) == 9
    assert candidate([5, 4, 5]) == 5
    assert candidate([3, 4, 9]) == 3
    assert candidate([3, 8, 6]) == 3
    assert candidate([6, 7, 3]) == 7
    assert candidate([4, 4, 1]) == 1
    assert candidate([3, 7, 9]) == 3
    assert candidate([2, 2, 9]) == 9
    assert candidate([5, 1, 1]) == 5
    assert candidate([5, 8, 10]) == 5
    assert candidate([4, 4, 3]) == 3
    assert candidate([2, 1, 4]) == 1
    assert candidate([3, 4, 2]) == 3
    assert candidate([4, 3, 1]) == 3
    assert candidate([3, 8, 9]) == 3
    assert candidate([6, 1, 6]) == 1
    assert candidate([1, 2, 6]) == 1
    assert candidate([5, 6, 5]) == 5
    assert candidate([1, 6, 9]) == 1
    assert candidate([3, 1, 5]) == 3
    assert candidate([5, 8, 6]) == 5
    assert candidate([5, 2, 9]) == 5
    assert candidate([1, 8, 9]) == 1
    assert candidate([1, 7, 10]) == 1
    assert candidate([2, 5, 10]) == 5
    assert candidate([2, 6, 8]) == -1
    assert candidate([6, 2, 10]) == -1
    assert candidate([1, 1, 1]) == 1
    assert candidate([5, 1, 3]) == 5
    assert candidate([3, 1, 5]) == 3
    assert candidate([6, 4, 1]) == 1
    assert candidate([5, 1, 2]) == 5
    assert candidate([1, 8, 10]) == 1
    assert candidate([1, 5, 10]) == 1
    assert candidate([3, 9, 1, 3]) == 3
    assert candidate([5, 3, 3, 7]) == 5
    assert candidate([2, 7, 1, 3]) == 7
    assert candidate([6, 6, 1, 1]) == 1
    assert candidate([4, 2, 3, 7]) == 3
    assert candidate([2, 9, 3, 8]) == 9
    assert candidate([7, 8, 4, 5]) == 7
    assert candidate([5, 8, 5, 7]) == 5
    assert candidate([3, 4, 1, 4]) == 3
    assert candidate([5, 1, 4, 5]) == 5
    assert candidate([3, 2, 4, 4]) == 3
    assert candidate([6, 8, 6, 6]) == -1
    assert candidate([5, 9, 2, 2]) == 5
    assert candidate([2, 1, 3, 7]) == 1
    assert candidate([2, 1, 4, 5]) == 1
    assert candidate([2, 9, 3, 1]) == 9
    assert candidate([1, 7, 4, 7]) == 1
    assert candidate([1, 3, 6, 1]) == 1
    assert candidate([6, 9, 6, 5]) == 9
    assert candidate([2, 8, 4, 1]) == 1
    assert candidate([3, 8, 2, 1]) == 3
    assert candidate([1, 7, 1, 1]) == 1
    assert candidate([6, 4, 4, 7]) == 7
    assert candidate([7, 1, 6, 7]) == 7
    assert candidate([3, 7, 5, 6]) == 3
    assert candidate([2, 8, 1, 2]) == 1
    assert candidate([2, 9, 6, 1]) == 9
    assert candidate([6, 2, 4, 8]) == -1
    assert candidate([7, 8, 6, 2]) == 7
    assert candidate([2, 2, 6, 1]) == 1
    assert candidate([6, 6, 1, 3]) == 1
    assert candidate([6, 3, 3, 3]) == 3
    assert candidate([7, 6, 6, 7]) == 7
    assert candidate([5, 12, 1]) == 5
    assert candidate([6, 13, 2]) == 13
    assert candidate([6, 9, 5]) == 9
    assert candidate([11, 8, 5]) == 11
    assert candidate([8, 14, 4]) == -1
    assert candidate([6, 10, 2]) == -1
    assert candidate([8, 5, 2]) == 5
    assert candidate([11, 13, 1]) == 11
    assert candidate([11, 8, 5]) == 11
    assert candidate([4, 10, 4]) == -1
    assert candidate([8, 13, 4]) == 13
    assert candidate([6, 5, 2]) == 5
    assert candidate([7, 6, 3]) == 7
    assert candidate([8, 13, 1]) == 13
    assert candidate([13, 13, 1]) == 13
    assert candidate([11, 13, 3]) == 11
    assert candidate([10, 12, 4]) == -1
    assert candidate([4, 7, 4]) == 7
    assert candidate([10, 8, 1]) == 1
    assert candidate([6, 8, 3]) == 3
    assert candidate([4, 13, 5]) == 13
    assert candidate([6, 8, 1]) == 1
    assert candidate([3, 10, 1]) == 3
    assert candidate([3, 13, 5]) == 3
    assert candidate([9, 11, 4]) == 9
    assert candidate([12, 12, 3]) == 3
    assert candidate([11, 11, 5]) == 11
    assert candidate([13, 10, 5]) == 13
    assert candidate([8, 5, 3]) == 5
    assert candidate([11, 8, 2]) == 11
    assert candidate([3, 7, 6]) == 3
    assert candidate([8, 8, 2]) == -1
    assert candidate([12, 5, 5]) == 5

if __name__ == '__main__':
    check(first_odd)