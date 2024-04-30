from case_MBPP_280 import unique_product


def check(candidate):
    assert candidate([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
    assert candidate([1, 2, 3, 1,]) == 6
    assert candidate([7, 8, 9, 0, 1, 1]) == 0
    assert candidate([8, 17, 29, 43, 17, 49, 55, 45]) == 20567269800
    assert candidate([5, 25, 28, 35, 23, 48, 55, 37]) == 275213400000
    assert candidate([8, 21, 31, 36, 18, 45, 57, 35]) == 302971233600
    assert candidate([11, 22, 30, 41, 17, 55, 60, 40]) == 667949040000
    assert candidate([9, 15, 31, 44, 23, 55, 56, 45]) == 587001492000
    assert candidate([9, 16, 26, 44, 24, 55, 64, 42]) == 584509685760
    assert candidate([11, 17, 31, 41, 22, 54, 64, 36]) == 650558075904
    assert candidate([8, 18, 34, 44, 20, 50, 59, 42]) == 533820672000
    assert candidate([14, 19, 35, 44, 17, 45, 63, 42]) == 829189191600
    assert candidate([12, 16, 27, 43, 22, 54, 61, 35]) == 565389538560
    assert candidate([6, 22, 25, 39, 21, 51, 64, 39]) == 8821612800
    assert candidate([9, 17, 29, 38, 22, 50, 59, 44]) == 481471293600
    assert candidate([8, 16, 26, 40, 22, 55, 62, 41]) == 409453158400
    assert candidate([11, 25, 30, 44, 15, 48, 58, 39]) == 591196320000
    assert candidate([14, 21, 26, 36, 24, 52, 58, 40]) == 796756746240
    assert candidate([10, 22, 25, 37, 21, 49, 64, 42]) == 562871232000
    assert candidate([12, 19, 33, 41, 23, 50, 64, 37]) == 840063628800
    assert candidate([8, 15, 28, 38, 25, 51, 55, 40]) == 358142400000
    assert candidate([13, 19, 34, 40, 18, 54, 55, 43]) == 772206177600
    assert candidate([9, 23, 31, 42, 18, 51, 62, 45]) == 690284647080
    assert candidate([10, 23, 26, 42, 19, 46, 63, 35]) == 484028017200
    assert candidate([13, 15, 29, 39, 24, 55, 59, 42]) == 721393873200
    assert candidate([13, 24, 34, 43, 20, 48, 57, 43]) == 24960199680
    assert candidate([6, 18, 34, 35, 25, 49, 57, 43]) == 385878087000
    assert candidate([14, 20, 30, 44, 16, 48, 59, 44]) == 16747315200
    assert candidate([14, 18, 25, 43, 15, 52, 55, 38]) == 441621180000
    assert candidate([14, 25, 32, 45, 19, 46, 62, 41]) == 1119740832000
    assert candidate([9, 16, 31, 37, 18, 52, 59, 41]) == 373970742912
    assert candidate([8, 24, 34, 45, 19, 50, 64, 44]) == 785866752000
    assert candidate([14, 24, 33, 44, 19, 55, 63, 41]) == 1316881177920
    assert candidate([5, 21, 27, 36, 22, 55, 62, 37]) == 283292024400
    assert candidate([12, 23, 34, 38, 21, 50, 59, 35]) == 773180604000
    assert candidate([11, 25, 35, 41, 18, 50, 61, 39]) == 844931587500
    assert candidate([6, 2, 1, 1]) == 12
    assert candidate([3, 6, 1, 5]) == 90
    assert candidate([2, 4, 1, 3]) == 24
    assert candidate([6, 5, 2, 3]) == 180
    assert candidate([5, 4, 1, 1]) == 20
    assert candidate([2, 1, 3, 3]) == 6
    assert candidate([5, 6, 7, 1]) == 210
    assert candidate([3, 3, 3, 6]) == 18
    assert candidate([4, 3, 4, 6]) == 72
    assert candidate([6, 4, 6, 5]) == 120
    assert candidate([3, 1, 6, 1]) == 18
    assert candidate([6, 7, 5, 2]) == 420
    assert candidate([2, 3, 7, 1]) == 42
    assert candidate([5, 1, 1, 6]) == 30
    assert candidate([3, 4, 3, 1]) == 12
    assert candidate([4, 4, 1, 5]) == 20
    assert candidate([2, 1, 2, 6]) == 12
    assert candidate([1, 4, 2, 4]) == 8
    assert candidate([3, 4, 8, 6]) == 576
    assert candidate([3, 7, 3, 2]) == 42
    assert candidate([4, 6, 5, 4]) == 120
    assert candidate([4, 5, 7, 2]) == 280
    assert candidate([1, 1, 5, 5]) == 5
    assert candidate([3, 3, 3, 6]) == 18
    assert candidate([6, 6, 3, 1]) == 18
    assert candidate([4, 2, 5, 1]) == 40
    assert candidate([2, 2, 3, 1]) == 6
    assert candidate([6, 5, 4, 5]) == 120
    assert candidate([5, 3, 2, 2]) == 30
    assert candidate([4, 5, 4, 5]) == 20
    assert candidate([4, 7, 1, 2]) == 56
    assert candidate([3, 3, 3, 3]) == 3
    assert candidate([1, 7, 3, 4]) == 84
    assert candidate([5, 13, 11, 4, 2, 6]) == 34320
    assert candidate([2, 7, 9, 1, 2, 4]) == 504
    assert candidate([3, 13, 7, 1, 3, 2]) == 546
    assert candidate([11, 8, 10, 3, 1, 4]) == 10560
    assert candidate([4, 5, 9, 3, 4, 5]) == 540
    assert candidate([9, 12, 5, 5, 4, 5]) == 2160
    assert candidate([12, 4, 10, 1, 4, 2]) == 960
    assert candidate([6, 9, 13, 1, 3, 4]) == 8424
    assert candidate([2, 3, 6, 5, 1, 3]) == 180
    assert candidate([4, 6, 14, 2, 2, 1]) == 672
    assert candidate([6, 9, 12, 4, 3, 6]) == 7776
    assert candidate([10, 6, 4, 5, 5, 2]) == 2400
    assert candidate([4, 9, 4, 2, 4, 4]) == 72
    assert candidate([6, 10, 8, 1, 5, 4]) == 9600
    assert candidate([2, 4, 10, 2, 3, 1]) == 240
    assert candidate([6, 9, 10, 2, 4, 6]) == 4320
    assert candidate([10, 9, 12, 5, 4, 1]) == 21600
    assert candidate([12, 6, 4, 1, 5, 1]) == 1440
    assert candidate([8, 3, 4, 1, 5, 1]) == 480
    assert candidate([3, 10, 8, 3, 1, 1]) == 240
    assert candidate([7, 13, 14, 2, 2, 6]) == 15288
    assert candidate([8, 7, 4, 4, 1, 5]) == 1120
    assert candidate([2, 4, 10, 4, 6, 3]) == 1440
    assert candidate([8, 6, 6, 2, 4, 2]) == 384
    assert candidate([9, 9, 12, 5, 3, 1]) == 1620
    assert candidate([9, 13, 5, 4, 2, 5]) == 4680
    assert candidate([2, 7, 4, 4, 2, 4]) == 56
    assert candidate([4, 10, 8, 3, 5, 5]) == 4800
    assert candidate([5, 4, 11, 3, 4, 1]) == 660
    assert candidate([12, 8, 4, 4, 6, 4]) == 2304
    assert candidate([11, 10, 10, 2, 2, 3]) == 660
    assert candidate([12, 9, 11, 1, 4, 2]) == 9504
    assert candidate([5, 6, 4, 3, 5, 6]) == 360

if __name__ == '__main__':
    check(unique_product)