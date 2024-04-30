from case_MBPP_016 import find_Max_Num


def check(candidate):
    assert candidate([1,2,3],3) == 321
    assert candidate([4,5,6,1],4) == 6541
    assert candidate([1,2,3,9],4) == 9321
    assert candidate([4, 3, 2], 3) == 432
    assert candidate([5, 1, 8], 2) == 85
    assert candidate([2, 2, 5], 1) == 5
    assert candidate([5, 7, 5], 1) == 7
    assert candidate([2, 2, 8], 3) == 822
    assert candidate([5, 1, 4], 1) == 5
    assert candidate([5, 1, 3], 2) == 53
    assert candidate([6, 3, 7], 3) == 763
    assert candidate([2, 4, 1], 2) == 42
    assert candidate([5, 2, 6], 1) == 6
    assert candidate([2, 3, 7], 1) == 7
    assert candidate([1, 3, 3], 3) == 331
    assert candidate([3, 1, 3], 1) == 3
    assert candidate([6, 7, 4], 1) == 7
    assert candidate([2, 5, 8], 1) == 8
    assert candidate([3, 4, 6], 3) == 643
    assert candidate([1, 7, 8], 2) == 87
    assert candidate([5, 7, 2], 2) == 75
    assert candidate([5, 6, 7], 3) == 765
    assert candidate([3, 4, 5], 1) == 5
    assert candidate([2, 7, 1], 3) == 721
    assert candidate([6, 1, 1], 2) == 61
    assert candidate([3, 3, 4], 2) == 43
    assert candidate([2, 5, 4], 1) == 5
    assert candidate([1, 1, 2], 2) == 21
    assert candidate([6, 4, 7], 2) == 76
    assert candidate([6, 4, 7], 2) == 76
    assert candidate([1, 3, 2], 2) == 32
    assert candidate([2, 2, 7], 2) == 72
    assert candidate([4, 2, 7], 1) == 7
    assert candidate([1, 4, 3], 3) == 431
    assert candidate([1, 1, 4], 3) == 411
    assert candidate([1, 3, 3], 2) == 33
    assert candidate([1, 9, 11, 5], 2) == 119
    assert candidate([1, 3, 1, 4], 2) == 43
    assert candidate([5, 8, 5, 3], 3) == 855
    assert candidate([4, 2, 8, 1], 4) == 8421
    assert candidate([2, 8, 11, 2], 3) == 1182
    assert candidate([2, 10, 10, 6], 1) == 10
    assert candidate([8, 3, 5, 5], 4) == 8553
    assert candidate([4, 1, 11, 5], 2) == 115
    assert candidate([4, 9, 7, 4], 3) == 974
    assert candidate([1, 10, 11, 2], 4) == 12021
    assert candidate([9, 7, 5, 2], 2) == 97
    assert candidate([3, 1, 6, 1], 2) == 63
    assert candidate([9, 7, 10, 3], 1) == 10
    assert candidate([3, 5, 3, 3], 4) == 5333
    assert candidate([2, 8, 9, 1], 3) == 982
    assert candidate([2, 1, 11, 3], 2) == 113
    assert candidate([5, 4, 3, 1], 3) == 543
    assert candidate([3, 6, 10, 2], 1) == 10
    assert candidate([8, 6, 10, 1], 1) == 10
    assert candidate([2, 8, 11, 2], 2) == 118
    assert candidate([1, 2, 7, 2], 3) == 722
    assert candidate([5, 7, 6, 1], 4) == 7651
    assert candidate([2, 10, 11, 3], 1) == 11
    assert candidate([5, 8, 10, 6], 3) == 1086
    assert candidate([6, 8, 6, 3], 1) == 8
    assert candidate([3, 4, 4, 2], 2) == 44
    assert candidate([7, 6, 8, 4], 4) == 8764
    assert candidate([4, 7, 11, 2], 2) == 117
    assert candidate([3, 4, 10, 5], 4) == 10543
    assert candidate([3, 8, 11, 4], 4) == 11843
    assert candidate([1, 6, 10, 5], 4) == 10651
    assert candidate([7, 7, 4, 4], 2) == 77
    assert candidate([2, 2, 4, 2], 1) == 4
    assert candidate([2, 5, 8, 5], 2) == 85
    assert candidate([6, 1, 5, 7], 3) == 765
    assert candidate([5, 2, 7, 12], 4) == 12752
    assert candidate([1, 1, 8, 7], 3) == 871
    assert candidate([3, 1, 4, 10], 2) == 104
    assert candidate([5, 2, 5, 11], 2) == 115
    assert candidate([5, 3, 4, 5], 1) == 5
    assert candidate([1, 1, 6, 7], 2) == 76
    assert candidate([3, 6, 5, 11], 4) == 11653
    assert candidate([5, 4, 2, 8], 2) == 85
    assert candidate([2, 5, 5, 6], 4) == 6552
    assert candidate([5, 5, 4, 4], 4) == 5544
    assert candidate([1, 7, 8, 7], 1) == 8
    assert candidate([6, 4, 2, 13], 4) == 13642
    assert candidate([5, 1, 4, 6], 2) == 65
    assert candidate([3, 2, 5, 7], 4) == 7532
    assert candidate([3, 1, 2, 14], 3) == 1432
    assert candidate([3, 6, 4, 9], 3) == 964
    assert candidate([3, 5, 6, 13], 3) == 1365
    assert candidate([4, 1, 4, 11], 4) == 11441
    assert candidate([4, 7, 7, 7], 2) == 77
    assert candidate([6, 1, 1, 10], 4) == 10611
    assert candidate([4, 3, 6, 12], 1) == 12
    assert candidate([1, 6, 3, 12], 1) == 12
    assert candidate([6, 2, 1, 10], 1) == 10
    assert candidate([3, 5, 3, 5], 4) == 5533
    assert candidate([6, 2, 5, 7], 3) == 765
    assert candidate([2, 2, 5, 6], 1) == 6
    assert candidate([6, 4, 3, 10], 2) == 106
    assert candidate([1, 2, 8, 10], 2) == 108
    assert candidate([2, 5, 5, 7], 3) == 755
    assert candidate([2, 7, 8, 4], 4) == 8742
    assert candidate([3, 6, 6, 5], 3) == 665

if __name__ == '__main__':
    check(find_Max_Num)