from case_HE_090 import next_smallest


def check(candidate):
    assert candidate([4, 1, 8, 2, 6]) == 2
    assert candidate([1, 6, 3, 1, 7]) == 3
    assert candidate([5, 1]) == 5
    assert candidate([5, 6, 5, 3, 3]) == 5
    assert candidate([3, 4, 8, 8, 5]) == 4
    assert candidate([5, 3]) == 5
    assert candidate([4, 5, 7, 7, 4]) == 5
    assert candidate([4, 2]) == 4
    assert candidate([4, 6, 1, 4, 5]) == 4
    assert candidate([2, 3, 1, 5, 5]) == 2
    assert candidate([10, 6, 8, 7, 3]) == 6
    assert candidate([6, 6]) == None
    assert candidate([3, 3]) == None
    assert candidate([6, 4, 1, 1, 5]) == 4
    assert candidate([5, 5]) == None
    assert candidate([1, 4, 1, 2, 1]) == 2
    assert candidate([5, 3, 2, 1, 1]) == 2
    assert candidate([6, 7, 8, 2, 7]) == 6
    assert candidate([7, 2, 9, 7, 7]) == 7
    assert candidate([4, 3, 8, 6, 9]) == 4
    assert candidate([2, 5, 5, 6, 2]) == 5
    assert candidate([5, 5, 4, 3, 2]) == 3
    assert candidate([1, 2, 1, 5, 3]) == 2
    assert candidate([1, 4, 6, 9, 4]) == 4
    assert candidate([1, 5]) == 5
    assert candidate([6, 4]) == 6
    assert candidate([1, 2, 3, 4, 5]) == 2
    assert candidate([1, 4]) == 4
    assert candidate([1, 1]) == None
    assert candidate([2, 1, 7, 7, 3]) == 2
    assert candidate([4, 2, 3, 2, 3]) == 3
    assert candidate([6, 3]) == 6
    assert candidate([5, 6, 6, 6, 5]) == 6
    assert candidate([1, 2, 1, 2, 3]) == 2
    assert candidate([3, 5, 3, 5, 6]) == 5
    assert candidate([4, 6]) == 6
    assert candidate([4, 4, 6, 5, 5]) == 5
    assert candidate([3, 3, 5, 1, 10]) == 3
    assert candidate([6, 2, 5, 3, 4]) == 3
    assert candidate([8, 3, 1, 5, 4]) == 3
    assert candidate([1, 3, 3, 9, 7]) == 3
    assert candidate([4, 6, 2, 4, 4]) == 4
    assert candidate([9, 6, 4, 1, 1]) == 4
    assert candidate([2, 4]) == 4
    assert candidate([5, 5, 3, 6, 5]) == 5
    assert candidate([2, 1, 6, 6, 3]) == 2
    assert candidate([6, 3, 4, 3, 2]) == 3
    assert candidate([1, 6]) == 6
    assert candidate([3, 5, 4, 9, 5]) == 4
    assert candidate([1,1,1,1,0]) == 1
    assert candidate([1, 2, 2, 4, 4]) == 2
    assert candidate([1, 5, 3, 6, 4]) == 3
    assert candidate([2, 6, 3, 2, 7]) == 3
    assert candidate([10, 6, 8, 2, 5]) == 5
    assert candidate([2, 2]) == None
    assert candidate([5, 4]) == 5
    assert candidate([5, 6, 6, 9, 10]) == 6
    assert candidate([4, 1]) == 4
    assert candidate([2, 3, 4, 6, 2]) == 3
    assert candidate([3, 1, 5, 1, 6]) == 3
    assert candidate([5, 5, 1, 8, 3]) == 3
    assert candidate([2, 3]) == 3
    assert candidate([1, 0**0]) == None
    assert candidate([4, 2, 5, 4, 7]) == 4
    assert candidate([4, 1, 5, 1, 2]) == 2
    assert candidate([6, 3, 1, 6, 2]) == 2
    assert candidate([3, 5, 4, 8, 5]) == 4
    assert candidate([6, 1, 4, 3, 2]) == 2
    assert candidate([-35, 34, 12, -45]) == -35

    # Check some edge cases that are easy to work out by hand.
    assert candidate([2, 4, 6, 5, 5]) == 4
    assert candidate([1, 1, 8, 9, 6]) == 6
    assert candidate([4, 5]) == 5
    assert candidate([4, 4]) == None
    assert candidate([4, 1, 3, 2, 2]) == 2
    assert candidate([2, 5]) == 5
    assert candidate([3, 2, 5, 4, 2]) == 3
    assert candidate([4, 1, 4, 8, 5]) == 4
    assert candidate([9, 6, 7, 7, 6]) == 7
    assert candidate([5, 1, 4, 3, 2]) == 2
    assert candidate([]) == None
    assert candidate([3, 1, 3, 3, 5]) == 3
    assert candidate([6, 5, 8, 5, 5]) == 6
    assert candidate([1, 1, 2, 3, 7]) == 2
    assert candidate([3, 6, 1, 4, 3]) == 3
    assert candidate([6, 2]) == 6
    assert candidate([5, 6]) == 6
    assert candidate([4, 3]) == 4

if __name__ == '__main__':
    check(next_smallest)