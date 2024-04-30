from case_MBPP_415 import _sum


def check(candidate):
    assert candidate([1, 2, 3]) == 6
    assert candidate([15, 12, 13, 10]) == 50
    assert candidate([0, 1, 2]) == 3
    assert candidate([2, 1, 3]) == 6
    assert candidate([3, 2, 4]) == 9
    assert candidate([2, 4, 7]) == 13
    assert candidate([5, 5, 5]) == 15
    assert candidate([3, 3, 6]) == 12
    assert candidate([4, 2, 3]) == 9
    assert candidate([1, 4, 2]) == 7
    assert candidate([4, 7, 3]) == 14
    assert candidate([6, 2, 4]) == 12
    assert candidate([1, 1, 7]) == 9
    assert candidate([3, 3, 4]) == 10
    assert candidate([3, 4, 5]) == 12
    assert candidate([2, 5, 4]) == 11
    assert candidate([5, 2, 5]) == 12
    assert candidate([1, 6, 3]) == 10
    assert candidate([5, 3, 5]) == 13
    assert candidate([2, 1, 8]) == 11
    assert candidate([1, 5, 5]) == 11
    assert candidate([6, 7, 5]) == 18
    assert candidate([5, 3, 1]) == 9
    assert candidate([4, 4, 4]) == 12
    assert candidate([5, 7, 3]) == 15
    assert candidate([5, 2, 1]) == 8
    assert candidate([4, 6, 5]) == 15
    assert candidate([3, 1, 8]) == 12
    assert candidate([5, 1, 2]) == 8
    assert candidate([6, 2, 3]) == 11
    assert candidate([2, 5, 7]) == 14
    assert candidate([1, 1, 3]) == 5
    assert candidate([4, 6, 3]) == 13
    assert candidate([2, 1, 2]) == 5
    assert candidate([3, 5, 7]) == 15
    assert candidate([1, 5, 1]) == 7
    assert candidate([14, 14, 16, 13]) == 57
    assert candidate([20, 15, 18, 5]) == 58
    assert candidate([15, 15, 11, 6]) == 47
    assert candidate([15, 10, 16, 15]) == 56
    assert candidate([18, 11, 18, 7]) == 54
    assert candidate([20, 17, 11, 8]) == 56
    assert candidate([14, 16, 13, 6]) == 49
    assert candidate([17, 7, 8, 12]) == 44
    assert candidate([12, 15, 9, 11]) == 47
    assert candidate([16, 14, 15, 14]) == 59
    assert candidate([16, 17, 9, 10]) == 52
    assert candidate([10, 9, 14, 11]) == 44
    assert candidate([19, 13, 18, 14]) == 64
    assert candidate([19, 8, 15, 6]) == 48
    assert candidate([19, 13, 14, 10]) == 56
    assert candidate([13, 10, 9, 14]) == 46
    assert candidate([17, 16, 10, 11]) == 54
    assert candidate([10, 12, 11, 9]) == 42
    assert candidate([15, 10, 11, 12]) == 48
    assert candidate([11, 13, 18, 12]) == 54
    assert candidate([16, 14, 8, 14]) == 52
    assert candidate([12, 13, 9, 8]) == 42
    assert candidate([16, 12, 8, 15]) == 51
    assert candidate([14, 14, 14, 10]) == 52
    assert candidate([12, 11, 16, 15]) == 54
    assert candidate([14, 17, 9, 5]) == 45
    assert candidate([10, 8, 11, 7]) == 36
    assert candidate([14, 15, 14, 12]) == 55
    assert candidate([19, 10, 15, 9]) == 53
    assert candidate([20, 13, 13, 8]) == 54
    assert candidate([16, 8, 17, 7]) == 48
    assert candidate([18, 12, 9, 5]) == 44
    assert candidate([11, 14, 12, 9]) == 46
    assert candidate([1, 4, 5]) == 10
    assert candidate([4, 3, 1]) == 8
    assert candidate([5, 1, 6]) == 12
    assert candidate([5, 6, 4]) == 15
    assert candidate([3, 4, 2]) == 9
    assert candidate([2, 6, 1]) == 9
    assert candidate([3, 6, 5]) == 14
    assert candidate([2, 5, 4]) == 11
    assert candidate([3, 4, 4]) == 11
    assert candidate([5, 4, 7]) == 16
    assert candidate([2, 6, 1]) == 9
    assert candidate([1, 4, 5]) == 10
    assert candidate([4, 6, 3]) == 13
    assert candidate([4, 2, 2]) == 8
    assert candidate([1, 3, 6]) == 10
    assert candidate([1, 4, 1]) == 6
    assert candidate([5, 6, 3]) == 14
    assert candidate([2, 2, 1]) == 5
    assert candidate([3, 4, 6]) == 13
    assert candidate([2, 5, 4]) == 11
    assert candidate([3, 3, 2]) == 8
    assert candidate([5, 4, 4]) == 13
    assert candidate([5, 2, 6]) == 13
    assert candidate([4, 6, 1]) == 11
    assert candidate([2, 5, 5]) == 12
    assert candidate([2, 2, 5]) == 9
    assert candidate([5, 2, 3]) == 10
    assert candidate([4, 2, 1]) == 7
    assert candidate([3, 6, 5]) == 14
    assert candidate([1, 2, 1]) == 4
    assert candidate([5, 6, 5]) == 16
    assert candidate([4, 2, 1]) == 7
    assert candidate([4, 3, 1]) == 8

if __name__ == '__main__':
    check(_sum)