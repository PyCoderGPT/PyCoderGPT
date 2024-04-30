from case_HE_069 import search


def check(candidate):
    assert candidate([6, 7, 3, 13, 7, 15, 8, 6, 3, 5, 6, 8, 7, 3, 12, 2, 8, 13]) == 3
    assert candidate([9, 1, 4, 1, 6, 6, 4, 2, 2, 6, 9, 12, 4, 14, 4, 6, 2, 4, 4, 2, 6, 6, 10, 10, 6, 2, 3, 14, 8, 6]) == 6
    assert candidate([3, 5, 8, 4, 8, 10, 8, 3, 6, 12, 2, 3]) == 3
    assert candidate([14, 4, 8, 6, 1, 4, 7, 6, 10, 2, 6, 8, 7, 9, 1, 9, 4, 5, 8, 8, 6, 5, 10, 9, 12, 1, 4, 14, 10, 5]) == 4
    assert candidate([5, 13, 8, 5, 6]) == -1
    assert candidate([2, 4, 9, 5, 6, 13, 11, 3, 9, 11, 6, 15, 6, 8, 9, 7, 2, 7, 6, 12, 3, 3]) == 3
    assert candidate([5, 10, 2, 9, 6, 9, 4, 7, 7, 10, 8, 7, 1, 11, 6, 7, 13, 9, 8, 4, 6, 6, 6, 7]) == 1
    assert candidate([3, 2, 8, 2]) == 2
    assert candidate([6, 4, 5, 14, 4, 10, 5, 6, 5, 10, 2, 5, 7, 3, 6, 2, 11, 8, 3, 10, 8]) == 2
    assert candidate([7, 7, 9, 6, 9, 2, 7, 12, 14, 10, 2, 11, 2]) == 2
    assert candidate([5, 4, 2, 5, 11, 13, 8, 3, 2, 7, 12]) == 2
    assert candidate([10, 6, 2, 2, 6, 4, 2, 2, 7, 4, 3, 11, 6, 15, 2, 10, 5, 4, 3, 4, 5, 5, 14, 9, 12, 7, 9, 5, 5, 8]) == 5
    assert candidate([6, 6, 4, 1, 4, 3, 9, 1, 5, 3, 9, 4, 6, 11, 3, 4, 7, 6, 7, 1, 3, 9, 6, 4, 12, 4, 8, 15, 12, 8]) == 4
    assert candidate([8, 5, 1, 11, 9, 11, 1, 13, 10, 2, 6]) == 1
    assert candidate([1, 13, 12, 4, 5, 12, 8, 8, 10, 1, 5, 8, 2, 9, 15, 7, 10, 3, 10, 5, 12, 4, 1, 8]) == 1
    assert candidate([6, 8, 7, 12, 6, 10, 10, 1, 3, 11, 5, 8, 2, 3, 4, 4, 2, 10]) == 2
    assert candidate([1, 7, 1, 11, 4, 7, 1, 3, 2, 6, 5]) == 1
    assert candidate([8, 10, 10, 12, 13, 11, 10, 12]) == -1
    assert candidate([3, 9, 13, 13, 3, 12, 12, 2, 9, 4, 6, 15, 7, 5, 5, 6, 6, 11, 3, 15, 13, 1]) == 3
    assert candidate([3, 10, 5, 1, 4, 14, 11, 8, 7, 13, 6, 4]) == 1
    assert candidate([12, 5, 5, 7, 8, 8, 4]) == -1
    assert candidate([2, 7, 8, 8, 4, 8, 7, 3, 9, 6, 5, 10, 4, 3, 6, 7, 1, 7, 4, 10, 8, 1]) == 1
    assert candidate([1, 6, 12, 11, 8, 13, 3, 3, 10, 6, 4, 11, 2, 6, 9, 6, 1, 2, 4, 13, 3, 1]) == 3
    assert candidate([4, 5, 4, 4, 3, 6, 1, 5, 3, 8, 12, 13, 2, 6, 9, 6, 13, 11, 3, 4, 9, 9, 6, 6]) == 4
    assert candidate([10, 4, 7, 3, 8, 2, 2, 3, 10, 2, 9, 8, 7, 2, 9, 1, 8, 10, 6, 3, 8, 4, 2, 10]) == 3
    assert candidate([3, 4, 3, 1, 9, 6]) == 1
    assert candidate([3, 2, 3, 2, 7, 8]) == 2
    assert candidate([3, 10, 10, 9, 2]) == -1
    assert candidate([6, 12, 10, 7, 7, 12, 8, 7, 12, 11, 10, 10, 1, 3, 5, 9, 4, 3, 5, 12, 10, 2]) == 1
    assert candidate([6, 12, 6, 3, 4]) == -1
    assert candidate([9, 9, 5, 9, 6]) == -1
    assert candidate([3, 3]) == -1
    assert candidate([9, 5, 6, 5, 1, 3, 13, 1, 6, 2, 8]) == 1
    assert candidate([2, 3, 9, 3, 3, 11, 2, 6, 8, 12, 2, 11, 5, 2, 3, 7, 7, 4, 7, 2, 2, 14, 3]) == 3
    assert candidate([4, 5, 8, 4, 4]) == -1
    assert candidate([11, 10, 2, 9, 4, 6, 4, 6, 10, 13, 4, 7, 6, 10, 11, 9, 9, 1, 12, 6, 6, 9, 5, 2, 11]) == 2
    assert candidate([6, 9, 7, 5, 8, 7, 5, 3, 7, 5, 10, 10, 3, 6, 10, 2, 8, 6, 5, 4, 9, 5, 3, 10]) == 5
    assert candidate([5]) == -1
    assert candidate([5, 5, 5, 5, 1]) == 1
    assert candidate([7, 6, 5, 7, 4]) == -1
    assert candidate([13]) == -1
    assert candidate([7, 6, 7, 2, 5, 9]) == -1
    assert candidate([4, 2]) == -1
    assert candidate([7, 12, 12, 10, 1, 1, 7, 9, 3, 1, 7, 7, 2, 3, 13, 4, 1, 1, 11, 4, 3, 3, 3]) == 3
    assert candidate([6, 11, 3, 15, 5, 11, 6, 7, 6, 7, 5, 8, 6, 3, 7, 5, 8, 2]) == -1
    assert candidate([10, 7, 10, 7, 3, 5, 7, 7]) == -1
    assert candidate([4, 12, 4, 10, 8, 3, 12, 4, 11, 3, 9, 5, 2, 4, 10, 5, 4, 4, 4, 10, 13, 1]) == 4
    assert candidate([12, 5, 4, 11, 2, 9, 4, 8, 11, 3, 5, 4, 5, 14, 8, 8, 3, 6, 11, 10, 4, 4]) == 4
    assert candidate([5, 4, 10, 2, 1, 1, 10, 3, 6, 1, 8]) == 1
    assert candidate([1]) == 1
    assert candidate([2, 10, 4, 8, 2, 10, 5, 1, 2, 9, 5, 5, 6, 3, 8, 6, 4, 10]) == 2
    assert candidate([3, 8, 8, 5, 2, 10, 4, 3, 9, 9, 6, 15, 10, 3, 8, 8, 9, 10, 2, 9, 10]) == 3
    assert candidate([6, 9, 6, 7, 1, 4, 7, 1, 8, 8, 9, 8, 10, 10, 8, 4, 10, 4, 10, 1, 2, 9, 5, 7, 9]) == 1
    assert candidate([9, 2, 4, 1, 5, 1, 5, 2, 5, 7, 7, 7, 3, 10, 1, 5, 4, 2, 8, 4, 1, 9, 10, 7, 10, 2, 8, 10, 9, 4]) == 4
    assert candidate([1, 9, 10, 1, 3]) == 1
    assert candidate([8, 13, 3, 13, 2, 10, 6, 5, 8, 7, 14, 6, 3, 1, 4, 5, 8, 5]) == 1
    assert candidate([2, 8, 10, 14, 7, 3, 1, 9, 13, 6, 7, 6, 3, 10, 9, 7, 5, 10, 6, 8, 3, 1]) == 3
    assert candidate([4, 8, 10, 5, 1]) == 1
    assert candidate([14, 6, 8, 1, 2, 3, 6, 13, 10, 12, 1, 10, 6]) == 1
    assert candidate([9, 7, 4, 4, 2, 6, 3, 9, 8, 6, 6, 10, 4]) == -1
    assert candidate([8, 5, 3, 10, 3, 7, 7, 7, 4, 5, 11, 10, 6, 8, 5, 2, 14, 12, 12, 7, 11]) == -1
    assert candidate([6, 5, 8, 1, 1, 9, 10, 11, 3, 6, 11, 7]) == 1
    assert candidate([9, 4, 6, 7, 11, 6, 1, 4, 3, 7, 5]) == 1
    assert candidate([4, 1, 4, 1, 4, 4]) == 4
    assert candidate([5, 3, 7, 2]) == -1
    assert candidate([8, 8, 10, 6, 4, 3, 5, 8, 2, 4, 2, 8, 4, 6, 10, 4, 2, 1, 10, 2, 1, 1, 5]) == 4
    assert candidate([12, 4, 5, 8, 1, 8, 5, 4, 8, 2, 5, 4, 3, 12, 4, 1, 8, 8, 6, 5, 5, 4]) == 5
    assert candidate([4, 3, 7, 4, 4, 1]) == 1
    assert candidate([7, 4, 3, 6, 4, 5, 8, 8, 3, 11, 2, 7, 8, 8, 13, 9, 2, 2, 7, 6, 3, 10, 4]) == 3
    assert candidate([7, 5, 13, 5]) == -1
    assert candidate([3, 9, 7, 8, 10, 10, 7]) == -1
    assert candidate([10, 9, 13, 3, 6, 3, 7, 4, 3, 4, 8]) == 3
    assert candidate([2, 1, 6, 1, 9, 12, 7, 11, 4, 9, 5, 2, 3, 7, 10, 9, 5, 3, 2, 1, 3, 14, 9]) == 3
    assert candidate([6, 7, 14, 5, 6, 7, 4, 5, 6, 2, 3, 10, 4, 3, 10, 1, 3, 2, 9, 5, 3, 1, 7]) == 3
    assert candidate([7, 8, 5, 7, 8, 10, 7]) == -1
    assert candidate([6, 3]) == -1
    assert candidate([10, 9, 6, 10, 2, 7, 5, 10, 3, 2, 5, 13, 9, 5, 7, 5, 4, 5, 15, 2, 5, 1, 8]) == 5
    assert candidate([8, 13, 3, 6, 10, 3, 13, 3]) == 3
    assert candidate([4, 4, 7, 7, 7, 10, 14, 5, 6, 13, 14, 4, 7, 7, 2, 1, 3, 1]) == 1
    assert candidate([3, 13, 10, 12, 2, 4, 6, 1, 4, 6, 14, 5, 9, 5, 4, 5, 7, 1, 6, 4, 2, 7, 10, 4, 11]) == 4
    assert candidate([1, 6, 10, 1, 6, 9, 10, 8, 6, 8, 7, 3]) == 1
    assert candidate([7, 3, 3, 3, 7]) == 3
    assert candidate([6, 8, 1, 6, 12, 13, 10, 6, 2, 6, 6]) == 1
    assert candidate([6, 8, 9, 3, 1]) == 1
    assert candidate([6, 4, 5, 6, 4, 2, 13, 5, 6, 1, 7]) == 1
    assert candidate([3, 3, 3, 7, 3]) == 3
    assert candidate([12]) == -1
    assert candidate([3, 8, 9, 6, 5, 4, 14, 5, 7, 12, 10, 1]) == 1
    assert candidate([5, 13, 5, 1, 6]) == 1
    assert candidate([12, 7, 6, 9, 6, 5, 9, 6]) == -1
    assert candidate([9, 8, 1, 5, 9, 3, 8]) == 1
    assert candidate([12, 11, 4, 12, 7, 1, 4, 5, 14, 6, 4, 4, 4, 12, 8, 1, 7, 10, 4, 9, 11, 1]) == 4
    assert candidate([13, 6, 11, 9, 9, 7, 10, 11, 2, 7, 5, 9, 8, 2, 11, 2, 2, 1, 14, 6, 5, 4, 9]) == 2
    assert candidate([8, 8, 3, 6, 5, 6, 4]) == -1
    assert candidate([4, 6, 5, 2, 13, 8, 1, 5, 9, 7, 5, 5, 4, 2, 6, 12, 1, 5, 5, 7, 6, 14, 7]) == 5
    assert candidate([2, 10, 9, 12, 6, 8, 11, 3, 7, 13, 8, 8, 6, 11, 8, 1, 13, 1, 6, 4, 7, 12, 1, 8, 5]) == 1
    assert candidate([6, 7, 1, 8, 8, 10, 5, 8, 5, 3, 10]) == 1
    assert candidate([10]) == -1
    assert candidate([7, 10, 3, 12, 8, 2, 6, 1, 13, 1, 6, 10, 15, 2, 6, 5, 8, 2, 6, 8, 12]) == 2
    assert candidate([6, 8, 8, 1, 7]) == 1
    assert candidate([8, 2, 1, 7, 3, 4, 8, 4, 8, 8, 6, 14, 6, 8, 3, 2, 9, 10, 2, 9, 11]) == 2
    assert candidate([1, 2]) == 1
    assert candidate([5, 5, 3, 9, 5, 6, 3, 2, 8, 5, 6, 10, 10, 6, 8, 4, 10, 7, 7, 10, 8]) == -1
    assert candidate([11, 2, 9, 6, 2, 8, 7, 15, 12, 11, 10, 7, 4]) == 2
    assert candidate([13, 5, 9, 13, 4, 8, 10, 4, 9, 6, 10, 4, 13, 5, 5, 6, 7, 6]) == -1
    assert candidate([8]) == -1
    assert candidate([2, 3, 3, 2, 2]) == 2

    # automatically generated tests
    assert candidate([6, 5, 8, 6, 3, 13, 3, 1, 1, 11, 8, 5, 6, 8, 5, 6, 7, 6]) == 1
    assert candidate([1, 8, 6, 5, 7, 14, 8, 12, 6, 3, 12, 8]) == 1
    assert candidate([4, 15, 3, 12, 3, 8, 5, 5, 6, 6, 2, 6, 9, 5, 3, 8, 5, 9]) == 3
    assert candidate([6, 3, 9, 9, 5]) == -1
    assert candidate([9, 8, 6, 10, 2, 6, 10, 2, 7, 8, 10, 3, 8, 2, 6, 2, 3, 1]) == 2
    assert candidate([7, 4, 1, 4, 1]) == 1
    assert candidate([4, 5, 10, 1, 2]) == 1
    assert candidate([6, 4, 6, 6, 1, 4, 2, 4, 5, 9, 10, 9, 9, 13, 12, 6, 6, 8, 13, 2, 6, 10, 6, 10, 4]) == 6
    assert candidate([3]) == -1
    assert candidate([6, 6, 6, 7, 3]) == -1
    assert candidate([2, 6, 4, 2, 8, 7, 5, 6, 4, 10, 4, 6, 3, 7, 8, 8, 3, 1, 4, 2, 2, 10, 7]) == 4
    assert candidate([8, 3]) == -1
    assert candidate([7, 1, 8, 5, 1, 1, 7, 6, 5, 6, 8]) == 1
    assert candidate([8, 3, 15, 4, 3, 3, 5, 7, 10, 3, 5]) == 3
    assert candidate([5, 10, 4, 9, 13, 7, 2, 3, 12, 10, 5, 6, 4, 6, 12, 7, 4, 11, 2, 9, 10, 2, 3, 12]) == 2
    assert candidate([4, 1, 8, 5, 9, 9]) == 1
    assert candidate([9, 7, 7, 2, 4, 7, 2, 10, 9, 7, 5, 7, 2]) == 2
    assert candidate([9, 4, 5, 1, 3, 3, 2]) == 1
    assert candidate([13, 10, 5, 5, 1, 3, 14, 5, 9, 5, 13, 5, 11, 5, 3, 1, 3, 4]) == 5
    assert candidate([11, 6, 12, 12, 4, 3, 4, 4, 8, 2, 1, 1, 2, 13, 11, 6, 5, 11, 7, 11, 10, 11]) == 2
    assert candidate([10, 7, 9, 4, 7, 8, 10, 12, 4, 9, 4, 7, 5, 4, 11, 8, 6, 4, 14, 5, 1, 1, 2]) == 4
    assert candidate([8, 5, 4, 4, 10, 5, 8, 8]) == -1
    assert candidate([3, 11, 2, 3, 4, 12, 5, 5, 7, 10, 7, 3, 3, 7, 7, 7, 5, 12]) == 3
    assert candidate([7, 9, 9, 9, 3, 4, 1, 5, 9, 1, 2, 1, 1, 10, 7, 5, 6, 7, 6, 7, 7, 6]) == 1
    assert candidate([11]) == -1
    assert candidate([6]) == -1
    assert candidate([8, 8, 8, 8, 8, 8, 8, 8]) == 8
    assert candidate([8, 7, 9, 9, 3, 4, 9, 5, 9, 10, 11, 10, 7, 11, 6, 7, 13, 5, 11, 5, 3, 8, 10, 7, 9]) == -1
    assert candidate([6, 8, 9, 6, 13, 10, 4, 8, 8, 5, 8, 5, 3, 8, 6, 10, 4, 2, 6, 2, 2, 10, 8]) == 2
    assert candidate([4, 3, 9, 6]) == -1
    assert candidate([14, 1, 5, 6, 7, 3, 1, 1, 3, 7, 7, 2, 3, 6, 3, 6, 8, 1, 7, 4, 4, 12, 11, 3, 7, 4, 4, 8, 13, 5]) == 4
    assert candidate([13, 10, 7, 5, 4, 10, 3, 13, 12, 9, 5, 9, 4]) == -1
    assert candidate([3, 6, 8, 6]) == -1
    assert candidate([8, 3, 7, 7]) == -1

if __name__ == '__main__':
    check(search)