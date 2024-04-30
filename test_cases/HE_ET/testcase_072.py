from case_HE_072 import will_it_fly


def check(candidate):
    assert candidate([7, 7, 2], 7) == False
    assert candidate([6, 3, 1], 8) == False
    assert candidate([6, 2], 10) == False
    assert candidate([2, 6, 5], 6) == False
    assert candidate([6], 1) == False
    assert candidate([4, 7, 1], 2) == False
    assert candidate([5], 5) is True
    assert candidate([5, 1, 4], 7) == False
    assert candidate([1], 5) == True
    assert candidate([1, 4], 4) == False
    assert candidate([2, 7], 1) == False
    assert candidate([3], 1) == False
    assert candidate([7], 9) == True
    assert candidate([3], 6) == True
    assert candidate([1, 6, 8], 4) == False
    assert candidate([1, 5], 4) == False
    assert candidate([1, 1, 8], 7) == False
    assert candidate([5, 7, 6], 1) == False
    assert candidate([3, 5, 3], 1) == False
    assert candidate([2, 6, 4], 8) == False
    assert candidate([4], 2) == False
    assert candidate([2, 4, 7], 14) == False
    assert candidate([5, 5, 2], 8) == False
    assert candidate([5, 4, 5], 5) == False
    assert candidate([3, 2], 3) == False
    assert candidate([4, 1, 1], 14) == False
    assert candidate([6, 1], 5) == False
    assert candidate([8, 6, 4], 12) == False
    assert candidate([3, 5], 1) == False
    assert candidate([5, 5, 7], 10) == False
    assert candidate([3, 3, 3], 5) == False
    assert candidate([3, 6, 3], 5) == False
    assert candidate([4, 3, 3], 2) == False
    assert candidate([5, 4], 4) == False
    assert candidate([2, 1, 4], 3) == False
    assert candidate([3, 2, 3], 9) is True
    assert candidate([2, 5, 6], 5) == False
    assert candidate([2, 1, 3], 2) == False
    assert candidate([5, 6], 9) == False
    assert candidate([7], 2) == False
    assert candidate([4, 5, 8], 9) == False
    assert candidate([8, 6, 6], 6) == False
    assert candidate([3, 2, 3], 1) is False


    # Check some edge cases that are easy to work out by hand.
    assert candidate([4, 5, 7], 8) == False
    assert candidate([1, 2], 5) is False
    assert candidate([1, 2, 3], 6) is False
    assert candidate([6], 10) == True
    assert candidate([3, 3, 6], 8) == False
    assert candidate([3, 3, 7], 4) == False
    assert candidate([3], 5) is True
    assert candidate([2, 7], 9) == False
    assert candidate([2, 4, 8], 3) == False
    assert candidate([1], 8) == True
    assert candidate([7], 7) == True
    assert candidate([4], 1) == False
    assert candidate([2], 3) == True
    assert candidate([3, 1, 1], 2) == False
    assert candidate([4, 4, 2], 4) == False
    assert candidate([3, 2, 6], 4) == False
    assert candidate([3, 2, 8], 4) == False
    assert candidate([1, 2, 7], 2) == False
    assert candidate([1, 2, 7], 3) == False
    assert candidate([5, 5], 1) == False
    assert candidate([3, 3], 9) == True
    assert candidate([1], 10) == True
    assert candidate([3, 7, 2], 6) == False
    assert candidate([5], 7) == True
    assert candidate([4, 3, 6], 3) == False
    assert candidate([2, 2, 2], 5) == False
    assert candidate([5, 4, 2], 11) == False
    assert candidate([7, 2, 5], 8) == False
    assert candidate([1, 2, 1], 8) == True
    assert candidate([7, 5, 6], 14) == False
    assert candidate([3, 3], 3) == False
    assert candidate([3, 3, 4], 2) == False
    assert candidate([7, 5, 5], 3) == False
    assert candidate([7, 6, 7], 6) == False
    assert candidate([7, 4, 8], 7) == False
    assert candidate([2, 4], 6) == False
    assert candidate([2, 5], 6) == False
    assert candidate([1, 1, 2], 1) == False
    assert candidate([3, 1, 2], 1) == False
    assert candidate([6, 3, 5], 2) == False
    assert candidate([5, 7, 1], 9) == False
    assert candidate([5, 4, 3], 3) == False
    assert candidate([3, 7, 7], 6) == False
    assert candidate([3, 5, 3], 2) == False
    assert candidate([3, 3, 4], 7) == False
    assert candidate([2, 5], 4) == False
    assert candidate([7], 3) == False
    assert candidate([2, 2, 5], 12) == False
    assert candidate([3], 3) == True
    assert candidate([2, 7, 7], 7) == False
    assert candidate([2, 4, 4], 9) == False
    assert candidate([5, 4, 5], 3) == False
    assert candidate([1, 3, 6], 6) == False
    assert candidate([8], 1) == False
    assert candidate([1, 3, 3], 8) == False
    assert candidate([5, 5], 10) == True
    assert candidate([2, 1, 7], 2) == False
    assert candidate([1, 1], 7) == True
    assert candidate([6, 7], 6) == False
    assert candidate([5, 3], 10) == False

if __name__ == '__main__':
    check(will_it_fly)