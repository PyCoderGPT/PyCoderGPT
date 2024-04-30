from case_MBPP_153 import all_unique


def check(candidate):
    assert candidate([1,2,3]) == True
    assert candidate([1,2,1,2]) == False
    assert candidate([1,2,3,4,5]) == True
    assert candidate([4, 5, 2]) == True
    assert candidate([4, 7, 5]) == True
    assert candidate([6, 4, 1]) == True
    assert candidate([4, 3, 6]) == True
    assert candidate([2, 3, 1]) == True
    assert candidate([5, 5, 3]) == False
    assert candidate([3, 3, 1]) == False
    assert candidate([6, 4, 1]) == True
    assert candidate([1, 2, 7]) == True
    assert candidate([5, 1, 2]) == True
    assert candidate([2, 6, 8]) == True
    assert candidate([4, 3, 6]) == True
    assert candidate([2, 3, 6]) == True
    assert candidate([6, 4, 3]) == True
    assert candidate([3, 3, 5]) == False
    assert candidate([2, 7, 4]) == True
    assert candidate([2, 6, 7]) == True
    assert candidate([3, 3, 4]) == False
    assert candidate([4, 3, 2]) == True
    assert candidate([2, 6, 6]) == False
    assert candidate([5, 1, 6]) == True
    assert candidate([3, 3, 2]) == False
    assert candidate([1, 3, 8]) == True
    assert candidate([2, 5, 5]) == False
    assert candidate([4, 7, 3]) == True
    assert candidate([1, 7, 5]) == True
    assert candidate([3, 5, 1]) == True
    assert candidate([6, 1, 1]) == False
    assert candidate([4, 1, 5]) == True
    assert candidate([5, 4, 7]) == True
    assert candidate([6, 2, 4]) == True
    assert candidate([2, 6, 7]) == True
    assert candidate([1, 6, 5]) == True
    assert candidate([1, 7, 4, 1]) == False
    assert candidate([6, 3, 1, 4]) == True
    assert candidate([5, 2, 6, 3]) == True
    assert candidate([4, 4, 4, 4]) == False
    assert candidate([6, 1, 6, 2]) == False
    assert candidate([6, 6, 3, 2]) == False
    assert candidate([6, 6, 3, 6]) == False
    assert candidate([1, 7, 2, 6]) == True
    assert candidate([2, 4, 4, 5]) == False
    assert candidate([4, 6, 1, 1]) == False
    assert candidate([4, 6, 5, 2]) == True
    assert candidate([1, 3, 4, 6]) == True
    assert candidate([6, 7, 1, 3]) == True
    assert candidate([4, 7, 6, 5]) == True
    assert candidate([1, 5, 3, 5]) == False
    assert candidate([6, 6, 4, 1]) == False
    assert candidate([3, 2, 3, 4]) == False
    assert candidate([1, 5, 6, 1]) == False
    assert candidate([3, 4, 3, 2]) == False
    assert candidate([2, 3, 4, 2]) == False
    assert candidate([6, 7, 3, 1]) == True
    assert candidate([3, 3, 4, 4]) == False
    assert candidate([1, 5, 5, 3]) == False
    assert candidate([3, 1, 3, 4]) == False
    assert candidate([4, 3, 2, 4]) == False
    assert candidate([3, 5, 3, 4]) == False
    assert candidate([6, 7, 1, 4]) == True
    assert candidate([1, 6, 5, 7]) == True
    assert candidate([5, 4, 3, 4]) == False
    assert candidate([2, 7, 2, 6]) == False
    assert candidate([6, 7, 4, 3]) == True
    assert candidate([6, 5, 3, 7]) == True
    assert candidate([2, 1, 5, 3]) == True
    assert candidate([6, 6, 3, 3, 2]) == False
    assert candidate([2, 4, 8, 3, 8]) == False
    assert candidate([6, 7, 5, 4, 10]) == True
    assert candidate([3, 7, 4, 2, 10]) == True
    assert candidate([6, 1, 8, 4, 9]) == True
    assert candidate([3, 7, 3, 4, 9]) == False
    assert candidate([6, 5, 5, 7, 8]) == False
    assert candidate([4, 1, 2, 7, 2]) == False
    assert candidate([2, 1, 1, 7, 4]) == False
    assert candidate([3, 4, 3, 9, 5]) == False
    assert candidate([5, 6, 7, 5, 10]) == False
    assert candidate([3, 4, 7, 2, 5]) == True
    assert candidate([6, 2, 1, 9, 2]) == False
    assert candidate([5, 5, 7, 7, 8]) == False
    assert candidate([6, 3, 6, 9, 7]) == False
    assert candidate([6, 6, 8, 1, 9]) == False
    assert candidate([3, 5, 6, 3, 2]) == False
    assert candidate([2, 2, 4, 1, 2]) == False
    assert candidate([3, 5, 5, 1, 2]) == False
    assert candidate([1, 5, 3, 1, 5]) == False
    assert candidate([5, 2, 4, 8, 2]) == False
    assert candidate([2, 7, 3, 8, 4]) == True
    assert candidate([6, 2, 4, 4, 3]) == False
    assert candidate([3, 2, 8, 3, 1]) == False
    assert candidate([4, 3, 8, 9, 6]) == True
    assert candidate([3, 7, 3, 3, 2]) == False
    assert candidate([3, 5, 7, 9, 9]) == False
    assert candidate([1, 7, 1, 3, 3]) == False
    assert candidate([3, 2, 2, 2, 3]) == False
    assert candidate([1, 7, 1, 3, 7]) == False
    assert candidate([1, 7, 5, 4, 2]) == True
    assert candidate([6, 2, 3, 7, 2]) == False
    assert candidate([1, 2, 4, 2, 6]) == False

if __name__ == '__main__':
    check(all_unique)