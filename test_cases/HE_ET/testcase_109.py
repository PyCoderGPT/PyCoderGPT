from case_HE_109 import move_one_ball


def check(candidate):
    assert candidate([4, 9, 5, 1, 2]) == False
    assert candidate([4, 8, 7, 3, 4]) == False
    assert candidate([6, 2, 7, 2, 1]) == False
    assert candidate([5, 3, 4, 5, 4]) == False
    assert candidate([5, 5, 2, 7]) == False
    assert candidate([2, 3, 7, 3, 4]) == False
    assert candidate([3, 5, 1, 3]) == True
    assert candidate([5, 6, 6, 7]) == True
    assert candidate([7, 1, 8, 2, 6]) == False
    assert candidate([1, 3, 3, 6, 2]) == False
    assert candidate([9, 5, 5, 6]) == True
    assert candidate([3, 10, 2, 5, 1]) == False
    assert candidate([4, 4, 2, 3]) == True
    assert candidate([1, 4, 6, 2]) == False
    assert candidate([1, 4, 2, 7]) == False
    assert candidate([2, 8, 6, 6, 1]) == False
    assert candidate([2, 5, 5, 2, 5]) == False
    assert candidate([7, 4, 3, 1]) == False
    assert candidate([6, 2, 3, 1, 1]) == False
    assert candidate([8, 8, 6, 3, 6]) == False
    assert candidate([1, 7, 9, 5, 3]) == False
    assert candidate([9, 3, 5, 4]) == False
    assert candidate([1, 8, 6, 6]) == False
    assert candidate([4, 1, 9, 1, 7]) == False
    assert candidate([5, 7, 3, 6, 6]) == False
    assert candidate([1, 5, 15, 5, 4]) == False
    assert candidate([4, 2, 6, 5]) == False
    assert candidate([2, 4, 5, 5, 3]) == False
    assert candidate([6, 6, 4, 1]) == False
    assert candidate([7, 2, 1, 3, 2]) == False
    assert candidate([1, 3, 4, 2, 4]) == False
    assert candidate([4, 2, 3, 1]) == False
    assert candidate([2, 3, 10, 4, 6]) == False
    assert candidate([8, 1, 3, 4, 7]) == True
    assert candidate([5, 4, 12, 2, 2]) == False
    assert candidate([7, 5, 8, 6, 3]) == False
    assert candidate([6, 6, 4, 6]) == True
    assert candidate([2, 2, 3, 2, 5]) == False
    assert candidate([7, 4, 4, 3]) == False
    assert candidate([9, 1, 4, 2]) == False
    assert candidate([4, 6, 9, 3, 1]) == False
    assert candidate([3, 1, 5, 1]) == False
    assert candidate([6, 8, 8, 3, 7]) == False
    assert candidate([1, 9, 8, 5, 2]) == False
    assert candidate([7, 1, 5, 2, 4]) == False
    assert candidate([5, 3, 4, 4]) == True
    assert candidate([7, 7, 4, 6, 3]) == False
    assert candidate([5, 2, 7, 5, 2]) == False
    assert candidate([2, 5, 6, 1, 7]) == False
    assert candidate([3, 2, 5, 5, 4]) == False
    assert candidate([1, 8, 10, 4, 6]) == False
    assert candidate([5, 7, 8, 4, 1]) == False
    assert candidate([3, 9, 14, 3, 6]) == False
    assert candidate([3, 5, 4, 1, 2])==False
    assert candidate([5, 4, 13, 3, 7]) == False
    assert candidate([4, 8, 5, 5, 1]) == False
    assert candidate([1, 9, 3, 2, 7]) == False
    assert candidate([1, 6, 1, 7]) == False
    assert candidate([8, 1, 5, 5, 7]) == True
    assert candidate([1, 6, 2, 2, 7]) == False
    assert candidate([4, 7, 6, 5]) == False
    assert candidate([5, 1, 2, 5, 7]) == False
    assert candidate([7, 8, 2, 4, 2]) == False
    assert candidate([2, 4, 1, 3, 6]) == False
    assert candidate([3, 7, 3, 2, 3]) == False
    assert candidate([2, 5, 2, 2, 1]) == False
    assert candidate([8, 1, 6, 5]) == False
    assert candidate([7, 4, 7, 5, 5]) == False
    assert candidate([1, 1, 9, 1, 3]) == False
    assert candidate([7, 9, 7, 1, 3]) == False
    assert candidate([8, 7, 5, 3, 7]) == False
    assert candidate([9, 3, 6, 3]) == False
    assert candidate([8, 3, 1, 6, 4]) == False
    assert candidate([3, 5, 10, 1, 2])==True
    assert candidate([2, 10, 3, 6, 2]) == False
    assert candidate([1, 8, 15, 2, 2]) == False
    assert candidate([6, 4, 6, 3, 3]) == False
    assert candidate([6, 5, 6, 6, 3]) == False
    assert candidate([9, 3, 5, 6]) == True
    assert candidate([1, 10, 11, 2, 6]) == False
    assert candidate([1, 3, 14, 2, 2]) == False
    assert candidate([1, 9, 10, 1, 6]) == False
    assert candidate([7, 9, 8, 3, 5]) == False
    assert candidate([7, 2, 10, 5, 4]) == False
    assert candidate([6, 2, 4, 1, 2]) == False
    assert candidate([6, 4, 8, 5, 4]) == False
    assert candidate([1, 1, 11, 3, 2]) == False
    assert candidate([5, 8, 2, 3, 5]) == True
    assert candidate([8, 1, 9, 5, 3]) == False
    assert candidate([6, 3, 4, 6, 5]) == False
    assert candidate([5, 2, 2, 2, 3]) == True
    assert candidate([6, 9, 10, 1, 4]) == True
    assert candidate([4, 8, 4, 7]) == False
    assert candidate([4, 3, 1, 2])==False
    # Check some edge cases that are easy to work out by hand.
    assert candidate([3, 4, 5, 5]) == True
    assert candidate([])==True
    assert candidate([8, 3, 9, 3, 7]) == False
    assert candidate([7, 9, 5, 5, 5]) == True
    assert candidate([]) == True
    assert candidate([1, 4, 8, 4, 5]) == False
    assert candidate([6, 4, 11, 5, 6]) == False
    assert candidate([2, 8, 9, 5, 6]) == False
    assert candidate([7, 10, 11, 3, 3]) == True
    assert candidate([1, 10, 1, 6, 1]) == False
    assert candidate([8, 8, 1, 1, 1]) == True
    assert candidate([3, 4, 5, 1, 2])==True

if __name__ == '__main__':
    check(move_one_ball)