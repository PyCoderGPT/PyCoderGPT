from case_MBPP_356 import sum_Of_Subarray_Prod


def check(candidate):
    assert candidate([1,2,3],3) == 20
    assert candidate([1,2],2) == 5
    assert candidate([1,2,3,4],4) == 84
    assert candidate([4, 5, 4], 3) == 133
    assert candidate([1, 4, 7], 3) == 72
    assert candidate([1, 1, 2], 3) == 9
    assert candidate([1, 5, 3], 3) == 44
    assert candidate([1, 5, 6], 1) == 1
    assert candidate([4, 6, 5], 1) == 4
    assert candidate([6, 1, 4], 2) == 13
    assert candidate([1, 1, 4], 1) == 1
    assert candidate([3, 4, 8], 2) == 19
    assert candidate([1, 5, 3], 3) == 44
    assert candidate([2, 7, 4], 1) == 2
    assert candidate([4, 6, 1], 3) == 65
    assert candidate([5, 3, 7], 2) == 23
    assert candidate([2, 6, 2], 3) == 58
    assert candidate([3, 6, 5], 3) == 152
    assert candidate([2, 7, 2], 3) == 67
    assert candidate([1, 5, 7], 3) == 88
    assert candidate([4, 1, 7], 2) == 9
    assert candidate([6, 3, 5], 1) == 6
    assert candidate([1, 4, 1], 2) == 9
    assert candidate([3, 2, 2], 1) == 3
    assert candidate([2, 1, 4], 2) == 5
    assert candidate([1, 3, 1], 2) == 7
    assert candidate([6, 6, 3], 2) == 48
    assert candidate([6, 2, 3], 2) == 20
    assert candidate([6, 5, 8], 1) == 6
    assert candidate([6, 6, 7], 3) == 349
    assert candidate([3, 2, 6], 2) == 11
    assert candidate([1, 5, 5], 1) == 1
    assert candidate([5, 3, 2], 3) == 61
    assert candidate([5, 1, 5], 2) == 11
    assert candidate([4, 4, 4], 1) == 4
    assert candidate([5, 2, 5], 1) == 5
    assert candidate([3, 5], 2) == 23
    assert candidate([6, 3], 1) == 6
    assert candidate([2, 4], 2) == 14
    assert candidate([5, 3], 2) == 23
    assert candidate([3, 5], 2) == 23
    assert candidate([5, 3], 2) == 23
    assert candidate([1, 6], 2) == 13
    assert candidate([1, 3], 1) == 1
    assert candidate([4, 6], 2) == 34
    assert candidate([1, 5], 2) == 11
    assert candidate([4, 6], 2) == 34
    assert candidate([3, 4], 1) == 3
    assert candidate([5, 7], 1) == 5
    assert candidate([6, 1], 2) == 13
    assert candidate([4, 2], 1) == 4
    assert candidate([5, 1], 1) == 5
    assert candidate([5, 1], 1) == 5
    assert candidate([6, 1], 1) == 6
    assert candidate([2, 7], 1) == 2
    assert candidate([3, 3], 1) == 3
    assert candidate([5, 6], 2) == 41
    assert candidate([4, 2], 2) == 14
    assert candidate([6, 4], 2) == 34
    assert candidate([3, 3], 1) == 3
    assert candidate([5, 4], 1) == 5
    assert candidate([3, 5], 1) == 3
    assert candidate([5, 4], 1) == 5
    assert candidate([2, 6], 2) == 20
    assert candidate([5, 1], 1) == 5
    assert candidate([6, 6], 1) == 6
    assert candidate([6, 4], 1) == 6
    assert candidate([6, 1], 1) == 6
    assert candidate([2, 2], 2) == 8
    assert candidate([1, 3, 1, 6], 1) == 1
    assert candidate([5, 7, 5, 8], 1) == 5
    assert candidate([4, 4, 6, 8], 1) == 4
    assert candidate([1, 2, 1, 3], 2) == 5
    assert candidate([4, 2, 3, 4], 4) == 183
    assert candidate([4, 2, 6, 8], 3) == 80
    assert candidate([4, 1, 5, 2], 1) == 4
    assert candidate([5, 4, 6, 1], 4) == 330
    assert candidate([4, 1, 6, 8], 4) == 341
    assert candidate([5, 3, 1, 4], 2) == 23
    assert candidate([3, 4, 6, 3], 2) == 19
    assert candidate([1, 2, 7, 4], 2) == 5
    assert candidate([2, 6, 3, 4], 1) == 2
    assert candidate([6, 2, 8, 7], 2) == 20
    assert candidate([2, 2, 8, 6], 3) == 64
    assert candidate([5, 3, 7, 6], 4) == 960
    assert candidate([5, 2, 7, 6], 2) == 17
    assert candidate([4, 7, 8, 7], 4) == 2350
    assert candidate([6, 6, 3, 6], 3) == 177
    assert candidate([1, 6, 6, 8], 2) == 13
    assert candidate([3, 4, 7, 5], 1) == 3
    assert candidate([5, 7, 7, 4], 3) == 348
    assert candidate([6, 6, 1, 1], 2) == 48
    assert candidate([1, 5, 8, 1], 3) == 99
    assert candidate([4, 6, 1, 7], 4) == 289
    assert candidate([2, 2, 1, 5], 1) == 2
    assert candidate([4, 2, 8, 2], 4) == 280
    assert candidate([2, 2, 4, 9], 2) == 8
    assert candidate([1, 6, 2, 8], 3) == 39
    assert candidate([3, 1, 2, 7], 2) == 7
    assert candidate([6, 6, 4, 7], 2) == 48
    assert candidate([2, 4, 7, 3], 4) == 381
    assert candidate([3, 4, 1, 3], 2) == 19

if __name__ == '__main__':
    check(sum_Of_Subarray_Prod)