from case_HE_114 import minSubArraySum


def check(candidate):
    assert candidate([105, -5, -2, 0, 10, -8]) == -8
    assert candidate([-3, -7, -4, 2, -6]) == -18
    assert candidate([-10000000000000001]) == -10000000000000001
    assert candidate([0, -3, 1]) == -3
    assert candidate([-9999999999999995]) == -9999999999999995
    assert candidate([5, -6]) == -6
    assert candidate([1, -3]) == -3
    assert candidate([5, -5]) == -5
    assert candidate([-11]) == -11
    assert candidate([102, -29, 30, -6, 2, -5]) == -29
    assert candidate([3, -6, -3, 15, -2]) == -9
    assert candidate([2, 3, 9, 2, 2, 6]) == 2
    assert candidate([4, 4, 2, 3, 2, 1]) == 1
    assert candidate([101, -6, -1, -3, 5, -9]) == -14
    assert candidate([2, -6]) == -6
    assert candidate([4, 7, 25, 1000789]) == 4
    assert candidate([98, -30, 31, 3, 2, -4]) == -30
    assert candidate([14, 11, 14, 7, 6, 5]) == 5
    assert candidate([100, 3, -2, 2, 6, -8]) == -8
    assert candidate([0, -5, 0, 1, -15]) == -19
    assert candidate([-9999999999999997]) == -9999999999999997
    assert candidate([7]) == 7
    assert candidate([4, -2, -8, 2, -11]) == -19
    assert candidate([2, 3, 4, 1, 2, 4]) == 1
    assert candidate([-6, 3, -6]) == -9
    assert candidate([3, 6, 22, 999684]) == 3
    assert candidate([-4, -3, -5, 5, -12]) == -19
    assert candidate([3, -5, -2, 5, -8]) == -10
    assert candidate([5, 6, 8, 3, 1, 9]) == 1
    assert candidate([6, 4, 6, 2, 5, 1]) == 1
    assert candidate([15, 12, 10, 3, 4, 7]) == 3
    assert candidate([95, -29, 34, 4, 5, -3]) == -29
    assert candidate([-1, -6, -1, 6, -9]) == -11
    assert candidate([98, -36, 34, 0, 2, 0]) == -36
    assert candidate([11]) == 11
    assert candidate([1, 1, 0, 2, -12]) == -12
    assert candidate([1, -1]) == -1
    assert candidate([1, 12, 21, 999192]) == 1
    assert candidate([99, -36, 35, -1, 1, -4]) == -36
    assert candidate([3, 4, 5, 6, 2, 7]) == 2
    assert candidate([-1, 2, -3, 3, -11]) == -11
    assert candidate([4, 6, 18, 1000090]) == 4
    assert candidate([10, 11, 13, 8, 3, 4]) == 3
    assert candidate([3, 4]) == 3
    assert candidate([100, -33, 32, -1, 0, -2]) == -33

    # Check some edge cases that are easy to work out by hand.
    assert candidate([-6, 3, -7]) == -10
    assert candidate([4, -3, -7]) == -10
    assert candidate([3, 12, 18, 1000591]) == 3
    assert candidate([6]) == 6
    assert candidate([-4, 2, 0]) == -4
    assert candidate([-1, -7, -1, 12, -1]) == -9
    assert candidate([104, 1, -3, -1, 6, -10]) == -10
    assert candidate([3, 15, 23, 1000022]) == 3
    assert candidate([3, 9, 15, 1000630]) == 3
    assert candidate([6, 2, 1, 2, 3, 1]) == 1
    assert candidate([3, -6]) == -6
    assert candidate([3, 7, 9, 6, 5, 7]) == 3
    assert candidate([-5, 3, -2, 8, -5]) == -5
    assert candidate([12]) == 12
    assert candidate([5, 3, 5, 2, 2, 4]) == 2
    assert candidate([11, 13, 17, 9, 5, 2]) == 2
    assert candidate([14, 15, 17, 11, 8, 1]) == 1
    assert candidate([4, -7, -1, 6, -6]) == -8
    assert candidate([-10000000000000000]) == -10000000000000000
    assert candidate([-10000000000000004]) == -10000000000000004
    assert candidate([101, 0, 2, 1, 14, -3]) == -3
    assert candidate([-9999999999999999]) == -9999999999999999
    assert candidate([5, 8, 12, 12, 4, 8]) == 4
    assert candidate([103, -38, 35, 4, 5, -4]) == -38
    assert candidate([4, 15, 24, 999923]) == 4
    assert candidate([4, -3, -7, 12, -2]) == -10
    assert candidate([-2, -6, -7, 3, -8]) == -20
    assert candidate([101, 1, -7, -5, 9, -1]) == -12
    assert candidate([8]) == 8
    assert candidate([100, 1, -2, 0, 8, -9]) == -9
    assert candidate([100, -1, -2, -3, 10, -5]) == -6
    assert candidate([6, 2]) == 2
    assert candidate([2, 10, 21, 1000935]) == 2
    assert candidate([-1, -2, -3, 10, -5]) == -6
    assert candidate([9, 12, 12, 9, 5, 1]) == 1
    assert candidate([95, -37, 29, 0, 1, -5]) == -37
    assert candidate([3, 1, -3]) == -3
    assert candidate([-9]) == -9
    assert candidate([-2, -4, 1]) == -6
    assert candidate([12, 11, 17, 12, 7, 2]) == 2
    assert candidate([3]) == 3
    assert candidate([5, -4]) == -4
    assert candidate([97, -35, 33, -1, 3, -4]) == -35
    assert candidate([96, -28, 37, 2, 5, 0]) == -28
    assert candidate([-6, 3, -4]) == -7
    assert candidate([-6]) == -6
    assert candidate([-12]) == -12
    assert candidate([-3, 0, 2]) == -3
    assert candidate([9]) == 9
    assert candidate([-5, -4, -3, 15, -6]) == -12
    assert candidate([-9999999999999998]) == -9999999999999998
    assert candidate([-10]) == -10
    assert candidate([1, 0, -2]) == -2
    assert candidate([7, 13, 10, 6, 3, 6]) == 3
    assert candidate([-1, -2, -3]) == -6
    assert candidate([4, 8, 3, 2, 5, 6]) == 2
    assert candidate([4, -1]) == -1
    assert candidate([15, 11, 16, 12, 3, 2]) == 2
    assert candidate([1, -7, 0, 9, -1]) == -7
    assert candidate([1, 1, -7, 11, -8]) == -8
    assert candidate([100, -30, 30, 2, 4, -7]) == -30
    assert candidate([97, -6, 0, 1, 5, -6]) == -6
    assert candidate([8, 8, 9, 5, 6, 5]) == 5
    assert candidate([4, 0, -4, 5, -8]) == -8
    assert candidate([-10]) == -10
    assert candidate([100, 0, -1, -7, 10, -9]) == -9
    assert candidate([-1, -2, -3, 2, -10]) == -14
    assert candidate([0, 10, 20, 1000000]) == 0
    assert candidate([96, 1, 1, -7, 14, -5]) == -7
    assert candidate([-1, 3, 1, 13, -6]) == -6
    assert candidate([2]) == 2
    assert candidate([1, 9, 16, 999736]) == 1
    assert candidate([5, 1, 9, 1, 1, 5]) == 1
    assert candidate([-15]) == -15
    assert candidate([0, -7, -3, 1, -12]) == -21

if __name__ == '__main__':
    check(minSubArraySum)