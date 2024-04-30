from case_HE_135 import can_arrange


def check(candidate):
    assert candidate([3, 2, 5, 9, 6, 10, 10, 9, 9]) == 7
    assert candidate([2, 3, 1, 4]) == 2
    assert candidate([4,8,5,7,3])==4

    # Check some edge cases that are easy to work out by hand.
    assert candidate([5, 1, 2, 5, 2]) == 4
    assert candidate([9, 12, 2, 2, 5]) == 2
    assert candidate([1, 5, 9, 5]) == 3
    assert candidate([3, 7, 7, 3, 4]) == 3
    assert candidate([1, 1, 3, 10]) == -1
    assert candidate([3, 11, 2, 5, 7]) == 2
    assert candidate([2, 7, 7, 6, 3]) == 4
    assert candidate([7, 11, 4, 9, 6]) == 4
    assert candidate([2, 8, 5, 2, 10, 9, 6, 7, 5]) == 8
    assert candidate([5, 7, 1, 6, 6]) == 2
    assert candidate([3, 6, 4, 6]) == 2
    assert candidate([1, 4, 8, 7, 4]) == 4
    assert candidate([2, 4, 6, 7, 2, 6, 9, 10, 5]) == 8
    assert candidate([4, 1, 3, 6]) == 1
    assert candidate([2, 9, 2, 8, 7, 2, 5, 6, 13]) == 5
    assert candidate([1, 5, 9, 8, 3]) == 4
    assert candidate([2, 4, 1, 10, 10, 7, 3, 10, 11]) == 6
    assert candidate([3, 5, 6, 8, 9]) == -1
    assert candidate([1, 3, 7, 5]) == 3
    assert candidate([4, 1, 2, 1, 3, 4, 10, 4, 10]) == 7
    assert candidate([3, 6, 3, 8, 10, 8, 9, 4, 5]) == 7
    assert candidate([5, 2, 4, 4, 1]) == 4
    assert candidate([3, 7, 2, 9]) == 2
    assert candidate([5, 11, 4, 9, 5]) == 4
    assert candidate([6, 11, 5, 8, 3]) == 4
    assert candidate([1, 5, 4, 7, 10, 2, 7, 14, 6]) == 8
    assert candidate([5, 12, 4, 6, 1]) == 4
    assert candidate([])==-1
    assert candidate([3, 5, 2, 3]) == 2
    assert candidate([7, 9, 6, 4, 8]) == 3
    assert candidate([4, 9, 5, 5, 7]) == 2
    assert candidate([5, 12, 5, 5, 8]) == 2
    assert candidate([3, 1, 4, 1, 3]) == 3
    assert candidate([1,2,4,5])==-1
    assert candidate([4, 4, 4, 5, 6]) == -1
    assert candidate([4, 3, 2, 10, 7, 7, 3, 12, 13]) == 6
    assert candidate([1, 4, 7, 4, 7]) == 3
    assert candidate([6, 4, 6, 7, 4]) == 4
    assert candidate([6, 5, 5, 4, 1]) == 4
    assert candidate([4, 5, 2, 4, 5]) == 2
    assert candidate([2, 3, 4, 1]) == 3
    assert candidate([4, 4, 3, 2]) == 3
    assert candidate([4, 5, 3, 4, 5, 4, 7, 7, 14]) == 5
    assert candidate([5, 5, 8, 1, 8]) == 3
    assert candidate([1, 3, 9, 9]) == -1
    assert candidate([3, 7, 2, 7, 11, 6, 11, 12, 14]) == 5
    assert candidate([9, 6, 3, 5, 6]) == 2
    assert candidate([4, 5, 2, 8, 9]) == 2
    assert candidate([5, 5, 2, 8, 4]) == 4
    assert candidate([5, 3, 1, 2]) == 2
    assert candidate([3, 7, 5, 6, 4]) == 4
    assert candidate([4, 5, 5, 9]) == -1
    assert candidate([1, 4, 9, 9]) == -1
    assert candidate([4, 1, 6, 4, 9, 6, 10, 7, 11]) == 7
    assert candidate([1, 4, 9, 4]) == 3
    assert candidate([1,2,4,3,5])==3
    assert candidate([6, 1, 2, 6]) == 1
    assert candidate([1, 6, 1, 3, 7, 8, 5, 5, 5]) == 6
    assert candidate([5, 7, 6, 9, 5]) == 4
    assert candidate([5, 6, 9, 5]) == 3
    assert candidate([3, 4, 2, 5, 2]) == 4
    assert candidate([2, 6, 2, 2, 6]) == 2
    assert candidate([5, 7, 5, 1, 10, 6, 11, 11, 6]) == 8
    assert candidate([3, 7, 2, 2, 9, 11, 10, 5, 14]) == 7
    assert candidate([2, 5, 3, 2, 5]) == 3
    assert candidate([4, 6, 6, 1, 2]) == 3
    assert candidate([5, 4, 5, 3, 7, 8, 5, 14, 12]) == 8
    assert candidate([4, 7, 6, 5]) == 3
    assert candidate([2, 5, 5, 3, 3]) == 3
    assert candidate([2, 3, 9, 2]) == 3
    assert candidate([4, 3, 4, 3, 6, 8, 6, 14, 5]) == 8
    assert candidate([3, 3, 5, 12, 6]) == 4
    assert candidate([6, 8, 5, 6, 10, 3, 10, 5, 11]) == 7
    assert candidate([5, 7, 7, 9]) == -1
    assert candidate([8, 4, 9, 9, 3]) == 4
    assert candidate([4, 5, 7, 8, 4]) == 4
    assert candidate([4, 2, 6, 2, 7]) == 3
    assert candidate([2, 6, 7, 1]) == 3
    assert candidate([2, 4, 5, 7, 7]) == -1
    assert candidate([7, 4, 1, 11, 3]) == 4
    assert candidate([3, 1, 4, 3]) == 3
    assert candidate([5, 7, 3, 9, 1, 8, 8, 4, 12]) == 7
    assert candidate([4, 12, 7, 3, 6]) == 3
    assert candidate([2, 4, 7, 3, 8, 6, 13, 8, 11]) == 7
    assert candidate([5, 2, 8, 6, 2]) == 4
    assert candidate([3, 1, 4, 6, 4]) == 4
    assert candidate([9, 8, 3, 7, 3]) == 4
    assert candidate([1, 7, 8, 4, 3]) == 4
    assert candidate([3, 9, 2, 5, 1, 12, 5, 4, 5]) == 7
    assert candidate([2, 5, 3, 3, 3, 8, 12, 8, 14]) == 7
    assert candidate([2, 3, 5, 2, 4]) == 3
    assert candidate([4, 6, 2, 6]) == 2
    assert candidate([5, 7, 7, 5, 3]) == 4
    assert candidate([3, 7, 7, 2]) == 3
    assert candidate([4, 4, 2, 8, 3, 11, 6, 8, 5]) == 8
    assert candidate([1, 5, 7, 3, 1, 12, 5, 14, 6]) == 8
    assert candidate([]) == -1
    assert candidate([4, 2, 2, 7, 3]) == 4
    assert candidate([1,4,2,5,6,7,8,9,10])==2
    assert candidate([3, 7, 6, 6, 4]) == 4
    assert candidate([2, 4, 1, 9]) == 2
    assert candidate([6, 4, 5, 1, 3, 11, 8, 5, 12]) == 7
    assert candidate([7, 10, 5, 4, 4]) == 3

if __name__ == '__main__':
    check(can_arrange)