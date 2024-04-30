from case_MBPP_347 import count_same_pair


def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
    assert candidate([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8],[2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==11
    assert candidate([2, 4, -6, -9, 11, -12, 14, -5, 17],[2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==1
    assert candidate([6, 1, 4, 8, 4, 6, 11, 8], [3, 4, 6, 2, 2, 9, 9, 14]) == 0
    assert candidate([1, 2, 7, 4, 8, 3, 12, 7], [2, 2, 8, 1, 5, 1, 6, 5]) == 1
    assert candidate([6, 1, 6, 8, 3, 2, 12, 5], [6, 4, 7, 1, 5, 3, 11, 12]) == 1
    assert candidate([6, 5, 1, 4, 7, 11, 6, 9], [3, 4, 4, 4, 3, 4, 3, 6]) == 1
    assert candidate([1, 3, 2, 1, 4, 9, 4, 13], [1, 2, 7, 5, 7, 6, 12, 6]) == 1
    assert candidate([5, 5, 3, 9, 10, 9, 7, 4], [7, 3, 4, 2, 3, 8, 2, 11]) == 0
    assert candidate([3, 2, 1, 3, 9, 9, 5, 7], [7, 7, 3, 5, 7, 2, 4, 14]) == 0
    assert candidate([5, 4, 6, 2, 1, 7, 9, 10], [6, 2, 8, 1, 7, 4, 9, 5]) == 1
    assert candidate([5, 5, 8, 4, 10, 3, 2, 7], [7, 7, 7, 5, 7, 3, 9, 6]) == 1
    assert candidate([5, 6, 2, 3, 6, 2, 6, 5], [2, 5, 4, 5, 6, 9, 4, 13]) == 1
    assert candidate([5, 4, 1, 5, 8, 5, 3, 13], [7, 7, 2, 6, 2, 7, 11, 6]) == 0
    assert candidate([3, 3, 5, 1, 2, 8, 7, 4], [5, 5, 2, 1, 5, 3, 3, 11]) == 1
    assert candidate([6, 4, 6, 8, 7, 4, 4, 7], [3, 1, 2, 5, 3, 5, 11, 13]) == 0
    assert candidate([6, 1, 2, 2, 2, 5, 9, 8], [3, 2, 1, 4, 2, 10, 4, 6]) == 1
    assert candidate([5, 2, 3, 4, 9, 2, 9, 3], [6, 6, 7, 3, 5, 10, 6, 6]) == 0
    assert candidate([2, 6, 1, 4, 5, 4, 12, 7], [6, 7, 4, 4, 1, 5, 12, 8]) == 2
    assert candidate([3, 2, 3, 2, 8, 7, 7, 3], [1, 7, 7, 2, 6, 9, 6, 7]) == 1
    assert candidate([1, 4, 7, 1, 5, 9, 6, 10], [1, 4, 3, 5, 5, 6, 9, 7]) == 3
    assert candidate([3, 7, 5, 3, 10, 10, 10, 13], [3, 3, 1, 4, 6, 2, 6, 9]) == 1
    assert candidate([1, 6, 6, 5, 8, 5, 9, 11], [2, 3, 2, 3, 2, 8, 3, 10]) == 0
    assert candidate([5, 3, 5, 1, 7, 8, 5, 12], [4, 4, 5, 4, 2, 8, 2, 9]) == 2
    assert candidate([2, 2, 7, 6, 10, 1, 8, 11], [4, 7, 3, 1, 5, 2, 9, 6]) == 0
    assert candidate([2, 5, 4, 8, 2, 2, 5, 4], [3, 5, 7, 4, 3, 10, 7, 11]) == 1
    assert candidate([6, 4, 4, 1, 7, 2, 5, 10], [2, 3, 2, 2, 1, 2, 12, 7]) == 1
    assert candidate([3, 7, 8, 9, 9, 2, 10, 11], [4, 6, 4, 2, 4, 7, 3, 9]) == 0
    assert candidate([3, 5, 8, 5, 10, 11, 10, 12], [4, 4, 4, 1, 5, 7, 7, 4]) == 0
    assert candidate([1, 6, 6, 9, 3, 6, 11, 12], [1, 1, 4, 6, 4, 11, 2, 12]) == 2
    assert candidate([1, 5, 6, 3, 5, 7, 12, 11], [6, 4, 6, 2, 5, 3, 10, 9]) == 2
    assert candidate([6, 4, 1, 6, 7, 8, 12, 6], [2, 2, 4, 3, 5, 2, 12, 9]) == 1
    assert candidate([6, 1, 2, 3, 1, 9, 11, 13], [4, 6, 3, 1, 3, 7, 10, 9]) == 0
    assert candidate([6, 7, 4, 2, 3, 7, 4, 13], [2, 6, 4, 1, 6, 7, 7, 8]) == 2
    assert candidate([4, 6, 2, 9, 4, 3, 9, 7], [4, 2, 3, 6, 1, 2, 7, 8]) == 1
    assert candidate([6, 5, 2, 4, 3, 10, 2, 3], [6, 6, 8, 6, 6, 7, 9, 10]) == 1
    assert candidate([2, 3, 2, -3, -6, 1, 3, -3, 2, 3, 8, 7, 8], [4, 3, 4, -6, -4, 5, 5, -7, 0, 1, 1, 6, 12]) == 1
    assert candidate([2, 5, 5, 0, -4, 9, 4, -2, -3, 2, 3, 4, 4], [4, 4, 6, -5, -6, 9, 4, -5, -3, 3, 3, 5, 9]) == 4
    assert candidate([5, 3, 2, 4, 0, 8, 4, -7, 2, 7, 5, 4, 13], [7, 5, 1, 4, -7, 7, 2, -2, -3, 4, 5, 5, 7]) == 2
    assert candidate([3, 5, 6, 3, -8, 1, 2, -5, 1, 3, 4, 8, 3], [4, 1, 4, -4, -2, 11, 6, -2, -1, 4, 4, 1, 11]) == 1
    assert candidate([3, 1, 7, 1, -2, 3, 3, -4, 0, 7, 9, 10, 7], [5, 4, 4, 2, -1, 5, 6, -8, -4, 8, 6, 8, 3]) == 0
    assert candidate([5, 4, 5, -2, 0, 8, 1, -6, -4, 4, 6, 1, 8], [2, 4, 4, 3, 0, 7, 8, -3, -5, 8, 4, 8, 4]) == 2
    assert candidate([3, 2, 5, -1, -6, 10, 3, -7, -1, 7, 1, 5, 6], [2, 5, 2, -1, -3, 9, 5, -3, -4, 8, 7, 8, 10]) == 1
    assert candidate([3, 5, 7, 4, -9, 9, 1, 2, -3, 1, 4, 11, 13], [2, 3, 2, 3, -10, 5, 5, -7, -6, 8, 9, 9, 6]) == 0
    assert candidate([3, 3, 2, 3, -3, 4, 3, -4, 2, 3, 9, 10, 8], [6, 5, 4, -4, -9, 6, 2, -8, 2, 1, 2, 9, 10]) == 1
    assert candidate([3, 1, 5, 0, -7, 1, 3, -1, -1, 5, 7, 8, 9], [3, 6, 1, -4, -5, 7, 3, -4, 0, 8, 8, 11, 11]) == 2
    assert candidate([5, 2, 2, -5, -5, 11, 3, 2, -1, 5, 8, 7, 4], [6, 4, 5, 2, -2, 6, 5, 2, -4, 3, 3, 2, 8]) == 1
    assert candidate([4, 5, 1, 2, -5, 1, 5, -6, -1, 2, 3, 10, 3], [2, 5, 7, -3, -5, 10, 4, -8, -7, 5, 1, 1, 12]) == 2
    assert candidate([2, 2, 4, -1, -9, 11, 4, 0, -1, 7, 1, 11, 12], [5, 2, 7, -3, -5, 5, 6, -3, -7, 7, 3, 2, 7]) == 2
    assert candidate([1, 1, 6, -6, -9, 11, 3, -5, -1, 6, 3, 11, 4], [2, 1, 4, -1, -10, 4, 5, -2, -2, 7, 2, 5, 8]) == 1
    assert candidate([4, 2, 5, 1, -5, 9, 4, -3, -3, 7, 7, 3, 12], [5, 1, 2, -6, -6, 5, 8, -4, -5, 4, 2, 3, 10]) == 1
    assert candidate([1, 1, 2, 0, -8, 10, 4, -3, 3, 6, 9, 11, 10], [6, 6, 7, -4, -10, 6, 7, -3, 1, 7, 5, 5, 5]) == 1
    assert candidate([5, 2, 1, 3, -1, 3, 1, -3, 3, 7, 9, 9, 3], [3, 1, 2, -6, -4, 2, 9, -1, 0, 8, 2, 1, 5]) == 0
    assert candidate([2, 1, 3, -5, -7, 1, 2, 1, 2, 4, 6, 5, 3], [2, 2, 6, -3, -1, 9, 3, -1, -5, 7, 8, 8, 7]) == 1
    assert candidate([2, 3, 6, 0, -9, 3, 4, 1, -2, 5, 7, 1, 12], [5, 4, 1, -2, -1, 8, 3, -2, -4, 1, 4, 8, 8]) == 0
    assert candidate([1, 5, 2, -1, -8, 6, 4, -1, -7, 3, 8, 9, 3], [5, 6, 1, 4, -6, 3, 9, 2, -4, 8, 1, 6, 11]) == 0
    assert candidate([3, 5, 3, 0, 0, 7, 5, -4, -5, 1, 3, 8, 7], [1, 1, 5, -4, -7, 6, 2, -6, 2, 1, 3, 10, 9]) == 2
    assert candidate([3, 4, 4, -3, 0, 10, 4, 2, -6, 5, 4, 4, 11], [6, 1, 2, -1, -3, 2, 7, -6, -2, 7, 5, 2, 6]) == 0
    assert candidate([2, 4, 5, 2, -8, 4, 3, 1, -7, 8, 7, 10, 5], [1, 4, 7, 2, -8, 4, 2, -4, 3, 4, 9, 2, 7]) == 4
    assert candidate([5, 6, 6, 2, -6, 2, 4, 0, -7, 1, 4, 2, 10], [1, 2, 2, 4, -10, 1, 7, -2, -3, 4, 3, 5, 7]) == 0
    assert candidate([3, 6, 4, 1, -10, 11, 1, 0, -4, 6, 3, 6, 9], [4, 5, 1, -1, 0, 6, 5, 1, -3, 8, 8, 7, 13]) == 0
    assert candidate([1, 1, 4, -1, -8, 7, 5, -5, -5, 3, 3, 2, 7], [2, 2, 4, -4, -10, 11, 3, -2, 0, 5, 2, 7, 3]) == 1
    assert candidate([5, 4, 4, 2, -7, 11, 2, -4, -4, 2, 3, 2, 9], [7, 1, 6, -2, -1, 9, 8, 1, 0, 4, 7, 10, 11]) == 0
    assert candidate([4, 1, 7, 2, -3, 10, 3, -1, -5, 5, 2, 2, 13], [7, 6, 3, -2, -10, 6, 4, -5, 2, 1, 1, 6, 3]) == 0
    assert candidate([3, 2, 2, 4, -3, 11, 2, -8, 0, 1, 4, 8, 4], [7, 1, 4, 1, -7, 7, 4, 1, 1, 7, 2, 8, 12]) == 1
    assert candidate([1, 3, 2, -3, -2, 2, 3, -5, 0, 2, 1, 1, 11], [2, 6, 2, -6, 0, 1, 6, -3, -4, 7, 8, 6, 13]) == 1
    assert candidate([3, 5, 5, 4, -1, 6, 2, -7, 0, 1, 8, 2, 7], [2, 2, 6, 1, -10, 5, 6, -2, 3, 1, 5, 9, 11]) == 1
    assert candidate([4, 1, 4, 2, -7, 6, 3, -2, -5, 2, 8, 7, 10], [1, 2, 7, -5, 0, 8, 5, -8, 2, 5, 5, 7, 10]) == 2
    assert candidate([5, 3, 5, -5, -10, 2, 2, 2, -6, 6, 9, 3, 6], [5, 2, 2, 4, -10, 5, 6, 1, -6, 8, 8, 5, 7]) == 3
    assert candidate([7, 1, -4, -5, 12, -7, 9, -5, 17], [1, 4, 1, 3, -8, 4, 9, -7, -4, 3, 9, 10, 13]) == 1
    assert candidate([1, 3, -10, -8, 7, -11, 18, -6, 13], [2, 2, 3, -3, -5, 7, 7, -1, -3, 6, 6, 8, 13]) == 0
    assert candidate([5, 9, -6, -11, 6, -9, 9, -5, 19], [2, 2, 5, -6, -10, 4, 4, -8, -2, 1, 1, 10, 6]) == 0
    assert candidate([7, 2, -7, -9, 6, -10, 15, -10, 12], [3, 2, 7, -4, -1, 1, 6, -6, 1, 7, 9, 6, 5]) == 1
    assert candidate([2, 7, -11, -12, 13, -10, 17, -10, 19], [3, 1, 2, 0, -5, 9, 9, -1, 1, 2, 4, 1, 7]) == 0
    assert candidate([7, 5, -2, -14, 15, -12, 11, -4, 18], [1, 2, 4, -5, -10, 4, 2, 2, -1, 1, 5, 7, 3]) == 0
    assert candidate([1, 7, -6, -4, 15, -15, 16, -8, 22], [2, 6, 7, 0, -1, 9, 3, -4, -1, 7, 8, 3, 12]) == 0
    assert candidate([2, 7, -8, -13, 8, -8, 15, 0, 22], [3, 3, 7, 2, -9, 4, 7, 0, -6, 8, 1, 1, 10]) == 1
    assert candidate([1, 1, -7, -10, 13, -13, 12, -7, 17], [4, 5, 2, -4, -5, 2, 1, -7, -4, 2, 1, 7, 5]) == 1
    assert candidate([2, 7, -2, -14, 8, -16, 19, -2, 18], [7, 3, 4, -6, -5, 9, 5, 1, 3, 1, 6, 11, 10]) == 0
    assert candidate([6, 1, -11, -9, 14, -13, 16, -6, 18], [6, 4, 2, -5, -3, 7, 3, -8, -4, 5, 5, 11, 4]) == 1
    assert candidate([1, 6, -6, -11, 12, -12, 10, -6, 13], [3, 4, 7, -3, -7, 3, 7, -5, -7, 5, 5, 7, 11]) == 0
    assert candidate([3, 8, -2, -4, 9, -8, 12, -8, 22], [3, 3, 1, 0, -3, 11, 5, -6, -6, 5, 3, 7, 12]) == 1
    assert candidate([3, 8, -10, -12, 8, -10, 17, 0, 21], [6, 6, 6, 2, 0, 3, 3, 1, 0, 6, 1, 6, 7]) == 0
    assert candidate([4, 9, -10, -13, 11, -15, 14, -10, 17], [7, 4, 4, -2, -8, 2, 6, 2, -7, 6, 4, 9, 5]) == 0
    assert candidate([3, 1, -7, -9, 14, -12, 16, -3, 22], [1, 2, 6, 3, -5, 6, 7, -1, 1, 2, 7, 5, 12]) == 0
    assert candidate([3, 2, -2, -7, 8, -7, 17, -9, 18], [7, 6, 5, -4, -9, 3, 5, -7, -2, 7, 8, 11, 4]) == 0
    assert candidate([1, 5, -7, -9, 9, -17, 13, -3, 17], [1, 3, 3, -2, -7, 9, 9, -6, -1, 1, 1, 4, 13]) == 1
    assert candidate([7, 6, -1, -13, 9, -14, 17, -7, 19], [1, 6, 1, 3, -10, 2, 9, -2, -1, 8, 7, 11, 12]) == 1
    assert candidate([5, 2, -5, -12, 8, -16, 9, -8, 15], [6, 1, 2, 2, -4, 11, 7, -7, -5, 1, 5, 7, 5]) == 0
    assert candidate([1, 4, -6, -6, 12, -16, 18, -7, 21], [2, 6, 7, 0, -10, 4, 7, -5, -5, 8, 2, 10, 3]) == 0
    assert candidate([3, 8, -2, -12, 13, -12, 19, 0, 12], [5, 1, 1, 0, -7, 4, 8, -8, -4, 2, 9, 4, 4]) == 0
    assert candidate([6, 1, -11, -10, 8, -14, 15, -2, 19], [3, 6, 5, -1, -1, 1, 1, -1, 1, 7, 6, 6, 10]) == 0
    assert candidate([7, 5, -11, -5, 7, -15, 18, -7, 21], [1, 3, 2, 1, 0, 8, 4, -7, -4, 2, 3, 11, 9]) == 1
    assert candidate([2, 9, -5, -11, 6, -7, 14, -7, 13], [7, 2, 1, -3, -3, 9, 6, -2, -3, 2, 2, 5, 12]) == 0
    assert candidate([3, 7, -10, -12, 7, -16, 15, 0, 13], [2, 6, 4, -3, -3, 3, 9, -2, -2, 8, 3, 1, 8]) == 0
    assert candidate([3, 1, -7, -11, 16, -17, 14, -3, 16], [5, 6, 1, -4, -10, 9, 2, -4, 1, 8, 5, 8, 4]) == 0
    assert candidate([1, 3, -1, -9, 10, -7, 19, -3, 15], [2, 5, 4, 2, -7, 9, 9, -2, -6, 1, 3, 7, 10]) == 0
    assert candidate([2, 3, -6, -14, 13, -16, 14, -7, 12], [5, 1, 1, 0, -8, 3, 5, -6, 3, 2, 3, 9, 3]) == 0
    assert candidate([1, 8, -7, -14, 12, -9, 19, -1, 18], [6, 3, 4, 4, -3, 9, 5, -7, -3, 8, 1, 2, 8]) == 0
    assert candidate([2, 4, -1, -8, 11, -7, 11, -1, 18], [2, 5, 2, -4, -2, 1, 7, -3, 1, 8, 7, 7, 4]) == 1
    assert candidate([2, 3, -7, -14, 11, -14, 17, -5, 17], [2, 1, 6, 1, -3, 8, 9, -6, 0, 8, 4, 7, 9]) == 1
    assert candidate([2, 1, -5, -8, 9, -15, 16, -3, 17], [2, 1, 6, 1, -1, 6, 7, -3, -5, 5, 6, 9, 5]) == 3

if __name__ == '__main__':
    check(count_same_pair)