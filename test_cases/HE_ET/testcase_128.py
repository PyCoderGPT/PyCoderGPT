from case_HE_128 import prod_signs


def check(candidate):
    assert candidate([4, 1, -3, 4]) == -12
    assert candidate([3, 1, 6, 0]) == 0
    assert candidate([4, 6, 1, 4]) == 15
    assert candidate([-1, 1, 1, 0]) == 0

    # Check some edge cases that are easy to work out by hand.
    assert candidate([6, 9, 3, 2, 0, 0, 6]) == 0
    assert candidate([6, 5, 1, 2, 1, 1, 11]) == 27
    assert candidate([4, 6]) == 10
    assert candidate([0, 1, 2, 3]) == 0
    assert candidate([1, 1, 1, 2, 3, -1, 1]) == -10
    assert candidate([4, 7, 1, 3, 0, -6, 6]) == 0
    assert candidate([5, 2]) == 7
    assert candidate([1, 2, 5, 6]) == 14
    assert candidate([4, 1, 5, 5]) == 15
    assert candidate([-4, 2, -3, 3]) == 12
    assert candidate([7, 4, 3, 4, 1, -1, 12]) == -32
    assert candidate([3, 5, 5, 5]) == 18
    assert candidate([4, 1, 2, 5, 5, -6, 5]) == -28
    assert candidate([-6, 6, -5, 2]) == 19
    assert candidate([1, 4, 2, 3]) == 10
    assert candidate([5, 5, 5, 3, 5, -4, 4]) == -31
    assert candidate([6, 3, 2, -9]) == -20
    assert candidate([-2, 1, 4, 3]) == -10
    assert candidate([5, 3, 2, -4]) == -14
    assert candidate([2, 4, 3, 6, 7, -4, 2]) == -28
    assert candidate([2, 8, 2, 7, 3, 2, 11]) == 35
    assert candidate([-3, 4, 4, 4]) == -15
    assert candidate([-1, 1, 1, 1]) == -4
    assert candidate([3, 2]) == 5
    assert candidate([-2, 5, -6, 1]) == 14
    assert candidate([5, 6, 1, 3, 5, -3, 3]) == -26
    assert candidate([4, 3, 5, -4]) == -16
    assert candidate([3, 3, 2, 4]) == 12
    assert candidate([4, 1]) == 5
    assert candidate([5, 9, 6, 1, 0, -4, 13]) == 0
    assert candidate([1, 5, 4, 5, 3, 4, 2]) == 24
    assert candidate([5, 3, 4, 1, 1, 1, 9]) == 24
    assert candidate([2, 4, 2, 1, 7, 1, 4]) == 21
    assert candidate([-1, 6, 1, 2]) == -10
    assert candidate([0, 5, 4, 4]) == 0
    assert candidate([7, 6, 1, 4, -5, 0, 5]) == 0
    assert candidate([3, 3, 4, 3]) == 13
    assert candidate([3, 1, 3, 5, -6, 3, 10]) == -31
    assert candidate([2, 4,1, 2, -1, -1, 9]) == 20
    assert candidate([1, 2, 6, 3]) == 12
    assert candidate([1, 2, 2, 6]) == 11
    assert candidate([6, 6, 3, 6, 0, 3, 8]) == 0
    assert candidate([3, 2, -3, 1]) == -9
    assert candidate([-4, 6, 6, 3]) == -19
    assert candidate([1, 3, 2, -7]) == -13
    assert candidate([2, 4]) == 6
    assert candidate([3, 6, 4, 1, 5, -6, 2]) == -27
    assert candidate([-5, 5, 2, 5]) == -17
    assert candidate([-6, 2, 1, 2]) == -11
    assert candidate([-6, 2, 6, 4]) == -18
    assert candidate([-1, 1, 6, 1]) == -9
    assert candidate([3, 5]) == 8
    assert candidate([0, 5, 2, 1]) == 0
    assert candidate([0, 1, 5, 3]) == 0
    assert candidate([1, 4, 2, 5]) == 12
    assert candidate([6, 4, 2, 3, 7, -1, 1]) == -24
    assert candidate([1, 5]) == 6
    assert candidate([4, 3, 3, 2, 7, -5, 2]) == -26
    assert candidate([-2, 1, 1, 3]) == -7
    assert candidate([-6, 2, 2, 4]) == -14
    assert candidate([1, 7, 5, 5, 2, 0, 6]) == 0
    assert candidate([1, 4, 6, -2]) == -13
    assert candidate([2, 6, 2, 2, 0, 4, 5]) == 0
    assert candidate([1, 2, 2, -4]) == -9
    assert candidate([0, 4, 4, 4]) == 0
    assert candidate([2, 4, 3, 1, 6, -4, 1]) == -21
    assert candidate([6, 5, 5, -5]) == -21
    assert candidate([4, 2, 3, 2]) == 11
    assert candidate([4, 5]) == 9
    assert candidate([-4, 2, 6, 3]) == -15
    assert candidate([3, 1]) == 4
    assert candidate([-4, 5, 3, 5]) == -17
    assert candidate([0, 1]) == 0
    assert candidate([6, 4, 7, -3]) == -20
    assert candidate([1, 1, 1, 5, 4, -1, 5]) == -18
    assert candidate([3, 8, 5, 2, 4, -4, 10]) == -36
    assert candidate([-4, 2, 2, 3]) == -11
    assert candidate([]) == None
    assert candidate([6, 7, 6, -1]) == -20
    assert candidate([3, 6, 1, 4, 7, -4, 1]) == -26
    assert candidate([3, 1, -3, 1]) == -8
    assert candidate([-5, 2, 3, 3]) == -13
    assert candidate([3, 1, 2, 5]) == 11
    assert candidate([5, 3, 5, 2, 6, 4, 2]) == 27
    assert candidate([2, 2, 4, 5]) == 13
    assert candidate([5, 5, 6, 1, 7, 0, 3]) == 0
    assert candidate([0, 4, 4, 5]) == 0
    assert candidate([1, 1]) == 2
    assert candidate([-6, 6, 5, 3]) == -20
    assert candidate([6, 6, 4, -4]) == -20
    assert candidate([3, 5, 4, -5]) == -17
    assert candidate([4, 6, 4, 4, 2, -5, 3]) == -28
    assert candidate([5, 6]) == 11
    assert candidate([6, 2, 6, -7]) == -21
    assert candidate([6, 7, 1, -9]) == -23
    assert candidate([3, 4, -2, 5]) == -14
    assert candidate([4, 2, 1, 6]) == 13
    assert candidate([4, 2, 5, -7]) == -18
    assert candidate([7, 5, 3, 3, -4, -3, 8]) == 33
    assert candidate([2, 2]) == 4
    assert candidate([7, 1, 4, 2, 0, 3, 6]) == 0
    assert candidate([3, 3, 5, -9]) == -20
    assert candidate([-1, 6, 1, 4]) == -12
    assert candidate([-1, 1, -1, 1]) == 4
    assert candidate([-4, 4, 2, 6]) == -16
    assert candidate([-5, 1, 4, 2]) == -12

if __name__ == '__main__':
    check(prod_signs)