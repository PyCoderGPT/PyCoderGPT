from case_MBPP_100 import sum_range_list


def check(candidate):
    assert candidate( [2,1,5,6,8,3,4,9,10,11,8,12],8,10)==29
    assert candidate( [2,1,5,6,8,3,4,9,10,11,8,12],5,7)==16
    assert candidate( [2,1,5,6,8,3,4,9,10,11,8,12],7,10)==38
    assert candidate([4, 5, 6, 6, 13, 1, 2, 5, 5, 10, 8, 15], 7, 6) == 0
    assert candidate([6, 1, 2, 9, 6, 7, 3, 7, 5, 6, 10, 16], 13, 7) == 0
    assert candidate([4, 3, 7, 7, 3, 4, 3, 7, 6, 6, 5, 7], 9, 7) == 0
    assert candidate([4, 3, 8, 6, 5, 8, 6, 5, 7, 15, 4, 14], 8, 7) == 0
    assert candidate([1, 3, 2, 9, 7, 5, 4, 10, 13, 14, 9, 9], 10, 5) == 0
    assert candidate([2, 4, 1, 10, 10, 4, 3, 9, 9, 11, 5, 14], 10, 7) == 0
    assert candidate([2, 4, 1, 3, 11, 1, 1, 11, 9, 11, 11, 13], 3, 10) == 58
    assert candidate([6, 1, 6, 11, 6, 1, 4, 7, 13, 8, 9, 16], 12, 7) == 0
    assert candidate([1, 3, 5, 9, 10, 3, 5, 9, 11, 16, 5, 16], 9, 10) == 21
    assert candidate([1, 4, 7, 1, 4, 4, 7, 10, 6, 7, 7, 12], 9, 8) == 0
    assert candidate([1, 1, 10, 9, 7, 2, 5, 7, 12, 16, 9, 14], 4, 6) == 14
    assert candidate([2, 6, 9, 10, 10, 6, 8, 5, 11, 14, 4, 12], 9, 11) == 30
    assert candidate([4, 1, 9, 3, 9, 8, 6, 4, 6, 12, 13, 11], 4, 8) == 33
    assert candidate([3, 4, 1, 1, 13, 7, 7, 8, 8, 16, 7, 16], 5, 9) == 46
    assert candidate([5, 1, 9, 4, 13, 1, 2, 12, 15, 15, 3, 14], 7, 8) == 27
    assert candidate([5, 2, 2, 8, 9, 7, 4, 11, 15, 8, 6, 9], 7, 11) == 49
    assert candidate([5, 5, 6, 11, 3, 5, 4, 7, 5, 11, 9, 11], 12, 10) == 0
    assert candidate([5, 3, 10, 9, 4, 1, 8, 12, 7, 12, 12, 11], 9, 5) == 0
    assert candidate([2, 6, 3, 6, 6, 6, 1, 14, 13, 13, 7, 7], 6, 11) == 55
    assert candidate([6, 3, 4, 6, 3, 1, 5, 5, 8, 7, 12, 13], 4, 9) == 29
    assert candidate([7, 4, 6, 1, 9, 7, 6, 7, 11, 7, 6, 17], 10, 11) == 23
    assert candidate([4, 6, 3, 11, 7, 2, 9, 11, 12, 14, 13, 14], 4, 11) == 82
    assert candidate([3, 1, 7, 10, 10, 8, 3, 13, 12, 11, 6, 13], 5, 8) == 36
    assert candidate([3, 4, 7, 9, 13, 4, 3, 11, 7, 10, 6, 7], 12, 8) == 0
    assert candidate([7, 2, 10, 11, 4, 4, 5, 7, 5, 7, 12, 10], 12, 10) == 0
    assert candidate([1, 4, 3, 2, 10, 6, 1, 10, 11, 8, 7, 7], 6, 6) == 1
    assert candidate([5, 4, 10, 7, 3, 3, 5, 9, 13, 12, 10, 17], 13, 9) == 0
    assert candidate([1, 5, 1, 10, 3, 1, 7, 13, 5, 6, 6, 10], 13, 9) == 0
    assert candidate([5, 2, 8, 9, 10, 6, 1, 14, 13, 14, 13, 9], 3, 7) == 40
    assert candidate([3, 2, 1, 8, 12, 2, 8, 5, 13, 6, 3, 13], 12, 11) == 0
    assert candidate([4, 4, 2, 3, 12, 2, 5, 9, 12, 7, 5, 10], 8, 7) == 0
    assert candidate([5, 5, 9, 2, 11, 2, 8, 8, 13, 10, 9, 11], 3, 8) == 44
    assert candidate([6, 4, 10, 7, 12, 5, 9, 9, 15, 15, 7, 16], 7, 5) == 0
    assert candidate([7, 6, 3, 8, 9, 4, 7, 4, 15, 11, 8, 9], 6, 9) == 37
    assert candidate([5, 6, 2, 8, 5, 1, 2, 6, 15, 11, 6, 9], 3, 8) == 37
    assert candidate([4, 2, 4, 11, 6, 1, 4, 9, 10, 16, 12, 10], 6, 11) == 61
    assert candidate([7, 3, 4, 5, 12, 2, 2, 14, 14, 7, 4, 17], 8, 5) == 0
    assert candidate([3, 3, 2, 2, 13, 1, 4, 4, 8, 6, 10, 13], 1, 3) == 7
    assert candidate([2, 1, 7, 10, 4, 8, 2, 9, 5, 6, 13, 7], 3, 3) == 10
    assert candidate([1, 1, 5, 11, 12, 1, 4, 9, 12, 14, 11, 15], 8, 10) == 37
    assert candidate([3, 6, 5, 2, 11, 4, 9, 11, 10, 6, 3, 11], 5, 9) == 40
    assert candidate([6, 4, 9, 9, 10, 5, 5, 7, 6, 16, 12, 11], 4, 10) == 61
    assert candidate([6, 6, 9, 9, 10, 3, 5, 5, 7, 14, 3, 7], 10, 5) == 0
    assert candidate([7, 6, 8, 7, 13, 6, 3, 6, 10, 13, 9, 11], 5, 3) == 0
    assert candidate([1, 4, 3, 5, 10, 1, 4, 9, 6, 16, 7, 7], 9, 4) == 0
    assert candidate([2, 2, 9, 11, 4, 1, 4, 10, 9, 16, 7, 15], 5, 7) == 15
    assert candidate([4, 4, 6, 11, 10, 4, 7, 12, 12, 7, 10, 13], 3, 3) == 11
    assert candidate([7, 2, 1, 11, 8, 3, 1, 6, 5, 11, 7, 11], 1, 6) == 26
    assert candidate([3, 5, 9, 1, 5, 3, 6, 8, 8, 10, 6, 7], 1, 6) == 29
    assert candidate([3, 2, 9, 3, 7, 5, 1, 10, 8, 11, 11, 17], 10, 11) == 28
    assert candidate([7, 3, 4, 9, 9, 8, 5, 13, 5, 6, 3, 7], 7, 5) == 0
    assert candidate([1, 6, 6, 6, 7, 3, 9, 5, 8, 16, 7, 10], 7, 7) == 5
    assert candidate([5, 4, 3, 8, 8, 7, 4, 14, 14, 8, 9, 17], 9, 6) == 0
    assert candidate([1, 1, 8, 8, 7, 6, 3, 11, 12, 15, 11, 7], 9, 4) == 0
    assert candidate([3, 3, 6, 7, 5, 7, 1, 6, 8, 6, 10, 15], 3, 11) == 65
    assert candidate([3, 3, 1, 10, 9, 5, 5, 6, 7, 13, 4, 14], 9, 4) == 0
    assert candidate([5, 5, 2, 1, 3, 4, 6, 12, 6, 6, 9, 10], 5, 8) == 28
    assert candidate([1, 5, 8, 3, 7, 5, 8, 10, 12, 9, 11, 12], 9, 4) == 0
    assert candidate([2, 6, 1, 1, 13, 6, 8, 9, 12, 10, 11, 16], 9, 7) == 0
    assert candidate([6, 5, 7, 10, 3, 3, 8, 12, 11, 11, 9, 13], 1, 8) == 59
    assert candidate([5, 3, 1, 1, 4, 2, 5, 7, 13, 7, 11, 11], 8, 7) == 0
    assert candidate([5, 4, 1, 10, 10, 8, 9, 5, 6, 6, 11, 11], 10, 8) == 0
    assert candidate([4, 3, 6, 4, 3, 5, 5, 4, 12, 15, 4, 10], 10, 3) == 0
    assert candidate([3, 1, 4, 6, 8, 7, 9, 7, 10, 7, 4, 10], 4, 2) == 0
    assert candidate([1, 6, 1, 6, 7, 4, 4, 13, 9, 10, 7, 11], 6, 6) == 4
    assert candidate([2, 6, 1, 5, 11, 6, 3, 7, 14, 9, 7, 7], 8, 7) == 0
    assert candidate([7, 2, 7, 10, 12, 5, 8, 11, 14, 13, 12, 11], 9, 7) == 0
    assert candidate([6, 1, 5, 5, 8, 4, 2, 11, 6, 15, 9, 15], 2, 5) == 22
    assert candidate([3, 1, 1, 6, 13, 3, 9, 9, 5, 16, 11, 7], 10, 10) == 11
    assert candidate([5, 4, 7, 5, 9, 4, 3, 6, 7, 14, 3, 14], 11, 10) == 0
    assert candidate([7, 5, 8, 8, 9, 3, 3, 10, 8, 12, 4, 15], 3, 7) == 33
    assert candidate([6, 5, 9, 5, 13, 5, 1, 8, 15, 16, 11, 12], 3, 8) == 47
    assert candidate([2, 6, 4, 3, 10, 8, 3, 9, 15, 9, 9, 15], 11, 9) == 0
    assert candidate([3, 1, 1, 1, 11, 6, 5, 6, 10, 8, 7, 12], 3, 6) == 23
    assert candidate([7, 3, 3, 9, 10, 6, 8, 4, 13, 10, 5, 11], 4, 7) == 28
    assert candidate([2, 1, 7, 3, 7, 6, 4, 7, 5, 15, 13, 9], 2, 6) == 27
    assert candidate([2, 2, 8, 2, 4, 8, 6, 10, 6, 6, 3, 15], 2, 11) == 68
    assert candidate([4, 3, 3, 3, 7, 8, 7, 10, 13, 15, 7, 12], 2, 9) == 66
    assert candidate([7, 4, 10, 3, 3, 2, 5, 6, 10, 11, 5, 8], 9, 8) == 0
    assert candidate([3, 6, 4, 2, 4, 7, 4, 4, 13, 14, 9, 8], 8, 11) == 44
    assert candidate([2, 6, 6, 5, 11, 4, 5, 5, 5, 9, 5, 12], 12, 7) == 0
    assert candidate([2, 1, 9, 1, 8, 4, 8, 10, 8, 11, 11, 12], 12, 9) == 0
    assert candidate([3, 6, 3, 11, 7, 2, 8, 10, 12, 16, 9, 16], 2, 6) == 31
    assert candidate([5, 6, 9, 8, 7, 5, 2, 5, 5, 10, 3, 9], 4, 11) == 46
    assert candidate([4, 3, 4, 3, 9, 6, 8, 11, 10, 12, 10, 17], 10, 9) == 0
    assert candidate([4, 2, 1, 7, 10, 1, 4, 14, 6, 6, 12, 9], 3, 10) == 60
    assert candidate([6, 5, 8, 10, 7, 3, 5, 5, 6, 8, 5, 15], 6, 8) == 16
    assert candidate([1, 6, 2, 10, 6, 7, 5, 12, 6, 14, 11, 8], 8, 11) == 39
    assert candidate([1, 5, 6, 8, 10, 8, 7, 5, 15, 12, 9, 14], 5, 9) == 47
    assert candidate([2, 5, 9, 2, 4, 6, 6, 6, 11, 11, 11, 7], 6, 7) == 12
    assert candidate([4, 3, 2, 4, 13, 4, 4, 13, 9, 7, 11, 7], 12, 7) == 0
    assert candidate([7, 3, 5, 1, 12, 6, 5, 14, 12, 12, 4, 13], 10, 8) == 0
    assert candidate([6, 3, 10, 7, 4, 6, 7, 14, 15, 14, 3, 9], 11, 7) == 0
    assert candidate([3, 2, 1, 10, 6, 5, 8, 11, 13, 8, 10, 11], 12, 10) == 0
    assert candidate([3, 4, 1, 7, 8, 8, 5, 12, 15, 9, 5, 10], 7, 9) == 36
    assert candidate([3, 6, 7, 9, 7, 7, 9, 8, 10, 16, 6, 8], 3, 8) == 50
    assert candidate([7, 6, 2, 11, 5, 6, 3, 5, 15, 16, 4, 14], 8, 9) == 31
    assert candidate([6, 4, 3, 4, 4, 6, 7, 12, 15, 7, 8, 12], 3, 9) == 55
    assert candidate([5, 3, 9, 2, 13, 7, 5, 12, 12, 14, 12, 15], 10, 9) == 0

if __name__ == '__main__':
    check(sum_range_list)