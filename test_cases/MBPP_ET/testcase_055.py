from case_MBPP_055 import kth_element


def check(candidate):
    assert candidate([12,3,5,7,19], 5, 2) == 3
    assert candidate([17,24,8,23], 4, 3) == 8
    assert candidate([16,21,25,36,4], 5, 4) == 36
    assert candidate([8, 1, 1, 2, 20], 3, 4) == 2
    assert candidate([16, 5, 3, 8, 18], 5, 3) == 3
    assert candidate([11, 4, 10, 12, 18], 3, 2) == 4
    assert candidate([9, 7, 2, 5, 15], 2, 5) == 15
    assert candidate([15, 1, 2, 7, 15], 3, 3) == 2
    assert candidate([8, 5, 2, 7, 18], 2, 1) == 8
    assert candidate([16, 2, 2, 5, 20], 2, 1) == 16
    assert candidate([12, 2, 10, 11, 17], 1, 5) == 17
    assert candidate([15, 7, 9, 3, 17], 3, 4) == 3
    assert candidate([17, 7, 4, 12, 15], 4, 3) == 4
    assert candidate([13, 4, 10, 9, 14], 3, 4) == 9
    assert candidate([17, 3, 6, 7, 14], 5, 1) == 17
    assert candidate([9, 1, 9, 4, 16], 2, 2) == 1
    assert candidate([14, 8, 8, 8, 19], 3, 4) == 8
    assert candidate([16, 1, 8, 12, 21], 1, 3) == 8
    assert candidate([17, 4, 8, 9, 21], 2, 5) == 21
    assert candidate([11, 4, 9, 3, 23], 4, 3) == 9
    assert candidate([17, 6, 8, 3, 14], 4, 5) == 14
    assert candidate([13, 1, 5, 5, 17], 2, 1) == 13
    assert candidate([10, 1, 10, 5, 19], 5, 5) == 19
    assert candidate([16, 4, 3, 12, 18], 3, 4) == 12
    assert candidate([16, 4, 2, 11, 14], 5, 4) == 11
    assert candidate([14, 8, 4, 8, 19], 3, 2) == 8
    assert candidate([10, 1, 9, 12, 15], 3, 4) == 12
    assert candidate([12, 6, 3, 6, 22], 4, 1) == 12
    assert candidate([9, 5, 8, 7, 23], 5, 3) == 8
    assert candidate([8, 7, 5, 12, 21], 1, 2) == 7
    assert candidate([11, 5, 10, 9, 15], 4, 5) == 15
    assert candidate([15, 7, 10, 4, 15], 5, 4) == 4
    assert candidate([10, 7, 10, 7, 14], 3, 1) == 10
    assert candidate([14, 2, 10, 7, 23], 3, 3) == 10
    assert candidate([9, 7, 6, 6, 24], 5, 4) == 6
    assert candidate([7, 3, 10, 3, 24], 2, 3) == 10
    assert candidate([18, 26, 6, 27], 3, 4) == 27
    assert candidate([17, 19, 4, 21], 2, 1) == 17
    assert candidate([15, 24, 10, 26], 1, 3) == 10
    assert candidate([21, 20, 5, 23], 1, 2) == 20
    assert candidate([14, 19, 5, 27], 3, 4) == 27
    assert candidate([21, 19, 13, 23], 3, 1) == 21
    assert candidate([17, 19, 3, 26], 2, 2) == 19
    assert candidate([12, 25, 6, 23], 1, 4) == 23
    assert candidate([19, 28, 10, 20], 4, 2) == 28
    assert candidate([22, 26, 4, 19], 4, 4) == 19
    assert candidate([14, 23, 11, 20], 4, 1) == 14
    assert candidate([12, 26, 13, 18], 1, 3) == 13
    assert candidate([17, 19, 12, 20], 4, 2) == 19
    assert candidate([16, 22, 4, 24], 4, 3) == 4
    assert candidate([20, 28, 7, 26], 3, 3) == 7
    assert candidate([17, 20, 3, 22], 3, 2) == 20
    assert candidate([14, 21, 12, 22], 2, 1) == 14
    assert candidate([18, 24, 11, 19], 4, 1) == 18
    assert candidate([17, 28, 8, 25], 2, 3) == 8
    assert candidate([16, 20, 7, 21], 1, 3) == 7
    assert candidate([20, 26, 5, 28], 3, 2) == 26
    assert candidate([19, 23, 5, 22], 4, 1) == 19
    assert candidate([21, 26, 6, 25], 4, 2) == 26
    assert candidate([17, 21, 3, 26], 3, 4) == 26
    assert candidate([16, 20, 11, 28], 2, 2) == 20
    assert candidate([17, 28, 9, 24], 3, 4) == 24
    assert candidate([17, 27, 4, 23], 1, 4) == 23
    assert candidate([12, 23, 8, 22], 4, 1) == 12
    assert candidate([20, 25, 9, 28], 3, 1) == 20
    assert candidate([13, 23, 10, 22], 3, 2) == 23
    assert candidate([21, 19, 11, 27], 4, 4) == 27
    assert candidate([12, 23, 13, 24], 4, 2) == 23
    assert candidate([13, 19, 4, 28], 2, 3) == 4
    assert candidate([16, 19, 30, 40, 4], 5, 1) == 16
    assert candidate([18, 23, 26, 33, 5], 1, 5) == 5
    assert candidate([18, 25, 23, 36, 6], 5, 5) == 6
    assert candidate([20, 16, 22, 31, 9], 1, 2) == 16
    assert candidate([21, 17, 30, 40, 9], 1, 2) == 17
    assert candidate([15, 17, 27, 36, 6], 5, 2) == 17
    assert candidate([12, 18, 20, 40, 7], 5, 3) == 20
    assert candidate([21, 25, 23, 37, 7], 1, 1) == 21
    assert candidate([16, 18, 22, 40, 9], 4, 2) == 18
    assert candidate([12, 26, 29, 39, 7], 3, 1) == 12
    assert candidate([14, 25, 22, 36, 1], 4, 5) == 1
    assert candidate([17, 16, 21, 32, 7], 4, 5) == 7
    assert candidate([12, 19, 21, 41, 9], 3, 5) == 9
    assert candidate([13, 21, 27, 34, 1], 3, 4) == 34
    assert candidate([13, 25, 20, 33, 4], 1, 4) == 33
    assert candidate([16, 22, 20, 32, 9], 4, 4) == 32
    assert candidate([13, 22, 27, 32, 9], 1, 3) == 27
    assert candidate([11, 26, 26, 37, 6], 2, 4) == 37
    assert candidate([17, 23, 28, 41, 7], 1, 2) == 23
    assert candidate([14, 19, 21, 31, 1], 5, 5) == 1
    assert candidate([21, 25, 22, 37, 9], 5, 1) == 21
    assert candidate([20, 16, 22, 39, 5], 4, 5) == 5
    assert candidate([17, 17, 28, 36, 9], 5, 4) == 36
    assert candidate([16, 24, 30, 39, 2], 2, 2) == 24
    assert candidate([16, 19, 22, 37, 1], 4, 5) == 1
    assert candidate([17, 24, 21, 33, 7], 2, 3) == 21
    assert candidate([21, 24, 23, 41, 5], 2, 5) == 5
    assert candidate([18, 16, 28, 39, 4], 4, 1) == 18
    assert candidate([20, 17, 29, 39, 6], 3, 3) == 29
    assert candidate([17, 17, 27, 40, 6], 1, 2) == 17
    assert candidate([18, 22, 30, 36, 5], 2, 1) == 18
    assert candidate([19, 17, 29, 32, 8], 1, 3) == 29
    assert candidate([15, 23, 23, 32, 8], 5, 1) == 15

if __name__ == '__main__':
    check(kth_element)