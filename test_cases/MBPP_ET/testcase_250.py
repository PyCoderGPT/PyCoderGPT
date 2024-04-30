from case_MBPP_250 import max_subarray_product


def check(candidate):
    assert candidate([1, -2, -3, 0, 7, -8, -2]) == 112
    assert candidate([6, -3, -10, 0, 2]) == 180 
    assert candidate([-2, -40, 0, -2, -3]) == 80
    assert candidate([6, 1, 1, 1, 8, -4, -1]) == 192
    assert candidate([6, -1, 1, 2, 4, -12, 0]) == 576
    assert candidate([1, -7, -7, 3, 5, -4, -2]) == 5880
    assert candidate([1, -5, -4, 2, 4, -3, 3]) == 288
    assert candidate([3, 1, -2, 2, 11, -10, 1]) == 1320
    assert candidate([1, -4, -1, 3, 6, -5, -4]) == 1440
    assert candidate([5, -4, -7, 1, 12, -5, 3]) == 1680
    assert candidate([5, -7, -7, 3, 8, -5, -7]) == 205800
    assert candidate([4, -5, -4, 2, 2, -7, -2]) == 4480
    assert candidate([5, -2, -1, 2, 7, -7, -3]) == 2940
    assert candidate([1, 2, 1, 3, 3, -4, 1]) == 18
    assert candidate([2, -3, -1, 5, 4, -6, -7]) == 5040
    assert candidate([6, 3, -3, 5, 5, -3, -5]) == 4050
    assert candidate([5, -6, -6, 4, 7, -9, 3]) == 5040
    assert candidate([1, -1, -1, 4, 3, -7, 1]) == 84
    assert candidate([2, -3, -2, 4, 11, -4, 1]) == 528
    assert candidate([2, 2, -1, 5, 2, -12, -2]) == 480
    assert candidate([5, -3, -3, 3, 3, -4, -6]) == 9720
    assert candidate([2, -4, -5, 2, 4, -6, -6]) == 11520
    assert candidate([2, -6, 0, 1, 3, -9, 0]) == 3
    assert candidate([2, 3, 2, 3, 11, -3, 0]) == 396
    assert candidate([6, 0, -6, 3, 12, -12, -6]) == 2592
    assert candidate([5, -7, 0, 2, 11, -8, -1]) == 176
    assert candidate([1, 3, -6, 1, 9, -8, -2]) == 1296
    assert candidate([4, 2, -5, 1, 9, -12, -2]) == 4320
    assert candidate([4, -2, 1, 3, 9, -9, -4]) == 1944
    assert candidate([1, -5, -1, 5, 4, -6, 3]) == 360
    assert candidate([4, 0, -2, 1, 12, -11, -3]) == 396
    assert candidate([5, 2, -6, 3, 6, -6, -5]) == 6480
    assert candidate([2, -5, -1, 2, 7, -7, -5]) == 4900
    assert candidate([5, -4, -6, 1, 11, -9, 3]) == 1782
    assert candidate([2, -1, -5, 5, 3, -9, -6]) == 8100
    assert candidate([1, 0, -7, 1, 7, -12, -7]) == 588
    assert candidate([3, -1, -12, 4, 7]) == 1008
    assert candidate([2, 0, -11, 2, 1]) == 2
    assert candidate([10, 2, -12, 3, 5]) == 20
    assert candidate([10, 0, -5, 4, 2]) == 10
    assert candidate([9, -7, -12, 4, 1]) == 3024
    assert candidate([2, -5, -10, 2, 1]) == 200
    assert candidate([4, -5, -13, 2, 1]) == 520
    assert candidate([5, -8, -7, 3, 1]) == 840
    assert candidate([1, -4, -7, 3, 7]) == 588
    assert candidate([10, -8, -7, 3, 1]) == 1680
    assert candidate([9, -5, -13, 3, 5]) == 8775
    assert candidate([2, -8, -9, 2, 3]) == 864
    assert candidate([1, 2, -14, 2, 6]) == 12
    assert candidate([5, 2, -15, 2, 1]) == 10
    assert candidate([7, -3, -10, 4, 4]) == 3360
    assert candidate([6, -4, -13, 1, 4]) == 1248
    assert candidate([6, -3, -5, 4, 4]) == 1440
    assert candidate([8, -8, -5, 2, 2]) == 1280
    assert candidate([7, -8, -11, 1, 1]) == 616
    assert candidate([3, -3, -12, 3, 6]) == 1944
    assert candidate([3, -6, -13, 4, 4]) == 3744
    assert candidate([11, 2, -9, 3, 4]) == 22
    assert candidate([9, -7, -12, 3, 7]) == 15876
    assert candidate([8, 0, -7, 3, 5]) == 15
    assert candidate([4, 1, -14, 5, 6]) == 30
    assert candidate([10, -7, -5, 5, 5]) == 8750
    assert candidate([3, -5, -14, 4, 2]) == 1680
    assert candidate([11, -6, -9, 5, 2]) == 5940
    assert candidate([4, -2, -9, 3, 6]) == 1296
    assert candidate([5, -6, -10, 1, 5]) == 1500
    assert candidate([4, 1, -10, 2, 6]) == 12
    assert candidate([6, -3, -11, 3, 7]) == 4158
    assert candidate([3, -1, -15, 3, 6]) == 810
    assert candidate([2, -39, 1, 0, 2]) == 2
    assert candidate([0, -35, 5, -1, 0]) == 175
    assert candidate([-2, -45, 1, -1, -3]) == 270
    assert candidate([3, -38, 1, 3, -4]) == 1368
    assert candidate([-1, -40, 3, 3, -1]) == 360
    assert candidate([2, -45, 4, -6, -3]) == 2160
    assert candidate([-7, -43, 4, -2, -6]) == 14448
    assert candidate([-1, -43, 5, -6, -3]) == 3870
    assert candidate([2, -45, 2, 0, -6]) == 2
    assert candidate([-2, -36, 5, -1, 0]) == 360
    assert candidate([0, -37, 3, -6, 1]) == 666
    assert candidate([3, -38, 4, -4, -1]) == 1824
    assert candidate([-4, -45, 2, -5, -8]) == 14400
    assert candidate([0, -44, 1, -4, 2]) == 352
    assert candidate([-3, -44, 3, -2, -7]) == 5544
    assert candidate([-4, -35, 2, 1, 0]) == 280
    assert candidate([-7, -36, 5, -5, -2]) == 12600
    assert candidate([-3, -45, 4, -3, -8]) == 12960
    assert candidate([-3, -36, 5, -7, -4]) == 15120
    assert candidate([-2, -38, 3, 2, -6]) == 1368
    assert candidate([3, -40, 5, -1, -4]) == 600
    assert candidate([-3, -41, 5, -7, -8]) == 34440
    assert candidate([2, -39, 5, -5, -4]) == 1950
    assert candidate([0, -38, 5, 0, 0]) == 5
    assert candidate([-7, -40, 2, -2, -5]) == 5600
    assert candidate([2, -43, 1, -7, -7]) == 602
    assert candidate([-1, -45, 5, -2, 1]) == 450
    assert candidate([-5, -45, 1, -3, -8]) == 5400
    assert candidate([1, -37, 1, -4, 0]) == 148
    assert candidate([-1, -44, 2, -4, 0]) == 352
    assert candidate([-5, -35, 3, -4, -1]) == 2100
    assert candidate([-1, -36, 2, -6, -2]) == 864
    assert candidate([3, -38, 4, -2, 2]) == 1824

if __name__ == '__main__':
    check(max_subarray_product)