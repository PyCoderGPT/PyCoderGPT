from case_HE_122 import add_elements


def check(candidate):
    assert candidate([16, 26, 4, 94, 5, 10, 5, 12, 5], 5) == 145
    assert candidate([115, 17, 2, 4311, 1, 9, 5, 9, 14], 3) == 19
    assert candidate([113, 23, 5, 3725, 1, 1, 2, 9, 6], 8) == 41
    assert candidate([15, 19, 6, 90, 6, 2, 7, 13, 10], 9) == 168
    assert candidate([5, 0, -6, 40, 55, 72, 87, 92, 95], 7) == 253
    assert candidate([3], 4) == 3
    assert candidate([111, 118, 3, 3448, 7, 8], 1) == 0
    assert candidate([8, 21, 1, 91, 5, 10, 9, 10, 6], 7) == 145
    assert candidate([13, 18, 4, 92, 8, 2, 8, 6, 5], 5) == 135
    assert candidate([1], 3) == 1
    assert candidate([5], 1) == 5
    assert candidate([15, 20, 8, 91, 6, 2, 6, 11, 10], 8) == 159
    assert candidate([107, 120, 6, 4699, 7, 11], 4) == 6
    assert candidate([5, 1, -8, 40, 58, 73, 84, 86, 96], 8) == 339
    assert candidate([4], 3) == 4
    assert candidate([115, 18, 4, 3479, 9, 9, 11, 10, 5], 6) == 40
    assert candidate([16, 22, 1, 86, 10, 8, 7, 4, 10], 4) == 125
    assert candidate([2], 6) == 2
    assert candidate([6, 1, -3, 44, 59, 74, 86, 84, 95], 1) == 6
    assert candidate([113, 122, 2, 4948, 10, 3], 4) == 2
    assert candidate([6, 19, 8, 95, 7, 3, 6, 10, 14], 9) == 168
    assert candidate([115, 24, 6, 3856, 5, 1, 4, 12, 14], 9) == 66
    assert candidate([110, 16, 5, 4445, 7, 4, 6, 9, 12], 8) == 47
    assert candidate([14, 20, 7, 93, 5, 7, 11, 11, 6], 6) == 146
    assert candidate([10, 23, 2, 94, 5, 3, 11, 8, 8], 6) == 137
    assert candidate([116, 26, 8, 3200, 10, 9, 2, 10, 7], 2) == 26
    assert candidate([3, -5, -6, 37, 61, 74, 82, 87, 102], 4) == 29
    assert candidate([5, -3, -8, 43, 56, 73, 91, 83, 97], 2) == 2
    assert candidate([1, -6, -3, 38, 55, 73, 85, 86, 100], 7) == 243
    assert candidate([109, 16, 3, 4057, 7, 2, 9, 4, 9], 3) == 19
    assert candidate([4, 2, 2, 42, 57, 81, 86, 91, 94], 4) == 50
    assert candidate([4, 1, -8, 37, 55, 76, 83, 84, 99], 3) == -3
    assert candidate([3, -5, -6, 44, 58, 72, 90, 85, 102], 7) == 256
    assert candidate([116, 19, 2, 3934, 3, 5, 6, 13, 14], 6) == 29
    assert candidate([11, 24, 1, 92, 1, 4, 8, 13, 12], 1) == 11
    assert candidate([6, -6, -6, 41, 56, 73, 83, 83, 94], 1) == 6
    assert candidate([109, 117, 7, 3709, 10, 3], 3) == 7
    assert candidate([115, 122, 6, 4698, 10, 7], 5) == 16
    assert candidate([107, 124, 8, 4426, 5, 9], 6) == 22
    assert candidate([11, 19, 8, 92, 9, 8, 3, 3, 9], 5) == 139
    assert candidate([3, -2, -8, 39, 56, 76, 84, 85, 101], 5) == 88
    assert candidate([16, 22, 4, 91, 8, 7, 4, 11, 11], 2) == 38
    assert candidate([116, 18, 5, 3825, 7, 4, 5, 3, 12], 8) == 42
    assert candidate([4, 1, -5, 40, 61, 78, 82, 87, 101], 7) == 261
    assert candidate([15, 19, 3, 94, 9, 11, 4, 11, 11], 9) == 177
    assert candidate([110, 125, 4, 3428, 1, 4], 7) == 9
    assert candidate([107, 22, 1, 3540, 4, 1, 5, 7, 14], 7) == 33
    assert candidate([10, 19, 7, 91, 5, 8, 4, 7, 11], 8) == 151
    assert candidate([5], 3) == 5
    assert candidate([2, -1, -4, 44, 60, 74, 91, 89, 101], 3) == -3
    assert candidate([114, 124, 1, 3460, 8, 3], 2) == 0
    assert candidate([113, 126, 2, 4104, 10, 5], 2) == 0
    assert candidate([111, 116, 5, 4847, 10, 5], 6) == 20
    assert candidate([107, 121, 4, 3034, 8, 2], 5) == 12
    assert candidate([1], 1) == 1
    assert candidate([4], 2) == 4
    assert candidate([107, 17, 7, 3610, 4, 1, 10, 5, 12], 1) == 0
    assert candidate([106, 17, 3, 3544, 9, 1, 6, 3, 10], 7) == 36
    assert candidate([110, 20, 3, 4098, 10, 6, 6, 11, 8], 5) == 33
    assert candidate([14, 25, 2, 87, 7, 3, 5, 3, 4], 1) == 14
    assert candidate([14, 26, 5, 88, 8, 7, 6, 6, 4], 4) == 133
    assert candidate([10, 19, 5, 94, 4, 5, 9, 4, 6], 7) == 146
    assert candidate([106, 117, 3, 3468, 10, 3], 6) == 16
    assert candidate([3, -7, -7, 38, 61, 80, 92, 86, 95], 2) == -4
    assert candidate([13, 18, 4, 85, 9, 1, 9, 8, 5], 7) == 139
    assert candidate([6], 5) == 6
    assert candidate([114, 118, 1, 4249, 5, 5], 5) == 6
    assert candidate([2, -5, -3, 37, 59, 74, 87, 83, 97], 1) == 2
    assert candidate([2, -1, -3, 37, 62, 77, 91, 89, 103], 7) == 265
    assert candidate([5], 4) == 5
    assert candidate([1, 3, -4, 37, 59, 75, 92, 92, 102], 2) == 4
    assert candidate([3], 5) == 3
    assert candidate([11, 21, 8, 95, 3, 1, 6, 11, 13], 4) == 135
    assert candidate([15, 19, 1, 85, 5, 1, 10, 5, 12], 7) == 136
    assert candidate([114, 16, 3, 4584, 10, 10, 2, 6, 12], 2) == 16
    assert candidate([1, -3, -6, 43, 62, 76, 92, 89, 94], 6) == 173
    assert candidate([111, 119, 8, 3568, 6, 8], 5) == 14
    assert candidate([1], 2) == 1
    assert candidate([111, 21, 6, 3469, 8, 7, 8, 10, 13], 2) == 21
    assert candidate([10, 20, 5, 91, 1, 11, 3, 4, 11], 9) == 156
    assert candidate([9, 19, 2, 92, 8, 9, 8, 4, 10], 8) == 151
    assert candidate([107, 116, 1, 4894, 9, 7], 5) == 10
    assert candidate([113, 121, 5, 3008, 8, 7], 6) == 20
    assert candidate([114, 25, 5, 4395, 10, 6, 3, 9, 5], 9) == 63
    assert candidate([1], 6) == 1
    assert candidate([111, 26, 3, 3885, 5, 2, 2, 12, 13], 1) == 0
    assert candidate([2, -3, -1, 42, 53, 74, 89, 83, 97], 5) == 93
    assert candidate([2, -1, 2, 40, 57, 73, 91, 83, 97], 5) == 100
    assert candidate([114, 125, 6, 3912, 6, 9], 6) == 21
    assert candidate([116, 23, 3, 4041, 5, 7, 2, 12, 8], 8) == 52
    assert candidate([112, 24, 8, 3223, 5, 4, 12, 11, 8], 6) == 41
    assert candidate([113, 18, 2, 4442, 9, 9, 7, 8, 7], 9) == 60
    assert candidate([5], 6) == 5
    assert candidate([3], 6) == 3
    assert candidate([108, 125, 1, 4105, 6, 6], 5) == 7
    assert candidate([111,21,3,4000,5,6,7,8,9], 4) == 24
    assert candidate([6, 26, 5, 91, 6, 6, 9, 4, 4], 1) == 6
    assert candidate([3], 1) == 3
    assert candidate([111,121,3,4000,5,6], 2) == 0
    assert candidate([6, 1, -1, 46, 60, 80, 92, 85, 100], 6) == 192
    assert candidate([106, 125, 5, 3265, 3, 9], 7) == 17
    assert candidate([106, 16, 4, 3953, 2, 2, 11, 3, 14], 7) == 35
    assert candidate([8, 26, 8, 93, 2, 2, 3, 11, 9], 1) == 8
    assert candidate([107, 118, 5, 4283, 10, 8], 4) == 5
    assert candidate([115, 126, 8, 3915, 4, 3], 3) == 8
    assert candidate([116, 122, 7, 3025, 1, 2], 5) == 8
    assert candidate([4, -1, 0, 45, 56, 74, 82, 83, 101], 7) == 260
    assert candidate([113, 20, 1, 3134, 4, 5, 10, 10, 14], 4) == 21
    assert candidate([1], 1) == 1
    assert candidate([115, 19, 2, 3182, 9, 3, 8, 7, 10], 6) == 33
    assert candidate([6, -3, 2, 45, 57, 76, 84, 90, 97], 3) == 5
    assert candidate([5, 1, -8, 41, 61, 73, 86, 93, 99], 1) == 5
    assert candidate([15, 19, 5, 91, 6, 2, 3, 4, 13], 9) == 158
    assert candidate([111, 23, 1, 3668, 1, 9, 4, 7, 6], 9) == 51
    assert candidate([6], 2) == 6
    assert candidate([11,21,3,90,5,6,7,8,9], 4) == 125
    assert candidate([106, 121, 3, 3648, 8, 3], 2) == 0
    assert candidate([114, 17, 2, 4324, 9, 9, 8, 7, 10], 4) == 19
    assert candidate([111, 118, 7, 3502, 6, 4], 4) == 7
    assert candidate([2], 1) == 2
    assert candidate([114, 117, 6, 3409, 7, 9], 2) == 0
    assert candidate([6], 4) == 6
    assert candidate([1,-2,-3,41,57,76,87,88,99], 3) == -4
    assert candidate([6, 3, -2, 39, 58, 77, 87, 89, 94], 6) == 181

if __name__ == '__main__':
    check(add_elements)