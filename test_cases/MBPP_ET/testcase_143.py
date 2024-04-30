from case_MBPP_143 import sum_even_and_even_index


def check(candidate):
    assert candidate([5, 6, 12, 1, 18, 8],6) == 30
    assert candidate([3, 20, 17, 9, 2, 10, 18, 13, 6, 18],10) == 26
    assert candidate([5, 6, 12, 1],4) == 12
    assert candidate([9, 9, 9, 3, 14, 4], 6) == 14
    assert candidate([7, 11, 17, 4, 23, 6], 6) == 0
    assert candidate([3, 9, 14, 2, 19, 6], 3) == 14
    assert candidate([3, 2, 12, 1, 21, 8], 5) == 12
    assert candidate([10, 7, 12, 5, 21, 5], 2) == 10
    assert candidate([6, 9, 14, 4, 13, 7], 1) == 6
    assert candidate([10, 4, 16, 5, 14, 12], 2) == 10
    assert candidate([4, 6, 16, 1, 23, 12], 1) == 4
    assert candidate([10, 3, 10, 4, 15, 10], 2) == 10
    assert candidate([4, 1, 13, 6, 21, 4], 1) == 4
    assert candidate([4, 5, 9, 2, 19, 13], 1) == 4
    assert candidate([1, 4, 15, 6, 18, 10], 4) == 0
    assert candidate([3, 8, 17, 4, 19, 11], 2) == 0
    assert candidate([2, 5, 10, 5, 23, 6], 3) == 12
    assert candidate([7, 6, 9, 4, 16, 3], 3) == 0
    assert candidate([9, 10, 8, 4, 22, 5], 4) == 8
    assert candidate([8, 3, 8, 4, 18, 5], 6) == 34
    assert candidate([2, 11, 15, 3, 22, 10], 2) == 2
    assert candidate([10, 4, 7, 6, 20, 13], 5) == 30
    assert candidate([1, 9, 7, 2, 23, 9], 3) == 0
    assert candidate([8, 2, 13, 5, 19, 11], 2) == 8
    assert candidate([2, 2, 7, 6, 14, 4], 3) == 2
    assert candidate([4, 2, 8, 4, 18, 12], 5) == 30
    assert candidate([4, 3, 9, 3, 18, 3], 3) == 4
    assert candidate([6, 5, 16, 5, 22, 12], 6) == 44
    assert candidate([7, 5, 7, 6, 20, 7], 4) == 0
    assert candidate([5, 5, 16, 6, 15, 10], 3) == 16
    assert candidate([8, 10, 11, 6, 19, 10], 1) == 8
    assert candidate([3, 3, 11, 1, 21, 9], 6) == 0
    assert candidate([2, 10, 17, 5, 19, 7], 5) == 2
    assert candidate([10, 8, 12, 6, 21, 8], 6) == 22
    assert candidate([3, 2, 9, 4, 20, 4], 6) == 20
    assert candidate([2, 2, 7, 3, 13, 9], 3) == 2
    assert candidate([7, 22, 13, 14, 3, 5, 14, 9, 11, 21], 8) == 14
    assert candidate([1, 21, 17, 5, 3, 10, 14, 14, 4, 13], 8) == 14
    assert candidate([4, 21, 18, 11, 6, 6, 15, 15, 3, 23], 7) == 28
    assert candidate([3, 18, 20, 14, 6, 13, 23, 11, 3, 17], 5) == 26
    assert candidate([1, 19, 12, 4, 5, 5, 21, 10, 11, 18], 7) == 12
    assert candidate([7, 20, 15, 11, 7, 12, 15, 11, 2, 19], 9) == 2
    assert candidate([2, 16, 22, 13, 3, 13, 23, 13, 10, 15], 9) == 34
    assert candidate([6, 16, 15, 12, 1, 9, 13, 13, 1, 23], 5) == 6
    assert candidate([5, 19, 22, 10, 1, 10, 15, 9, 4, 14], 10) == 26
    assert candidate([6, 24, 22, 6, 2, 12, 20, 12, 11, 14], 7) == 50
    assert candidate([2, 20, 12, 8, 2, 6, 23, 14, 9, 14], 8) == 16
    assert candidate([6, 22, 14, 13, 5, 14, 22, 14, 11, 21], 10) == 42
    assert candidate([3, 25, 13, 12, 1, 9, 21, 9, 11, 17], 8) == 0
    assert candidate([2, 25, 13, 8, 7, 10, 22, 11, 9, 16], 9) == 24
    assert candidate([1, 23, 14, 9, 7, 5, 16, 12, 3, 18], 7) == 30
    assert candidate([2, 15, 16, 14, 3, 14, 17, 9, 7, 21], 10) == 18
    assert candidate([2, 22, 22, 8, 4, 7, 23, 9, 5, 20], 6) == 28
    assert candidate([3, 18, 16, 11, 4, 11, 16, 9, 11, 22], 9) == 36
    assert candidate([3, 19, 14, 12, 2, 11, 17, 8, 6, 17], 7) == 16
    assert candidate([3, 18, 22, 7, 2, 8, 18, 15, 3, 13], 7) == 42
    assert candidate([4, 20, 13, 8, 6, 10, 16, 12, 6, 17], 6) == 10
    assert candidate([3, 23, 21, 8, 7, 5, 23, 8, 5, 20], 5) == 0
    assert candidate([7, 20, 15, 5, 4, 9, 16, 18, 11, 14], 9) == 20
    assert candidate([1, 20, 12, 14, 2, 11, 15, 8, 6, 23], 9) == 20
    assert candidate([3, 24, 13, 8, 2, 7, 15, 15, 1, 19], 10) == 2
    assert candidate([2, 18, 21, 5, 4, 11, 22, 13, 8, 13], 6) == 6
    assert candidate([1, 15, 17, 13, 7, 14, 15, 14, 2, 20], 10) == 2
    assert candidate([8, 21, 14, 12, 5, 5, 21, 9, 11, 16], 9) == 22
    assert candidate([4, 16, 19, 12, 1, 8, 18, 13, 10, 16], 10) == 32
    assert candidate([3, 18, 15, 8, 5, 14, 19, 18, 1, 17], 10) == 0
    assert candidate([5, 19, 13, 7, 7, 10, 17, 9, 1, 19], 7) == 0
    assert candidate([4, 22, 15, 13, 7, 8, 18, 18, 7, 23], 5) == 4
    assert candidate([3, 21, 14, 4, 2, 11, 17, 8, 7, 13], 5) == 16
    assert candidate([4, 3, 7, 3], 2) == 4
    assert candidate([1, 8, 16, 4], 4) == 16
    assert candidate([7, 2, 7, 2], 1) == 0
    assert candidate([3, 2, 10, 5], 2) == 0
    assert candidate([1, 3, 7, 6], 1) == 0
    assert candidate([2, 9, 11, 2], 2) == 2
    assert candidate([7, 6, 16, 6], 2) == 0
    assert candidate([4, 11, 13, 3], 1) == 4
    assert candidate([8, 2, 11, 6], 3) == 8
    assert candidate([1, 9, 17, 1], 4) == 0
    assert candidate([4, 7, 14, 5], 4) == 18
    assert candidate([6, 8, 17, 3], 3) == 6
    assert candidate([2, 1, 14, 5], 1) == 2
    assert candidate([7, 7, 15, 6], 2) == 0
    assert candidate([3, 3, 9, 6], 4) == 0
    assert candidate([6, 2, 8, 4], 3) == 14
    assert candidate([9, 7, 7, 1], 3) == 0
    assert candidate([3, 11, 11, 2], 1) == 0
    assert candidate([2, 6, 9, 5], 2) == 2
    assert candidate([4, 8, 15, 1], 2) == 4
    assert candidate([3, 2, 13, 4], 3) == 0
    assert candidate([5, 11, 13, 6], 4) == 0
    assert candidate([3, 4, 13, 3], 1) == 0
    assert candidate([3, 7, 7, 6], 4) == 0
    assert candidate([5, 10, 17, 6], 2) == 0
    assert candidate([2, 10, 17, 3], 3) == 2
    assert candidate([6, 6, 12, 3], 3) == 18
    assert candidate([7, 3, 8, 2], 4) == 8
    assert candidate([4, 9, 16, 5], 1) == 4
    assert candidate([9, 11, 17, 6], 4) == 0
    assert candidate([5, 10, 14, 6], 1) == 0
    assert candidate([8, 9, 7, 4], 2) == 8
    assert candidate([6, 9, 16, 5], 3) == 22

if __name__ == '__main__':
    check(sum_even_and_even_index)