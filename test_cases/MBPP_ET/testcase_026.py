from case_MBPP_026 import is_Monotonic


def check(candidate):
    assert candidate([6, 5, 4, 4]) == True
    assert candidate([1, 2, 2, 3]) == True
    assert candidate([1, 3, 2]) == False
    assert candidate([3, 10, 7, 7]) == False
    assert candidate([9, 4, 4, 2]) == True
    assert candidate([4, 2, 8, 8]) == False
    assert candidate([11, 1, 1, 3]) == False
    assert candidate([2, 5, 4, 9]) == False
    assert candidate([5, 1, 8, 7]) == False
    assert candidate([5, 3, 7, 7]) == False
    assert candidate([6, 10, 9, 3]) == False
    assert candidate([6, 6, 1, 8]) == False
    assert candidate([6, 4, 3, 6]) == False
    assert candidate([7, 5, 4, 2]) == True
    assert candidate([7, 8, 5, 1]) == False
    assert candidate([8, 1, 7, 6]) == False
    assert candidate([8, 5, 6, 2]) == False
    assert candidate([5, 6, 6, 6]) == True
    assert candidate([11, 2, 3, 8]) == False
    assert candidate([9, 4, 7, 6]) == False
    assert candidate([3, 10, 9, 9]) == False
    assert candidate([7, 2, 2, 1]) == True
    assert candidate([11, 8, 3, 2]) == True
    assert candidate([10, 10, 5, 6]) == False
    assert candidate([6, 2, 8, 2]) == False
    assert candidate([1, 5, 5, 4]) == False
    assert candidate([10, 3, 4, 8]) == False
    assert candidate([8, 1, 6, 9]) == False
    assert candidate([10, 7, 8, 8]) == False
    assert candidate([6, 8, 7, 9]) == False
    assert candidate([7, 7, 2, 1]) == True
    assert candidate([5, 1, 5, 8]) == False
    assert candidate([3, 10, 4, 5]) == False
    assert candidate([3, 2, 2, 8]) == False
    assert candidate([1, 10, 4, 8]) == False
    assert candidate([5, 7, 3, 2]) == False
    assert candidate([6, 3, 6, 5]) == False
    assert candidate([6, 3, 4, 1]) == False
    assert candidate([6, 3, 2, 7]) == False
    assert candidate([2, 2, 6, 7]) == True
    assert candidate([1, 2, 3, 4]) == True
    assert candidate([2, 1, 1, 5]) == False
    assert candidate([3, 6, 1, 4]) == False
    assert candidate([5, 1, 5, 6]) == False
    assert candidate([2, 2, 6, 1]) == False
    assert candidate([2, 2, 6, 2]) == False
    assert candidate([3, 5, 4, 7]) == False
    assert candidate([4, 7, 1, 1]) == False
    assert candidate([4, 6, 5, 6]) == False
    assert candidate([6, 5, 3, 6]) == False
    assert candidate([6, 6, 2, 2]) == True
    assert candidate([1, 5, 1, 4]) == False
    assert candidate([4, 1, 3, 8]) == False
    assert candidate([4, 6, 7, 7]) == True
    assert candidate([3, 4, 6, 1]) == False
    assert candidate([3, 7, 7, 6]) == False
    assert candidate([4, 1, 1, 2]) == False
    assert candidate([4, 5, 1, 4]) == False
    assert candidate([3, 7, 6, 7]) == False
    assert candidate([5, 4, 3, 4]) == False
    assert candidate([6, 6, 7, 1]) == False
    assert candidate([2, 4, 7, 7]) == True
    assert candidate([6, 6, 3, 3]) == True
    assert candidate([3, 4, 5, 2]) == False
    assert candidate([6, 1, 6, 8]) == False
    assert candidate([3, 1, 2, 3]) == False
    assert candidate([3, 6, 7, 8]) == True
    assert candidate([1, 4, 3, 2]) == False
    assert candidate([5, 6, 6, 7]) == True
    assert candidate([4, 1, 2]) == False
    assert candidate([2, 2, 4]) == True
    assert candidate([1, 4, 4]) == True
    assert candidate([3, 2, 1]) == True
    assert candidate([3, 2, 3]) == False
    assert candidate([2, 1, 1]) == True
    assert candidate([3, 2, 4]) == False
    assert candidate([1, 5, 2]) == False
    assert candidate([3, 8, 6]) == False
    assert candidate([2, 8, 7]) == False
    assert candidate([6, 7, 4]) == False
    assert candidate([6, 6, 5]) == True
    assert candidate([1, 1, 5]) == True
    assert candidate([2, 5, 5]) == True
    assert candidate([3, 3, 6]) == True
    assert candidate([6, 5, 1]) == True
    assert candidate([6, 3, 4]) == False
    assert candidate([5, 2, 3]) == False
    assert candidate([5, 4, 3]) == True
    assert candidate([4, 7, 2]) == False
    assert candidate([6, 5, 4]) == True
    assert candidate([1, 4, 7]) == True
    assert candidate([3, 7, 7]) == True
    assert candidate([4, 1, 1]) == True
    assert candidate([2, 2, 3]) == True
    assert candidate([2, 2, 6]) == True
    assert candidate([5, 5, 1]) == True
    assert candidate([2, 3, 1]) == False
    assert candidate([4, 7, 5]) == False
    assert candidate([2, 1, 5]) == False
    assert candidate([5, 5, 3]) == True
    assert candidate([6, 5, 1]) == True
    assert candidate([2, 5, 3]) == False

if __name__ == '__main__':
    check(is_Monotonic)