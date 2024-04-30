from case_HE_003 import below_zero


def check(candidate):
    assert candidate([3, -3, 7, 1, 8, -1, 9, 0]) == False
    assert candidate([6, -4, 3, -3, 10, -5, 7, -2]) == False
    assert candidate([1, -1, 2, -2, 5, -5, 4, -4]) == False
    assert candidate([2, -6, 5, 2, 7, -8, 1, -9]) == True
    assert candidate([4, -7, 2, -5, 2, -5, 1, -2]) == True
    assert candidate([4, 3, 1, 0, 6, -10, 6, 1]) == False
    assert candidate([5, 1, -5, 7, 10]) == False
    assert candidate([4, 4, -8, 1, 6, 0]) == False
    assert candidate([4, 2, -7, 6, 1, -7]) == True
    assert candidate([4, -1, 7, 1, 9, -5, 8, -1]) == False
    assert candidate([4, 0, 6, -7, 1, -6, 6, -2]) == True
    assert candidate([3, 1, 4, -3, 7, -9, 9, -5]) == False
    assert candidate([4, -6, 6, -2, 5, -6, 3, -3]) == True
    assert candidate([5, 3, 3, 3, 1, -9, 5, -6]) == False
    assert candidate([1, -6, 6, -4, 3, -10, 2, -7]) == True
    assert candidate([6, 1, 2, -4, 5, -5, 1, -3]) == False
    assert candidate([6, 6, -4, 3, 2, -4]) == False
    assert candidate([3, -3, 2, -1, 10, -9, 3, -8]) == True
    assert candidate([2, 4, 5, 3, 6, 0, 8, 0]) == False
    assert candidate([4, 5, -7, 5, 11]) == False
    assert candidate([3, 0, 7, -3, 8, -6, 6, -7]) == False
    assert candidate([1, -1, 7, -6, 8, -10, 5, -9]) == True
    assert candidate([1, -4, 3, 0, 1, -1, 4, -5]) == True
    assert candidate([2, -6, 2, 0, 3, -7, 7, -10]) == True
    assert candidate([2, -6, 3, 0, 3, -8, 7, -9]) == True
    assert candidate([2, -6, 5, -3, 1, -1, 5, -8]) == True
    assert candidate([3, 2, 6, 3, 10, -6, 4, -9]) == False
    assert candidate([3, -7, 5, -3, 9, -1, 6, -1]) == True
    assert candidate([1, 1, 6, 1, 7, -7, 1, -9]) == False
    assert candidate([2, 3, -8, 2, 3]) == True
    assert candidate([6, 3, -4, 4, 10]) == False
    assert candidate([1, 2, -4, 5, 6]) == True
    assert candidate([6, 4, 1, 1, 9]) == False
    assert candidate([4, 1, -7, 1, 4, -4]) == True
    assert candidate([2, 5, -3, 1, 2, -4]) == False
    assert candidate([3, 5, 1, 8, 7]) == False
    assert candidate([5, 1, -8, 1, 6, -2]) == True
    assert candidate([2, 1, -4, 6, 6]) == True
    assert candidate([4, 5, -8, 5, 1, -5]) == False
    assert candidate([5, 2, 2, 1, 6, 1]) == False
    assert candidate([1, 3, 5, -5, 4, -5, 4, 1]) == False
    assert candidate([1, 7, -7, 1, 2, 2]) == False
    assert candidate([6, 5, -4, 10, 6]) == False
    assert candidate([5, 0, 1, 3, 10, -8, 2, 1]) == False
    assert candidate([3, 7, -2, 2, 2, 1]) == False
    assert candidate([6, 1, 1, -2, 9, -9, 9, 0]) == False
    assert candidate([5, -6, 2, -3, 6, -1, 1, -6]) == True
    assert candidate([5, -7, 2, -2, 2, -3, 6, 1]) == True
    assert candidate([2, 0, 4, -2, 2, -2, 5, -8]) == False
    assert candidate([6, 3, 6, -5, 3, -1, 1, -6]) == False
    assert candidate([3, 4, 0, 4, 11]) == False
    assert candidate([1, 2, 1, 3, 7, 0, 4, -4]) == False
    assert candidate([2, 3, -9, 10, 10]) == True
    assert candidate([4, 6, -4, 1, 4]) == False
    assert candidate([6, 6, -3, 8, 6]) == False
    assert candidate([5, -1, 3, 1, 5, -3, 3, -7]) == False
    assert candidate([2, 6, -1, 2, 5]) == False
    assert candidate([6, 0, 7, 3, 4, -8, 4, -4]) == False
    assert candidate([3, 6, -3, 3, 1, -1]) == False
    assert candidate([1, -3, 5, 2, 2, -9, 8, -4]) == True
    assert candidate([5, 7, -1, 7, 11]) == False
    assert candidate([5, -5, 4, -3, 3, -2, 1, 0]) == False
    assert candidate([5, 4, 1, 1, 6, -2]) == False
    assert candidate([6, -5, 6, -1, 5, -2, 5, -1]) == False
    assert candidate([4, -5, 5, -6, 8, -6, 5, -6]) == True
    assert candidate([1, 4, -4, 1, 1, -1]) == False
    assert candidate([3, 2, -2, 6, 7, -3]) == False
    assert candidate([4, -6, 5, -5, 4, -1, 1, -2]) == True
    assert candidate([]) == False
    assert candidate([6, 1, -1, 10, 2]) == False
    assert candidate([2, -3, 5, 2, 2, -4, 6, -2]) == True
    assert candidate([3, 5, -5, 1, 5]) == False
    assert candidate([4, 4, -2, 1, 1, -6]) == False
    assert candidate([4, 7, 2, 6, 3, -6]) == False
    assert candidate([1, 2, -3, 1, 2, -3]) == False
    assert candidate([1, -5, 3, -2, 1, -10, 1, -9]) == True
    assert candidate([1, -3, 3, -3, 1, -9, 7, 1]) == True
    assert candidate([5, -5, 2, -4, 10, -3, 5, -1]) == True
    assert candidate([5, -6, 4, -1, 1, -10, 9, -1]) == True
    assert candidate([4, -4, 5, -1, 7, -9, 8, -3]) == False
    assert candidate([2, 7, -2, 3, 1, -1]) == False
    assert candidate([5, 4, 3, -3, 1, -5, 9, -6]) == False
    assert candidate([2, 3, 3, 2, 8, -2, 1, 1]) == False
    assert candidate([4, -6, 5, 3, 8, -8, 9, -1]) == True
    assert candidate([1, -1, 6, -6, 8, -9, 9, 0]) == True
    assert candidate([1, -2, 2, -2, 5, -5, 4, -4]) == True
    assert candidate([5, 6, -5, 9, 2]) == False
    assert candidate([6, 0, 5, 1, 3, -5, 1, -6]) == False
    assert candidate([2, -2, 1, -7, 1, -9, 6, 0]) == True
    assert candidate([1, -1, 2, -2, 5, -5, 4, -5]) == True
    assert candidate([5, 2, 5, 1, 2, -7, 9, -4]) == False

if __name__ == '__main__':
    check(below_zero)