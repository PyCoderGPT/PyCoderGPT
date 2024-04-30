from case_HE_073 import smallest_change


def check(candidate):
    assert candidate([4, 5, 5, 6]) == 1
    assert candidate([4, 1, 4, 3]) == 2
    assert candidate([2, 7, 3]) == 1
    assert candidate([6, 1, 6, 10, 7, 10, 11, 5]) == 4
    assert candidate([1, 4, 2]) == 1
    assert candidate([6, 5, 7, 6, 6, 5, 7]) == 2
    assert candidate([7, 1, 5, 7]) == 1
    assert candidate([2, 1, 9, 5]) == 2
    assert candidate([5, 1, 5, 6, 1, 10, 9, 1]) == 4
    assert candidate([3]) == 0
    assert candidate([1, 1, 8, 4, 2, 6, 3]) == 3
    assert candidate([2]) == 0
    assert candidate([2, 7, 4]) == 1
    assert candidate([2, 7, 5, 8, 5, 8, 4, 4]) == 4
    assert candidate([5, 7, 3, 5, 6, 5, 5]) == 2
    assert candidate([6, 1, 3, 3, 1]) == 2
    assert candidate([5]) == 0
    assert candidate([4, 2, 3, 2, 3]) == 1
    assert candidate([1, 6, 1, 4, 5]) == 2
    assert candidate([2, 2, 1, 9, 6, 8, 11, 9]) == 4
    assert candidate([6, 8, 1, 2]) == 2
    assert candidate([4, 1, 4, 2, 2, 4, 5]) == 3
    assert candidate([4, 8, 9, 5]) == 2
    assert candidate([6, 5, 3, 7, 5, 4, 4]) == 3
    assert candidate([4, 2, 1, 4]) == 1
    assert candidate([3, 6, 7, 5, 6, 1, 7]) == 3
    assert candidate([1, 6, 2]) == 1
    assert candidate([6, 4, 4, 2]) == 1
    assert candidate([2, 1, 6]) == 1
    assert candidate([3, 6, 4]) == 1
    assert candidate([1, 2, 6, 3, 6, 8, 6, 9]) == 4
    assert candidate([5, 2, 3, 3, 1]) == 2
    assert candidate([2, 5, 8, 6, 3, 7, 5]) == 3
    assert candidate([2, 7, 6, 7]) == 2
    assert candidate([0, 1]) == 1
    assert candidate([4, 7, 4, 7]) == 2
    assert candidate([6, 4, 4, 3]) == 1
    assert candidate([1, 5, 4, 2, 6]) == 2
    assert candidate([6, 5, 3]) == 1
    assert candidate([5, 7, 7, 4]) == 1
    assert candidate([1, 4, 4, 2]) == 1

    # Check some edge cases that are easy to work out by hand.
    assert candidate([3, 5, 4, 7]) == 2
    assert candidate([1, 4, 5]) == 1
    assert candidate([1, 2, 3, 4, 3, 2, 2]) == 1
    assert candidate([2, 5, 2, 10, 4, 12, 5, 9]) == 3
    assert candidate([2, 2, 7, 3, 8, 7, 4, 8]) == 3
    assert candidate([3, 6, 5, 8, 1, 11, 11, 1]) == 4
    assert candidate([6, 6, 8, 4, 5, 5, 5]) == 3
    assert candidate([4, 4, 7]) == 1
    assert candidate([4, 4, 4]) == 0
    assert candidate([2, 3, 4, 3]) == 2
    assert candidate([6, 4, 7]) == 1
    assert candidate([2, 6, 1, 7]) == 2
    assert candidate([3, 3, 1, 7, 2, 7, 9, 10]) == 4
    assert candidate([2, 5, 3, 3, 1]) == 2
    assert candidate([3, 4, 5, 5, 2, 3, 1]) == 3
    assert candidate([1, 4, 6, 4, 8, 6, 9, 6]) == 3
    assert candidate([5, 8, 3, 7]) == 2
    assert candidate([1, 2, 3, 2, 1]) == 0
    assert candidate([5, 6, 1, 4, 2]) == 2
    assert candidate([4]) == 0
    assert candidate([4, 1, 8, 8, 5, 3, 2]) == 3
    assert candidate([5, 5, 1, 9, 5, 5, 1]) == 2
    assert candidate([5, 8, 4]) == 1
    assert candidate([1]) == 0
    assert candidate([1, 4, 5, 8]) == 2
    assert candidate([6, 7, 3, 5, 6, 10, 11, 9]) == 4
    assert candidate([4, 6, 7, 1, 1]) == 2
    assert candidate([6, 1, 2, 6]) == 1
    assert candidate([6, 2, 3, 6]) == 1
    assert candidate([7, 2, 3, 6]) == 2
    assert candidate([5, 5, 6, 1, 2]) == 2
    assert candidate([4, 8, 6]) == 1
    assert candidate([4, 1, 6, 2]) == 2
    assert candidate([3, 1, 2, 5, 6, 6, 1]) == 3
    assert candidate([4, 5, 8, 7]) == 2
    assert candidate([1, 4, 1]) == 0
    assert candidate([3, 3, 3]) == 0
    assert candidate([5, 2, 5, 5]) == 1
    assert candidate([7, 4, 1, 7]) == 1
    assert candidate([6, 4, 1, 4, 2, 2, 4]) == 3
    assert candidate([6, 7, 3, 10, 1, 7, 12, 10]) == 4
    assert candidate([6, 4, 5, 1, 5]) == 2
    assert candidate([2, 7, 2, 5, 2]) == 1
    assert candidate([2, 5, 6]) == 1
    assert candidate([6, 8, 5, 7]) == 2
    assert candidate([2, 8, 3, 6]) == 2
    assert candidate([4, 1, 3, 6, 2]) == 2
    assert candidate([5, 2, 8, 3, 8, 5, 9, 8]) == 4
    assert candidate([6, 6, 6, 3, 5]) == 2
    assert candidate([5, 4, 6, 7]) == 2
    assert candidate([3, 1, 1, 3]) == 0
    assert candidate([1, 1, 6, 2, 6]) == 2
    assert candidate([2, 6, 6, 5, 4]) == 2
    assert candidate([1, 1, 4, 7]) == 2
    assert candidate([4, 3, 1, 1, 9, 8, 9, 2]) == 4
    assert candidate([3, 4, 9, 4]) == 2
    assert candidate([6, 6, 4, 8]) == 2
    assert candidate([1, 1, 2, 6, 1, 4, 14, 3]) == 4
    assert candidate([3, 5, 7, 6, 2, 6, 7]) == 3
    assert candidate([4, 2, 8, 7, 6, 3, 1]) == 3
    assert candidate([1,2,3,5,4,7,9,6]) == 4

if __name__ == '__main__':
    check(smallest_change)