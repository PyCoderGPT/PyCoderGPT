from case_HE_108 import count_nums


def check(candidate):
    assert candidate([5, 2]) == 2
    assert candidate([-2, -5, 1]) == 1
    assert candidate([5, 4, 2, 0, 7, 2, 5]) == 6
    assert candidate([1, 102, 101, -3, 2, -5]) == 4
    assert candidate([7, 24, 39, -48, -54, 3]) == 5
    assert candidate([3, 3, 14, -4, 2, 4, 10]) == 6
    assert candidate([1, 1, 10, -9, 1, 1, 9]) == 6
    assert candidate([5, 99, 93, -9, 3, -4]) == 4
    assert candidate([5, 7, 13, -10, 1, 2, 1]) == 6
    assert candidate([3, 5, 3, -4, 5, 7, 2]) == 6
    assert candidate([]) == 0
    assert candidate([5, 4, 5, -8, 1, 3, 2]) == 6
    assert candidate([6, 103, 99, -8, 4, -1]) == 4
    assert candidate([-4, 3, 1]) == 2
    assert candidate([4, 1, 1]) == 3
    assert candidate([2, 97, 101, -8, 5, 3]) == 5
    assert candidate([1]) == 1

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1, 101, 102, -3, 2, -3]) == 4
    assert candidate([13, 26, 39, -42, -59, 4]) == 5
    assert candidate([3, 2, 6, -1, 5, 2, 3]) == 6
    assert candidate([5, 2, 8, -1, 5, 4, 1]) == 6
    assert candidate([8, 19, 38, -42, -61, 1]) == 4
    assert candidate([-2, -7, 1]) == 1
    assert candidate([5, 4, 5, 3, 5, 4, 8]) == 7
    assert candidate([2, 1, 4, -5, 5, 2, 9]) == 6
    assert candidate([4, -1, 1]) == 2
    assert candidate([2, 4, 4, 2, 1, 2, 3]) == 7
    assert candidate([2]) == 1
    assert candidate([1, 5, 1, -6, 6, 1, 1]) == 6
    assert candidate([3, 95, 96, -10, 5, -1]) == 4
    assert candidate([-4, -3, 3]) == 1
    assert candidate([2, 2]) == 2
    assert candidate([1]) == 1
    assert candidate([17, 21, 29, -42, -52, 3]) == 4
    assert candidate([6, 4, 1, -5, 3, 3, 10]) == 6
    assert candidate([-6, -7, 2]) == 1
    assert candidate([5, 3]) == 2
    assert candidate([2, -7, 4]) == 2
    assert candidate([11, 18, 38, -48, -59, 1]) == 6
    assert candidate([1, 100, 94, -4, 2, 2]) == 5
    assert candidate([-5, 1, 4]) == 2
    assert candidate([2, 6, 6, -4, 1, 9, 8]) == 6
    assert candidate([-1, -2, 0]) == 0
    assert candidate([2, 2, 7, -3, 6, 2, 5]) == 6
    assert candidate([10, 26, 34, -49, -60, 1]) == 5
    assert candidate([1, 2]) == 2
    assert candidate([12, 21, 31, -45, -52, 2]) == 5
    assert candidate([14, 18, 34, -45, -51, 1]) == 5
    assert candidate([4, 1, 2]) == 3
    assert candidate([4, -1, 2]) == 2
    assert candidate([3, 3, 1, -5, 4, 1, 5]) == 6
    assert candidate([1, 6, 9, -6, 0, 1, 5]) == 5
    assert candidate([4, 1, 3, -2, 5, 6, 3]) == 6
    assert candidate([3, 3]) == 2
    assert candidate([8, 22, 32, -44, -59, 1]) == 5
    assert candidate([4]) == 1
    assert candidate([3, 3, 4, -3, 2, 8, 7]) == 6
    assert candidate([14, 23, 37, -48, -53, 1]) == 5
    assert candidate([17, 26, 31, -40, -61, 4]) == 4
    assert candidate([5, 2, 1, -1, 1, 8, 3]) == 6
    assert candidate([6, 1, 7, -1, 4, 4, 10]) == 6
    assert candidate([-3, -6, 5]) == 1
    assert candidate([1, 1, 6, -8, 2, 3, 9]) == 6
    assert candidate([2, 5, 3, -2, 2, 6, 10]) == 6
    assert candidate([1, 100, 98, -7, 1, -1]) == 4
    assert candidate([5, 5]) == 2
    assert candidate([6, 105, 98, -6, 4, -2]) == 4
    assert candidate([7, 23, 37, -42, -53, 1]) == 4
    assert candidate([5, 5, 10, -1, 1, 1, 10]) == 6
    assert candidate([-0, 1**0]) == 1
    assert candidate([1, 1, 2, -2, 3, 4, 5]) == 6
    assert candidate([2, 3, 5]) == 3
    assert candidate([6, 96, 102, -11, 4, 1]) == 5
    assert candidate([4, 96, 97, -7, 2, -5]) == 4
    assert candidate([4, 2, 10, -3, 4, 2, 4]) == 6
    assert candidate([1, 4]) == 2
    assert candidate([3]) == 1
    assert candidate([12, 25, 32, -41, -60, 2]) == 4
    assert candidate([3, 0, 4]) == 2
    assert candidate([2, 105, 99, -12, 2, 0]) == 5
    assert candidate([4, 101, 103, -11, 3, -6]) == 4
    assert candidate([4, 8, 13, -4, 2, 6, 8]) == 6
    assert candidate([2, 105, 100, -9, 5, -4]) == 4
    assert candidate([5, 6, 3, -4, 4, 8, 3]) == 6
    assert candidate([9, 26, 29, -42, -61, 1]) == 4
    assert candidate([5]) == 1
    assert candidate([-1, 1, 3]) == 2
    assert candidate([15, 20, 39, -43, -54, 3]) == 4
    assert candidate([4, 4, 14, -10, 3, 6, 10]) == 6
    assert candidate([5, 2, 14, -10, 3, 1, 1]) == 6
    assert candidate([2, 11, 7, -1, 2, 6, 5]) == 6
    assert candidate([3, 11, 6, -7, 5, 5, 5]) == 6
    assert candidate([5, 105, 93, -7, 6, -6]) == 4
    assert candidate([12, 23, 34, -45, -56, 0]) == 5
    assert candidate([1, 97, 95, -8, 6, -4]) == 4
    assert candidate([5, 6]) == 2

if __name__ == '__main__':
    check(count_nums)