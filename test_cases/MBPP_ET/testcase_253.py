from case_MBPP_253 import max_product


def check(candidate):
    assert candidate([3, 100, 4, 5, 150, 6], 6) == 45000 
    assert candidate([4, 42, 55, 68, 80], 5) == 50265600
    assert candidate([10, 22, 9, 33, 21, 50, 41, 60], 8) == 21780000 
    assert candidate([8, 96, 2, 8, 154, 4], 6) == 118272
    assert candidate([7, 95, 8, 9, 155, 9], 3) == 665
    assert candidate([2, 105, 2, 10, 145, 1], 5) == 30450
    assert candidate([4, 104, 9, 9, 150, 3], 1) == 4
    assert candidate([4, 100, 5, 7, 149, 7], 1) == 4
    assert candidate([8, 103, 2, 4, 149, 2], 2) == 824
    assert candidate([3, 105, 4, 9, 150, 10], 4) == 315
    assert candidate([6, 98, 5, 5, 147, 5], 5) == 86436
    assert candidate([7, 100, 6, 10, 155, 8], 4) == 700
    assert candidate([5, 100, 5, 8, 150, 4], 5) == 75000
    assert candidate([1, 97, 6, 4, 155, 7], 5) == 15035
    assert candidate([2, 100, 6, 10, 153, 10], 6) == 30600
    assert candidate([8, 99, 1, 1, 145, 7], 3) == 792
    assert candidate([1, 95, 4, 10, 150, 1], 2) == 95
    assert candidate([7, 100, 3, 9, 147, 4], 6) == 102900
    assert candidate([8, 97, 4, 3, 145, 7], 1) == 8
    assert candidate([7, 96, 2, 2, 152, 5], 5) == 102144
    assert candidate([3, 100, 6, 7, 154, 8], 1) == 3
    assert candidate([4, 95, 3, 8, 148, 11], 3) == 380
    assert candidate([4, 101, 5, 8, 155, 11], 3) == 404
    assert candidate([1, 104, 4, 8, 145, 11], 4) == 104
    assert candidate([6, 103, 2, 2, 155, 7], 4) == 618
    assert candidate([5, 99, 8, 8, 155, 3], 2) == 495
    assert candidate([6, 105, 5, 4, 146, 3], 3) == 630
    assert candidate([1, 100, 2, 6, 153, 2], 5) == 15300
    assert candidate([7, 95, 1, 1, 148, 11], 1) == 7
    assert candidate([8, 97, 8, 2, 155, 3], 3) == 776
    assert candidate([2, 101, 4, 10, 151, 11], 3) == 202
    assert candidate([7, 101, 7, 3, 148, 3], 5) == 104636
    assert candidate([6, 95, 8, 1, 147, 7], 1) == 6
    assert candidate([4, 99, 5, 1, 148, 6], 3) == 396
    assert candidate([8, 100, 8, 6, 149, 8], 4) == 800
    assert candidate([5, 103, 2, 7, 145, 6], 4) == 515
    assert candidate([6, 45, 59, 70, 81], 3) == 15930
    assert candidate([7, 43, 51, 73, 77], 2) == 301
    assert candidate([1, 39, 52, 68, 82], 1) == 1
    assert candidate([8, 40, 58, 71, 84], 4) == 1317760
    assert candidate([6, 37, 60, 68, 80], 2) == 222
    assert candidate([6, 41, 53, 65, 80], 3) == 13038
    assert candidate([4, 44, 59, 69, 84], 4) == 716496
    assert candidate([9, 43, 59, 64, 79], 3) == 22833
    assert candidate([5, 42, 50, 66, 81], 4) == 693000
    assert candidate([4, 44, 53, 71, 85], 5) == 56294480
    assert candidate([7, 47, 56, 66, 78], 5) == 94846752
    assert candidate([9, 45, 51, 68, 82], 5) == 115172280
    assert candidate([9, 47, 51, 69, 82], 4) == 1488537
    assert candidate([8, 37, 58, 68, 77], 4) == 1167424
    assert candidate([1, 38, 60, 65, 78], 5) == 11559600
    assert candidate([3, 39, 54, 63, 78], 3) == 6318
    assert candidate([1, 44, 56, 67, 78], 5) == 12876864
    assert candidate([5, 39, 54, 65, 84], 5) == 57493800
    assert candidate([3, 46, 59, 65, 83], 4) == 529230
    assert candidate([1, 42, 54, 66, 85], 2) == 42
    assert candidate([6, 38, 59, 73, 77], 3) == 13452
    assert candidate([8, 42, 58, 72, 75], 2) == 336
    assert candidate([1, 40, 56, 69, 81], 1) == 1
    assert candidate([4, 40, 58, 63, 84], 3) == 9280
    assert candidate([5, 40, 59, 63, 75], 5) == 55755000
    assert candidate([4, 47, 60, 64, 78], 3) == 11280
    assert candidate([7, 43, 60, 68, 81], 3) == 18060
    assert candidate([9, 45, 53, 69, 79], 4) == 1481085
    assert candidate([6, 39, 53, 71, 75], 2) == 234
    assert candidate([2, 38, 54, 72, 77], 1) == 2
    assert candidate([5, 37, 51, 64, 75], 4) == 603840
    assert candidate([2, 41, 52, 67, 78], 2) == 82
    assert candidate([5, 38, 57, 65, 75], 2) == 190
    assert candidate([14, 18, 10, 37, 21, 45, 39, 61], 4) == 9324
    assert candidate([12, 22, 10, 37, 19, 45, 39, 58], 6) == 439560
    assert candidate([14, 24, 9, 34, 20, 47, 46, 65], 5) == 11424
    assert candidate([6, 24, 5, 34, 18, 48, 37, 55], 8) == 12925440
    assert candidate([14, 24, 5, 31, 18, 55, 45, 63], 5) == 10416
    assert candidate([9, 19, 5, 38, 20, 55, 36, 57], 3) == 171
    assert candidate([15, 18, 6, 31, 21, 48, 40, 55], 7) == 401760
    assert candidate([7, 24, 10, 30, 22, 47, 38, 58], 4) == 5040
    assert candidate([12, 19, 9, 30, 24, 53, 36, 56], 5) == 6840
    assert candidate([9, 19, 7, 34, 24, 55, 45, 62], 5) == 5814
    assert candidate([6, 23, 7, 38, 26, 54, 39, 59], 4) == 5244
    assert candidate([5, 19, 6, 38, 20, 54, 40, 55], 7) == 194940
    assert candidate([9, 22, 5, 32, 26, 49, 44, 61], 8) == 18938304
    assert candidate([11, 18, 13, 29, 20, 53, 43, 61], 8) == 18563886
    assert candidate([5, 20, 12, 37, 21, 45, 41, 58], 4) == 3700
    assert candidate([5, 27, 5, 30, 26, 46, 43, 56], 5) == 4050
    assert candidate([6, 20, 13, 30, 21, 52, 39, 63], 7) == 187200
    assert candidate([5, 26, 9, 29, 19, 49, 45, 65], 8) == 12007450
    assert candidate([12, 20, 10, 29, 22, 46, 38, 64], 7) == 320160
    assert candidate([13, 17, 9, 31, 24, 54, 45, 56], 3) == 221
    assert candidate([7, 23, 11, 30, 17, 48, 36, 56], 4) == 4830
    assert candidate([12, 23, 8, 28, 22, 54, 41, 58], 8) == 24204096
    assert candidate([5, 22, 9, 29, 18, 53, 40, 62], 8) == 10482340
    assert candidate([5, 19, 4, 35, 17, 55, 45, 63], 5) == 3325
    assert candidate([13, 17, 13, 28, 23, 47, 41, 60], 3) == 221
    assert candidate([8, 21, 12, 33, 25, 47, 37, 61], 5) == 5544
    assert candidate([12, 18, 9, 28, 20, 46, 40, 57], 5) == 6048
    assert candidate([8, 23, 4, 30, 19, 52, 39, 64], 7) == 287040
    assert candidate([6, 25, 10, 37, 24, 54, 41, 56], 5) == 5550
    assert candidate([5, 20, 14, 29, 19, 46, 36, 58], 5) == 2900
    assert candidate([11, 21, 9, 38, 22, 47, 44, 57], 6) == 412566
    assert candidate([8, 22, 8, 28, 26, 50, 39, 63], 3) == 176
    assert candidate([10, 22, 12, 29, 25, 46, 45, 62], 8) == 18195760

if __name__ == '__main__':
    check(max_product)