from case_MBPP_059 import count


def check(candidate):
    assert candidate([True,False,True]) == 2
    assert candidate([False,False]) == 0
    assert candidate([True,True,True]) == 3
    assert candidate([1, 1, 4]) == 6
    assert candidate([5, 1, 1]) == 7
    assert candidate([1, 5, 2]) == 8
    assert candidate([4, 5, 5]) == 14
    assert candidate([6, 4, 1]) == 11
    assert candidate([5, 1, 6]) == 12
    assert candidate([1, 4, 6]) == 11
    assert candidate([3, 3, 2]) == 8
    assert candidate([1, 4, 4]) == 9
    assert candidate([2, 5, 4]) == 11
    assert candidate([6, 1, 2]) == 9
    assert candidate([5, 2, 4]) == 11
    assert candidate([5, 4, 6]) == 15
    assert candidate([1, 4, 2]) == 7
    assert candidate([4, 4, 1]) == 9
    assert candidate([1, 3, 1]) == 5
    assert candidate([4, 4, 6]) == 14
    assert candidate([5, 3, 3]) == 11
    assert candidate([5, 1, 2]) == 8
    assert candidate([1, 1, 3]) == 5
    assert candidate([1, 4, 3]) == 8
    assert candidate([6, 3, 2]) == 11
    assert candidate([2, 3, 2]) == 7
    assert candidate([6, 4, 4]) == 14
    assert candidate([4, 4, 5]) == 13
    assert candidate([5, 2, 6]) == 13
    assert candidate([5, 2, 5]) == 12
    assert candidate([6, 5, 5]) == 16
    assert candidate([2, 5, 2]) == 9
    assert candidate([3, 4, 1]) == 8
    assert candidate([6, 3, 1]) == 10
    assert candidate([1, 4, 2]) == 7
    assert candidate([5, 1, 3]) == 9
    assert candidate([2, 3]) == 5
    assert candidate([4, 5]) == 9
    assert candidate([4, 5]) == 9
    assert candidate([5, 3]) == 8
    assert candidate([5, 4]) == 9
    assert candidate([4, 2]) == 6
    assert candidate([1, 3]) == 4
    assert candidate([1, 4]) == 5
    assert candidate([1, 5]) == 6
    assert candidate([2, 2]) == 4
    assert candidate([1, 3]) == 4
    assert candidate([3, 5]) == 8
    assert candidate([2, 3]) == 5
    assert candidate([3, 5]) == 8
    assert candidate([3, 5]) == 8
    assert candidate([4, 1]) == 5
    assert candidate([5, 5]) == 10
    assert candidate([3, 5]) == 8
    assert candidate([3, 5]) == 8
    assert candidate([1, 4]) == 5
    assert candidate([3, 5]) == 8
    assert candidate([2, 4]) == 6
    assert candidate([4, 3]) == 7
    assert candidate([5, 1]) == 6
    assert candidate([5, 1]) == 6
    assert candidate([3, 5]) == 8
    assert candidate([2, 3]) == 5
    assert candidate([1, 3]) == 4
    assert candidate([1, 5]) == 6
    assert candidate([5, 5]) == 10
    assert candidate([3, 4]) == 7
    assert candidate([1, 3]) == 4
    assert candidate([2, 1]) == 3
    assert candidate([2, 4, 4]) == 10
    assert candidate([1, 5, 6]) == 12
    assert candidate([6, 3, 3]) == 12
    assert candidate([6, 3, 2]) == 11
    assert candidate([5, 2, 4]) == 11
    assert candidate([1, 3, 3]) == 7
    assert candidate([6, 2, 3]) == 11
    assert candidate([1, 6, 2]) == 9
    assert candidate([2, 4, 5]) == 11
    assert candidate([3, 5, 2]) == 10
    assert candidate([5, 1, 5]) == 11
    assert candidate([2, 6, 5]) == 13
    assert candidate([6, 5, 4]) == 15
    assert candidate([1, 3, 5]) == 9
    assert candidate([6, 4, 3]) == 13
    assert candidate([3, 5, 4]) == 12
    assert candidate([5, 4, 2]) == 11
    assert candidate([4, 6, 2]) == 12
    assert candidate([1, 3, 6]) == 10
    assert candidate([4, 2, 2]) == 8
    assert candidate([5, 3, 5]) == 13
    assert candidate([5, 6, 2]) == 13
    assert candidate([3, 3, 5]) == 11
    assert candidate([3, 3, 6]) == 12
    assert candidate([2, 4, 1]) == 7
    assert candidate([2, 4, 5]) == 11
    assert candidate([4, 6, 6]) == 16
    assert candidate([4, 2, 4]) == 10
    assert candidate([3, 6, 6]) == 15
    assert candidate([6, 1, 5]) == 12
    assert candidate([6, 1, 2]) == 9
    assert candidate([2, 2, 4]) == 8
    assert candidate([2, 1, 1]) == 4

if __name__ == '__main__':
    check(count)