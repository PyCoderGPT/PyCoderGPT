from case_MBPP_401 import Odd_Length_Sum


def check(candidate):
    assert candidate([1,2,4]) == 14
    assert candidate([1,2,1,2]) == 15
    assert candidate([1,7]) == 8
    assert candidate([1, 1, 6]) == 16
    assert candidate([4, 4, 6]) == 28
    assert candidate([4, 2, 5]) == 22
    assert candidate([2, 3, 5]) == 20
    assert candidate([5, 5, 7]) == 34
    assert candidate([4, 4, 7]) == 30
    assert candidate([5, 3, 3]) == 22
    assert candidate([4, 3, 7]) == 28
    assert candidate([1, 3, 3]) == 14
    assert candidate([6, 4, 5]) == 30
    assert candidate([4, 4, 4]) == 24
    assert candidate([6, 7, 4]) == 34
    assert candidate([6, 2, 4]) == 24
    assert candidate([6, 7, 2]) == 30
    assert candidate([1, 6, 5]) == 24
    assert candidate([5, 1, 2]) == 16
    assert candidate([2, 4, 3]) == 18
    assert candidate([5, 6, 3]) == 28
    assert candidate([1, 1, 5]) == 14
    assert candidate([1, 5, 2]) == 16
    assert candidate([2, 3, 4]) == 18
    assert candidate([5, 6, 6]) == 34
    assert candidate([1, 1, 9]) == 22
    assert candidate([5, 7, 7]) == 38
    assert candidate([4, 2, 3]) == 18
    assert candidate([1, 5, 2]) == 16
    assert candidate([2, 5, 7]) == 28
    assert candidate([6, 7, 6]) == 38
    assert candidate([2, 3, 6]) == 22
    assert candidate([4, 7, 4]) == 30
    assert candidate([6, 3, 3]) == 24
    assert candidate([6, 5, 4]) == 30
    assert candidate([1, 4, 9]) == 28
    assert candidate([6, 3, 2, 6]) == 39
    assert candidate([6, 2, 4, 4]) == 38
    assert candidate([5, 3, 6, 4]) == 45
    assert candidate([5, 3, 3, 7]) == 42
    assert candidate([1, 1, 4, 3]) == 23
    assert candidate([4, 3, 1, 3]) == 26
    assert candidate([5, 7, 6, 5]) == 59
    assert candidate([6, 5, 5, 7]) == 56
    assert candidate([4, 6, 4, 5]) == 48
    assert candidate([2, 3, 5, 7]) == 42
    assert candidate([2, 7, 5, 7]) == 54
    assert candidate([6, 4, 6, 1]) == 44
    assert candidate([2, 1, 4, 4]) == 27
    assert candidate([1, 4, 1, 6]) == 29
    assert candidate([4, 1, 4, 6]) == 35
    assert candidate([3, 1, 1, 6]) == 24
    assert candidate([5, 7, 1, 4]) == 42
    assert candidate([4, 3, 2, 1]) == 25
    assert candidate([2, 3, 4, 5]) == 35
    assert candidate([2, 6, 3, 3]) == 37
    assert candidate([3, 6, 5, 2]) == 43
    assert candidate([1, 5, 5, 2]) == 36
    assert candidate([1, 4, 4, 6]) == 38
    assert candidate([4, 6, 1, 4]) == 37
    assert candidate([1, 6, 2, 4]) == 34
    assert candidate([1, 5, 2, 6]) == 35
    assert candidate([3, 5, 4, 2]) == 37
    assert candidate([4, 1, 5, 4]) == 34
    assert candidate([6, 6, 4, 7]) == 56
    assert candidate([4, 7, 5, 6]) == 56
    assert candidate([1, 2, 3, 4]) == 25
    assert candidate([4, 3, 2, 7]) == 37
    assert candidate([4, 4, 5, 4]) == 43
    assert candidate([6, 5]) == 11
    assert candidate([2, 4]) == 6
    assert candidate([6, 4]) == 10
    assert candidate([4, 7]) == 11
    assert candidate([6, 2]) == 8
    assert candidate([2, 7]) == 9
    assert candidate([2, 5]) == 7
    assert candidate([3, 7]) == 10
    assert candidate([6, 2]) == 8
    assert candidate([3, 9]) == 12
    assert candidate([3, 9]) == 12
    assert candidate([2, 5]) == 7
    assert candidate([3, 4]) == 7
    assert candidate([5, 6]) == 11
    assert candidate([3, 3]) == 6
    assert candidate([5, 4]) == 9
    assert candidate([6, 9]) == 15
    assert candidate([2, 5]) == 7
    assert candidate([2, 6]) == 8
    assert candidate([2, 3]) == 5
    assert candidate([3, 6]) == 9
    assert candidate([5, 5]) == 10
    assert candidate([6, 9]) == 15
    assert candidate([5, 2]) == 7
    assert candidate([6, 10]) == 16
    assert candidate([2, 9]) == 11
    assert candidate([3, 3]) == 6
    assert candidate([1, 3]) == 4
    assert candidate([1, 8]) == 9
    assert candidate([4, 10]) == 14
    assert candidate([1, 10]) == 11
    assert candidate([2, 5]) == 7
    assert candidate([4, 4]) == 8

if __name__ == '__main__':
    check(Odd_Length_Sum)