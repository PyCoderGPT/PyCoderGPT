from case_MBPP_396 import find_Sum


def check(candidate):
    assert candidate([1,2,3,1,1,4,5,6],8) == 21
    assert candidate([1,10,9,4,2,10,10,45,4],9) == 71
    assert candidate([12,10,9,45,2,10,10,45,10],9) == 78
    assert candidate([4, 5, 5, 2, 5, 5, 5, 4], 8) == 11
    assert candidate([1, 6, 7, 2, 3, 6, 10, 2], 3) == 3
    assert candidate([4, 1, 8, 3, 1, 2, 4, 10], 3) == 3
    assert candidate([5, 5, 6, 2, 3, 8, 4, 2], 5) == 14
    assert candidate([2, 5, 8, 3, 6, 6, 10, 7], 6) == 23
    assert candidate([2, 1, 3, 4, 4, 5, 8, 2], 8) == 23
    assert candidate([6, 3, 5, 6, 5, 6, 1, 2], 7) == 17
    assert candidate([1, 2, 3, 3, 6, 6, 10, 2], 6) == 12
    assert candidate([3, 2, 2, 2, 4, 2, 4, 1], 4) == 3
    assert candidate([1, 1, 4, 6, 3, 6, 10, 7], 6) == 14
    assert candidate([4, 2, 8, 6, 6, 8, 8, 10], 3) == 12
    assert candidate([5, 1, 5, 6, 1, 8, 10, 6], 4) == 6
    assert candidate([2, 6, 8, 2, 6, 3, 8, 2], 4) == 5
    assert candidate([5, 3, 1, 6, 4, 4, 10, 7], 8) == 36
    assert candidate([1, 2, 3, 4, 4, 3, 6, 5], 4) == 6
    assert candidate([5, 7, 3, 6, 2, 7, 5, 11], 3) == 10
    assert candidate([2, 5, 7, 2, 2, 8, 9, 8], 7) == 22
    assert candidate([3, 4, 2, 1, 3, 5, 3, 2], 4) == 6
    assert candidate([3, 2, 1, 5, 2, 9, 1, 3], 3) == 3
    assert candidate([5, 6, 1, 4, 1, 9, 4, 8], 3) == 5
    assert candidate([4, 3, 1, 5, 5, 1, 7, 2], 3) == 3
    assert candidate([2, 3, 2, 2, 5, 5, 9, 11], 3) == 2
    assert candidate([3, 6, 4, 5, 6, 7, 8, 6], 6) == 18
    assert candidate([6, 3, 5, 3, 1, 8, 3, 10], 5) == 9
    assert candidate([1, 7, 8, 6, 4, 4, 10, 1], 6) == 18
    assert candidate([5, 7, 8, 5, 2, 6, 3, 10], 6) == 23
    assert candidate([5, 7, 3, 6, 4, 7, 3, 7], 7) == 25
    assert candidate([4, 4, 7, 2, 3, 6, 4, 6], 5) == 9
    assert candidate([2, 7, 2, 4, 2, 7, 1, 2], 8) == 14
    assert candidate([2, 5, 7, 4, 3, 1, 10, 2], 8) == 32
    assert candidate([5, 1, 1, 4, 4, 9, 4, 6], 6) == 10
    assert candidate([1, 6, 5, 1, 6, 9, 8, 8], 7) == 20
    assert candidate([6, 6, 3, 6, 1, 7, 6, 5], 6) == 15
    assert candidate([5, 6, 10, 1, 4, 11, 5, 46, 9], 8) == 46
    assert candidate([5, 11, 8, 3, 2, 6, 11, 49, 1], 7) == 36
    assert candidate([6, 12, 10, 9, 2, 10, 8, 46, 5], 9) == 98
    assert candidate([1, 10, 14, 3, 2, 7, 7, 44, 8], 6) == 21
    assert candidate([5, 6, 14, 9, 3, 11, 13, 50, 5], 6) == 34
    assert candidate([6, 12, 12, 7, 3, 14, 5, 45, 8], 8) == 55
    assert candidate([2, 7, 13, 2, 4, 7, 14, 47, 3], 8) == 43
    assert candidate([2, 5, 12, 6, 7, 10, 12, 42, 9], 6) == 39
    assert candidate([1, 6, 4, 9, 7, 7, 8, 40, 8], 6) == 26
    assert candidate([5, 10, 14, 9, 3, 13, 9, 40, 3], 5) == 17
    assert candidate([6, 8, 14, 1, 7, 11, 10, 45, 6], 8) == 57
    assert candidate([1, 13, 11, 2, 3, 7, 15, 48, 5], 8) == 57
    assert candidate([2, 7, 4, 7, 4, 8, 8, 46, 1], 4) == 7
    assert candidate([3, 10, 12, 3, 2, 6, 13, 42, 2], 7) == 33
    assert candidate([6, 13, 13, 8, 3, 13, 11, 41, 7], 8) == 48
    assert candidate([1, 15, 13, 7, 3, 12, 11, 46, 8], 4) == 19
    assert candidate([3, 8, 12, 9, 2, 5, 6, 49, 3], 6) == 24
    assert candidate([1, 8, 7, 6, 3, 7, 6, 49, 4], 6) == 21
    assert candidate([4, 13, 10, 6, 7, 10, 7, 42, 4], 9) == 82
    assert candidate([5, 8, 7, 5, 4, 15, 6, 44, 7], 4) == 15
    assert candidate([1, 6, 5, 5, 6, 14, 8, 41, 5], 7) == 20
    assert candidate([2, 10, 8, 8, 3, 9, 14, 50, 7], 4) == 20
    assert candidate([4, 8, 8, 2, 4, 10, 12, 49, 9], 4) == 14
    assert candidate([5, 14, 9, 4, 2, 5, 15, 48, 1], 6) == 21
    assert candidate([1, 10, 7, 8, 4, 5, 9, 46, 7], 7) == 34
    assert candidate([3, 14, 4, 9, 5, 9, 7, 41, 7], 4) == 19
    assert candidate([6, 9, 11, 8, 4, 14, 8, 47, 2], 6) == 29
    assert candidate([2, 13, 10, 8, 1, 10, 15, 43, 3], 8) == 52
    assert candidate([3, 6, 7, 2, 6, 11, 15, 45, 3], 6) == 18
    assert candidate([5, 9, 7, 3, 7, 5, 8, 41, 5], 7) == 23
    assert candidate([1, 5, 12, 5, 6, 7, 10, 43, 2], 4) == 8
    assert candidate([6, 5, 4, 7, 3, 12, 12, 40, 6], 8) == 37
    assert candidate([3, 8, 9, 4, 7, 7, 7, 46, 7], 6) == 14
    assert candidate([14, 5, 10, 41, 7, 5, 5, 43, 13], 9) == 133
    assert candidate([12, 14, 12, 50, 7, 5, 6, 43, 14], 9) == 137
    assert candidate([12, 8, 10, 40, 3, 12, 12, 49, 13], 4) == 33
    assert candidate([15, 13, 5, 49, 2, 12, 12, 50, 6], 5) == 25
    assert candidate([17, 6, 5, 42, 4, 15, 9, 41, 14], 7) == 70
    assert candidate([13, 10, 9, 46, 6, 11, 11, 47, 12], 6) == 48
    assert candidate([10, 11, 5, 44, 3, 11, 13, 46, 6], 5) == 35
    assert candidate([12, 7, 7, 47, 1, 12, 12, 44, 6], 5) == 26
    assert candidate([11, 6, 12, 42, 6, 12, 12, 42, 9], 4) == 26
    assert candidate([9, 7, 10, 44, 3, 5, 7, 42, 10], 6) == 34
    assert candidate([12, 13, 13, 43, 1, 8, 7, 47, 15], 8) == 99
    assert candidate([16, 8, 9, 48, 3, 6, 12, 44, 10], 4) == 26
    assert candidate([17, 8, 12, 50, 3, 9, 12, 45, 8], 5) == 32
    assert candidate([14, 13, 11, 46, 7, 5, 8, 41, 10], 8) == 109
    assert candidate([11, 9, 5, 47, 6, 7, 10, 49, 8], 7) == 56
    assert candidate([12, 15, 7, 41, 6, 15, 12, 40, 15], 8) == 80
    assert candidate([14, 9, 4, 44, 5, 10, 7, 41, 9], 9) == 134
    assert candidate([7, 5, 6, 41, 3, 12, 8, 50, 6], 4) == 14
    assert candidate([7, 6, 8, 50, 2, 7, 11, 47, 14], 9) == 145
    assert candidate([16, 15, 13, 48, 7, 9, 5, 50, 8], 4) == 29
    assert candidate([12, 5, 9, 50, 5, 9, 13, 41, 5], 9) == 130
    assert candidate([11, 14, 6, 43, 3, 7, 6, 45, 12], 6) == 39
    assert candidate([13, 12, 6, 42, 7, 7, 12, 48, 9], 8) == 89
    assert candidate([17, 14, 7, 48, 3, 5, 10, 48, 14], 8) == 104
    assert candidate([7, 9, 13, 47, 7, 14, 15, 49, 13], 6) == 43
    assert candidate([13, 5, 12, 46, 1, 10, 13, 43, 6], 7) == 47
    assert candidate([7, 13, 5, 49, 2, 7, 14, 43, 8], 7) == 49
    assert candidate([9, 5, 6, 49, 7, 15, 14, 47, 7], 5) == 27
    assert candidate([8, 15, 13, 43, 3, 13, 13, 42, 6], 9) == 130
    assert candidate([12, 14, 10, 47, 6, 12, 8, 43, 15], 5) == 36
    assert candidate([17, 5, 6, 50, 3, 11, 5, 42, 13], 9) == 147
    assert candidate([8, 7, 10, 40, 4, 11, 12, 46, 15], 8) == 107
    assert candidate([15, 14, 10, 48, 7, 13, 8, 47, 11], 7) == 78

if __name__ == '__main__':
    check(find_Sum)