from case_HE_136 import largest_smallest_integers


def check(candidate):
    assert candidate([2, 2, 6, 8, 14, 7, 8, -13]) == (-13, 2)
    assert candidate([-7, -3, 1, 0, 5]) == (-3, 1)
    assert candidate([-2, -4, 0, -5, -103, 1]) == (-2, 1)
    assert candidate([2, 5, 6, 1, 7, 2, -7]) == (-7, 1)
    assert candidate([-3, -5, -4, -11]) == (-3, None)
    assert candidate([2, 9, 5, 3, 9, 4, 2]) == (None, 2)
    assert candidate([3, 1, 4, 6, 3, 6]) == (None, 1)
    assert candidate([-4, -1, -6, -3]) == (-1, None)
    assert candidate([6, 9, 1, 4, 5, 11]) == (None, 1)
    assert candidate([-1, -5, -9, -10]) == (-1, None)
    assert candidate([-1, -7, -3, -3, 4]) == (-1, 4)
    assert candidate([2, 2, -1, -4]) == (-1, 2)
    assert candidate([2, 9, 3, 2, 3, 3]) == (None, 2)
    assert candidate([2]) == (None, 2)
    assert candidate([-3, 0, -2, -1, -102, 6]) == (-1, 6)
    assert candidate([5, 3, 1, 8, 7, 9, 0]) == (None, 1)
    assert candidate([-11, -7, -1, -3, 6]) == (-1, 6)
    assert candidate([5, 3, 6, 9, 4, 7, -5]) == (-5, 3)
    assert candidate([9, 7, 1, 2, 5, 11, -3]) == (-3, 1)
    assert candidate([5]) == (None, 5)
    assert candidate([-2, -7, -4, -3, -102, 6]) == (-2, 6)
    assert candidate([-1, -3, -5, -6, 0]) == (-1, None)
    assert candidate([5, 7, 12, 9, 11, 6, 6, -4]) == (-4, 5)
    assert candidate([-8, -8, -3, -2, 5]) == (-2, 5)
    assert candidate([8, 4, 3, 8, 6, 1, 10, -8]) == (-8, 1)
    assert candidate([5, 5, 3, 3, 3, 4]) == (None, 3)
    assert candidate([4, 5, 6, 5, 8, 7, 1, -9]) == (-9, 1)
    assert candidate([6, 3, 1, 6, 8, 4, 4]) == (None, 1)
    assert candidate([7, 2, 4, 1, 4, 11, -6]) == (-6, 1)
    assert candidate([1, 3, 2, 4, 5, 6, -2]) == (-2, 1)
    assert candidate([1, 3, 5, 4, 1, 10]) == (None, 1)
    assert candidate([11, 6, 7, 3, 6, 6, 5, -14]) == (-14, 3)
    assert candidate([-6, -6, -6, -2, 2]) == (-2, 2)
    assert candidate([8, 2, 3, 11, 6, 5, -11]) == (-11, 2)
    assert candidate([6, 2, 3, 5, 5, 8, -2]) == (-2, 2)
    assert candidate([9, 8, 8, 1, 3, 3, -8]) == (-8, 1)
    assert candidate([1, 7, 1, 5, 3, 12, 2]) == (None, 1)
    assert candidate([2, 4, 1, 3, 5, 7, 0]) == (None, 1)
    assert candidate([4, 9, 1, 5, 5, 9]) == (None, 1)
    assert candidate([-1, -7, -1, 1, -104, 1]) == (-1, 1)
    assert candidate([-6, -1, -10, -11]) == (-1, None)
    assert candidate([6, 1, 2, 3, 6, 2, 3]) == (None, 1)
    assert candidate([0, -8, -7, -8]) == (-7, None)
    assert candidate([4, 2, 5, 5, 9, 5, 2]) == (None, 2)
    assert candidate([-3, -8, -7, 0, 1]) == (-3, 1)
    assert candidate([7, 4, 2, 7, 7, 5, 2]) == (None, 2)
    assert candidate([1, 1, 1, 8, 4, 11]) == (None, 1)
    assert candidate([3, 4, 1, 9, 5, 7, -12]) == (-12, 1)
    assert candidate([9, 6, 5, 6, 3, 2, -11]) == (-11, 2)
    assert candidate([6, 7, 5, 7, 2, 11, 4]) == (None, 2)
    assert candidate([1, 8, 1, 9, 3, 1, 3]) == (None, 1)
    assert candidate([3, 6, 2, 6, 10, 9]) == (None, 2)
    assert candidate([3, 3, 6, 1, 4, 8, -2]) == (-2, 1)
    assert candidate([3, 4, 5, 6, 1, 9, -2]) == (-2, 1)
    assert candidate([-6, -4, -4, -3, -100, 1]) == (-3, 1)

    # Check some edge cases that are easy to work out by hand.
    assert candidate([-5, -5, 1, 2, -95, 6]) == (-5, 1)
    assert candidate([-4, -3, -1, -4, -102, 4]) == (-1, 4)
    assert candidate([5, 2, 5, 1, 10, 7, 5]) == (None, 1)
    assert candidate([1]) == (None, 1)
    assert candidate([5, 3, 12, 7, 10, 6, 10, -12]) == (-12, 3)
    assert candidate([-1, -3, -8, 2, -97, 3]) == (-1, 2)
    assert candidate([-6, -4, -4, -3, 1]) == (-3, 1)
    assert candidate([2, 4, 4, 5, 10, 12, 5]) == (None, 2)
    assert candidate([1, -7, -4, -11, 1]) == (-4, 1)
    assert candidate([4, 7, 8, 9, 4, 5, -4]) == (-4, 4)
    assert candidate([1, 0, -8, -5]) == (-5, 1)
    assert candidate([-4, -8, -7, -3, 5]) == (-3, 5)
    assert candidate([-1, 1, -10, -6, 1]) == (-1, 1)
    assert candidate([4, 5, 3, 6, 2, 7, -7]) == (-7, 2)
    assert candidate([-10, -5, -8, 2, -100, 5]) == (-5, 2)
    assert candidate([-6, -8, -7, -11, 5]) == (-6, 5)
    assert candidate([]) == (None, None)
    assert candidate([-1, -9, -1, -6, -100, 2]) == (-1, 2)
    assert candidate([-9, -2, -7, -6, 4]) == (-2, 4)
    assert candidate([5, 6, 3, 7, 9, 1, -6]) == (-6, 1)
    assert candidate([-3, -1, -5, -3, -102, 3]) == (-1, 3)
    assert candidate([4, -7, -4, -10, 1]) == (-4, 1)
    assert candidate([-9, -4, -3, -8, 4]) == (-3, 4)
    assert candidate([8, 1, 11, 9, 12, 7, 5, -11]) == (-11, 1)
    assert candidate([7, 7, 7, 1, 5, 7, 5, -10]) == (-10, 1)
    assert candidate([3]) == (None, 3)
    assert candidate([1, -1, -10, -8]) == (-1, 1)
    assert candidate([0]) == (None, None)
    assert candidate([3, -6, -3, -9]) == (-3, 3)
    assert candidate([7, 3, 8, 4, 9, 2, 5, -9]) == (-9, 2)
    assert candidate([9, 2, 4, 1, 6, 5, -4]) == (-4, 1)
    assert candidate([-1, -3, -5, -6]) == (-1, None)
    assert candidate([9, 6, 4, 3, 7, 4, 4, -9]) == (-9, 3)
    assert candidate([-4, -9, -8, 2, -100, 2]) == (-4, 2)
    assert candidate([4]) == (None, 4)
    assert candidate([-4, -8, 0, -8, 1]) == (-4, 1)
    assert candidate([3, 4, 2, 7, 5, 3, 4]) == (None, 2)
    assert candidate([5, 7, 3, 7, 7, 3, -1]) == (-1, 3)
    assert candidate([-1, 2, -5, -2]) == (-1, 2)
    assert candidate([1, 6, 2, 5, 7, 3]) == (None, 1)
    assert candidate([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert candidate([1, 6, 1, 9, 5, 4, 0]) == (None, 1)
    assert candidate([1, -3, -3, -3, 1]) == (-3, 1)
    assert candidate([-6, 1, -8, -3, 5]) == (-3, 1)
    assert candidate([-4, -6, 1, -8, 1]) == (-4, 1)
    assert candidate([4, 4, 2, 5, 4, 10]) == (None, 2)
    assert candidate([1, 7, 4, 3, 5, 5, 0]) == (None, 1)
    assert candidate([4, 4, 5, 5, 5, 6]) == (None, 4)
    assert candidate([-7, -6, 0, -8, 1]) == (-6, 1)
    assert candidate([5, 9, 6, 4, 3, 7]) == (None, 3)
    assert candidate([1, 5, 8, 10, 1, 2, -3]) == (-3, 1)
    assert candidate([-6, 0, -2, -4]) == (-2, None)
    assert candidate([5, 3, 5, 1, 13, 4, 5, -4]) == (-4, 1)
    assert candidate([-6, -8, 1, 0, -103, 5]) == (-6, 1)
    assert candidate([-6, -1, -3, -1, 1]) == (-1, 1)
    assert candidate([2, 8, 6, 7, 1, 10, -8]) == (-8, 1)
    assert candidate([-3, -4, -3, -3, 5]) == (-3, 5)
    assert candidate([2, 3, 5, 9, 5, 9, 3]) == (None, 2)
    assert candidate([-3, 1, -9, -8, 2]) == (-3, 1)
    assert candidate([-7, -4, -5, -6, 5]) == (-4, 5)
    assert candidate([3, 8, 2, 5, 9, 1, 2]) == (None, 1)
    assert candidate([-1, -7, -10, -1, 1]) == (-1, 1)
    assert candidate([5, 7, 4, 3, 3, 11, 2]) == (None, 2)
    assert candidate([2, 8, 13, 2, 11, 6, 10, -10]) == (-10, 2)
    assert candidate([-7, -8, -7, -3, 3]) == (-3, 3)
    assert candidate([7, 1, 4, 5, 9, 8, 3]) == (None, 1)
    assert candidate([-2, -4, -10, -2]) == (-2, None)
    assert candidate([7, 9, 1, 8, 10, 6, 3]) == (None, 1)
    assert candidate([2, 1, 4, 9, 11, 7, 6, -7]) == (-7, 1)

if __name__ == '__main__':
    check(largest_smallest_integers)