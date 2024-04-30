from case_MBPP_255 import find_remainder


def check(candidate):
    assert candidate([ 100, 10, 5, 25, 35, 14 ],6,11) ==9
    assert candidate([1,1,1],3,1) == 0
    assert candidate([1,2,1],3,2) == 0
    assert candidate([96, 14, 8, 20, 36, 12], 1, 9) == 6
    assert candidate([98, 13, 3, 29, 30, 15], 5, 8) == 4
    assert candidate([103, 12, 9, 26, 34, 13], 1, 11) == 4
    assert candidate([96, 11, 9, 22, 40, 19], 3, 9) == 0
    assert candidate([96, 14, 8, 27, 33, 17], 3, 10) == 2
    assert candidate([101, 9, 5, 24, 32, 19], 5, 9) == 0
    assert candidate([103, 10, 5, 22, 31, 13], 6, 9) == 2
    assert candidate([101, 6, 10, 29, 35, 10], 4, 15) == 0
    assert candidate([98, 8, 10, 20, 30, 16], 3, 8) == 0
    assert candidate([100, 13, 7, 26, 30, 16], 1, 12) == 4
    assert candidate([101, 14, 3, 27, 39, 11], 4, 13) == 4
    assert candidate([98, 12, 10, 25, 36, 19], 1, 10) == 8
    assert candidate([102, 12, 1, 25, 40, 15], 6, 14) == 8
    assert candidate([98, 5, 7, 24, 30, 14], 4, 16) == 0
    assert candidate([103, 9, 2, 28, 32, 10], 3, 16) == 14
    assert candidate([102, 5, 2, 30, 30, 14], 2, 15) == 0
    assert candidate([97, 5, 10, 27, 32, 11], 1, 15) == 7
    assert candidate([101, 13, 10, 26, 31, 15], 1, 6) == 5
    assert candidate([103, 14, 7, 20, 39, 19], 2, 15) == 2
    assert candidate([99, 14, 10, 26, 37, 18], 2, 12) == 6
    assert candidate([103, 5, 6, 27, 33, 17], 4, 6) == 0
    assert candidate([96, 12, 10, 25, 30, 14], 5, 7) == 5
    assert candidate([100, 11, 5, 28, 40, 10], 6, 8) == 0
    assert candidate([96, 15, 4, 23, 35, 15], 6, 14) == 0
    assert candidate([103, 15, 4, 27, 32, 18], 5, 8) == 0
    assert candidate([101, 6, 5, 25, 40, 18], 2, 8) == 6
    assert candidate([103, 14, 10, 22, 40, 13], 2, 15) == 2
    assert candidate([104, 9, 4, 30, 33, 9], 2, 7) == 5
    assert candidate([101, 10, 2, 25, 38, 15], 5, 9) == 2
    assert candidate([96, 11, 8, 22, 30, 17], 6, 11) == 0
    assert candidate([104, 7, 2, 24, 32, 11], 5, 9) == 3
    assert candidate([97, 5, 2, 30, 34, 9], 5, 8) == 0
    assert candidate([102, 14, 7, 29, 32, 14], 5, 13) == 8
    assert candidate([1, 1, 6], 3, 3) == 0
    assert candidate([3, 4, 6], 3, 3) == 0
    assert candidate([5, 3, 6], 1, 4) == 1
    assert candidate([3, 1, 3], 1, 5) == 3
    assert candidate([3, 1, 3], 1, 4) == 3
    assert candidate([2, 2, 5], 1, 3) == 2
    assert candidate([4, 1, 2], 2, 6) == 4
    assert candidate([5, 3, 1], 1, 1) == 0
    assert candidate([4, 3, 2], 1, 1) == 0
    assert candidate([6, 2, 4], 3, 5) == 3
    assert candidate([3, 5, 1], 2, 1) == 0
    assert candidate([6, 5, 5], 1, 3) == 0
    assert candidate([6, 3, 4], 2, 5) == 3
    assert candidate([3, 2, 1], 2, 4) == 2
    assert candidate([2, 5, 4], 1, 4) == 2
    assert candidate([2, 1, 2], 3, 5) == 4
    assert candidate([3, 6, 4], 2, 1) == 0
    assert candidate([6, 6, 2], 1, 5) == 1
    assert candidate([3, 2, 6], 1, 3) == 0
    assert candidate([1, 3, 2], 3, 2) == 0
    assert candidate([3, 6, 1], 2, 3) == 0
    assert candidate([5, 2, 5], 1, 6) == 5
    assert candidate([2, 1, 3], 2, 6) == 2
    assert candidate([4, 3, 6], 3, 3) == 0
    assert candidate([2, 6, 5], 2, 3) == 0
    assert candidate([2, 1, 3], 2, 4) == 2
    assert candidate([4, 6, 3], 3, 5) == 2
    assert candidate([6, 3, 2], 2, 4) == 2
    assert candidate([1, 6, 4], 1, 1) == 0
    assert candidate([6, 4, 6], 3, 6) == 0
    assert candidate([2, 5, 1], 3, 5) == 0
    assert candidate([1, 6, 2], 1, 5) == 1
    assert candidate([6, 2, 6], 1, 2) == 0
    assert candidate([6, 2, 6], 1, 2) == 0
    assert candidate([3, 7, 3], 2, 4) == 1
    assert candidate([6, 5, 1], 1, 1) == 0
    assert candidate([1, 1, 2], 2, 1) == 0
    assert candidate([6, 2, 4], 2, 6) == 0
    assert candidate([2, 1, 1], 1, 5) == 2
    assert candidate([5, 5, 3], 1, 4) == 1
    assert candidate([5, 7, 6], 3, 4) == 2
    assert candidate([2, 4, 1], 3, 4) == 0
    assert candidate([1, 7, 3], 3, 6) == 3
    assert candidate([5, 2, 1], 2, 6) == 4
    assert candidate([6, 7, 4], 2, 5) == 2
    assert candidate([3, 7, 1], 2, 1) == 0
    assert candidate([1, 7, 5], 1, 2) == 1
    assert candidate([4, 3, 6], 1, 2) == 0
    assert candidate([1, 1, 4], 3, 2) == 0
    assert candidate([3, 6, 3], 1, 1) == 0
    assert candidate([6, 1, 3], 1, 2) == 0
    assert candidate([3, 7, 6], 1, 2) == 1
    assert candidate([1, 4, 3], 2, 2) == 0
    assert candidate([1, 3, 3], 1, 7) == 1
    assert candidate([6, 6, 2], 3, 2) == 0
    assert candidate([3, 1, 4], 1, 6) == 3
    assert candidate([3, 1, 1], 3, 1) == 0
    assert candidate([1, 5, 4], 3, 6) == 2
    assert candidate([4, 5, 1], 2, 3) == 2
    assert candidate([2, 1, 1], 1, 1) == 0
    assert candidate([5, 3, 3], 1, 3) == 2
    assert candidate([6, 3, 5], 2, 6) == 0
    assert candidate([3, 7, 2], 1, 1) == 0
    assert candidate([5, 4, 2], 1, 4) == 1
    assert candidate([1, 4, 4], 3, 1) == 0
    assert candidate([3, 4, 3], 3, 2) == 0

if __name__ == '__main__':
    check(find_remainder)