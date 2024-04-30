from case_MBPP_403 import mul_even_odd


def check(candidate):
    assert candidate([1,3,5,7,4,1,6,8])==4
    assert candidate([1,2,3,4,5,6,7,8,9,10])==2
    assert candidate([1,5,7,9,10])==10
    assert candidate([5, 1, 6, 10, 6, 2, 4, 3]) == 30
    assert candidate([5, 3, 6, 6, 3, 2, 8, 5]) == 30
    assert candidate([2, 8, 4, 6, 7, 6, 2, 8]) == 14
    assert candidate([4, 1, 2, 12, 6, 6, 7, 4]) == 4
    assert candidate([1, 4, 4, 8, 2, 4, 7, 6]) == 4
    assert candidate([5, 8, 3, 12, 2, 2, 7, 7]) == 40
    assert candidate([6, 8, 6, 6, 5, 3, 2, 7]) == 30
    assert candidate([4, 8, 4, 2, 6, 6, 6, 4]) == -4
    assert candidate([4, 4, 9, 7, 4, 5, 7, 7]) == 36
    assert candidate([5, 5, 2, 12, 3, 4, 6, 13]) == 10
    assert candidate([2, 2, 9, 11, 7, 6, 3, 8]) == 18
    assert candidate([5, 4, 1, 8, 1, 3, 8, 11]) == 20
    assert candidate([4, 3, 5, 3, 9, 2, 5, 7]) == 12
    assert candidate([1, 3, 5, 4, 2, 3, 6, 6]) == 4
    assert candidate([5, 3, 2, 8, 8, 5, 1, 4]) == 10
    assert candidate([6, 1, 1, 10, 5, 5, 1, 3]) == 6
    assert candidate([4, 7, 1, 11, 9, 1, 4, 11]) == 28
    assert candidate([5, 8, 9, 7, 4, 3, 7, 3]) == 40
    assert candidate([1, 3, 9, 3, 6, 4, 4, 7]) == 6
    assert candidate([3, 6, 6, 10, 3, 3, 6, 10]) == 18
    assert candidate([2, 6, 4, 9, 1, 1, 2, 10]) == 18
    assert candidate([1, 5, 3, 4, 9, 4, 9, 6]) == 4
    assert candidate([1, 8, 3, 10, 2, 6, 5, 13]) == 8
    assert candidate([5, 2, 7, 6, 2, 5, 1, 9]) == 10
    assert candidate([3, 4, 4, 8, 2, 2, 7, 13]) == 12
    assert candidate([3, 6, 3, 8, 3, 5, 11, 12]) == 18
    assert candidate([1, 7, 4, 4, 9, 1, 1, 7]) == 4
    assert candidate([2, 7, 3, 12, 9, 2, 2, 5]) == 14
    assert candidate([1, 6, 1, 7, 4, 4, 7, 6]) == 6
    assert candidate([6, 5, 6, 8, 3, 3, 8, 5]) == 30
    assert candidate([5, 2, 5, 10, 3, 3, 11, 6]) == 10
    assert candidate([6, 8, 10, 3, 9, 3, 6, 12]) == 18
    assert candidate([1, 7, 4, 2, 5, 3, 8, 4]) == 4
    assert candidate([5, 6, 4, 6, 9, 4, 7, 11, 7, 6]) == 30
    assert candidate([6, 5, 3, 4, 9, 2, 12, 7, 13, 13]) == 30
    assert candidate([3, 2, 2, 8, 9, 5, 3, 11, 10, 10]) == 6
    assert candidate([6, 1, 2, 6, 9, 11, 8, 11, 11, 13]) == 6
    assert candidate([3, 7, 6, 8, 9, 4, 2, 7, 10, 12]) == 18
    assert candidate([5, 1, 7, 5, 1, 11, 4, 5, 12, 8]) == 20
    assert candidate([3, 5, 7, 1, 4, 9, 6, 4, 8, 10]) == 12
    assert candidate([3, 3, 3, 4, 8, 11, 6, 4, 9, 8]) == 12
    assert candidate([2, 4, 8, 1, 7, 11, 8, 3, 6, 13]) == 2
    assert candidate([6, 3, 5, 6, 7, 11, 10, 12, 11, 12]) == 18
    assert candidate([3, 7, 1, 1, 2, 11, 11, 9, 10, 5]) == 6
    assert candidate([3, 1, 3, 5, 5, 4, 4, 3, 14, 12]) == 12
    assert candidate([1, 6, 1, 9, 2, 8, 9, 13, 7, 7]) == 6
    assert candidate([3, 1, 3, 7, 5, 7, 9, 9, 11, 13]) == -3
    assert candidate([4, 5, 5, 5, 7, 11, 3, 12, 9, 8]) == 20
    assert candidate([4, 3, 7, 7, 2, 7, 5, 4, 10, 6]) == 12
    assert candidate([3, 6, 5, 3, 2, 1, 6, 11, 14, 14]) == 18
    assert candidate([3, 7, 3, 8, 1, 4, 9, 6, 9, 6]) == 24
    assert candidate([5, 3, 4, 3, 6, 5, 7, 8, 12, 14]) == 20
    assert candidate([5, 4, 3, 7, 10, 6, 11, 8, 7, 12]) == 20
    assert candidate([3, 7, 3, 8, 4, 5, 2, 10, 9, 10]) == 24
    assert candidate([2, 6, 4, 9, 7, 4, 8, 5, 4, 15]) == 18
    assert candidate([6, 1, 4, 9, 3, 11, 11, 10, 8, 13]) == 6
    assert candidate([6, 1, 4, 9, 2, 2, 8, 5, 13, 9]) == 6
    assert candidate([4, 1, 1, 6, 6, 8, 3, 7, 12, 7]) == 4
    assert candidate([2, 7, 4, 2, 5, 1, 4, 10, 11, 13]) == 14
    assert candidate([3, 3, 1, 8, 10, 4, 7, 8, 9, 11]) == 24
    assert candidate([2, 6, 6, 6, 4, 3, 2, 5, 10, 15]) == 6
    assert candidate([4, 1, 7, 3, 8, 7, 8, 12, 14, 8]) == 4
    assert candidate([6, 5, 3, 5, 2, 10, 6, 7, 8, 7]) == 30
    assert candidate([5, 3, 7, 6, 8, 10, 12, 4, 8, 12]) == 30
    assert candidate([6, 4, 6, 7, 10, 6, 5, 11, 4, 12]) == 42
    assert candidate([3, 1, 2, 2, 1, 1, 12, 5, 8, 10]) == 6
    assert candidate([3, 1, 2, 9, 11]) == 6
    assert candidate([5, 7, 8, 11, 14]) == 40
    assert candidate([6, 6, 2, 6, 14]) == -6
    assert candidate([1, 6, 11, 5, 11]) == 6
    assert candidate([6, 4, 8, 8, 6]) == -6
    assert candidate([2, 9, 2, 13, 10]) == 18
    assert candidate([5, 1, 11, 9, 11]) == -5
    assert candidate([3, 6, 5, 4, 7]) == 18
    assert candidate([1, 10, 7, 8, 11]) == 10
    assert candidate([6, 10, 5, 14, 15]) == 30
    assert candidate([5, 6, 6, 8, 9]) == 30
    assert candidate([1, 6, 3, 14, 7]) == 6
    assert candidate([4, 7, 9, 12, 15]) == 28
    assert candidate([2, 8, 7, 4, 6]) == 14
    assert candidate([3, 3, 8, 13, 14]) == 24
    assert candidate([2, 4, 4, 12, 15]) == 30
    assert candidate([4, 8, 9, 6, 10]) == 36
    assert candidate([1, 10, 5, 7, 5]) == 10
    assert candidate([2, 6, 11, 14, 15]) == 22
    assert candidate([6, 4, 11, 13, 13]) == 66
    assert candidate([6, 3, 10, 5, 8]) == 18
    assert candidate([2, 4, 3, 4, 12]) == 6
    assert candidate([2, 4, 4, 4, 10]) == -2
    assert candidate([6, 5, 5, 4, 14]) == 30
    assert candidate([1, 4, 11, 10, 13]) == 4
    assert candidate([6, 10, 3, 4, 5]) == 18
    assert candidate([4, 1, 12, 14, 10]) == 4
    assert candidate([4, 8, 4, 6, 12]) == -4
    assert candidate([5, 2, 10, 14, 5]) == 10
    assert candidate([4, 7, 11, 5, 7]) == 28
    assert candidate([4, 10, 2, 7, 8]) == 28
    assert candidate([3, 4, 11, 13, 11]) == 12
    assert candidate([4, 10, 2, 6, 12]) == -4

if __name__ == '__main__':
    check(mul_even_odd)