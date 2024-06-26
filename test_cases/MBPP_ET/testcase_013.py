from case_MBPP_013 import test_duplicate


def check(candidate):
    assert candidate(([1,2,3,4,5]))==False
    assert candidate(([1,2,3,4, 4]))==True
    assert candidate([1,1,2,2,3,3,4,4,5])==True
    assert candidate([3, 1, 6, 8, 5]) == False
    assert candidate([1, 4, 3, 4, 2]) == True
    assert candidate([1, 5, 4, 6, 8]) == False
    assert candidate([1, 2, 5, 2, 1]) == True
    assert candidate([4, 3, 2, 7, 6]) == False
    assert candidate([6, 3, 1, 2, 8]) == False
    assert candidate([4, 4, 7, 2, 5]) == True
    assert candidate([6, 3, 8, 5, 2]) == False
    assert candidate([1, 4, 2, 2, 3]) == True
    assert candidate([2, 1, 6, 6, 5]) == True
    assert candidate([1, 2, 8, 1, 3]) == True
    assert candidate([3, 3, 8, 6, 5]) == True
    assert candidate([5, 6, 5, 1, 8]) == True
    assert candidate([4, 7, 6, 5, 5]) == True
    assert candidate([6, 7, 5, 3, 9]) == False
    assert candidate([2, 1, 7, 6, 8]) == False
    assert candidate([3, 7, 7, 2, 9]) == True
    assert candidate([4, 6, 8, 4, 4]) == True
    assert candidate([6, 3, 8, 1, 2]) == False
    assert candidate([4, 4, 8, 6, 9]) == True
    assert candidate([2, 6, 5, 7, 4]) == False
    assert candidate([6, 7, 3, 2, 3]) == True
    assert candidate([4, 5, 6, 1, 5]) == True
    assert candidate([4, 7, 3, 4, 3]) == True
    assert candidate([6, 7, 1, 4, 3]) == False
    assert candidate([5, 6, 2, 1, 2]) == True
    assert candidate([4, 7, 2, 3, 7]) == True
    assert candidate([2, 6, 5, 6, 8]) == True
    assert candidate([3, 7, 3, 5, 4]) == True
    assert candidate([1, 5, 4, 6, 9]) == False
    assert candidate([3, 1, 8, 3, 6]) == True
    assert candidate([4, 3, 2, 1, 9]) == False
    assert candidate([2, 5, 8, 2, 9]) == True
    assert candidate([6, 3, 5, 8, 5]) == True
    assert candidate([1, 2, 4, 1, 3]) == True
    assert candidate([2, 3, 8, 4, 4]) == True
    assert candidate([3, 5, 7, 5, 3]) == True
    assert candidate([2, 4, 7, 4, 4]) == True
    assert candidate([6, 6, 4, 6, 8]) == True
    assert candidate([4, 4, 7, 1, 6]) == True
    assert candidate([4, 6, 5, 9, 2]) == False
    assert candidate([1, 1, 5, 3, 7]) == True
    assert candidate([2, 1, 5, 9, 9]) == True
    assert candidate([6, 6, 4, 3, 2]) == True
    assert candidate([1, 7, 8, 1, 8]) == True
    assert candidate([4, 4, 4, 2, 3]) == True
    assert candidate([6, 5, 3, 7, 6]) == True
    assert candidate([4, 4, 6, 6, 1]) == True
    assert candidate([3, 7, 3, 7, 1]) == True
    assert candidate([3, 5, 7, 4, 9]) == False
    assert candidate([1, 6, 6, 2, 6]) == True
    assert candidate([3, 6, 3, 9, 9]) == True
    assert candidate([4, 6, 7, 3, 5]) == False
    assert candidate([4, 5, 3, 7, 9]) == False
    assert candidate([5, 4, 8, 2, 6]) == False
    assert candidate([3, 6, 2, 2, 1]) == True
    assert candidate([5, 1, 8, 4, 8]) == True
    assert candidate([1, 3, 7, 7, 7]) == True
    assert candidate([2, 1, 7, 7, 5]) == True
    assert candidate([3, 1, 4, 9, 8]) == False
    assert candidate([4, 6, 1, 9, 2]) == False
    assert candidate([2, 6, 3, 8, 6]) == True
    assert candidate([1, 7, 4, 5, 3]) == False
    assert candidate([4, 5, 6, 6, 5]) == True
    assert candidate([3, 4, 4, 4, 7]) == True
    assert candidate([3, 4, 1, 8, 6]) == False
    assert candidate([4, 2, 2, 5, 4, 4, 4, 9, 5]) == True
    assert candidate([2, 5, 1, 4, 4, 5, 2, 2, 7]) == True
    assert candidate([1, 6, 7, 1, 7, 3, 4, 1, 4]) == True
    assert candidate([1, 6, 1, 2, 8, 1, 9, 6, 1]) == True
    assert candidate([6, 1, 5, 7, 3, 6, 6, 8, 9]) == True
    assert candidate([5, 1, 7, 3, 6, 1, 9, 6, 7]) == True
    assert candidate([2, 3, 6, 6, 4, 5, 1, 7, 6]) == True
    assert candidate([1, 1, 2, 4, 7, 6, 5, 3, 2]) == True
    assert candidate([6, 1, 3, 2, 4, 7, 1, 9, 1]) == True
    assert candidate([2, 3, 3, 4, 1, 1, 5, 7, 5]) == True
    assert candidate([5, 3, 4, 2, 4, 1, 1, 4, 8]) == True
    assert candidate([3, 1, 5, 1, 8, 8, 6, 3, 3]) == True
    assert candidate([3, 1, 1, 5, 5, 8, 5, 9, 8]) == True
    assert candidate([5, 5, 2, 7, 3, 8, 9, 3, 1]) == True
    assert candidate([6, 5, 5, 7, 4, 5, 8, 6, 1]) == True
    assert candidate([3, 2, 6, 1, 4, 5, 7, 8, 5]) == True
    assert candidate([4, 1, 3, 5, 8, 4, 2, 4, 1]) == True
    assert candidate([6, 2, 4, 6, 1, 5, 4, 7, 5]) == True
    assert candidate([3, 5, 3, 5, 3, 6, 6, 2, 1]) == True
    assert candidate([6, 2, 4, 1, 3, 8, 6, 9, 6]) == True
    assert candidate([4, 3, 4, 1, 7, 5, 2, 5, 10]) == True
    assert candidate([3, 5, 5, 1, 6, 6, 3, 6, 1]) == True
    assert candidate([3, 5, 4, 7, 2, 6, 3, 7, 9]) == True
    assert candidate([2, 6, 7, 6, 3, 5, 9, 7, 10]) == True
    assert candidate([1, 2, 3, 4, 4, 7, 2, 7, 8]) == True
    assert candidate([1, 6, 2, 1, 5, 3, 5, 9, 2]) == True
    assert candidate([3, 3, 5, 6, 8, 8, 2, 7, 1]) == True
    assert candidate([5, 6, 2, 6, 7, 4, 2, 9, 5]) == True
    assert candidate([3, 4, 1, 2, 1, 3, 4, 2, 7]) == True
    assert candidate([3, 6, 4, 2, 8, 4, 7, 3, 5]) == True
    assert candidate([6, 6, 2, 3, 6, 8, 5, 6, 2]) == True
    assert candidate([2, 5, 5, 7, 2, 4, 9, 8, 8]) == True
    assert candidate([6, 5, 5, 1, 7, 6, 1, 7, 7]) == True

if __name__ == '__main__':
    check(test_duplicate)