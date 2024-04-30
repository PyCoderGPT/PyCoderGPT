from case_MBPP_256 import check_Consecutive


def check(candidate):
    assert candidate([1,2,3,4,5]) == True
    assert candidate([1,2,3,5,6]) == False
    assert candidate([1,2,1]) == False
    assert candidate([1, 7, 7, 6, 2]) == False
    assert candidate([2, 1, 7, 9, 8]) == False
    assert candidate([2, 6, 6, 1, 1]) == False
    assert candidate([4, 5, 5, 5, 7]) == False
    assert candidate([1, 3, 5, 4, 2]) == True
    assert candidate([2, 7, 6, 4, 6]) == False
    assert candidate([5, 5, 4, 5, 1]) == False
    assert candidate([1, 5, 3, 3, 6]) == False
    assert candidate([2, 4, 8, 2, 6]) == False
    assert candidate([3, 6, 4, 7, 2]) == False
    assert candidate([6, 6, 6, 1, 3]) == False
    assert candidate([3, 2, 8, 4, 6]) == False
    assert candidate([3, 2, 4, 7, 7]) == False
    assert candidate([3, 6, 8, 5, 10]) == False
    assert candidate([5, 3, 4, 6, 7]) == True
    assert candidate([2, 5, 1, 1, 5]) == False
    assert candidate([1, 7, 8, 9, 1]) == False
    assert candidate([6, 3, 3, 7, 6]) == False
    assert candidate([1, 1, 2, 4, 4]) == False
    assert candidate([3, 3, 3, 1, 10]) == False
    assert candidate([5, 6, 6, 5, 5]) == False
    assert candidate([6, 3, 4, 1, 4]) == False
    assert candidate([2, 2, 3, 2, 3]) == False
    assert candidate([3, 7, 5, 6, 6]) == False
    assert candidate([2, 3, 5, 7, 5]) == False
    assert candidate([4, 3, 5, 5, 7]) == False
    assert candidate([1, 7, 5, 6, 8]) == False
    assert candidate([1, 4, 5, 9, 9]) == False
    assert candidate([3, 2, 4, 5, 8]) == False
    assert candidate([4, 3, 2, 2, 10]) == False
    assert candidate([4, 1, 4, 3, 8]) == False
    assert candidate([4, 2, 8, 1, 3]) == False
    assert candidate([2, 1, 4, 8, 4]) == False
    assert candidate([2, 3, 1, 1, 6]) == False
    assert candidate([3, 4, 6, 6, 7]) == False
    assert candidate([6, 7, 2, 5, 2]) == False
    assert candidate([3, 1, 1, 4, 11]) == False
    assert candidate([1, 2, 2, 8, 10]) == False
    assert candidate([1, 4, 3, 5, 2]) == True
    assert candidate([5, 7, 3, 9, 9]) == False
    assert candidate([2, 2, 5, 2, 7]) == False
    assert candidate([5, 2, 1, 4, 8]) == False
    assert candidate([6, 2, 7, 7, 11]) == False
    assert candidate([1, 6, 5, 8, 2]) == False
    assert candidate([5, 7, 1, 4, 5]) == False
    assert candidate([4, 1, 2, 6, 3]) == False
    assert candidate([4, 2, 6, 9, 7]) == False
    assert candidate([1, 3, 2, 4, 3]) == False
    assert candidate([2, 4, 7, 3, 9]) == False
    assert candidate([1, 2, 3, 1, 9]) == False
    assert candidate([1, 3, 2, 4, 10]) == False
    assert candidate([1, 4, 8, 1, 1]) == False
    assert candidate([2, 1, 5, 7, 7]) == False
    assert candidate([1, 7, 5, 9, 3]) == False
    assert candidate([6, 4, 5, 7, 1]) == False
    assert candidate([4, 6, 1, 3, 9]) == False
    assert candidate([5, 3, 5, 4, 10]) == False
    assert candidate([3, 7, 8, 4, 6]) == False
    assert candidate([1, 5, 1, 9, 6]) == False
    assert candidate([3, 4, 2, 9, 5]) == False
    assert candidate([4, 6, 1, 5, 5]) == False
    assert candidate([6, 1, 7, 9, 5]) == False
    assert candidate([5, 6, 3, 9, 5]) == False
    assert candidate([3, 4, 4, 3, 7]) == False
    assert candidate([4, 4, 6, 10, 7]) == False
    assert candidate([4, 2, 7, 9, 2]) == False
    assert candidate([3, 3, 1]) == False
    assert candidate([6, 5, 1]) == False
    assert candidate([1, 7, 5]) == False
    assert candidate([1, 4, 6]) == False
    assert candidate([4, 6, 5]) == True
    assert candidate([6, 1, 4]) == False
    assert candidate([4, 6, 1]) == False
    assert candidate([4, 5, 1]) == False
    assert candidate([6, 2, 2]) == False
    assert candidate([4, 4, 5]) == False
    assert candidate([2, 4, 4]) == False
    assert candidate([5, 7, 6]) == True
    assert candidate([5, 4, 2]) == False
    assert candidate([6, 2, 4]) == False
    assert candidate([5, 2, 1]) == False
    assert candidate([5, 3, 2]) == False
    assert candidate([4, 4, 6]) == False
    assert candidate([3, 3, 6]) == False
    assert candidate([1, 7, 3]) == False
    assert candidate([6, 3, 3]) == False
    assert candidate([5, 5, 6]) == False
    assert candidate([3, 1, 1]) == False
    assert candidate([4, 4, 4]) == False
    assert candidate([2, 4, 4]) == False
    assert candidate([3, 5, 1]) == False
    assert candidate([3, 7, 6]) == False
    assert candidate([2, 6, 5]) == False
    assert candidate([6, 2, 6]) == False
    assert candidate([1, 4, 4]) == False
    assert candidate([6, 7, 6]) == False
    assert candidate([5, 7, 1]) == False
    assert candidate([5, 7, 3]) == False
    assert candidate([2, 1, 4]) == False

if __name__ == '__main__':
    check(check_Consecutive)