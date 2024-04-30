from case_MBPP_419 import count_Rotation


def check(candidate):
    assert candidate([3,2,1],3) == 1
    assert candidate([4,5,1,2,3],5) == 2
    assert candidate([7,8,9,1,2,3],6) == 3
    assert candidate([6, 7, 5], 4) == 2
    assert candidate([1, 5, 4], 6) == 2
    assert candidate([8, 4, 3], 4) == 1
    assert candidate([5, 7, 2], 2) == 0
    assert candidate([4, 2, 2], 7) == 1
    assert candidate([5, 6, 5], 8) == 2
    assert candidate([2, 1, 3], 1) == 0
    assert candidate([5, 7, 5], 7) == 2
    assert candidate([5, 3, 2], 8) == 1
    assert candidate([1, 1, 6], 1) == 0
    assert candidate([2, 1, 5], 5) == 1
    assert candidate([4, 6, 2], 8) == 2
    assert candidate([3, 4, 6], 3) == 0
    assert candidate([2, 2, 3], 3) == 0
    assert candidate([4, 4, 5], 3) == 0
    assert candidate([7, 4, 1], 5) == 1
    assert candidate([1, 7, 6], 7) == 2
    assert candidate([5, 5, 2], 8) == 2
    assert candidate([8, 5, 6], 8) == 1
    assert candidate([5, 1, 6], 7) == 1
    assert candidate([7, 3, 4], 3) == 1
    assert candidate([4, 2, 3], 5) == 1
    assert candidate([2, 1, 5], 1) == 0
    assert candidate([6, 3, 6], 4) == 1
    assert candidate([3, 1, 1], 5) == 1
    assert candidate([7, 1, 3], 5) == 1
    assert candidate([2, 7, 2], 1) == 0
    assert candidate([1, 3, 4], 1) == 0
    assert candidate([8, 5, 4], 1) == 0
    assert candidate([7, 6, 5], 4) == 1
    assert candidate([8, 2, 2], 4) == 1
    assert candidate([1, 2, 2], 3) == 0
    assert candidate([7, 2, 3], 7) == 1
    assert candidate([9, 10, 6, 1, 4], 7) == 2
    assert candidate([1, 10, 5, 3, 3], 3) == 2
    assert candidate([3, 3, 4, 5, 3], 5) == 4
    assert candidate([9, 5, 3, 4, 5], 7) == 1
    assert candidate([6, 8, 5, 1, 2], 5) == 2
    assert candidate([5, 9, 1, 4, 2], 10) == 2
    assert candidate([9, 9, 4, 5, 5], 6) == 2
    assert candidate([9, 9, 2, 1, 8], 6) == 2
    assert candidate([7, 9, 2, 3, 6], 2) == 0
    assert candidate([3, 4, 3, 5, 2], 9) == 2
    assert candidate([8, 5, 1, 1, 7], 2) == 1
    assert candidate([7, 6, 4, 7, 3], 3) == 1
    assert candidate([9, 9, 4, 7, 1], 6) == 2
    assert candidate([4, 1, 6, 7, 4], 4) == 1
    assert candidate([3, 1, 3, 5, 6], 10) == 1
    assert candidate([9, 2, 4, 7, 5], 7) == 1
    assert candidate([5, 4, 1, 3, 8], 10) == 1
    assert candidate([4, 7, 2, 6, 1], 10) == 2
    assert candidate([4, 4, 6, 3, 2], 4) == 3
    assert candidate([2, 4, 5, 4, 3], 10) == 3
    assert candidate([4, 9, 5, 6, 2], 5) == 2
    assert candidate([5, 9, 2, 5, 2], 4) == 2
    assert candidate([6, 6, 2, 7, 6], 6) == 2
    assert candidate([7, 9, 4, 1, 8], 4) == 2
    assert candidate([5, 5, 4, 3, 1], 9) == 2
    assert candidate([5, 5, 6, 1, 7], 9) == 3
    assert candidate([9, 9, 4, 4, 2], 2) == 0
    assert candidate([1, 1, 3, 5, 1], 10) == 4
    assert candidate([3, 6, 3, 2, 5], 7) == 2
    assert candidate([8, 7, 2, 5, 5], 2) == 1
    assert candidate([8, 6, 5, 3, 4], 5) == 1
    assert candidate([3, 1, 1, 6, 6], 10) == 1
    assert candidate([9, 8, 3, 1, 6], 3) == 1
    assert candidate([5, 4, 6, 6, 3, 8], 10) == 1
    assert candidate([4, 13, 9, 4, 7, 3], 10) == 2
    assert candidate([6, 11, 10, 6, 2, 6], 5) == 2
    assert candidate([6, 7, 8, 6, 3, 8], 4) == 3
    assert candidate([10, 9, 12, 2, 6, 2], 5) == 1
    assert candidate([4, 12, 5, 5, 2, 7], 11) == 2
    assert candidate([5, 7, 12, 2, 4, 2], 3) == 0
    assert candidate([2, 4, 14, 5, 7, 4], 1) == 0
    assert candidate([12, 4, 5, 4, 4, 1], 10) == 1
    assert candidate([2, 7, 8, 6, 5, 4], 8) == 3
    assert candidate([10, 13, 4, 1, 4, 7], 3) == 2
    assert candidate([5, 13, 13, 3, 2, 2], 4) == 3
    assert candidate([6, 8, 4, 3, 7, 4], 7) == 2
    assert candidate([5, 8, 4, 3, 5, 3], 1) == 0
    assert candidate([11, 9, 11, 5, 1, 2], 6) == 1
    assert candidate([12, 4, 9, 2, 3, 2], 8) == 1
    assert candidate([2, 8, 7, 3, 3, 2], 1) == 0
    assert candidate([9, 9, 8, 6, 3, 5], 9) == 2
    assert candidate([8, 7, 8, 3, 1, 8], 10) == 1
    assert candidate([9, 9, 11, 6, 1, 7], 5) == 3
    assert candidate([10, 12, 8, 5, 6, 7], 9) == 2
    assert candidate([8, 13, 10, 5, 7, 1], 6) == 2
    assert candidate([10, 8, 14, 3, 2, 2], 3) == 1
    assert candidate([5, 8, 14, 5, 6, 8], 5) == 3
    assert candidate([10, 9, 8, 2, 6, 3], 4) == 1
    assert candidate([5, 11, 4, 4, 3, 1], 5) == 2
    assert candidate([8, 11, 5, 2, 2, 2], 9) == 2
    assert candidate([2, 3, 5, 2, 3, 5], 11) == 3
    assert candidate([12, 10, 13, 1, 3, 2], 11) == 1
    assert candidate([4, 11, 8, 4, 5, 3], 5) == 2
    assert candidate([10, 7, 13, 1, 7, 2], 7) == 1
    assert candidate([4, 8, 5, 1, 1, 6], 7) == 2
    assert candidate([3, 13, 11, 5, 7, 2], 7) == 2

if __name__ == '__main__':
    check(count_Rotation)