from case_MBPP_323 import largest_subset


def check(candidate):
    assert candidate([ 1, 3, 6, 13, 17, 18 ], 6) == 4
    assert candidate([10, 5, 3, 15, 20], 5) == 3
    assert candidate([18, 1, 3, 6, 13, 17], 6) == 4
    assert candidate([1, 6, 5, 13, 12, 17], 1) == 1
    assert candidate([4, 7, 4, 9, 22, 14], 1) == 1
    assert candidate([1, 8, 10, 13, 12, 23], 4) == 2
    assert candidate([3, 5, 9, 11, 18, 14], 3) == 2
    assert candidate([3, 5, 3, 15, 12, 20], 6) == 3
    assert candidate([3, 8, 10, 18, 15, 20], 2) == 1
    assert candidate([2, 2, 5, 8, 19, 17], 1) == 1
    assert candidate([3, 5, 8, 18, 13, 20], 2) == 1
    assert candidate([2, 5, 4, 11, 21, 23], 5) == 2
    assert candidate([5, 7, 10, 15, 17, 14], 6) == 2
    assert candidate([1, 5, 4, 11, 20, 18], 4) == 2
    assert candidate([2, 5, 1, 13, 20, 15], 3) == 2
    assert candidate([3, 7, 10, 11, 15, 13], 3) == 1
    assert candidate([3, 8, 11, 13, 14, 20], 3) == 1
    assert candidate([4, 7, 9, 16, 20, 14], 2) == 1
    assert candidate([4, 5, 5, 10, 16, 15], 5) == 3
    assert candidate([1, 2, 6, 16, 16, 14], 2) == 2
    assert candidate([4, 1, 6, 9, 22, 23], 1) == 1
    assert candidate([3, 4, 3, 13, 14, 22], 2) == 1
    assert candidate([3, 2, 8, 17, 18, 20], 1) == 1
    assert candidate([6, 6, 4, 14, 17, 17], 1) == 1
    assert candidate([6, 4, 11, 13, 14, 22], 6) == 2
    assert candidate([3, 5, 4, 10, 20, 17], 1) == 1
    assert candidate([2, 7, 5, 14, 16, 14], 4) == 2
    assert candidate([6, 8, 5, 14, 15, 19], 2) == 1
    assert candidate([5, 2, 1, 8, 14, 13], 4) == 3
    assert candidate([2, 2, 2, 10, 19, 19], 4) == 4
    assert candidate([2, 5, 11, 13, 17, 22], 1) == 1
    assert candidate([3, 6, 8, 10, 22, 16], 3) == 2
    assert candidate([3, 2, 11, 11, 18, 17], 4) == 2
    assert candidate([4, 1, 5, 14, 12, 22], 6) == 3
    assert candidate([4, 1, 4, 16, 14, 22], 6) == 4
    assert candidate([2, 3, 7, 10, 19, 15], 3) == 1
    assert candidate([11, 6, 2, 12, 16], 2) == 1
    assert candidate([14, 8, 7, 14, 16], 4) == 3
    assert candidate([12, 8, 2, 16, 16], 2) == 1
    assert candidate([11, 2, 4, 18, 20], 3) == 2
    assert candidate([12, 4, 1, 16, 18], 5) == 4
    assert candidate([8, 6, 6, 17, 23], 1) == 1
    assert candidate([5, 10, 4, 15, 17], 1) == 1
    assert candidate([10, 4, 7, 13, 15], 3) == 1
    assert candidate([8, 3, 4, 15, 15], 4) == 2
    assert candidate([6, 8, 2, 20, 19], 1) == 1
    assert candidate([5, 7, 3, 11, 24], 5) == 2
    assert candidate([10, 7, 5, 17, 21], 3) == 2
    assert candidate([8, 7, 7, 19, 16], 2) == 1
    assert candidate([5, 6, 2, 14, 23], 1) == 1
    assert candidate([13, 9, 2, 13, 22], 4) == 2
    assert candidate([5, 9, 5, 14, 16], 4) == 2
    assert candidate([7, 7, 2, 19, 18], 2) == 2
    assert candidate([8, 4, 8, 18, 16], 5) == 4
    assert candidate([7, 5, 3, 16, 16], 3) == 1
    assert candidate([13, 10, 7, 11, 19], 4) == 1
    assert candidate([12, 6, 2, 17, 22], 1) == 1
    assert candidate([13, 9, 1, 17, 16], 5) == 3
    assert candidate([9, 1, 7, 11, 20], 5) == 3
    assert candidate([11, 1, 7, 15, 18], 4) == 3
    assert candidate([13, 8, 4, 18, 18], 4) == 2
    assert candidate([6, 9, 8, 12, 22], 5) == 2
    assert candidate([5, 4, 5, 20, 20], 2) == 1
    assert candidate([12, 8, 4, 11, 20], 1) == 1
    assert candidate([7, 9, 5, 17, 23], 4) == 1
    assert candidate([9, 10, 6, 15, 18], 5) == 2
    assert candidate([10, 10, 7, 17, 17], 5) == 2
    assert candidate([14, 4, 5, 11, 25], 2) == 1
    assert candidate([8, 4, 4, 16, 17], 3) == 3
    assert candidate([23, 6, 4, 10, 13, 18], 2) == 1
    assert candidate([23, 1, 1, 5, 16, 22], 2) == 2
    assert candidate([14, 5, 2, 10, 13, 20], 2) == 1
    assert candidate([16, 4, 4, 6, 12, 21], 6) == 4
    assert candidate([19, 2, 2, 4, 9, 21], 5) == 3
    assert candidate([13, 3, 8, 10, 18, 19], 1) == 1
    assert candidate([21, 1, 3, 7, 11, 12], 6) == 4
    assert candidate([15, 3, 7, 7, 8, 19], 5) == 2
    assert candidate([23, 6, 2, 4, 9, 15], 4) == 3
    assert candidate([21, 6, 4, 10, 18, 15], 6) == 2
    assert candidate([15, 5, 5, 2, 15, 14], 1) == 1
    assert candidate([17, 1, 2, 8, 16, 12], 3) == 3
    assert candidate([15, 4, 8, 1, 10, 13], 6) == 4
    assert candidate([16, 1, 4, 1, 16, 16], 6) == 6
    assert candidate([23, 2, 8, 1, 10, 19], 1) == 1
    assert candidate([23, 4, 3, 9, 13, 22], 5) == 2
    assert candidate([19, 2, 3, 7, 10, 15], 6) == 2
    assert candidate([22, 5, 1, 4, 17, 15], 1) == 1
    assert candidate([21, 3, 7, 4, 9, 22], 3) == 2
    assert candidate([13, 4, 4, 6, 9, 18], 6) == 2
    assert candidate([22, 5, 6, 8, 16, 18], 4) == 1
    assert candidate([16, 5, 5, 8, 14, 21], 2) == 1
    assert candidate([13, 6, 1, 4, 13, 15], 5) == 3
    assert candidate([20, 3, 6, 4, 9, 13], 5) == 2
    assert candidate([14, 3, 5, 8, 12, 17], 3) == 1
    assert candidate([14, 2, 7, 8, 9, 13], 3) == 2
    assert candidate([17, 2, 8, 9, 8, 14], 3) == 2
    assert candidate([19, 6, 6, 7, 14, 13], 2) == 1
    assert candidate([15, 5, 6, 6, 10, 15], 4) == 2
    assert candidate([22, 4, 2, 9, 15, 14], 3) == 2
    assert candidate([23, 3, 1, 5, 9, 12], 6) == 3
    assert candidate([23, 6, 6, 7, 14, 20], 3) == 2
    assert candidate([17, 5, 2, 11, 9, 22], 3) == 1

if __name__ == '__main__':
    check(largest_subset)