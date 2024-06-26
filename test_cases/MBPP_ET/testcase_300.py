from case_MBPP_300 import diff_even_odd


def check(candidate):
    assert candidate([1,3,5,7,4,1,6,8])==3
    assert candidate([1,2,3,4,5,6,7,8,9,10])==1
    assert candidate([1,5,7,9,10])==9
    assert candidate([5, 1, 3, 6, 7, 3, 5, 4]) == 1
    assert candidate([3, 6, 7, 7, 8, 6, 8, 13]) == 3
    assert candidate([5, 3, 1, 11, 6, 2, 10, 4]) == 1
    assert candidate([1, 1, 1, 8, 4, 2, 11, 5]) == 7
    assert candidate([5, 6, 5, 10, 1, 1, 1, 10]) == 1
    assert candidate([1, 2, 4, 7, 4, 2, 2, 13]) == 1
    assert candidate([5, 7, 9, 6, 5, 1, 9, 13]) == 1
    assert candidate([6, 3, 2, 5, 5, 4, 2, 9]) == 3
    assert candidate([4, 6, 8, 8, 3, 5, 10, 4]) == 1
    assert candidate([4, 6, 9, 12, 1, 4, 2, 8]) == -5
    assert candidate([5, 3, 7, 8, 2, 4, 11, 3]) == 3
    assert candidate([5, 8, 5, 8, 7, 1, 3, 12]) == 3
    assert candidate([1, 6, 8, 11, 4, 1, 7, 11]) == 5
    assert candidate([6, 2, 9, 7, 2, 5, 8, 12]) == -3
    assert candidate([5, 4, 2, 4, 6, 4, 7, 13]) == -1
    assert candidate([6, 2, 5, 2, 2, 5, 11, 13]) == 1
    assert candidate([2, 1, 9, 6, 1, 4, 7, 9]) == 1
    assert candidate([3, 4, 4, 4, 9, 1, 9, 5]) == 1
    assert candidate([3, 8, 7, 7, 3, 2, 5, 12]) == 5
    assert candidate([4, 6, 9, 11, 8, 5, 4, 3]) == -5
    assert candidate([3, 5, 3, 10, 7, 1, 6, 13]) == 7
    assert candidate([6, 1, 1, 2, 1, 5, 4, 3]) == 5
    assert candidate([6, 5, 2, 12, 5, 2, 2, 5]) == 1
    assert candidate([6, 2, 3, 5, 1, 1, 6, 9]) == 3
    assert candidate([3, 8, 1, 5, 4, 1, 8, 9]) == 5
    assert candidate([5, 7, 4, 6, 5, 6, 10, 11]) == -1
    assert candidate([1, 1, 2, 2, 4, 3, 8, 12]) == 1
    assert candidate([6, 2, 4, 2, 7, 5, 3, 4]) == -1
    assert candidate([1, 4, 9, 12, 8, 5, 9, 11]) == 3
    assert candidate([5, 8, 9, 4, 2, 4, 3, 12]) == 3
    assert candidate([1, 2, 2, 8, 4, 1, 11, 3]) == 1
    assert candidate([6, 2, 10, 11, 6, 4, 3, 13]) == -5
    assert candidate([1, 7, 6, 5, 2, 1, 3, 10]) == 5
    assert candidate([3, 7, 3, 8, 6, 5, 9, 8, 7, 15]) == 5
    assert candidate([4, 1, 5, 9, 9, 4, 8, 3, 10, 8]) == 3
    assert candidate([5, 6, 5, 6, 7, 10, 2, 4, 11, 12]) == 1
    assert candidate([4, 6, 1, 4, 10, 6, 12, 6, 12, 8]) == 3
    assert candidate([6, 6, 2, 2, 9, 5, 10, 12, 10, 15]) == -3
    assert candidate([6, 4, 2, 3, 6, 3, 5, 5, 4, 10]) == 3
    assert candidate([4, 1, 7, 6, 3, 11, 9, 11, 14, 14]) == 3
    assert candidate([6, 3, 1, 2, 3, 1, 11, 3, 5, 10]) == 3
    assert candidate([4, 4, 4, 6, 5, 7, 10, 10, 10, 5]) == -1
    assert candidate([1, 1, 6, 2, 4, 10, 5, 5, 4, 5]) == 5
    assert candidate([6, 3, 4, 8, 7, 2, 6, 3, 13, 9]) == 3
    assert candidate([2, 5, 4, 9, 3, 7, 10, 6, 4, 6]) == -3
    assert candidate([3, 1, 7, 9, 1, 4, 6, 12, 13, 15]) == 1
    assert candidate([2, 5, 6, 3, 9, 4, 6, 11, 4, 8]) == -3
    assert candidate([3, 5, 4, 4, 10, 4, 9, 6, 6, 14]) == 1
    assert candidate([6, 6, 3, 6, 9, 8, 4, 6, 9, 5]) == 3
    assert candidate([6, 5, 7, 7, 2, 3, 9, 9, 9, 5]) == 1
    assert candidate([6, 2, 5, 4, 5, 11, 12, 3, 11, 9]) == 1
    assert candidate([1, 4, 4, 7, 3, 3, 3, 11, 8, 7]) == 3
    assert candidate([1, 6, 8, 9, 9, 10, 7, 7, 4, 7]) == 5
    assert candidate([3, 4, 2, 1, 8, 7, 6, 9, 14, 15]) == 1
    assert candidate([5, 7, 5, 1, 1, 5, 5, 5, 4, 13]) == -1
    assert candidate([5, 2, 7, 4, 2, 10, 9, 7, 12, 13]) == -3
    assert candidate([6, 1, 1, 8, 4, 7, 6, 13, 7, 6]) == 5
    assert candidate([5, 6, 7, 7, 10, 11, 8, 9, 5, 8]) == 1
    assert candidate([5, 6, 5, 3, 8, 10, 12, 7, 10, 15]) == 1
    assert candidate([6, 4, 6, 5, 1, 2, 4, 4, 6, 9]) == 1
    assert candidate([3, 6, 3, 1, 10, 5, 11, 12, 5, 5]) == 3
    assert candidate([2, 2, 4, 1, 4, 7, 10, 4, 13, 11]) == 1
    assert candidate([5, 1, 6, 1, 6, 9, 2, 6, 6, 9]) == 1
    assert candidate([4, 5, 8, 2, 5, 9, 10, 8, 12, 11]) == -1
    assert candidate([4, 4, 1, 2, 2, 5, 8, 10, 6, 8]) == 3
    assert candidate([4, 1, 2, 6, 8, 9, 8, 12, 14, 15]) == 3
    assert candidate([4, 2, 9, 10, 7]) == -5
    assert candidate([1, 7, 7, 8, 8]) == 7
    assert candidate([6, 7, 2, 6, 5]) == -1
    assert candidate([6, 6, 8, 5, 10]) == 1
    assert candidate([5, 7, 12, 10, 13]) == 7
    assert candidate([6, 5, 4, 14, 5]) == 1
    assert candidate([4, 9, 5, 10, 9]) == -5
    assert candidate([3, 9, 12, 12, 13]) == 9
    assert candidate([6, 5, 7, 8, 9]) == 1
    assert candidate([3, 10, 9, 6, 6]) == 7
    assert candidate([1, 1, 3, 7, 8]) == 7
    assert candidate([4, 10, 12, 8, 15]) == -11
    assert candidate([2, 3, 3, 13, 15]) == -1
    assert candidate([2, 9, 2, 7, 6]) == -7
    assert candidate([3, 4, 2, 13, 10]) == 1
    assert candidate([3, 8, 2, 12, 15]) == 5
    assert candidate([4, 4, 6, 11, 5]) == -7
    assert candidate([2, 5, 2, 10, 9]) == -3
    assert candidate([4, 8, 2, 6, 6]) == 5
    assert candidate([4, 3, 11, 11, 10]) == 1
    assert candidate([4, 8, 8, 4, 8]) == 5
    assert candidate([3, 7, 8, 7, 12]) == 5
    assert candidate([3, 4, 8, 11, 13]) == 1
    assert candidate([6, 7, 12, 10, 7]) == -1
    assert candidate([1, 2, 3, 11, 7]) == 1
    assert candidate([1, 2, 8, 7, 5]) == 1
    assert candidate([5, 8, 5, 13, 15]) == 3
    assert candidate([2, 1, 11, 9, 14]) == 1
    assert candidate([6, 1, 11, 7, 9]) == 5
    assert candidate([5, 1, 3, 7, 8]) == 3
    assert candidate([4, 7, 2, 9, 8]) == -3
    assert candidate([2, 7, 6, 12, 14]) == -5
    assert candidate([4, 8, 4, 14, 5]) == -1

if __name__ == '__main__':
    check(diff_even_odd)