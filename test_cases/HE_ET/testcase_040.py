from case_HE_040 import triples_sum_to_zero


def check(candidate):
    assert candidate([3, 5, 1, 5]) == False
    assert candidate([3, 1, 4, 3]) == False
    assert candidate([3, 6, -1, 1, 14, 7]) == False
    assert candidate([102, 5, 9, -103]) == False
    assert candidate([5, 1, 6, -96]) == False
    assert candidate([102, 5, 8, -104]) == False
    assert candidate([1, 3, 5, 0]) == False
    assert candidate([6, 1, 2, 3]) == False
    assert candidate([4, 6, 2, 7]) == False
    assert candidate([4, 7, 1, 5]) == False
    assert candidate([1, 2, -8, 5, 8, 10]) == False
    assert candidate([3, 9, -6, 7, 13, 6]) == False
    assert candidate([5, 2, 7, 8]) == False
    assert candidate([2, 8, -4, 2]) == True
    assert candidate([2, 2, 4, 7]) == False
    assert candidate([6, 4, 5, 10]) == False
    assert candidate([6, 6, 7, 1]) == False
    assert candidate([2, 3, -1, 1]) == False
    assert candidate([5, 8, 9, -101]) == False
    assert candidate([3]) == False
    assert candidate([1, 4, 7, 9]) == False
    assert candidate([3, 7, -10, 2, 6, 12]) == True
    assert candidate([2, 8, 4, 1]) == False
    assert candidate([4]) == False
    assert candidate([3, 1, 7, -3]) == False
    assert candidate([2, 7, 5, -104]) == False
    assert candidate([1, 4, 7, 10]) == False
    assert candidate([3, 1, 4, -2]) == False
    assert candidate([4, 1, 7, 2]) == False
    assert candidate([6, 3, 1, 9]) == False
    assert candidate([2, 8, 2, -99]) == False
    assert candidate([5, 6, 7, -1]) == False
    assert candidate([6, 1, 4, -5]) == True
    assert candidate([2, 4, -5, 3, 9, 7]) == True
    assert candidate([2, 6, -1, 6]) == False
    assert candidate([5, 3, 5, 5]) == False
    assert candidate([100, 3, 5, -100]) == False
    assert candidate([2, 7, -9, 3, 10, 8]) == True
    assert candidate([1, 8, 5, 2]) == False
    assert candidate([5]) == False
    assert candidate([3, 5, 10, -105]) == False
    assert candidate([2, 3, 3, 4]) == False
    assert candidate([3, 1, 1, -96]) == False
    assert candidate([2, 4, 1, 2]) == False
    assert candidate([6]) == False
    assert candidate([1, 3, 5, -100]) == False
    assert candidate([6, 6, 7, -100]) == False
    assert candidate([6, 3, -7, 5]) == False
    assert candidate([1, 2, 0, 1]) == False
    assert candidate([4, 1, 1, 2]) == False
    assert candidate([1, 3, -5, 3, 9, 7]) == False
    assert candidate([5, 5, 6, 1]) == False
    assert candidate([1, 7, 6, 9]) == False
    assert candidate([3, 1, 10, -98]) == False
    assert candidate([5, 3, -6, 3]) == True
    assert candidate([1]) == False
    assert candidate([5, 6, 7, 2]) == False
    assert candidate([6, 5, 1, -4]) == False
    assert candidate([5, 7, 5, 1]) == False
    assert candidate([1, 1, 4, 4]) == False
    assert candidate([2]) == False
    assert candidate([2, 4, 7, 2]) == False
    assert candidate([2, 7, 9, 3]) == False
    assert candidate([2, 8, -3, 5, 6, 12]) == False
    assert candidate([98, 1, 2, -105]) == False
    assert candidate([4, 5, 9, 7]) == False
    assert candidate([4, 3, 1, 2]) == False
    assert candidate([5, 8, -6, 2]) == False
    assert candidate([3, 1, 6, 2]) == False
    assert candidate([1, 3, 5, -1]) == False
    assert candidate([1, 3, -2, 1]) == True
    assert candidate([3, 8, -2, 6, 12, 7]) == False
    assert candidate([6, 4, -10, 6, 5, 6]) == True
    assert candidate([3, 7, 10, 12]) == False
    assert candidate([6, 6, 6, 12]) == False
    assert candidate([105, 3, 3, -97]) == False
    assert candidate([6, 3, -2, 5, 11, 4]) == False
    assert candidate([96, 2, 5, -98]) == True
    assert candidate([6, 2, 8, 3]) == False
    assert candidate([6, 9, -9, 5, 5, 8]) == False
    assert candidate([1, 1, 5, 2]) == False
    assert candidate([5, 3, 5, -97]) == False
    assert candidate([3, 1, 9, 10]) == False
    assert candidate([3, 1, 6, -104]) == False
    assert candidate([6, 1, 3, -102]) == False
    assert candidate([5, 4, -6, 3]) == False
    assert candidate([95, 6, 9, -95]) == False
    assert candidate([4, 1, 1, 3]) == False
    assert candidate([100, 3, 4, -98]) == False
    assert candidate([4, 8, -9, 7, 9, 10]) == False
    assert candidate([6, 5, 10, 2]) == False
    assert candidate([1, 6, -5, 2]) == False
    assert candidate([100, 7, 3, -102]) == False
    assert candidate([5, 3, 8, 2]) == False
    assert candidate([2, 1, 4, 2]) == False
    assert candidate([5, 3, 4, 4]) == False
    assert candidate([1, 7, 6, 5]) == False
    assert candidate([98, 1, 1, -100]) == False
    assert candidate([6, 4, 4, -98]) == False
    assert candidate([5, 6, 3, 5]) == False
    assert candidate([5, 1, 6, -2]) == False
    assert candidate([2, 1, 5, 6]) == False
    assert candidate([1, 2, 5, 7]) == False
    assert candidate([103, 4, 4, -99]) == False
    assert candidate([3, 3, -3, 6]) == False
    assert candidate([3, 2, -6, 6]) == False
    assert candidate([1, 4, 7, -5]) == True
    assert candidate([99, 7, 5, -104]) == True
    assert candidate([3, 1, 1, 2]) == False
    assert candidate([98, 1, 3, -95]) == False
    assert candidate([99, 4, 5, -101]) == False
    assert candidate([4, 7, -7, 2]) == False
    assert candidate([6, 3, 7, 3]) == False
    assert candidate([5, 6, 5, 2]) == False
    assert candidate([3, 1, 4, 9]) == False
    assert candidate([98, 4, 1, -99]) == True
    assert candidate([3, 3, 9, -5]) == False
    assert candidate([7, 6, -2, 8, 10, 6]) == False
    assert candidate([1, 2, -7, 2]) == False
    assert candidate([4, 5, 9, 3]) == False
    assert candidate([5, 5, 3, 2]) == False
    assert candidate([4, 5, 9, -100]) == False
    assert candidate([1, 2, 3, 7]) == False
    assert candidate([6, 1, 3, -97]) == False
    assert candidate([1, 8, 2, 4]) == False
    assert candidate([5, 9, -6, 1, 4, 12]) == True

if __name__ == '__main__':
    check(triples_sum_to_zero)