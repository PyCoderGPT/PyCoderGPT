from case_MBPP_260 import big_sum


def check(candidate):
    assert candidate([1,2,3]) == 4
    assert candidate([-1,2,3,4]) == 3
    assert candidate([2,3,6]) == 8
    assert candidate([4, 6, 3]) == 9
    assert candidate([5, 4, 5]) == 9
    assert candidate([6, 6, 8]) == 14
    assert candidate([4, 3, 3]) == 7
    assert candidate([1, 2, 2]) == 3
    assert candidate([2, 2, 3]) == 5
    assert candidate([2, 7, 2]) == 9
    assert candidate([3, 4, 5]) == 8
    assert candidate([5, 5, 8]) == 13
    assert candidate([3, 1, 3]) == 4
    assert candidate([3, 1, 8]) == 9
    assert candidate([6, 7, 6]) == 13
    assert candidate([5, 1, 2]) == 6
    assert candidate([2, 4, 5]) == 7
    assert candidate([1, 4, 5]) == 6
    assert candidate([6, 4, 7]) == 11
    assert candidate([1, 1, 4]) == 5
    assert candidate([1, 2, 1]) == 3
    assert candidate([2, 4, 6]) == 8
    assert candidate([3, 4, 3]) == 7
    assert candidate([1, 5, 8]) == 9
    assert candidate([5, 4, 3]) == 8
    assert candidate([4, 4, 5]) == 9
    assert candidate([1, 1, 6]) == 7
    assert candidate([2, 2, 2]) == 4
    assert candidate([4, 6, 8]) == 12
    assert candidate([4, 7, 1]) == 8
    assert candidate([3, 2, 4]) == 6
    assert candidate([2, 4, 3]) == 6
    assert candidate([6, 7, 4]) == 11
    assert candidate([3, 2, 5]) == 7
    assert candidate([5, 2, 5]) == 7
    assert candidate([1, 5, 3]) == 6
    assert candidate([-1, 3, 2, 4]) == 3
    assert candidate([-1, 5, 2, 9]) == 8
    assert candidate([2, 4, 2, 3]) == 6
    assert candidate([0, 1, 7, 7]) == 7
    assert candidate([-3, 3, 1, 8]) == 5
    assert candidate([1, 4, 1, 9]) == 10
    assert candidate([0, 3, 3, 7]) == 7
    assert candidate([-3, 1, 4, 5]) == 2
    assert candidate([4, 1, 5, 3]) == 6
    assert candidate([4, 6, 7, 2]) == 9
    assert candidate([3, 2, 8, 7]) == 10
    assert candidate([4, 7, 3, 7]) == 10
    assert candidate([1, 5, 6, 5]) == 7
    assert candidate([4, 2, 1, 6]) == 7
    assert candidate([-4, 6, 1, 3]) == 2
    assert candidate([-6, 5, 2, 5]) == -1
    assert candidate([-3, 4, 4, 3]) == 1
    assert candidate([-6, 4, 4, 9]) == 3
    assert candidate([-5, 2, 2, 7]) == 2
    assert candidate([-5, 7, 6, 1]) == 2
    assert candidate([-4, 5, 5, 2]) == 1
    assert candidate([4, 7, 1, 1]) == 8
    assert candidate([0, 3, 8, 3]) == 8
    assert candidate([-3, 2, 8, 4]) == 5
    assert candidate([4, 6, 8, 3]) == 11
    assert candidate([2, 2, 4, 7]) == 9
    assert candidate([2, 5, 3, 4]) == 7
    assert candidate([-1, 2, 5, 6]) == 5
    assert candidate([2, 2, 5, 7]) == 9
    assert candidate([4, 6, 1, 6]) == 7
    assert candidate([0, 4, 5, 9]) == 9
    assert candidate([0, 1, 7, 6]) == 7
    assert candidate([-6, 1, 5, 2]) == -1
    assert candidate([3, 5, 4]) == 8
    assert candidate([2, 6, 9]) == 11
    assert candidate([2, 6, 9]) == 11
    assert candidate([7, 8, 2]) == 10
    assert candidate([3, 3, 8]) == 11
    assert candidate([5, 4, 10]) == 14
    assert candidate([3, 7, 6]) == 10
    assert candidate([2, 3, 11]) == 13
    assert candidate([1, 4, 3]) == 5
    assert candidate([3, 4, 10]) == 13
    assert candidate([6, 4, 5]) == 10
    assert candidate([5, 2, 2]) == 7
    assert candidate([1, 2, 6]) == 7
    assert candidate([6, 8, 6]) == 14
    assert candidate([3, 3, 3]) == 6
    assert candidate([4, 1, 6]) == 7
    assert candidate([6, 7, 4]) == 11
    assert candidate([7, 7, 3]) == 10
    assert candidate([1, 1, 2]) == 3
    assert candidate([3, 7, 9]) == 12
    assert candidate([1, 7, 11]) == 12
    assert candidate([5, 5, 4]) == 9
    assert candidate([7, 1, 5]) == 8
    assert candidate([1, 6, 8]) == 9
    assert candidate([6, 4, 11]) == 15
    assert candidate([4, 8, 6]) == 12
    assert candidate([2, 5, 6]) == 8
    assert candidate([1, 1, 6]) == 7
    assert candidate([7, 7, 3]) == 10
    assert candidate([4, 1, 8]) == 9
    assert candidate([6, 2, 8]) == 10
    assert candidate([1, 3, 2]) == 4
    assert candidate([6, 1, 10]) == 11

if __name__ == '__main__':
    check(big_sum)