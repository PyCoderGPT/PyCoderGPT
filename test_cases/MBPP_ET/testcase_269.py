from case_MBPP_269 import max_sub_array_sum


def check(candidate):
    assert candidate([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert candidate([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
    assert candidate([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10
    assert candidate([-2, -5, 5, 1, -7, 2, 4, -7], 4) == 6
    assert candidate([-5, -3, 3, -6, -7, 3, 6, -7], 6) == 3
    assert candidate([-2, 2, 5, -5, -4, 2, 4, -7], 6) == 7
    assert candidate([-1, -7, 4, -3, -2, 5, 5, 2], 4) == 4
    assert candidate([-7, -4, 6, 2, -4, 4, 9, -5], 5) == 8
    assert candidate([-3, -7, 3, 4, -4, 6, 1, -5], 4) == 7
    assert candidate([2, -7, 2, 0, -2, 2, 3, -7], 6) == 2
    assert candidate([-4, -2, 7, 1, -7, 2, 2, -8], 6) == 8
    assert candidate([-1, -8, 8, 0, -5, 6, 3, 1], 3) == 8
    assert candidate([-7, 2, 1, 2, -2, 4, 3, -1], 4) == 5
    assert candidate([-1, -1, 8, -3, 0, 6, 2, -3], 4) == 8
    assert candidate([2, -1, 9, 4, 0, 5, 5, 2], 5) == 14
    assert candidate([0, 0, 5, 4, -2, 5, 6, -6], 4) == 9
    assert candidate([-4, -3, 3, -6, -7, 2, 7, -6], 4) == 3
    assert candidate([-7, 2, 5, 2, -5, 3, 9, -1], 6) == 9
    assert candidate([1, 0, 8, -6, -1, 2, 6, 1], 8) == 11
    assert candidate([-2, -8, 3, 4, 2, 5, 1, -8], 6) == 14
    assert candidate([-1, -1, 5, -2, 0, 2, 7, -5], 4) == 5
    assert candidate([-5, -5, 2, 2, 0, 5, 7, -7], 6) == 9
    assert candidate([3, -5, 8, 2, 2, 6, 3, -2], 6) == 18
    assert candidate([2, -4, 6, -5, 0, 5, 2, 2], 5) == 6
    assert candidate([-4, -4, 6, -3, -4, 1, 4, 0], 5) == 6
    assert candidate([3, -2, 6, -6, -5, 6, 10, 2], 4) == 7
    assert candidate([0, -8, 6, 0, 1, 4, 9, -5], 8) == 20
    assert candidate([-6, -2, 8, -5, 3, 2, 4, -4], 6) == 8
    assert candidate([-2, -4, 6, -6, -5, 1, 2, -5], 7) == 6
    assert candidate([-1, -1, 8, -2, -6, 2, 5, 0], 4) == 8
    assert candidate([-5, -2, 4, 3, -5, 5, 1, -1], 8) == 8
    assert candidate([-1, -5, 3, 3, -1, 5, 5, -5], 8) == 15
    assert candidate([-4, -4, 6, -3, 3, 1, 5, -1], 7) == 12
    assert candidate([1, -8, 2, -2, 1, 2, 7, -5], 4) == 2
    assert candidate([1, 2, 7, 4, -2, 2, 6, -7], 3) == 10
    assert candidate([-4, -2, 1, 0, -1, 6, 8, -2], 7) == 14
    assert candidate([-2, -4, 1, -6, 2, 6, 2, -8], 3) == 1
    assert candidate([-6, 0, 8, 2, -2, 6, 2, 0], 6) == 14
    assert candidate([-3, -3, 3, -3, -2, 6, 4, -9], 3) == 3
    assert candidate([-3, -2, 4, -3, -6, 6, 4, 1], 4) == 4
    assert candidate([-5, -4, 7, -2, -6, 4, 7, -8], 7) == 11
    assert candidate([1, -5, 8, -1, -7, 5, 4, -4], 4) == 8
    assert candidate([-2, 1, 4, -6, -6, 4, 9, -7], 8) == 13
    assert candidate([-1, -9, 3, -7, 0, 4, 1, 1], 7) == 5
    assert candidate([-5, -7, 10, -4, -3, 6, 9, -6], 8) == 18
    assert candidate([1, -6, 5, -4, 2, 6, 6, -1], 3) == 5
    assert candidate([1, -9, 10, -2, -3, 7, 6, -8], 8) == 18
    assert candidate([-4, -8, 8, -1, -1, 1, 2, -9], 7) == 9
    assert candidate([-3, -4, 4, 1, -8, 7, 10, 1], 7) == 17
    assert candidate([-3, -3, 9, -1, -7, 3, 4, -6], 3) == 9
    assert candidate([-2, -9, 9, 3, -3, 1, 1, -2], 3) == 9
    assert candidate([-3, -3, 10, -5, 2, 1, 5, -4], 7) == 13
    assert candidate([-7, -8, 5, 3, -8, 7, 4, -6], 5) == 8
    assert candidate([2, -1, 2, -3, -1, 7, 9, -3], 7) == 16
    assert candidate([0, -5, 10, -4, -8, 4, 8, -7], 5) == 10
    assert candidate([-4, 1, 9, -5, -8, 3, 1, -1], 5) == 10
    assert candidate([2, -9, 4, 3, -6, 4, 3, -2], 8) == 8
    assert candidate([-3, -1, 10, -7, -2, 6, 3, -3], 8) == 10
    assert candidate([-1, -2, 1, 0, -4, 5, 8, -9], 7) == 13
    assert candidate([-2, -9, 8, -6, 2, 1, 5, -3], 3) == 8
    assert candidate([-4, -7, 3, -5, 1, 5, 7, -4], 7) == 13
    assert candidate([-8, -6, 5, 3, -7, 5, 7, -9], 8) == 13
    assert candidate([-2, -8, 1, 2, -7, 5, 5, -7], 7) == 10
    assert candidate([2, -2, 5, -6, -2, 7, 5, 0], 4) == 5
    assert candidate([-8, -3, 1, 3, -1, 7, 5, -1], 4) == 4
    assert candidate([-5, -5, 5, -5, 0, 5, 2, -2], 7) == 7
    assert candidate([-2, 1, 9, 0, -6, 5, 4, 1], 6) == 10
    assert candidate([-6, -2, 1, -4, -1, 7, 5, -9], 3) == 1
    assert candidate([1, -1, 1, -7, -3, 2, 3, 0], 7) == 5
    assert candidate([-2, -6, 6, -7, -2, 7, 6, -2], 5) == 6
    assert candidate([-6, 0, 5, -5, -4, 3, 2, -6], 5) == 5
    assert candidate([-9, -4, 1, -5, 1, 4, 12, -3], 8) == 17
    assert candidate([-9, -9, 4, 1, -9, 1, 12, -9], 7) == 13
    assert candidate([-2, -6, 6, -5, -3, 7, 6, -6], 3) == 6
    assert candidate([-5, 0, 6, -4, -3, 4, 12, -7], 3) == 6
    assert candidate([0, 0, 6, -4, -8, 1, 12, -3], 8) == 13
    assert candidate([-3, -4, 3, -2, -4, 8, 11, -4], 7) == 19
    assert candidate([-8, -10, 5, -4, 1, 5, 8, -3], 3) == 5
    assert candidate([0, -7, 9, -1, 0, 5, 6, 0], 3) == 9
    assert candidate([-3, -4, 7, 1, -2, 8, 8, -4], 6) == 14
    assert candidate([-3, -9, 8, -6, -4, 7, 7, -1], 8) == 14
    assert candidate([-3, -7, 10, -7, -4, 3, 3, -4], 7) == 10
    assert candidate([-5, -8, 7, -4, 0, 7, 7, -4], 3) == 7
    assert candidate([1, -5, 5, -2, -1, 4, 11, 0], 3) == 5
    assert candidate([1, -7, 5, -2, -7, 2, 8, -6], 6) == 5
    assert candidate([0, -5, 4, -4, -2, 5, 12, -8], 5) == 4
    assert candidate([1, -8, 7, 2, -7, 8, 6, -3], 4) == 9
    assert candidate([-2, -9, 10, -4, -5, 7, 10, -7], 4) == 10
    assert candidate([-9, -7, 9, -4, -4, 2, 4, -1], 4) == 9
    assert candidate([1, -10, 8, -8, -7, 3, 5, -4], 6) == 8
    assert candidate([-7, -8, 6, 2, -7, 4, 4, -6], 7) == 9
    assert candidate([-5, 0, 10, 0, -8, 6, 12, -4], 5) == 10
    assert candidate([0, -1, 11, 0, -2, 3, 7, -1], 3) == 11
    assert candidate([-9, -4, 10, -6, 0, 2, 7, -5], 3) == 10
    assert candidate([-2, -4, 2, 1, -8, 6, 8, -1], 3) == 2
    assert candidate([-4, -5, 3, -4, -8, 7, 12, 0], 8) == 19
    assert candidate([-1, -8, 3, -3, 0, 6, 5, -6], 5) == 3
    assert candidate([-3, -7, 11, 2, -2, 7, 12, -9], 5) == 13
    assert candidate([-4, -7, 1, -7, -4, 6, 3, -6], 5) == 1
    assert candidate([-6, -7, 4, -2, 1, 6, 8, -4], 3) == 4
    assert candidate([0, -10, 9, 2, -6, 5, 4, -2], 5) == 11
    assert candidate([1, -3, 9, -7, 0, 3, 8, -5], 4) == 9

if __name__ == '__main__':
    check(max_sub_array_sum)