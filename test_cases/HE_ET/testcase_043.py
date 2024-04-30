from case_HE_043 import pairs_sum_to_zero


def check(candidate):
    assert candidate([1, 11, -3, 6, 7, 30]) == False
    assert candidate([3, 7, -4, 1, 1, 11]) == False
    assert candidate([-8, 11, 0, 3, 6, 26]) == False
    assert candidate([1, 14, 0, 5, 2, 34]) == False
    assert candidate([1, 2, 3, 7]) == False
    assert candidate([4, 2, 9, 3]) == False
    assert candidate([-3, 9, -1, 4, 2, 31]) == False
    assert candidate([3]) == False
    assert candidate([-1, 14, 1, 8, 6, 36]) == True
    assert candidate([3, 9, 0, 8, 5, 9]) == False
    assert candidate([1, 4, -6, 7, 1, 32]) == False
    assert candidate([2, 8, -2, 3]) == True
    assert candidate([-2, 10, 0, 6, 5, 30]) == False
    assert candidate([3, 1, -2, 2]) == True
    assert candidate([3, 2, -1, 2]) == False
    assert candidate([-1, 4, -2, 5, 5, 27]) == False
    assert candidate([1]) == False
    assert candidate([6, 5, -3, 3]) == True
    assert candidate([4, 3, -4, 5]) == True
    assert candidate([-2, 4, -5, 4, 1, 25]) == False
    assert candidate([2, 6, -4, 5]) == False
    assert candidate([-7, 5, 2, 4, 1, 26]) == False
    assert candidate([-8, 14, 0, 1, 7, 30]) == False
    assert candidate([1, 8, -5, 3, 7, 35]) == False
    assert candidate([6, 9, -9, 2, 7, 11]) == True
    assert candidate([-8, 7, -1, 2, 1, 28]) == True
    assert candidate([-3, 9, -1, 3, 2, 31]) == True
    assert candidate([6, 6, -7, 6]) == False
    assert candidate([-4, 9, 2, 3, 4, 30]) == True
    assert candidate([1, 6, 1, 2]) == False
    assert candidate([5, 1, 3, 5]) == False
    assert candidate([4, 5, 8, 3]) == False
    assert candidate([6, 7, 2, 5]) == False
    assert candidate([2, 8, 10, 3]) == False
    assert candidate([1, 13, -5, 7, 7, 27]) == False
    assert candidate([4, 5, -10, 2, 10, 9]) == True
    assert candidate([2, 3, 1, 8]) == False
    assert candidate([1, 7, 4, 6]) == False
    assert candidate([2, 9, -5, 4, 6, 30]) == False
    assert candidate([4, 6, 2, 4]) == False
    assert candidate([5, 2, 1, 11]) == False
    assert candidate([5, 2, 7, 3]) == False
    assert candidate([5, 5, 2, 2]) == False
    assert candidate([-8, 14, -2, 8, 2, 35]) == True
    assert candidate([1, 3, 5, 0]) == False
    assert candidate([-1, 8, 4, 3, 7, 29]) == False
    assert candidate([2, 12, 1, 9, 6, 33]) == False
    assert candidate([-4, 11, 1, 6, 6, 28]) == False
    assert candidate([0, 11, -3, 8, 7, 26]) == False
    assert candidate([-8, 10, -4, 8, 6, 26]) == True
    assert candidate([2]) == False
    assert candidate([2, 3, 7, 1]) == False
    assert candidate([6, 1, -4, 6]) == False
    assert candidate([-2, 12, -4, 7, 1, 36]) == False
    assert candidate([2, 12, 1, 6, 7, 25]) == False
    assert candidate([-4, 11, -3, 6, 2, 27]) == False
    assert candidate([0, 13, -2, 7, 3, 31]) == False
    assert candidate([1, 4, -10, 5, 10, 9]) == True
    assert candidate([4, 1, 3, 7]) == False
    assert candidate([6, 8, 2, 5]) == False
    assert candidate([-7, 14, 2, 4, 6, 30]) == False
    assert candidate([1, 5, 1, 12]) == False
    assert candidate([-3, 9, -1, 3, 2, 30]) == True
    assert candidate([-1, 5, -6, 8, 1, 33]) == True
    assert candidate([2, 3, 7, 4]) == False
    assert candidate([0, 14, -6, 5, 1, 35]) == False
    assert candidate([5, 4, -1, 5, 10, 6]) == False
    assert candidate([0, 13, -2, 4, 4, 28]) == False
    assert candidate([2, 2, 6, 4]) == False
    assert candidate([0, 4, -1, 5, 3, 33]) == False
    assert candidate([3, 3, 1, 4]) == False
    assert candidate([7, 5, -1, 1, 8, 10]) == True
    assert candidate([1, 3, 4, 3]) == False
    assert candidate([5, 7, 3, 4]) == False
    assert candidate([-7, 12, -3, 2, 6, 29]) == False
    assert candidate([-4, 9, -3, 6, 7, 31]) == False
    assert candidate([4, 7, -9, 5, 4, 6]) == False
    assert candidate([-4, 6, 0, 6, 3, 26]) == False
    assert candidate([4]) == False
    assert candidate([2, 7, 8, 5]) == False
    assert candidate([2, 4, -5, 3, 5, 7]) == True
    assert candidate([1, 4, -1, 8, 8, 12]) == True
    assert candidate([-3, 8, 1, 1, 6, 31]) == False
    assert candidate([-6, 14, 1, 8, 2, 28]) == False
    assert candidate([-3, 6, -5, 7, 7, 30]) == False
    assert candidate([3, 4, -7, 1, 2, 3]) == False
    assert candidate([-8, 11, -6, 5, 7, 36]) == False
    assert candidate([-7, 14, 0, 5, 1, 28]) == False
    assert candidate([-5, 9, -1, 7, 4, 34]) == False
    assert candidate([1, 3, 3, 5]) == False
    assert candidate([-5, 10, 2, 9, 3, 33]) == False
    assert candidate([2, 4, 1, 2]) == False
    assert candidate([-3, 9, -1, 4, 2, 30]) == False
    assert candidate([1, 3, -2, 1]) == False
    assert candidate([2, 10, -2, 2, 4, 33]) == True
    assert candidate([3, 9, -8, 6, 2, 5]) == False
    assert candidate([-6, 7, -4, 4, 2, 32]) == True
    assert candidate([3, 4, 10, 1]) == False
    assert candidate([7, 8, -10, 7, 2, 4]) == False
    assert candidate([-6, 8, 0, 4, 5, 27]) == False
    assert candidate([-6, 14, -4, 5, 6, 32]) == True
    assert candidate([-5, 12, 1, 8, 6, 31]) == False
    assert candidate([-3, 12, -6, 6, 7, 29]) == True
    assert candidate([1, 5, 1, 3]) == False
    assert candidate([5, 8, -4, 5]) == False
    assert candidate([3, 2, 1, 6]) == False
    assert candidate([-5, 4, 3, 6, 2, 27]) == False
    assert candidate([-1, 11, -4, 3, 5, 28]) == False
    assert candidate([-7, 9, 2, 1, 6, 34]) == False
    assert candidate([-1, 13, -4, 6, 3, 28]) == False
    assert candidate([6, 1, 0, 3]) == False
    assert candidate([-5, 5, -2, 3, 1, 32]) == True
    assert candidate([1, 5, -1, 8, 8, 4]) == True
    assert candidate([1, 2, 2, 2]) == False
    assert candidate([6]) == False
    assert candidate([2, 8, 1, 4]) == False
    assert candidate([2, 6, 2, 5]) == False
    assert candidate([2, 14, 3, 6, 2, 29]) == False
    assert candidate([-5, 13, -2, 8, 7, 35]) == False
    assert candidate([6, 1, 3, 2]) == False
    assert candidate([5]) == False
    assert candidate([-4, 8, -1, 7, 6, 26]) == False
    assert candidate([-4, 12, 0, 1, 7, 28]) == False
    assert candidate([5, 3, 6, 7]) == False
    assert candidate([4, 6, -8, 1, 2, 8]) == True
    assert candidate([-4, 8, -3, 9, 5, 29]) == False

if __name__ == '__main__':
    check(pairs_sum_to_zero)