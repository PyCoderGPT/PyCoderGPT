from case_HE_085 import add


def check(candidate):
    assert candidate([3, 1, 9, 6]) == 6
    assert candidate([5, 2, 10, 3]) == 2
    assert candidate([4, 4, 6, 8]) == 12

    # Check some edge cases that are easy to work out by hand.
    assert candidate([6, 92]) == 92
    assert candidate([6, 88]) == 88
    assert candidate([6, 3, 6, 11]) == 0
    assert candidate([2, 1, 10, 12]) == 12
    assert candidate([8, 1, 9, 9, 1, 124]) == 124
    assert candidate([3, 10, 9, 8, 1, 122]) == 140
    assert candidate([1, 1, 5, 4, 3, 124]) == 128
    assert candidate([6, 3, 8, 2]) == 2
    assert candidate([5, 4, 2, 12]) == 16
    assert candidate([4, 86]) == 86
    assert candidate([9, 89]) == 0
    assert candidate([7, 89]) == 0
    assert candidate([7, 8, 2, 8, 5, 119]) == 16
    assert candidate([1, 87]) == 0
    assert candidate([4, 4, 1, 8, 6, 125]) == 12
    assert candidate([2, 4, 11, 8, 6, 123]) == 12
    assert candidate([6, 4, 6, 3]) == 4
    assert candidate([9, 93]) == 0
    assert candidate([9, 87]) == 0
    assert candidate([4, 0, 6, 7]) == 0
    assert candidate([9, 3, 8, 2]) == 2
    assert candidate([8, 7, 5, 6, 2, 127]) == 6
    assert candidate([3, 8, 5, 4, 4, 121]) == 12
    assert candidate([5, 5, 9, 9]) == 0
    assert candidate([4, 5, 6, 7, 2, 122]) == 122
    assert candidate([6, 3, 1, 6]) == 6
    assert candidate([7, 1, 8, 12]) == 12
    assert candidate([3, 87]) == 0
    assert candidate([5, 9, 1, 3, 6, 125]) == 0
    assert candidate([8, 83]) == 0
    assert candidate([4, 1, 8, 6]) == 6
    assert candidate([5, 3, 5, 12]) == 12
    assert candidate([5, 5, 5, 9]) == 0
    assert candidate([6, 4, 9, 12, 1, 122]) == 138
    assert candidate([7, 88]) == 88
    assert candidate([4, 8, 9, 6, 2, 121]) == 14
    assert candidate([3, 88]) == 88
    assert candidate([5, 8, 10, 8, 7, 117]) == 16
    assert candidate([5, 2, 5, 6]) == 8
    assert candidate([3, 3, 11, 8]) == 8
    assert candidate([1, 9, 11, 10, 3, 118]) == 128
    assert candidate([5, 85]) == 0
    assert candidate([4, 84]) == 84
    assert candidate([2, 85]) == 0
    assert candidate([9, 3, 9, 2]) == 2
    assert candidate([8, 5, 8, 3]) == 0
    assert candidate([7, 5, 1, 11, 4, 120]) == 120
    assert candidate([2, 10, 1, 5, 1, 127]) == 10
    assert candidate([7, 2, 10, 5]) == 2
    assert candidate([8, 2, 2, 8]) == 10
    assert candidate([4, 5, 10, 9]) == 0
    assert candidate([9, 91]) == 0
    assert candidate([6, 3, 9, 12]) == 12
    assert candidate([4, 88]) == 88
    assert candidate([2, 3, 1, 11]) == 0
    assert candidate([8, 84]) == 84
    assert candidate([6, 9, 7, 8, 2, 124]) == 132
    assert candidate([2, 84]) == 84
    assert candidate([8, 91]) == 0
    assert candidate([9, 90]) == 90
    assert candidate([2, 2, 3, 6, 7, 123]) == 8
    assert candidate([9, 6, 11, 5, 4, 120]) == 126
    assert candidate([6, 85]) == 0
    assert candidate([8, 1, 8, 4]) == 4
    assert candidate([6, 91]) == 0
    assert candidate([5, 91]) == 0
    assert candidate([5, 5, 4, 12, 5, 120]) == 132
    assert candidate([7, 90]) == 90
    assert candidate([6, 4, 7, 6]) == 10
    assert candidate([9, 10, 4, 10, 2, 120]) == 140
    assert candidate([8, 85]) == 0
    assert candidate([6, 7, 5, 4, 7, 117]) == 4
    assert candidate([7, 1, 1, 7, 7, 123]) == 0
    assert candidate([1, 7, 3, 5, 6, 126]) == 126
    assert candidate([2, 9, 5, 12, 6, 127]) == 12
    assert candidate([9, 9, 11, 10, 6, 121]) == 10
    assert candidate([7, 2, 9, 2]) == 4
    assert candidate([6, 90]) == 90
    assert candidate([1, 4, 7, 6, 5, 127]) == 10
    assert candidate([8, 3, 8, 7, 4, 120]) == 120
    assert candidate([7, 3, 4, 12, 5, 119]) == 12
    assert candidate([2, 4, 6, 2]) == 6
    assert candidate([5, 92]) == 92
    assert candidate([4, 3, 3, 4]) == 4
    assert candidate([7, 5, 9, 12, 6, 120]) == 132
    assert candidate([1, 5, 7, 10]) == 10
    assert candidate([2, 5, 1, 6, 3, 122]) == 128
    assert candidate([2, 1, 11, 5]) == 0
    assert candidate([3, 10, 4, 10, 4, 118]) == 138
    assert candidate([5, 5, 6, 9]) == 0
    assert candidate([7, 5, 4, 9]) == 0
    assert candidate([9, 4, 9, 11, 2, 127]) == 4

if __name__ == '__main__':
    check(add)