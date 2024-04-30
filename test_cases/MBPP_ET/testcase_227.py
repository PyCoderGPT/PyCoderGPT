from case_MBPP_227 import multiple_to_single


def check(candidate):
    assert candidate([11, 33, 50])==113350
    assert candidate([-1,2,3,4,5,6])==-123456
    assert candidate([10,15,20,25])==10152025
    assert candidate([7, 36, 50]) == 73650
    assert candidate([13, 38, 48]) == 133848
    assert candidate([8, 29, 48]) == 82948
    assert candidate([12, 28, 48]) == 122848
    assert candidate([15, 32, 45]) == 153245
    assert candidate([15, 36, 46]) == 153646
    assert candidate([12, 37, 54]) == 123754
    assert candidate([11, 35, 46]) == 113546
    assert candidate([8, 32, 55]) == 83255
    assert candidate([12, 29, 47]) == 122947
    assert candidate([14, 37, 51]) == 143751
    assert candidate([9, 29, 50]) == 92950
    assert candidate([11, 38, 45]) == 113845
    assert candidate([8, 37, 51]) == 83751
    assert candidate([12, 33, 49]) == 123349
    assert candidate([12, 38, 49]) == 123849
    assert candidate([13, 37, 50]) == 133750
    assert candidate([7, 29, 47]) == 72947
    assert candidate([16, 31, 51]) == 163151
    assert candidate([13, 34, 55]) == 133455
    assert candidate([12, 38, 55]) == 123855
    assert candidate([6, 31, 52]) == 63152
    assert candidate([13, 38, 49]) == 133849
    assert candidate([9, 33, 55]) == 93355
    assert candidate([16, 29, 49]) == 162949
    assert candidate([14, 34, 53]) == 143453
    assert candidate([11, 30, 51]) == 113051
    assert candidate([11, 34, 47]) == 113447
    assert candidate([11, 29, 48]) == 112948
    assert candidate([14, 29, 49]) == 142949
    assert candidate([13, 38, 54]) == 133854
    assert candidate([9, 33, 53]) == 93353
    assert candidate([12, 30, 49]) == 123049
    assert candidate([0, 2, 3, 1, 7, 5]) == 23175
    assert candidate([-5, 1, 5, 6, 8, 3]) == -515683
    assert candidate([0, 6, 7, 3, 7, 3]) == 67373
    assert candidate([-3, 3, 7, 9, 8, 1]) == -337981
    assert candidate([-5, 2, 8, 1, 3, 3]) == -528133
    assert candidate([-4, 7, 7, 5, 1, 3]) == -477513
    assert candidate([-5, 4, 5, 4, 9, 10]) == -5454910
    assert candidate([1, 4, 4, 9, 5, 5]) == 144955
    assert candidate([-6, 3, 3, 3, 9, 3]) == -633393
    assert candidate([-1, 3, 7, 9, 5, 3]) == -137953
    assert candidate([-4, 6, 2, 7, 4, 11]) == -4627411
    assert candidate([1, 5, 4, 9, 9, 8]) == 154998
    assert candidate([-5, 7, 5, 2, 7, 4]) == -575274
    assert candidate([4, 5, 5, 4, 2, 7]) == 455427
    assert candidate([-1, 3, 5, 3, 2, 9]) == -135329
    assert candidate([-5, 7, 6, 3, 10, 3]) == -5763103
    assert candidate([2, 2, 4, 8, 1, 6]) == 224816
    assert candidate([-2, 3, 1, 7, 9, 8]) == -231798
    assert candidate([0, 4, 3, 4, 8, 11]) == 434811
    assert candidate([4, 7, 7, 1, 8, 6]) == 477186
    assert candidate([4, 2, 6, 3, 6, 5]) == 426365
    assert candidate([4, 7, 5, 2, 9, 2]) == 475292
    assert candidate([0, 4, 4, 3, 10, 9]) == 443109
    assert candidate([-1, 3, 2, 9, 6, 9]) == -132969
    assert candidate([-6, 2, 8, 2, 2, 10]) == -6282210
    assert candidate([-6, 1, 6, 6, 7, 9]) == -616679
    assert candidate([-4, 5, 7, 6, 9, 9]) == -457699
    assert candidate([-1, 1, 8, 1, 8, 10]) == -1181810
    assert candidate([4, 5, 6, 2, 7, 10]) == 4562710
    assert candidate([2, 5, 5, 1, 3, 6]) == 255136
    assert candidate([3, 7, 7, 7, 3, 1]) == 377731
    assert candidate([3, 2, 6, 1, 1, 1]) == 326111
    assert candidate([4, 4, 4, 9, 4, 5]) == 444945
    assert candidate([7, 13, 21, 27]) == 7132127
    assert candidate([6, 19, 22, 28]) == 6192228
    assert candidate([6, 14, 20, 25]) == 6142025
    assert candidate([14, 20, 22, 22]) == 14202222
    assert candidate([15, 12, 19, 24]) == 15121924
    assert candidate([8, 14, 18, 23]) == 8141823
    assert candidate([13, 16, 17, 20]) == 13161720
    assert candidate([15, 19, 18, 25]) == 15191825
    assert candidate([13, 12, 17, 24]) == 13121724
    assert candidate([7, 10, 16, 23]) == 7101623
    assert candidate([10, 18, 15, 23]) == 10181523
    assert candidate([10, 14, 25, 29]) == 10142529
    assert candidate([9, 20, 16, 22]) == 9201622
    assert candidate([9, 14, 17, 22]) == 9141722
    assert candidate([9, 12, 23, 20]) == 9122320
    assert candidate([10, 11, 20, 20]) == 10112020
    assert candidate([14, 13, 25, 29]) == 14132529
    assert candidate([5, 17, 22, 20]) == 5172220
    assert candidate([6, 16, 18, 21]) == 6161821
    assert candidate([10, 13, 17, 21]) == 10131721
    assert candidate([9, 12, 24, 26]) == 9122426
    assert candidate([10, 19, 17, 26]) == 10191726
    assert candidate([5, 19, 15, 20]) == 5191520
    assert candidate([8, 10, 24, 24]) == 8102424
    assert candidate([6, 14, 23, 26]) == 6142326
    assert candidate([6, 19, 21, 22]) == 6192122
    assert candidate([14, 15, 20, 30]) == 14152030
    assert candidate([6, 11, 15, 22]) == 6111522
    assert candidate([7, 18, 24, 29]) == 7182429
    assert candidate([5, 14, 19, 28]) == 5141928
    assert candidate([8, 14, 25, 26]) == 8142526
    assert candidate([15, 17, 18, 22]) == 15171822
    assert candidate([8, 20, 25, 23]) == 8202523

if __name__ == '__main__':
    check(multiple_to_single)