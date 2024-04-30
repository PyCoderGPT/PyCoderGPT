from case_MBPP_158 import max_sub_array_sum_repeated


def check(candidate):
    assert candidate([10, 20, -30, -1], 4, 3) == 30
    assert candidate([-1, 10, 20], 3, 2) == 59
    assert candidate([-1, -2, -3], 3, 3) == -1
    assert candidate([11, 25, -25, -3], 2, 3) == 108
    assert candidate([12, 15, -31, 2], 1, 3) == 36
    assert candidate([12, 16, -35, -1], 1, 1) == 12
    assert candidate([11, 16, -27, 1], 4, 8) == 34
    assert candidate([10, 20, -26, -3], 1, 1) == 10
    assert candidate([8, 19, -26, -1], 4, 3) == 27
    assert candidate([6, 18, -35, 4], 2, 7) == 168
    assert candidate([5, 15, -34, -6], 1, 1) == 5
    assert candidate([5, 19, -28, 2], 1, 5) == 25
    assert candidate([13, 15, -34, 0], 1, 8) == 104
    assert candidate([9, 24, -31, 2], 2, 3) == 99
    assert candidate([9, 21, -26, 0], 3, 4) == 42
    assert candidate([10, 16, -32, 1], 1, 3) == 30
    assert candidate([12, 15, -32, -1], 3, 1) == 27
    assert candidate([15, 18, -29, 3], 2, 7) == 231
    assert candidate([10, 24, -35, -3], 2, 1) == 34
    assert candidate([12, 20, -30, 3], 1, 6) == 72
    assert candidate([11, 16, -31, 3], 4, 8) == 30
    assert candidate([10, 17, -31, -2], 2, 7) == 189
    assert candidate([5, 18, -33, -2], 1, 2) == 10
    assert candidate([14, 15, -31, -2], 3, 7) == 29
    assert candidate([11, 19, -33, 0], 2, 5) == 150
    assert candidate([10, 24, -32, 4], 3, 4) == 40
    assert candidate([15, 20, -25, 2], 3, 6) == 85
    assert candidate([11, 25, -25, -5], 1, 7) == 77
    assert candidate([9, 24, -27, 0], 3, 8) == 75
    assert candidate([8, 21, -27, -2], 2, 3) == 87
    assert candidate([15, 17, -28, -3], 2, 1) == 32
    assert candidate([11, 24, -26, -4], 3, 2) == 44
    assert candidate([15, 21, -32, -4], 4, 6) == 36
    assert candidate([11, 15, -34, 4], 1, 2) == 22
    assert candidate([14, 23, -25, 4], 2, 6) == 222
    assert candidate([12, 19, -34, 4], 4, 3) == 36
    assert candidate([0, 11, 18], 2, 3) == 33
    assert candidate([1, 14, 21], 2, 5) == 75
    assert candidate([3, 8, 22], 1, 2) == 6
    assert candidate([4, 13, 21], 3, 3) == 114
    assert candidate([3, 9, 22], 1, 5) == 15
    assert candidate([2, 9, 23], 2, 7) == 77
    assert candidate([0, 12, 22], 2, 2) == 24
    assert candidate([-6, 6, 20], 3, 6) == 126
    assert candidate([4, 7, 22], 1, 4) == 16
    assert candidate([-1, 12, 16], 2, 7) == 78
    assert candidate([-5, 11, 20], 2, 6) == 41
    assert candidate([-5, 8, 18], 1, 6) == -5
    assert candidate([2, 12, 25], 3, 7) == 273
    assert candidate([-3, 9, 17], 3, 3) == 72
    assert candidate([-5, 12, 15], 2, 2) == 19
    assert candidate([2, 9, 23], 3, 1) == 34
    assert candidate([-4, 6, 19], 3, 1) == 25
    assert candidate([-2, 10, 20], 1, 5) == -2
    assert candidate([-6, 7, 25], 1, 1) == -6
    assert candidate([-4, 8, 22], 2, 1) == 8
    assert candidate([2, 12, 25], 3, 2) == 78
    assert candidate([-5, 14, 17], 1, 5) == -5
    assert candidate([-5, 5, 15], 2, 1) == 5
    assert candidate([3, 12, 15], 2, 1) == 15
    assert candidate([-3, 7, 22], 3, 1) == 29
    assert candidate([-2, 9, 24], 1, 1) == -2
    assert candidate([1, 13, 15], 2, 3) == 42
    assert candidate([4, 7, 23], 2, 4) == 44
    assert candidate([-3, 15, 20], 2, 7) == 87
    assert candidate([-6, 6, 15], 3, 7) == 111
    assert candidate([-5, 15, 22], 3, 2) == 69
    assert candidate([3, 14, 18], 1, 2) == 6
    assert candidate([-6, 15, 18], 3, 2) == 60
    assert candidate([0, -4, 2], 2, 6) == 0
    assert candidate([3, -5, -2], 3, 5) == 3
    assert candidate([-1, -2, 2], 1, 4) == -1
    assert candidate([2, -7, -6], 1, 2) == 4
    assert candidate([3, -5, 0], 3, 4) == 3
    assert candidate([-4, 2, 1], 3, 5) == 3
    assert candidate([-1, -5, -1], 1, 2) == -1
    assert candidate([3, 0, -3], 2, 4) == 12
    assert candidate([-3, 1, -1], 2, 8) == 1
    assert candidate([2, -4, -2], 1, 4) == 8
    assert candidate([-6, 2, -8], 2, 8) == 2
    assert candidate([-2, -1, -6], 3, 8) == -1
    assert candidate([-5, -3, -1], 3, 2) == -1
    assert candidate([-3, -1, -2], 3, 6) == -1
    assert candidate([-6, -6, -5], 2, 5) == -6
    assert candidate([2, 1, -7], 2, 3) == 9
    assert candidate([-2, -3, -1], 3, 5) == -1
    assert candidate([0, -6, -8], 2, 8) == 0
    assert candidate([4, -4, 1], 1, 6) == 24
    assert candidate([-3, 1, 2], 3, 6) == 3
    assert candidate([2, -1, -3], 1, 6) == 12
    assert candidate([2, -1, -7], 3, 8) == 2
    assert candidate([-4, -7, -3], 2, 1) == -4
    assert candidate([-1, 0, -3], 1, 5) == -1
    assert candidate([0, 1, -5], 2, 4) == 4
    assert candidate([-4, -5, -5], 2, 2) == -4
    assert candidate([2, 2, -5], 1, 2) == 4
    assert candidate([2, -3, -6], 2, 8) == 2
    assert candidate([-3, -4, -5], 1, 6) == -3
    assert candidate([3, -5, -3], 1, 1) == 3
    assert candidate([-2, -3, -2], 3, 2) == -2
    assert candidate([4, -4, 2], 2, 3) == 4
    assert candidate([-4, -4, -5], 1, 7) == -4

if __name__ == '__main__':
    check(max_sub_array_sum_repeated)