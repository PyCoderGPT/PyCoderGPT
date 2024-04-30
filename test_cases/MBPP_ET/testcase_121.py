from case_MBPP_121 import max_sum


def check(candidate):
    assert candidate([1, 15, 51, 45, 33, 100, 12, 18, 9], 9) == 194
    assert candidate([80, 60, 30, 40, 20, 10], 6) == 210
    assert candidate([2, 3 ,14, 16, 21, 23, 29, 30], 8) == 138
    assert candidate([1, 10, 51, 50, 31, 102, 15, 17, 4], 4) == 123
    assert candidate([1, 18, 49, 50, 37, 100, 13, 18, 4], 5) == 122
    assert candidate([2, 16, 49, 47, 38, 96, 15, 18, 7], 7) == 188
    assert candidate([3, 10, 55, 49, 38, 99, 17, 18, 7], 5) == 124
    assert candidate([6, 14, 56, 50, 38, 99, 17, 18, 12], 7) == 205
    assert candidate([3, 17, 50, 43, 29, 95, 16, 22, 5], 4) == 122
    assert candidate([3, 11, 50, 50, 31, 99, 12, 21, 7], 7) == 191
    assert candidate([6, 15, 48, 43, 37, 102, 7, 17, 11], 8) == 199
    assert candidate([6, 15, 47, 42, 38, 97, 7, 21, 4], 5) == 122
    assert candidate([6, 17, 51, 50, 37, 99, 8, 13, 12], 4) == 124
    assert candidate([6, 13, 56, 43, 35, 104, 14, 15, 10], 5) == 129
    assert candidate([2, 12, 56, 41, 32, 97, 17, 21, 14], 4) == 132
    assert candidate([4, 18, 56, 40, 32, 103, 13, 17, 13], 5) == 133
    assert candidate([2, 15, 54, 47, 37, 98, 10, 18, 6], 6) == 193
    assert candidate([2, 17, 53, 40, 31, 104, 16, 18, 13], 4) == 135
    assert candidate([1, 17, 54, 41, 34, 104, 10, 23, 12], 6) == 211
    assert candidate([6, 19, 49, 43, 37, 104, 9, 22, 10], 9) == 210
    assert candidate([2, 17, 47, 50, 32, 101, 7, 21, 4], 9) == 242
    assert candidate([6, 20, 46, 46, 32, 100, 12, 16, 14], 5) == 130
    assert candidate([3, 17, 47, 42, 29, 96, 14, 19, 13], 9) == 195
    assert candidate([4, 11, 49, 46, 29, 99, 7, 21, 11], 9) == 195
    assert candidate([4, 13, 56, 47, 35, 98, 13, 14, 11], 6) == 196
    assert candidate([5, 13, 46, 40, 34, 98, 16, 13, 12], 4) == 139
    assert candidate([6, 17, 53, 42, 28, 101, 11, 18, 11], 6) == 206
    assert candidate([4, 15, 56, 44, 29, 97, 8, 21, 14], 9) == 207
    assert candidate([1, 11, 55, 49, 30, 95, 16, 20, 8], 4) == 123
    assert candidate([4, 19, 56, 47, 35, 99, 17, 18, 11], 6) == 207
    assert candidate([5, 18, 52, 41, 35, 97, 10, 13, 7], 7) == 192
    assert candidate([1, 10, 47, 47, 32, 97, 7, 21, 9], 7) == 185
    assert candidate([2, 17, 56, 41, 36, 98, 17, 16, 14], 9) == 220
    assert candidate([1, 18, 52, 45, 33, 100, 7, 17, 4], 7) == 192
    assert candidate([3, 15, 53, 50, 37, 102, 17, 21, 6], 5) == 129
    assert candidate([4, 11, 48, 50, 29, 101, 11, 17, 7], 5) == 125
    assert candidate([76, 56, 34, 37, 21, 9], 5) == 123
    assert candidate([81, 61, 34, 42, 19, 6], 6) == 209
    assert candidate([83, 57, 33, 40, 16, 14], 4) == 103
    assert candidate([75, 60, 29, 44, 22, 7], 5) == 133
    assert candidate([80, 56, 29, 38, 21, 7], 5) == 122
    assert candidate([85, 65, 35, 44, 25, 11], 6) == 230
    assert candidate([78, 65, 32, 35, 19, 9], 3) == 78
    assert candidate([83, 58, 25, 45, 23, 11], 6) == 220
    assert candidate([79, 61, 27, 40, 24, 14], 6) == 218
    assert candidate([75, 64, 34, 41, 21, 8], 5) == 134
    assert candidate([85, 65, 35, 44, 18, 15], 3) == 85
    assert candidate([84, 58, 33, 43, 16, 15], 4) == 107
    assert candidate([84, 57, 31, 43, 22, 8], 6) == 214
    assert candidate([81, 55, 25, 39, 25, 13], 2) == 81
    assert candidate([82, 55, 27, 36, 21, 12], 6) == 206
    assert candidate([76, 55, 34, 42, 25, 7], 6) == 205
    assert candidate([84, 64, 27, 42, 23, 15], 3) == 84
    assert candidate([77, 59, 35, 36, 16, 9], 1) == 77
    assert candidate([80, 59, 28, 42, 23, 13], 3) == 80
    assert candidate([76, 64, 33, 37, 22, 13], 2) == 76
    assert candidate([83, 63, 30, 35, 22, 7], 5) == 127
    assert candidate([75, 57, 33, 39, 18, 7], 3) == 75
    assert candidate([78, 59, 28, 36, 23, 6], 2) == 78
    assert candidate([81, 63, 30, 39, 15, 7], 4) == 91
    assert candidate([81, 62, 34, 39, 17, 5], 2) == 81
    assert candidate([77, 63, 27, 40, 23, 7], 6) == 210
    assert candidate([77, 64, 27, 42, 19, 7], 5) == 132
    assert candidate([79, 64, 30, 44, 19, 13], 2) == 79
    assert candidate([76, 61, 33, 39, 17, 13], 4) == 102
    assert candidate([76, 57, 35, 36, 16, 9], 2) == 76
    assert candidate([82, 55, 30, 41, 16, 14], 5) == 126
    assert candidate([79, 62, 26, 41, 15, 15], 1) == 79
    assert candidate([75, 58, 27, 44, 23, 12], 4) == 106
    assert candidate([5, 2, 15, 19, 23, 19, 25, 29], 3) == 29
    assert candidate([5, 2, 12, 16, 16, 22, 33, 33], 5) == 33
    assert candidate([5, 3, 13, 20, 22, 28, 26, 26], 8) == 114
    assert candidate([3, 5, 16, 17, 21, 21, 26, 32], 3) == 32
    assert candidate([6, 3, 16, 16, 26, 26, 31, 31], 3) == 31
    assert candidate([2, 1, 11, 17, 19, 22, 29, 28], 7) == 128
    assert candidate([3, 8, 14, 13, 17, 24, 31, 26], 8) == 123
    assert candidate([3, 8, 15, 14, 22, 25, 28, 25], 7) == 126
    assert candidate([1, 6, 12, 19, 22, 21, 32, 29], 7) == 121
    assert candidate([2, 6, 10, 12, 17, 20, 27, 25], 8) == 119
    assert candidate([6, 4, 15, 13, 16, 18, 29, 29], 3) == 29
    assert candidate([7, 4, 9, 21, 20, 18, 25, 25], 7) == 75
    assert candidate([7, 5, 10, 14, 19, 18, 24, 32], 7) == 74
    assert candidate([1, 4, 11, 13, 17, 23, 24, 33], 8) == 126
    assert candidate([1, 5, 16, 15, 22, 27, 33, 32], 7) == 136
    assert candidate([1, 1, 14, 12, 20, 20, 34, 35], 3) == 35
    assert candidate([3, 3, 13, 17, 20, 18, 32, 28], 7) == 113
    assert candidate([4, 7, 18, 15, 22, 28, 25, 33], 8) == 112
    assert candidate([2, 4, 10, 20, 20, 24, 30, 26], 7) == 116
    assert candidate([3, 2, 11, 20, 26, 22, 34, 26], 4) == 60
    assert candidate([2, 8, 19, 12, 16, 19, 30, 25], 3) == 55
    assert candidate([4, 2, 9, 15, 20, 28, 32, 28], 4) == 60
    assert candidate([3, 6, 14, 14, 24, 20, 28, 32], 7) == 75
    assert candidate([5, 3, 14, 13, 16, 24, 30, 25], 5) == 55
    assert candidate([7, 6, 15, 21, 25, 27, 25, 34], 8) == 129
    assert candidate([2, 5, 19, 21, 19, 27, 24, 31], 5) == 66
    assert candidate([3, 1, 18, 12, 24, 20, 24, 25], 7) == 65
    assert candidate([6, 8, 9, 20, 16, 18, 24, 25], 7) == 81
    assert candidate([1, 1, 13, 12, 24, 20, 32, 27], 6) == 59
    assert candidate([6, 3, 13, 16, 22, 23, 25, 27], 3) == 27
    assert candidate([6, 8, 12, 13, 16, 20, 26, 31], 5) == 55
    assert candidate([4, 3, 11, 11, 22, 28, 28, 32], 5) == 37
    assert candidate([7, 1, 17, 15, 26, 28, 27, 26], 5) == 81

if __name__ == '__main__':
    check(max_sum)