from case_MBPP_335 import pair_OR_Sum


def check(candidate):
    assert candidate([5,9,7,6],4) == 47
    assert candidate([7,3,5],3) == 12
    assert candidate([7,3],2) == 4
    assert candidate([4, 13, 9, 1], 1) == 0
    assert candidate([2, 6, 3, 11], 1) == 0
    assert candidate([10, 4, 9, 10], 2) == 14
    assert candidate([4, 12, 3, 11], 4) == 60
    assert candidate([9, 5, 3, 10], 1) == 0
    assert candidate([3, 12, 5, 3], 3) == 30
    assert candidate([8, 9, 12, 9], 3) == 10
    assert candidate([1, 7, 12, 10], 2) == 6
    assert candidate([9, 11, 2, 10], 3) == 22
    assert candidate([4, 10, 6, 11], 2) == 14
    assert candidate([4, 9, 2, 1], 1) == 0
    assert candidate([6, 6, 6, 3], 4) == 15
    assert candidate([6, 10, 8, 8], 4) == 44
    assert candidate([3, 7, 10, 6], 3) == 26
    assert candidate([7, 11, 11, 10], 1) == 0
    assert candidate([8, 13, 3, 4], 3) == 30
    assert candidate([8, 10, 10, 7], 4) == 45
    assert candidate([9, 7, 9, 3], 1) == 0
    assert candidate([3, 5, 9, 2], 1) == 0
    assert candidate([2, 10, 9, 10], 1) == 0
    assert candidate([1, 12, 8, 3], 3) == 26
    assert candidate([10, 8, 11, 8], 3) == 6
    assert candidate([2, 7, 4, 6], 4) == 21
    assert candidate([8, 9, 3, 4], 1) == 0
    assert candidate([3, 6, 9, 1], 1) == 0
    assert candidate([7, 10, 3, 8], 3) == 26
    assert candidate([5, 13, 6, 4], 2) == 8
    assert candidate([5, 11, 5, 4], 2) == 14
    assert candidate([4, 13, 9, 8], 3) == 26
    assert candidate([9, 6, 6, 4], 1) == 0
    assert candidate([5, 9, 3, 5], 3) == 28
    assert candidate([1, 7, 7, 3], 1) == 0
    assert candidate([2, 4, 6, 2], 4) == 22
    assert candidate([11, 3, 1], 3) == 20
    assert candidate([12, 6, 2], 3) == 28
    assert candidate([8, 8, 5], 2) == 0
    assert candidate([6, 5, 1], 2) == 3
    assert candidate([3, 3, 7], 1) == 0
    assert candidate([12, 1, 6], 1) == 0
    assert candidate([12, 8, 10], 2) == 4
    assert candidate([2, 8, 9], 1) == 0
    assert candidate([12, 1, 10], 2) == 13
    assert candidate([4, 2, 5], 1) == 0
    assert candidate([4, 8, 5], 3) == 26
    assert candidate([8, 4, 2], 2) == 12
    assert candidate([7, 7, 3], 2) == 0
    assert candidate([12, 8, 7], 3) == 30
    assert candidate([4, 4, 10], 1) == 0
    assert candidate([6, 1, 2], 2) == 7
    assert candidate([10, 1, 5], 3) == 30
    assert candidate([3, 4, 9], 1) == 0
    assert candidate([12, 6, 9], 1) == 0
    assert candidate([2, 5, 1], 2) == 7
    assert candidate([4, 6, 1], 2) == 2
    assert candidate([8, 2, 7], 1) == 0
    assert candidate([5, 8, 10], 2) == 13
    assert candidate([10, 6, 6], 1) == 0
    assert candidate([5, 1, 7], 3) == 12
    assert candidate([7, 7, 5], 3) == 4
    assert candidate([9, 2, 5], 1) == 0
    assert candidate([8, 1, 5], 3) == 26
    assert candidate([8, 1, 1], 1) == 0
    assert candidate([6, 8, 4], 1) == 0
    assert candidate([10, 5, 10], 1) == 0
    assert candidate([8, 1, 1], 2) == 9
    assert candidate([7, 4, 9], 1) == 0
    assert candidate([8, 2], 1) == 0
    assert candidate([10, 7], 1) == 0
    assert candidate([2, 4], 2) == 6
    assert candidate([9, 6], 2) == 15
    assert candidate([3, 6], 1) == 0
    assert candidate([8, 2], 1) == 0
    assert candidate([7, 4], 2) == 3
    assert candidate([3, 4], 2) == 7
    assert candidate([6, 4], 2) == 2
    assert candidate([12, 5], 1) == 0
    assert candidate([4, 6], 2) == 2
    assert candidate([7, 8], 2) == 15
    assert candidate([11, 7], 2) == 12
    assert candidate([2, 6], 1) == 0
    assert candidate([2, 3], 2) == 1
    assert candidate([6, 2], 1) == 0
    assert candidate([3, 7], 1) == 0
    assert candidate([12, 4], 2) == 8
    assert candidate([9, 2], 2) == 11
    assert candidate([6, 1], 1) == 0
    assert candidate([9, 7], 1) == 0
    assert candidate([6, 2], 1) == 0
    assert candidate([7, 2], 1) == 0
    assert candidate([9, 4], 1) == 0
    assert candidate([10, 6], 1) == 0
    assert candidate([11, 7], 1) == 0
    assert candidate([12, 8], 1) == 0
    assert candidate([8, 2], 1) == 0
    assert candidate([9, 1], 2) == 8
    assert candidate([4, 6], 1) == 0
    assert candidate([10, 1], 1) == 0
    assert candidate([9, 6], 1) == 0
    assert candidate([10, 8], 1) == 0

if __name__ == '__main__':
    check(pair_OR_Sum)