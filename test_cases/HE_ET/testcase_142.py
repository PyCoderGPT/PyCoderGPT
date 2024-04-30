from case_HE_142 import sum_squares


def check(candidate):
    assert candidate([-3, 2, 1, 2, 3, 5, 3, 2, -2]) == 51
    assert candidate([3, 4, 2]) == 15
    assert candidate([3, 6, 6, 2, 3, 1, 3, 3, 2]) == 73
    assert candidate([-56,-99,1,0,-2]) == 3030
    assert candidate([-1, -5, 21, 2, -10, 9, -5, 12, -13, -7, -7, 14, -17, 2, 10, 10, 14, 16, 8, 11]) == 162
    assert candidate([-54, -104, 5, 2, -5]) == 2696
    assert candidate([2, 4, 6, 2, 1, 1, 1, 3, 4]) == 88
    assert candidate([-1, 1, -1, -1, -3, 3, 1, -5, -1]) == -27
    assert candidate([1, -1, 22, -5, -13, 12, -2, 17, -14, -11, -3, 13, -18, 11, 15, 9, 17, 15, 2, 12]) == 645
    assert candidate([4, 6, 5]) == 27
    assert candidate([-17, -10, 3, 36, 37, 23, -17, 27, -36, 22, 0, 8, -21, 33, 39]) == 6919
    assert candidate([-6, -2, 15, 1, -15, 15, 2, 15, -10, -12, -8, 16, -9, 2, 18, 15, 14, 11, 4, 5]) == -1037
    assert candidate([6, 1, 1]) == 38
    assert candidate([-5, 4, -2, 4, 0, 2, 4, -1, 0]) == 60
    assert candidate([-55, -98, 3, 4, -6]) == 2730
    assert candidate([-5, 1, 13, 4, -19, 9, 0, 19, -16, -10, -7, 16, -14, 8, 15, 12, 11, 18, 1, 6]) == -9044
    assert candidate([4, 0, 4, 4, -7]) == -307
    assert candidate([1, 3, 2, 1, 4, 2, 1, 6, 1]) == 81
    assert candidate([6, 7, 1]) == 44
    assert candidate([-2, 5, 1, 4, 2, 1, 5, 2, 4]) == 126
    assert candidate([2, 3, 3]) == 10
    assert candidate([0, -6, 14, 4, -16, 14, 4, 11, -13, -9, -5, 15, -18, 10, 18, 7, 13, 14, 9, 9]) == -3435
    assert candidate([5, 6, 4, 4, 4, 6, 6, 3, 2]) == 168
    assert candidate([-56, -96, 1, 5, 0]) == 3066
    assert candidate([-19, -8, 2, 33, 37, 31, -24, 29, -39, 22, -8, 17, -23, 34, 35]) == -5495
    assert candidate([-1,-5,2,-1,-5]) == -126
    assert candidate([3, 4, 3, 4, 3, 4, 1, 2, 4]) == 130
    assert candidate([-3, -6, 0, 1, -2, 3, 4, 1, -4]) == -48
    assert candidate([-59, -96, 3, 4, 1]) == 3405
    assert candidate([-1, -6, -5, -3, -3, 4, -3, -6, -1]) == -22
    assert candidate([-60, -95, 1, 5, -3]) == 3504
    assert candidate([-1,0,0,0,0,0,0,0,-1]) == 0
    assert candidate([3, 3, 7]) == 19
    assert candidate([1,1,1,1,1,1,1,1,1]) == 9
    assert candidate([3, -8, 6, -1, -10]) == -992
    assert candidate([]) == 0
    assert candidate([-1, 5, 3, 4, 1, 3, 2, 2, 1]) == 36
    assert candidate([4, 1, 13]) == 30
    assert candidate([4, 5, 4, 4, 4, 1, 2, 3, 3]) == 140
    assert candidate([2, 0, 22, 0, -15, 15, -2, 13, -12, -14, -5, 13, -10, 2, 16, 11, 18, 15, 5, 8]) == 1278
    assert candidate([3, 3, -4, 2, -2, -6, -2, -1, 3]) == 28
    assert candidate([-18, -14, 0, 34, 33, 25, -21, 22, -39, 21, -5, 11, -28, 33, 34]) == -20130
    assert candidate([0, -7, 4, -3, -1]) == 5
    assert candidate([4, 3, 5]) == 24
    assert candidate([-5, 5, 1, 3, 4, 4, 5, 3, 0]) == 136
    assert candidate([0]) == 0
    assert candidate([-16, -4, -7, 31, 33, 23, -23, 25, -38, 21, -8, 15, -25, 32, 39]) == -16008
    assert candidate([3, 5, 10]) == 24
    assert candidate([-4, 0, 3, 0, -2]) == 11
    assert candidate([-4, -10, 6, -4, -7]) == -315
    assert candidate([-1,-1,-1,-1,-1,-1,-1,-1,-1]) == -3
    assert candidate([-11, -6, -7, 41, 36, 23, -18, 29, -39, 23, -5, 9, -31, 36, 36]) == -8932
    assert candidate([4, -5, 22, 4, -14, 10, -4, 16, -12, -16, -2, 15, -17, 6, 17, 15, 14, 16, 3, 7]) == -799
    assert candidate([2, 1, 1, 2, 5, 3, 2, 2, 3]) == 171
    assert candidate([1, -4, -3, -5, 1, 3, -2, -1, -6]) == -190
    assert candidate([-17, -13, -6, 33, 37, 23, -25, 26, -38, 25, -2, 16, -31, 38, 39]) == -509
    assert candidate([-4, 5, 3, 3, 1, 4, 1, 5, -5]) == -81
    assert candidate([1, 3, 2]) == 6
    assert candidate([3, -1, 18, -1, -12, 11, 2, 17, -13, -9, -4, 19, -10, 8, 13, 9, 11, 16, 1, 9]) == -2211
    assert candidate([-1, -5, 7, -3, -6]) == -204
    assert candidate([-15, -8, -6, 37, 34, 31, -22, 27, -42, 16, -3, 16, -27, 30, 35]) == -31599
    assert candidate([1, 0, -2, 3, -6, -2, -3, 4, 4]) == -133
    assert candidate([2, -2, 1, 4, -10]) == -981
    assert candidate([-3, -5, 3, -6, -6]) == -173
    assert candidate([4, 4, 1, 5, 6, 3, 5, 6, 4]) == 360
    assert candidate([4, 1, 5]) == 22
    assert candidate([-6, 2, 5, 4, 2, 1, 3, 5, -5]) == -43
    assert candidate([3, 0, 19, 0, -14, 16, -3, 19, -10, -16, -3, 15, -9, 2, 16, 12, 12, 12, 5, 15]) == -1381
    assert candidate([-4, 2, 3, 2, 2, 4, 3, 5, 2]) == 59
    assert candidate([5, 6, 8]) == 39
    assert candidate([1, 4, 5, 5, 3, 2, 5, 3, 4]) == 156
    assert candidate([4, 4, 5, 5, 2, 6, 1, 5, 1]) == 71
    assert candidate([1,4,9]) == 14
    assert candidate([1, 1, 5]) == 7
    assert candidate([-51, -102, 5, 1, -5]) == 2380
    assert candidate([5, 7, 14]) == 46
    assert candidate([5, 9, 10]) == 44
    assert candidate([-20, -9, -7, 38, 38, 28, -17, 23, -40, 17, -7, 7, -22, 34, 36]) == -6117
    assert candidate([-17, -6, -1, 36, 37, 28, -16, 27, -43, 15, -6, 11, -29, 38, 39]) == -25817
    assert candidate([-60, -104, 4, 3, 3]) == 3536
    assert candidate([-58, -98, 6, 2, 3]) == 3303
    assert candidate([0, 1, -1, 0, -6, -1, 4, 3, -1]) == -199
    assert candidate([4]) == 16
    assert candidate([-16, -9, -2, 36, 36, 26, -20, 25, -40, 20, -4, 12, -26, 35, 37]) == -14196
    assert candidate([-11, -6, -4, 37, 32, 25, -23, 28, -35, 20, -3, 17, -22, 31, 40]) == -7076
    assert candidate([1, 4, 1, 6, 3, 3, 4, 5, 4]) == 157
    assert candidate([-5, 0, 7, -2, 0]) == 36
    assert candidate([4, 6, 4, 5, 6, 1, 4, 3, 6]) == 503
    assert candidate([3, 4, 6]) == 19
    assert candidate([1,2,3]) == 6
    assert candidate([2, 1, 4, 5, 3, 3, 5, 2, 1]) == 92
    assert candidate([3, -7, 15, -2, -10, 18, 1, 18, -14, -10, 0, 19, -12, 1, 18, 9, 17, 13, 7, 9]) == 1661
    assert candidate([5]) == 25
    assert candidate([-4, -5, 2, 2, -2, -3, -5, -2, -5]) == -96
    assert candidate([4, 3, 6, 5, 1, 4, 1, 4, 1]) == 61
    assert candidate([2]) == 4
    assert candidate([-56, -97, 4, 5, -7]) == 2725
    assert candidate([6, 3, 4, 3, 4, 3, 2, 1, 1]) == 125
    assert candidate([-5, -5, -3, -5, 4, 3, 3, 3, -1]) == 120
    assert candidate([-2, 1, 2, 5, 4, 3, 2, 2, -4]) == 41
    assert candidate([2, 1, 6]) == 11
    assert candidate([-3, -9, 2, -5, -4]) == -37
    assert candidate([5, 2, 5]) == 32
    assert candidate([-53, -94, 3, 2, -1]) == 2721
    assert candidate([5, 3, 9]) == 37
    assert candidate([2, -2, 14, -6, -19, 13, -5, 12, -11, -13, -3, 11, -19, 1, 14, 9, 16, 18, 9, 5]) == -3254
    assert candidate([-21, -6, -5, 40, 34, 21, -25, 23, -44, 16, -8, 13, -27, 33, 37]) == -42121
    assert candidate([3, 5, 5]) == 19
    assert candidate([3, 9, 13]) == 31
    assert candidate([0, 0, 14, 3, -11, 8, -3, 11, -10, -13, -5, 18, -18, 7, 10, 9, 15, 20, 5, 8]) == 1752
    assert candidate([1, 4, 1, -2, -4, 3, -1, -6, -6]) == -272
    assert candidate([-5, -8, 6, -6, -6]) == -157
    assert candidate([-12, -4, -2, 33, 37, 23, -20, 26, -39, 24, -6, 17, -24, 35, 37]) == -5755
    assert candidate([-52, -101, 6, 1, -7]) == 2267
    assert candidate([4, -3, 7, -3, -9]) == -700
    assert candidate([-58, -103, 5, 3, 0]) == 3275
    assert candidate([5, 7, 13]) == 45
    assert candidate([5, 2, 1]) == 28
    assert candidate([-1, -3, 17, -1, -15, 13, -1, 14, -14, -12, -5, 14, -14, 6, 13, 11, 16, 16, 4, 10]) == -1448
    
    
    # Don't remove this line:
    assert candidate([-1, 4, 4, 5, 2, 1, 3, 4, 3]) == 83
    assert candidate([2, 3, -1, 1, 0, -5, 3, 4, 1]) == 16
    assert candidate([3]) == 9

if __name__ == '__main__':
    check(sum_squares)