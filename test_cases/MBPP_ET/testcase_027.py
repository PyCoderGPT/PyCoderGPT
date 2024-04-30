from case_MBPP_027 import is_sublist


def check(candidate):
    assert candidate([2,4,3,5,7],[3,7])==False
    assert candidate([2,4,3,5,7],[4,3])==True
    assert candidate([2,4,3,5,7],[1,6])==False
    assert candidate([2, 7, 5, 8, 6], [4, 9]) == False
    assert candidate([5, 7, 3, 6, 10], [4, 2]) == False
    assert candidate([2, 4, 3, 7, 11], [7, 2]) == False
    assert candidate([1, 2, 4, 5, 6], [8, 12]) == False
    assert candidate([1, 8, 3, 8, 7], [3, 2]) == False
    assert candidate([3, 9, 7, 1, 3], [8, 7]) == False
    assert candidate([7, 1, 5, 1, 3], [7, 9]) == False
    assert candidate([1, 8, 4, 1, 12], [7, 5]) == False
    assert candidate([7, 1, 1, 5, 7], [5, 5]) == False
    assert candidate([1, 5, 3, 4, 5], [1, 4]) == False
    assert candidate([4, 5, 7, 6, 2], [3, 7]) == False
    assert candidate([5, 2, 5, 4, 2], [7, 12]) == False
    assert candidate([4, 3, 1, 1, 5], [2, 12]) == False
    assert candidate([7, 1, 7, 8, 2], [8, 4]) == False
    assert candidate([3, 6, 1, 1, 11], [8, 5]) == False
    assert candidate([6, 3, 6, 10, 5], [8, 10]) == False
    assert candidate([7, 2, 7, 9, 7], [6, 3]) == False
    assert candidate([6, 4, 4, 3, 2], [5, 3]) == False
    assert candidate([5, 8, 8, 9, 2], [7, 7]) == False
    assert candidate([3, 3, 5, 2, 12], [7, 10]) == False
    assert candidate([2, 9, 1, 10, 9], [1, 7]) == False
    assert candidate([5, 8, 8, 3, 11], [8, 9]) == False
    assert candidate([6, 6, 8, 4, 6], [2, 7]) == False
    assert candidate([4, 5, 4, 3, 10], [6, 9]) == False
    assert candidate([2, 1, 2, 1, 12], [2, 6]) == False
    assert candidate([7, 7, 4, 7, 3], [1, 10]) == False
    assert candidate([7, 1, 7, 9, 9], [3, 7]) == False
    assert candidate([2, 3, 2, 4, 10], [5, 8]) == False
    assert candidate([6, 7, 5, 7, 7], [6, 6]) == False
    assert candidate([6, 2, 8, 7, 12], [6, 6]) == False
    assert candidate([2, 1, 7, 6, 11], [6, 3]) == False
    assert candidate([1, 9, 6, 6, 8], [3, 7]) == False
    assert candidate([5, 2, 2, 10, 4], [7, 2]) == False
    assert candidate([2, 5, 8, 8, 2], [3, 8]) == False
    assert candidate([6, 6, 5, 7, 2], [1, 8]) == False
    assert candidate([7, 3, 2, 10, 3], [9, 4]) == False
    assert candidate([6, 8, 3, 3, 12], [8, 6]) == False
    assert candidate([2, 7, 7, 6, 7], [3, 1]) == False
    assert candidate([7, 4, 6, 6, 4], [3, 1]) == False
    assert candidate([3, 7, 4, 5, 7], [5, 2]) == False
    assert candidate([4, 8, 1, 9, 6], [9, 7]) == False
    assert candidate([3, 3, 6, 5, 3], [6, 7]) == False
    assert candidate([1, 2, 3, 4, 9], [8, 2]) == False
    assert candidate([3, 1, 7, 9, 10], [7, 4]) == False
    assert candidate([5, 1, 3, 1, 11], [3, 6]) == False
    assert candidate([4, 6, 1, 5, 4], [1, 2]) == False
    assert candidate([3, 7, 7, 10, 8], [1, 1]) == False
    assert candidate([4, 5, 3, 7, 10], [3, 1]) == False
    assert candidate([2, 5, 2, 5, 4], [2, 1]) == False
    assert candidate([2, 3, 8, 10, 11], [7, 6]) == False
    assert candidate([1, 7, 6, 6, 12], [4, 8]) == False
    assert candidate([3, 9, 8, 6, 5], [9, 8]) == True
    assert candidate([5, 4, 4, 6, 4], [7, 7]) == False
    assert candidate([7, 3, 3, 1, 8], [1, 2]) == False
    assert candidate([7, 6, 7, 8, 12], [4, 2]) == False
    assert candidate([3, 6, 7, 4, 12], [4, 7]) == False
    assert candidate([5, 7, 7, 7, 12], [5, 5]) == False
    assert candidate([4, 6, 1, 9, 7], [5, 3]) == False
    assert candidate([5, 2, 5, 2, 3], [6, 2]) == False
    assert candidate([1, 5, 2, 1, 5], [8, 1]) == False
    assert candidate([7, 6, 2, 3, 11], [3, 8]) == False
    assert candidate([1, 9, 6, 4, 12], [7, 8]) == False
    assert candidate([4, 7, 3, 10, 7], [1, 4]) == False
    assert candidate([4, 7, 8, 2, 10], [2, 4]) == False
    assert candidate([3, 5, 4, 9, 7], [9, 1]) == False
    assert candidate([6, 4, 4, 10, 6], [7, 1]) == False
    assert candidate([7, 3, 4, 7, 4], [1, 2]) == False
    assert candidate([5, 4, 4, 3, 7], [4, 10]) == False
    assert candidate([2, 1, 8, 10, 6], [2, 10]) == False
    assert candidate([3, 2, 7, 1, 7], [2, 8]) == False
    assert candidate([1, 2, 1, 4, 12], [1, 1]) == False
    assert candidate([3, 8, 8, 9, 3], [4, 3]) == False
    assert candidate([4, 3, 5, 9, 12], [5, 5]) == False
    assert candidate([1, 5, 5, 9, 2], [1, 6]) == False
    assert candidate([7, 3, 7, 1, 10], [3, 4]) == False
    assert candidate([5, 2, 4, 7, 2], [1, 7]) == False
    assert candidate([7, 1, 8, 7, 11], [5, 8]) == False
    assert candidate([5, 1, 2, 3, 6], [3, 5]) == False
    assert candidate([2, 7, 1, 6, 6], [3, 11]) == False
    assert candidate([7, 2, 1, 1, 7], [5, 11]) == False
    assert candidate([3, 3, 3, 4, 12], [6, 9]) == False
    assert candidate([4, 4, 4, 9, 11], [2, 2]) == False
    assert candidate([7, 1, 1, 1, 6], [2, 7]) == False
    assert candidate([4, 1, 7, 10, 8], [6, 8]) == False
    assert candidate([3, 4, 4, 5, 4], [2, 11]) == False
    assert candidate([4, 6, 5, 8, 12], [1, 3]) == False
    assert candidate([2, 2, 5, 2, 11], [3, 1]) == False
    assert candidate([2, 2, 5, 5, 4], [6, 1]) == False
    assert candidate([2, 9, 5, 3, 6], [5, 1]) == False
    assert candidate([6, 5, 4, 10, 10], [3, 5]) == False
    assert candidate([1, 9, 5, 10, 8], [3, 6]) == False
    assert candidate([5, 2, 2, 8, 10], [2, 3]) == False
    assert candidate([3, 8, 3, 3, 4], [1, 9]) == False
    assert candidate([5, 5, 8, 5, 4], [6, 4]) == False
    assert candidate([1, 6, 7, 3, 10], [2, 9]) == False
    assert candidate([1, 5, 8, 8, 6], [3, 5]) == False
    assert candidate([7, 8, 3, 3, 2], [4, 8]) == False
    assert candidate([6, 5, 4, 10, 3], [4, 8]) == False
    assert candidate([5, 3, 8, 2, 12], [1, 6]) == False

if __name__ == '__main__':
    check(is_sublist)