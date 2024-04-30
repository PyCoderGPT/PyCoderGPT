from case_HE_035 import max_element


def check(candidate):
    assert candidate([5, 2, -8, 4, 2, 3, 12, 4, 128, 4, -14]) == 128
    assert candidate([4, 1, 6]) == 6
    assert candidate([4, 1, -3, 5, -6, 3, 4, 5, 119, 2, -5]) == 119
    assert candidate([1, 5, 7]) == 7
    assert candidate([3, 5, 8]) == 8
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124
    assert candidate([7, 3, -6, 2, -7, 6, 11, 1, 124, 6, -10]) == 124
    assert candidate([6, 3, 1]) == 6
    assert candidate([6, 3, 6]) == 6
    assert candidate([7, 6, -5, 1, -2, 4, 10, 4, 129, 6, -5]) == 129
    assert candidate([9, 4, -4, 2, -3, 8, 8, 4, 123, 3, -13]) == 123
    assert candidate([10, 8, -4, 5, -1, 6, 5, 5, 120, 4, -5]) == 120
    assert candidate([3, 6, -1, 4, -2, 1, 10, 2, 129, 5, -9]) == 129
    assert candidate([7, 6, -7, 3, 0, 4, 11, 3, 121, 1, -7]) == 121
    assert candidate([7, 4, -10, 6, -1, 8, 4, 5, 122, 6, -11]) == 122
    assert candidate([5, 6, 3]) == 6
    assert candidate([1, 7, 4]) == 7
    assert candidate([5, 6, -3, 7, -3, 2, 14, 5, 126, 5, -8]) == 126
    assert candidate([8, 6, 0, 7, -5, 6, 13, 3, 127, 5, -6]) == 127
    assert candidate([6, 4, 7]) == 7
    assert candidate([6, 5, 8]) == 8
    assert candidate([3, 8, -4, 7, -7, 3, 7, 3, 121, 3, -13]) == 121
    assert candidate([4, 1, -2, 7, -6, 8, 14, 4, 121, 1, -12]) == 121
    assert candidate([6, 6, 7]) == 7
    assert candidate([5, 8, -10, 3, -5, 5, 10, 3, 127, 2, -12]) == 127
    assert candidate([3, 6, 5]) == 6
    assert candidate([2, 7, 8]) == 8
    assert candidate([2, 4, -2, 3, -5, 6, 4, 3, 119, 4, -8]) == 119
    assert candidate([8, 3, -10, 6, 2, 3, 10, 5, 129, 2, -8]) == 129
    assert candidate([6, 1, 7]) == 7
    assert candidate([2, 4, 7]) == 7
    assert candidate([2, 4, -3, 6, -8, 8, 10, 4, 122, 4, -11]) == 122
    assert candidate([2, 1, 6]) == 6
    assert candidate([2, 3, 3]) == 3
    assert candidate([1, 5, 3]) == 5
    assert candidate([1, 6, -6, 6, -2, 2, 12, 3, 129, 4, -14]) == 129
    assert candidate([5, 8, -5, 2, 0, 3, 7, 5, 125, 5, -15]) == 125
    assert candidate([2, 2, 8]) == 8
    assert candidate([10, 5, -2, 5, -7, 4, 4, 5, 127, 3, -15]) == 127
    assert candidate([5, 6, -9, 2, 2, 6, 7, 4, 122, 3, -7]) == 122
    assert candidate([2, 2, 6]) == 6
    assert candidate([6, 6, -9, 1, -7, 8, 13, 1, 123, 2, -8]) == 123
    assert candidate([1, 1, -9, 6, -3, 1, 14, 4, 129, 2, -10]) == 129
    assert candidate([8, 1, -8, 3, -7, 6, 10, 4, 123, 4, -8]) == 123
    assert candidate([3, 5, -4, 3, 2, 3, 8, 1, 120, 5, -13]) == 120
    assert candidate([2, 7, 5]) == 7
    assert candidate([3, 1, 8]) == 8
    assert candidate([2, 4, 6]) == 6
    assert candidate([2, 5, 3]) == 5
    assert candidate([3, 2, 8]) == 8
    assert candidate([5, 1, 5]) == 5
    assert candidate([9, 2, -9, 1, -3, 6, 4, 3, 119, 3, -8]) == 119
    assert candidate([3, 4, 0, 1, -7, 2, 7, 1, 124, 4, -13]) == 124
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 1, -10, 4, -4, 7, 5, 5, 128, 6, -13]) == 128
    assert candidate([7, 7, -7, 5, -5, 5, 7, 1, 129, 2, -14]) == 129
    assert candidate([3, 6, -2, 4, -4, 7, 6, 4, 128, 2, -5]) == 128
    assert candidate([1, 5, 2]) == 5
    assert candidate([6, 7, -5, 2, -8, 5, 12, 2, 129, 5, -13]) == 129
    assert candidate([5, 4, 5]) == 5
    assert candidate([4, 8, -8, 4, -3, 6, 4, 1, 129, 2, -13]) == 129
    assert candidate([5, 4, 8]) == 8
    assert candidate([4, 2, 2]) == 4
    assert candidate([1, 3, -5, 1, -7, 4, 12, 1, 129, 6, -12]) == 129
    assert candidate([4, 5, -9, 1, -6, 6, 8, 5, 121, 6, -5]) == 121
    assert candidate([3, 4, 6]) == 6
    assert candidate([10, 3, -6, 1, 1, 6, 10, 4, 126, 3, -14]) == 126
    assert candidate([10, 8, -6, 2, -6, 1, 11, 1, 125, 5, -7]) == 125
    assert candidate([6, 2, 8]) == 8
    assert candidate([1, 6, -3, 5, -2, 7, 8, 4, 126, 1, -14]) == 126
    assert candidate([3, 7, 3]) == 7
    assert candidate([6, 3, -10, 2, -1, 8, 10, 4, 123, 1, -8]) == 123
    assert candidate([4, 4, -8, 4, -7, 3, 4, 1, 122, 6, -15]) == 122
    assert candidate([9, 8, -3, 1, 1, 8, 4, 5, 128, 1, -10]) == 128
    assert candidate([3, 2, 5]) == 5
    assert candidate([5, 1, 1]) == 5
    assert candidate([5, 3, 6]) == 6
    assert candidate([2, 5, 4]) == 5
    assert candidate([1, 1, 6]) == 6
    assert candidate([2, 4, 5]) == 5
    assert candidate([5, 2, 6]) == 6
    assert candidate([1, 3, 1]) == 3
    assert candidate([2, 2, -7, 1, -8, 6, 14, 4, 120, 6, -5]) == 120
    assert candidate([3, 4, -6, 7, -2, 7, 7, 4, 120, 2, -14]) == 120
    assert candidate([2, 3, 8]) == 8
    assert candidate([7, 6, -9, 1, -8, 7, 6, 1, 121, 5, -7]) == 121
    assert candidate([3, 3, 6]) == 6
    assert candidate([5, 1, 2]) == 5
    assert candidate([5, 1, 7]) == 7
    assert candidate([4, 5, -5, 6, -6, 6, 8, 5, 127, 2, -10]) == 127
    assert candidate([9, 8, -7, 7, -7, 4, 9, 1, 124, 4, -7]) == 124
    assert candidate([5, 6, 1]) == 6
    assert candidate([5, 8, -9, 4, -7, 1, 9, 3, 122, 6, -14]) == 122
    assert candidate([7, 6, -6, 6, 0, 6, 8, 3, 120, 1, -11]) == 120
    assert candidate([9, 6, 0, 5, 0, 5, 7, 4, 128, 4, -6]) == 128
    assert candidate([1, 2, 5]) == 5
    assert candidate([1, 2, 1]) == 2
    assert candidate([1, 7, 1]) == 7
    assert candidate([10, 6, -7, 3, 2, 4, 4, 1, 123, 1, -15]) == 123
    assert candidate([6, 4, -10, 7, -4, 5, 4, 5, 121, 5, -5]) == 121
    assert candidate([5, 4, -9, 4, -8, 4, 8, 3, 128, 2, -10]) == 128
    assert candidate([9, 3, 0, 7, -4, 4, 14, 5, 121, 6, -9]) == 121
    assert candidate([2, 2, -7, 6, 1, 1, 8, 3, 128, 1, -10]) == 128
    assert candidate([2, 6, 4]) == 6
    assert candidate([5, 6, 8]) == 8
    assert candidate([1, 2, 4]) == 4
    assert candidate([4, 5, 3]) == 5
    assert candidate([10, 1, -10, 4, -7, 4, 7, 1, 129, 3, -9]) == 129
    assert candidate([3, 5, -3, 6, -8, 3, 10, 1, 124, 2, -14]) == 124
    assert candidate([1, 3, 8]) == 8
    assert candidate([8, 7, -1, 3, -5, 1, 11, 5, 122, 6, -5]) == 122
    assert candidate([3, 3, 1]) == 3
    assert candidate([5, 6, 5]) == 6
    assert candidate([3, 3, 0, 1, -2, 6, 10, 5, 127, 3, -7]) == 127
    assert candidate([5, 8, -4, 7, -2, 1, 6, 2, 129, 1, -5]) == 129
    assert candidate([6, 3, -1, 4, 1, 3, 14, 1, 129, 3, -12]) == 129
    assert candidate([6, 6, 8]) == 8
    assert candidate([6, 7, 3]) == 7
    assert candidate([3, 5, 4]) == 5
    assert candidate([2, 8, -9, 6, -5, 6, 6, 1, 129, 3, -13]) == 129
    assert candidate([2, 8, -10, 4, -8, 7, 5, 1, 122, 5, -12]) == 122
    assert candidate([1, 8, -6, 2, -2, 1, 10, 4, 123, 3, -10]) == 123
    assert candidate([2, 2, -5, 5, -5, 1, 9, 5, 126, 1, -12]) == 126
    assert candidate([5, 5, 8]) == 8
    assert candidate([1, 7, 8]) == 8

if __name__ == '__main__':
    check(max_element)