from case_MBPP_294 import big_diff


def check(candidate):
    assert candidate([1,2,3,4]) == 3
    assert candidate([4,5,12]) == 8
    assert candidate([9,2,3]) == 7
    assert candidate([5, 4, 6, 1]) == 5
    assert candidate([5, 3, 3, 1]) == 4
    assert candidate([5, 4, 6, 8]) == 4
    assert candidate([3, 5, 5, 8]) == 5
    assert candidate([4, 6, 1, 5]) == 5
    assert candidate([3, 5, 7, 8]) == 5
    assert candidate([5, 3, 5, 1]) == 4
    assert candidate([3, 1, 5, 1]) == 4
    assert candidate([4, 6, 1, 9]) == 8
    assert candidate([5, 1, 1, 8]) == 7
    assert candidate([6, 3, 4, 6]) == 3
    assert candidate([2, 2, 6, 1]) == 5
    assert candidate([3, 7, 8, 6]) == 5
    assert candidate([5, 7, 2, 4]) == 5
    assert candidate([1, 7, 5, 1]) == 6
    assert candidate([5, 4, 2, 6]) == 4
    assert candidate([5, 2, 7, 5]) == 5
    assert candidate([4, 2, 5, 5]) == 3
    assert candidate([1, 4, 1, 5]) == 4
    assert candidate([3, 7, 3, 7]) == 4
    assert candidate([5, 6, 6, 3]) == 3
    assert candidate([1, 5, 2, 2]) == 4
    assert candidate([4, 1, 6, 1]) == 5
    assert candidate([4, 7, 4, 4]) == 3
    assert candidate([4, 3, 5, 1]) == 4
    assert candidate([6, 4, 2, 4]) == 4
    assert candidate([3, 2, 8, 1]) == 7
    assert candidate([4, 2, 4, 9]) == 7
    assert candidate([6, 2, 7, 5]) == 5
    assert candidate([6, 6, 2, 4]) == 4
    assert candidate([5, 3, 1, 6]) == 5
    assert candidate([5, 2, 2, 6]) == 4
    assert candidate([6, 1, 7, 1]) == 6
    assert candidate([2, 8, 9]) == 7
    assert candidate([8, 10, 10]) == 2
    assert candidate([1, 8, 9]) == 8
    assert candidate([9, 9, 16]) == 7
    assert candidate([4, 9, 15]) == 11
    assert candidate([7, 10, 11]) == 4
    assert candidate([7, 6, 13]) == 7
    assert candidate([6, 10, 10]) == 4
    assert candidate([5, 6, 14]) == 9
    assert candidate([2, 4, 10]) == 8
    assert candidate([2, 9, 15]) == 13
    assert candidate([8, 9, 17]) == 9
    assert candidate([5, 7, 11]) == 6
    assert candidate([1, 6, 11]) == 10
    assert candidate([8, 5, 12]) == 7
    assert candidate([6, 1, 15]) == 14
    assert candidate([2, 5, 12]) == 10
    assert candidate([3, 9, 14]) == 11
    assert candidate([5, 6, 8]) == 3
    assert candidate([9, 10, 17]) == 8
    assert candidate([1, 5, 9]) == 8
    assert candidate([5, 7, 15]) == 10
    assert candidate([7, 1, 11]) == 10
    assert candidate([1, 1, 17]) == 16
    assert candidate([4, 2, 9]) == 7
    assert candidate([9, 1, 16]) == 15
    assert candidate([6, 3, 8]) == 5
    assert candidate([3, 3, 8]) == 5
    assert candidate([6, 1, 12]) == 11
    assert candidate([4, 2, 13]) == 11
    assert candidate([3, 3, 7]) == 4
    assert candidate([3, 3, 17]) == 14
    assert candidate([6, 8, 12]) == 6
    assert candidate([12, 7, 5]) == 7
    assert candidate([5, 4, 5]) == 1
    assert candidate([13, 2, 8]) == 11
    assert candidate([12, 3, 4]) == 9
    assert candidate([6, 6, 5]) == 1
    assert candidate([6, 5, 1]) == 5
    assert candidate([14, 3, 7]) == 11
    assert candidate([5, 1, 7]) == 6
    assert candidate([7, 6, 5]) == 2
    assert candidate([5, 7, 1]) == 6
    assert candidate([11, 7, 5]) == 6
    assert candidate([7, 4, 5]) == 3
    assert candidate([13, 4, 5]) == 9
    assert candidate([7, 3, 6]) == 4
    assert candidate([8, 1, 8]) == 7
    assert candidate([8, 7, 8]) == 1
    assert candidate([6, 1, 5]) == 5
    assert candidate([5, 1, 4]) == 4
    assert candidate([4, 2, 7]) == 5
    assert candidate([12, 7, 1]) == 11
    assert candidate([8, 5, 7]) == 3
    assert candidate([6, 2, 2]) == 4
    assert candidate([8, 2, 3]) == 6
    assert candidate([8, 6, 8]) == 2
    assert candidate([9, 6, 5]) == 4
    assert candidate([13, 5, 8]) == 8
    assert candidate([6, 2, 8]) == 6
    assert candidate([13, 1, 8]) == 12
    assert candidate([4, 7, 1]) == 6
    assert candidate([12, 3, 1]) == 11
    assert candidate([13, 3, 6]) == 10
    assert candidate([5, 5, 4]) == 1
    assert candidate([9, 1, 1]) == 8

if __name__ == '__main__':
    check(big_diff)