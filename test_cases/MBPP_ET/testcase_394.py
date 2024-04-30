from case_MBPP_394 import odd_position


def check(candidate):
    assert candidate([2,1,4,3,6,7,6,3]) == True
    assert candidate([4,1,2]) == True
    assert candidate([1,2,3]) == False
    assert candidate([5, 6, 1, 2, 11, 6, 8, 7]) == False
    assert candidate([5, 6, 8, 7, 8, 3, 6, 2]) == False
    assert candidate([7, 2, 8, 6, 5, 6, 4, 3]) == False
    assert candidate([6, 2, 2, 2, 2, 8, 10, 7]) == False
    assert candidate([2, 6, 7, 4, 2, 4, 8, 5]) == False
    assert candidate([5, 5, 9, 4, 7, 6, 10, 3]) == False
    assert candidate([7, 5, 5, 7, 4, 2, 10, 1]) == False
    assert candidate([3, 1, 7, 8, 11, 9, 9, 4]) == False
    assert candidate([6, 3, 8, 6, 4, 5, 5, 1]) == False
    assert candidate([3, 1, 6, 4, 2, 2, 3, 1]) == False
    assert candidate([5, 3, 4, 4, 9, 12, 9, 5]) == False
    assert candidate([4, 1, 6, 2, 4, 8, 10, 1]) == False
    assert candidate([5, 1, 1, 5, 7, 3, 9, 6]) == False
    assert candidate([1, 1, 8, 6, 11, 5, 5, 5]) == False
    assert candidate([2, 1, 9, 6, 10, 10, 5, 1]) == False
    assert candidate([2, 4, 4, 4, 8, 12, 7, 7]) == False
    assert candidate([3, 5, 8, 2, 5, 9, 11, 1]) == False
    assert candidate([6, 4, 3, 5, 2, 2, 9, 3]) == False
    assert candidate([2, 4, 6, 2, 10, 7, 4, 2]) == False
    assert candidate([3, 2, 2, 6, 6, 9, 3, 7]) == False
    assert candidate([4, 2, 3, 6, 11, 6, 2, 2]) == False
    assert candidate([4, 3, 6, 4, 1, 10, 3, 7]) == False
    assert candidate([1, 2, 1, 7, 4, 6, 6, 6]) == False
    assert candidate([6, 4, 9, 1, 6, 10, 6, 3]) == False
    assert candidate([2, 5, 8, 2, 1, 10, 10, 3]) == False
    assert candidate([6, 1, 6, 1, 6, 11, 8, 2]) == False
    assert candidate([7, 6, 2, 5, 3, 10, 4, 1]) == False
    assert candidate([5, 2, 7, 5, 6, 8, 10, 8]) == False
    assert candidate([3, 5, 2, 6, 2, 9, 1, 7]) == False
    assert candidate([4, 5, 1, 7, 7, 6, 2, 4]) == False
    assert candidate([3, 1, 8, 1, 8, 2, 6, 4]) == False
    assert candidate([4, 2, 2, 2, 2, 9, 3, 4]) == False
    assert candidate([3, 1, 4, 1, 10, 6, 8, 1]) == False
    assert candidate([4, 1, 5]) == False
    assert candidate([6, 2, 3]) == False
    assert candidate([1, 1, 2]) == False
    assert candidate([2, 6, 7]) == False
    assert candidate([1, 2, 4]) == False
    assert candidate([6, 3, 7]) == False
    assert candidate([6, 1, 2]) == True
    assert candidate([7, 6, 4]) == False
    assert candidate([4, 5, 4]) == True
    assert candidate([7, 2, 4]) == False
    assert candidate([5, 2, 3]) == False
    assert candidate([6, 5, 6]) == True
    assert candidate([8, 5, 3]) == False
    assert candidate([6, 6, 7]) == False
    assert candidate([1, 2, 5]) == False
    assert candidate([6, 6, 3]) == False
    assert candidate([7, 2, 1]) == False
    assert candidate([4, 6, 6]) == False
    assert candidate([3, 6, 4]) == False
    assert candidate([3, 3, 2]) == False
    assert candidate([5, 1, 3]) == False
    assert candidate([9, 6, 1]) == False
    assert candidate([7, 4, 2]) == False
    assert candidate([5, 1, 6]) == False
    assert candidate([7, 2, 3]) == False
    assert candidate([1, 2, 3]) == False
    assert candidate([7, 1, 1]) == False
    assert candidate([1, 4, 2]) == False
    assert candidate([8, 3, 5]) == False
    assert candidate([8, 4, 7]) == False
    assert candidate([6, 1, 2]) == True
    assert candidate([9, 3, 1]) == False
    assert candidate([8, 1, 4]) == True
    assert candidate([3, 4, 3]) == False
    assert candidate([2, 2, 1]) == False
    assert candidate([6, 2, 4]) == False
    assert candidate([4, 5, 3]) == False
    assert candidate([4, 4, 8]) == False
    assert candidate([5, 1, 5]) == False
    assert candidate([5, 1, 6]) == False
    assert candidate([1, 1, 1]) == False
    assert candidate([4, 2, 3]) == False
    assert candidate([4, 4, 8]) == False
    assert candidate([1, 5, 5]) == False
    assert candidate([1, 5, 7]) == False
    assert candidate([4, 3, 1]) == False
    assert candidate([1, 2, 3]) == False
    assert candidate([6, 7, 3]) == False
    assert candidate([1, 1, 2]) == False
    assert candidate([3, 5, 3]) == False
    assert candidate([3, 2, 5]) == False
    assert candidate([6, 4, 5]) == False
    assert candidate([3, 4, 6]) == False
    assert candidate([4, 6, 8]) == False
    assert candidate([3, 2, 8]) == False
    assert candidate([5, 4, 3]) == False
    assert candidate([1, 5, 1]) == False
    assert candidate([6, 5, 1]) == False
    assert candidate([6, 7, 1]) == False
    assert candidate([1, 4, 4]) == False
    assert candidate([1, 5, 7]) == False
    assert candidate([1, 1, 7]) == False
    assert candidate([5, 1, 5]) == False
    assert candidate([3, 6, 2]) == False
    assert candidate([3, 7, 5]) == False
    assert candidate([3, 7, 8]) == False

if __name__ == '__main__':
    check(odd_position)