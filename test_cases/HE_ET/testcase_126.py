from case_HE_126 import is_sorted


def check(candidate):
    assert candidate([1, 1, 3, 6, 7, 8]) == True
    assert candidate([6, 2, 2, 3, 10, 4, 6]) == False
    assert candidate([2, 3, 3, 5]) == True
    assert candidate([1, 4, 4, 5, 6, 6, 10]) == True
    assert candidate([3, 7, 5]) == False
    assert candidate([1, 1, 3, 5, 6, 6]) == True
    assert candidate([5, 6, 3]) == False
    assert candidate([3, 4, 4, 4, 4, 7]) == False
    assert candidate([1, 5, 7, 4, 4, 2]) == False
    assert candidate([2, 2, 6, 8]) == True
    assert candidate([3, 4, 6, 7, 7]) == True
    assert candidate([3, 3, 5, 7, 1, 5]) == False
    assert candidate([2, 4, 8, 9]) == True
    assert candidate([6, 4, 4]) == False
    assert candidate([8, 1, 2]) == False
    assert candidate([1, 3, 4, 5]) == True
    assert candidate([3, 6, 3, 9, 10, 4, 10]) == False
    assert candidate([1, 3, 2, 4, 5]) == False
    assert candidate([1]) == True
    assert candidate([1, 2, 3, 3, 4, 5, 8]) == True
    assert candidate([3, 2, 1]) == False
    assert candidate([1, 1, 3, 5]) == True
    assert candidate([4, 3, 5, 6, 5, 3]) == False
    assert candidate([1, 3, 5, 5, 7]) == True
    assert candidate([5, 4, 6, 7, 1, 5]) == False
    assert candidate([4, 5, 8, 4, 2, 7]) == False
    assert candidate([2, 5, 4, 1, 1, 8, 9]) == False
    assert candidate([5, 5, 2, 3, 3, 4]) == False
    assert candidate([1, 2, 2, 2, 3, 4]) == False
    assert candidate([6, 1, 3, 6, 3, 7]) == False
    assert candidate([1, 1, 1, 2, 5, 8]) == False
    assert candidate([1, 2, 2, 2, 3, 4]) == False
    assert candidate([2, 4, 6, 4, 3, 6, 4]) == False
    assert candidate([3, 7, 7, 6, 6, 7]) == False
    assert candidate([10]) == True
    assert candidate([3, 3, 4, 6, 7, 8]) == True
    assert candidate([2, 2, 2, 5, 8, 11]) == False
    assert candidate([1, 2, 3, 3, 7, 9]) == True
    assert candidate([2, 4, 2, 9, 10]) == False
    assert candidate([3, 4, 6, 7]) == True
    assert candidate([4, 3, 6, 6, 4, 1, 9]) == False
    assert candidate([1, 2, 3, 5, 5, 8]) == True
    assert candidate([6, 1, 2, 3, 3, 3]) == False
    assert candidate([1]) == True
    assert candidate([1, 2, 2, 4, 4, 6, 8]) == True
    assert candidate([1, 3, 3, 4, 5]) == True
    assert candidate([1, 4, 4, 4, 5]) == False
    assert candidate([3, 2, 2, 2, 3]) == False
    assert candidate([3, 5, 5, 6, 7, 8, 10]) == True
    assert candidate([1, 2, 3, 4, 5]) == True
    assert candidate([4]) == True
    assert candidate([5, 7, 4, 2, 2, 4]) == False
    assert candidate([6]) == True
    assert candidate([3, 7, 4, 8, 1, 4]) == False
    assert candidate([1, 6, 3]) == False
    assert candidate([1, 3, 2, 4, 5, 6, 7]) == False
    assert candidate([6, 2, 3, 5, 2, 7]) == False
    assert candidate([1, 2, 4, 4, 6, 7, 10]) == True
    assert candidate([1, 5, 5, 6, 6, 9]) == True
    assert candidate([2, 3, 4, 4, 8, 10]) == True
    assert candidate([1, 5, 5, 6, 9]) == True
    assert candidate([1, 2, 3, 4]) == True
    assert candidate([2, 4, 5]) == True
    assert candidate([7]) == True
    assert candidate([2, 2, 3, 3, 6, 7]) == True
    assert candidate([3, 3, 6, 9, 9]) == True
    assert candidate([1, 5, 6, 7, 9, 10, 10]) == True
    assert candidate([5, 3, 3, 3, 10]) == False
    assert candidate([1, 5, 3, 4, 3]) == False
    assert candidate([2, 4, 4]) == True
    assert candidate([1, 1, 2, 4, 5, 5]) == True
    assert candidate([2, 5, 4]) == False
    assert candidate([1, 2, 2, 3, 3, 4]) == True
    assert candidate([1, 2, 3, 4, 5, 6, 7]) == True
    assert candidate([6, 3, 7, 3, 5, 6, 6]) == False
    assert candidate([1, 2, 3, 3, 3, 4]) == False
    assert candidate([1, 2, 2, 7, 8]) == True
    assert candidate([2, 1, 1, 7, 8, 9, 3]) == False
    assert candidate([1, 2, 3, 4, 5, 6]) == True
    assert candidate([1, 1, 1, 7, 3, 8]) == False
    assert candidate([3, 8, 4, 4, 10]) == False
    assert candidate([]) == True
    assert candidate([1, 2, 3, 3, 5, 7, 9]) == True
    assert candidate([2, 6, 1, 4, 5, 4, 2]) == False
    assert candidate([2, 5, 6, 8]) == True
    assert candidate([4, 5, 7, 8]) == True
    assert candidate([3, 4, 4, 4, 6, 7, 8]) == False
    assert candidate([3]) == True
    assert candidate([3, 3, 3, 3, 5, 6]) == False
    assert candidate([3, 6, 3]) == False
    assert candidate([1, 3, 4, 4, 5, 5]) == True
    assert candidate([3, 1, 8, 4, 7, 4]) == False
    assert candidate([5, 7, 5, 7, 10, 6, 8]) == False
    assert candidate([1, 4, 5, 5, 7, 8]) == True
    assert candidate([1, 4, 6, 1, 6, 7]) == False
    assert candidate([2, 3, 6, 7, 7]) == True
    assert candidate([5]) == True
    assert candidate([]) == True
    assert candidate([3, 2, 6, 3, 6, 4]) == False
    assert candidate([2, 5, 2, 2, 2, 7]) == False
    assert candidate([2, 6, 3, 9, 1]) == False
    assert candidate([1, 1, 1, 3, 4]) == False
    assert candidate([8]) == True
    assert candidate([2, 3, 3, 5, 5, 6, 7]) == True
    assert candidate([2, 4, 5, 7]) == True
    assert candidate([3, 1, 3, 2, 1]) == False
    assert candidate([3, 3, 4, 7, 8, 9]) == True
    assert candidate([1, 5, 6, 6, 7, 7]) == True
    assert candidate([6, 7, 3, 4, 8, 6]) == False
    assert candidate([1, 8, 6, 7, 8]) == False

if __name__ == '__main__':
    check(is_sorted)