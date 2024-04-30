from case_HE_121 import solution


def check(candidate):
    assert candidate([29, 9, 22, 322]) == 29
    assert candidate([8, 6, 12, 5]) == 0
    assert candidate([7, 11, 6, 4]) == 7
    assert candidate([6, 7]) == 0
    assert candidate([2, 10, 7, 6]) == 7
    assert candidate([9, 14]) == 9
    assert candidate([4, 8, 13]) == 13
    assert candidate([5, 8, 12]) == 5
    assert candidate([35, 14, 19, 323]) == 54
    assert candidate([5, 3, 8, 1, 6]) == 5
    assert candidate([33, 16, 28, 27]) == 33
    assert candidate([29, 16, 21, 325]) == 50
    assert candidate([1, 13, 9, 4]) == 10
    assert candidate([9, 5]) == 9
    assert candidate([25, 17, 22, 29]) == 25
    assert candidate([29, 17, 25, 34]) == 54
    assert candidate([30, 14, 27, 319]) == 27
    assert candidate([6, 3, 1, 1, 7]) == 8
    assert candidate([10, 7]) == 0
    assert candidate([8, 13, 10, 1]) == 0
    assert candidate([10, 5]) == 0
    assert candidate([31, 13, 20, 323]) == 31
    assert candidate([6, 2, 13]) == 13
    assert candidate([8, 8]) == 0
    assert candidate([1, 3, 3, 6]) == 4
    assert candidate([3, 6]) == 3
    assert candidate([7, 3, 6, 8, 4]) == 7
    assert candidate([26, 11, 29, 325]) == 29
    assert candidate([3, 13, 2, 9]) == 3

    # Check some edge cases that are easy to work out by hand.
    assert candidate([7, 9, 7, 11]) == 14
    assert candidate([31, 11, 21, 27]) == 52
    assert candidate([7, 17, 1, 4]) == 8
    assert candidate([4, 3, 5, 6, 4]) == 5
    assert candidate([3, 3, 2, 1, 3]) == 6
    assert candidate([7, 3, 2, 4]) == 7
    assert candidate([1, 2, 4, 1, 8]) == 1
    assert candidate([3, 12, 7, 14]) == 10
    assert candidate([5, 16, 3, 12]) == 8
    assert candidate([7, 4, 5]) == 12
    assert candidate([4, 4, 8, 2]) == 0
    assert candidate([7, 6, 5, 5]) == 12
    assert candidate([26, 14, 28, 324]) == 0
    assert candidate([34, 13, 23, 36]) == 23
    assert candidate([29, 17, 18, 34]) == 29
    assert candidate([31, 17, 28, 318]) == 31
    assert candidate([7, 16, 7, 9]) == 14
    assert candidate([30, 12, 18, 27]) == 0
    assert candidate([3, 3, 3, 3, 3]) == 9
    assert candidate([4, 15, 5, 9]) == 5
    assert candidate([8, 4, 8, 2, 1]) == 1
    assert candidate([35, 16, 28, 30]) == 35
    assert candidate([4, 7]) == 0
    assert candidate([27, 18, 21, 32]) == 48
    assert candidate([6, 10]) == 0
    assert candidate([10, 7, 6, 4]) == 0
    assert candidate([10, 12, 4, 1]) == 0
    assert candidate([6, 6, 3, 7, 3]) == 6
    assert candidate([27, 14, 21, 29]) == 48
    assert candidate([7, 15, 1, 10]) == 8
    assert candidate([30, 8, 26, 325]) == 0
    assert candidate([1, 8, 8, 1, 1]) == 2
    assert candidate([7, 4, 12]) == 7
    assert candidate([32, 17, 22, 31]) == 0
    assert candidate([2, 12, 4, 7]) == 0
    assert candidate([2, 12, 7, 9]) == 7
    assert candidate([29, 10, 28, 37]) == 29
    assert candidate([6, 4, 4]) == 0
    assert candidate([5, 4, 3, 1, 7]) == 15
    assert candidate([32, 17, 27, 321]) == 27
    assert candidate([29, 8, 29, 319]) == 58
    assert candidate([4, 2, 4, 1, 6]) == 0
    assert candidate([7, 5, 9]) == 16
    assert candidate([3, 9, 4, 7]) == 3
    assert candidate([3, 8, 10, 5]) == 3
    assert candidate([7, 2, 13]) == 20
    assert candidate([7, 6, 13]) == 20
    assert candidate([31, 8, 26, 34]) == 31
    assert candidate([1, 5]) == 1
    assert candidate([9, 9, 9, 2]) == 18
    assert candidate([2, 4, 13]) == 13
    assert candidate([1, 10]) == 1
    assert candidate([8, 9, 3, 8]) == 3
    assert candidate([4, 4, 6]) == 0
    assert candidate([3, 5]) == 3
    assert candidate([1, 9]) == 1
    assert candidate([5, 9]) == 5
    assert candidate([2, 2, 4, 2, 7]) == 7
    assert candidate([4, 3, 11]) == 11
    assert candidate([5, 12, 6, 1]) == 5
    assert candidate([5, 6, 7, 1]) == 12
    assert candidate([4, 8, 11]) == 11
    assert candidate([1, 16, 4, 8]) == 1
    assert candidate([7, 7, 3]) == 10
    assert candidate([1, 7, 9]) == 10
    assert candidate([32, 13, 28, 325]) == 0
    assert candidate([3, 13, 6, 7]) == 3
    assert candidate([8, 4, 5, 6, 4]) == 5
    assert candidate([6, 6]) == 0
    assert candidate([5, 3, 10]) == 5
    assert candidate([5, 8, 7, 1])    == 12
    assert candidate([30, 13, 23, 32]) == 23
    assert candidate([26, 12, 18, 31]) == 0
    assert candidate([1, 4]) == 1
    assert candidate([10, 9]) == 0
    assert candidate([7, 1, 7, 1, 4]) == 14
    assert candidate([29, 11, 18, 30]) == 29
    assert candidate([4, 8]) == 0
    assert candidate([29, 18, 20, 323]) == 29
    assert candidate([5, 12, 3, 11]) == 8
    assert candidate([29, 10, 27, 323]) == 56
    assert candidate([26, 11, 23, 319]) == 23
    assert candidate([6, 3, 3, 3, 7]) == 10
    assert candidate([6, 11, 4, 9]) == 0
    assert candidate([1, 11]) == 1
    assert candidate([34, 16, 24, 326]) == 0
    assert candidate([35, 18, 24, 318]) == 35
    assert candidate([5, 3, 1, 1, 6]) == 6
    assert candidate([6, 13, 11, 6]) == 11
    assert candidate([2, 9, 10]) == 0
    assert candidate([33, 10, 20, 37]) == 33
    assert candidate([8, 7, 7, 7, 2]) == 7
    assert candidate([30, 13, 24, 321]) == 0
    assert candidate([7, 9, 4]) == 7
    assert candidate([2, 4, 8]) == 0
    assert candidate([5, 13, 3, 9]) == 8
    assert candidate([34, 16, 22, 323]) == 0
    assert candidate([3, 10, 12, 2]) == 3
    assert candidate([2, 15, 5, 9]) == 5
    assert candidate([1, 3, 2, 3, 8]) == 1
    assert candidate([9, 4, 8, 3]) == 9
    assert candidate([32, 14, 20, 35]) == 0
    assert candidate([27, 13, 24, 35]) == 27
    assert candidate([1, 7, 3, 6]) == 4

if __name__ == '__main__':
    check(solution)