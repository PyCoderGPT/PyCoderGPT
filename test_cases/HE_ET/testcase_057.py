from case_HE_057 import monotonic


def check(candidate):
    assert candidate([6, 2, 5, 7, 4, 65]) == False
    assert candidate([3, 3, 7, 4, 3, 64]) == False
    assert candidate([3, 1, 5, 8]) == False
    assert candidate([4, 3, 5, 7, 1, 62]) == False
    assert candidate([4, 4, 1, 1]) == True
    assert candidate([3, 2, 7, 6]) == False
    assert candidate([2, 7, 7, 15]) == True
    assert candidate([4, 7, 7, 1, 1, 57]) == False
    assert candidate([1, 1, 8, 13]) == True
    assert candidate([5, 5, 8, 17]) == True
    assert candidate([2, 22, 8, 7]) == False
    assert candidate([2, 23, 5, 6]) == False
    assert candidate([3, 2, 2, 18]) == False
    assert candidate([2, 2, 2, 6]) == True
    assert candidate([7, 5, 3, 2]) == True
    assert candidate([7, 5, 2, -5]) == True
    assert candidate([6, 19, 9, 12]) == False
    assert candidate([1, 2, 4, 10]) == True
    assert candidate([5, 4, 6, 18]) == False
    assert candidate([6, 1, 7, 3, 4, 56]) == False
    assert candidate([6, 3, 7, 3, 8, 61]) == False
    assert candidate([2, 17, 7, 8]) == False
    assert candidate([5, 1, 4, 5, 3, 59]) == False
    assert candidate([3, 5, 5, 5, 3, 65]) == False
    assert candidate([6, 19, 9, 7]) == False
    assert candidate([1, 16, 9, 7]) == False
    assert candidate([7, 6, 2, -14]) == True
    assert candidate([5, 6, 4, 16]) == False
    assert candidate([1, 6, 5, -10]) == False
    assert candidate([1, 22, 4, 10]) == False
    assert candidate([1, 6, 8, 6, 3, 62]) == False
    assert candidate([1, 5, 1, 6, 4, 62]) == False
    assert candidate([1, 1, 7, 2, 4, 56]) == False
    assert candidate([2, 1, 5, 12]) == False
    assert candidate([1, 3, 1, 4]) == False
    assert candidate([4, 19, 8, 7]) == False
    assert candidate([3, 5, 8, 5, 5, 56]) == False
    assert candidate([1, 3, 6, 25]) == True
    assert candidate([2, 3, 1, 7]) == False
    assert candidate([8, 6, 2, 5]) == False
    assert candidate([6, 3, 6, 2, 8, 62]) == False
    assert candidate([6, 4, 6, 4]) == False
    assert candidate([3, 6, 1, 3]) == False
    assert candidate([4, 2, 5, 7, 6, 62]) == False
    assert candidate([3, 7, 1, 20]) == False
    assert candidate([3, 1, 5, 17]) == False
    assert candidate([5, 5, 7, 5, 5, 57]) == False
    assert candidate([1, 20, 4, 10]) == False
    assert candidate([6, 16, 4, 14]) == False
    assert candidate([3, 17, 2, 14]) == False
    assert candidate([4, 5, 7, 2, 8, 63]) == False
    assert candidate([1, 2, 4, 20]) == True
    assert candidate([3, 3, 3, -5]) == True
    assert candidate([4, 2, 3, 4]) == False
    assert candidate([3, 5, 4, 2, 1, 60]) == False
    assert candidate([6, 4, 7, 24]) == False
    assert candidate([6, 3, 1, 1, 2, 61]) == False
    assert candidate([1, 4, 3, -8]) == False
    assert candidate([2, 6, 3, 5, 10, 63]) == False
    assert candidate([4, 6, 3, 3, 10, 57]) == False
    assert candidate([5, 4, 9, 14]) == False
    assert candidate([1, 3, 5, 17]) == True
    assert candidate([6, 7, 1, 8]) == False
    assert candidate([9, 2, 5, -5]) == False
    assert candidate([3, 2, 5, 1]) == False
    assert candidate([9, 9, 9, 9]) == True
    assert candidate([1, 2, 3, 4, 5, 60]) == True
    assert candidate([6, 2, 5, 6, 3, 62]) == False
    assert candidate([5, 1, 3, -9]) == False
    assert candidate([1, 5, 7, 6]) == False
    assert candidate([1, 24, 9, 12]) == False
    assert candidate([2, 6, 7, 6, 6, 61]) == False
    assert candidate([4, 1, 1, 0]) == True
    assert candidate([2, 1, 3, 3, 3, 65]) == False
    assert candidate([1, 2, 8, 5, 9, 55]) == False
    assert candidate([2, 16, 2, 11]) == False
    assert candidate([6, 16, 3, 15]) == False
    assert candidate([1, 5, 2, 4, 2, 55]) == False
    assert candidate([3, 1, 8, 7, 7, 65]) == False
    assert candidate([2, 20, 2, 5]) == False
    assert candidate([7, 2, 3, -10]) == False
    assert candidate([4, 3, 5, 4, 8, 63]) == False
    assert candidate([7, 2, 1, -12]) == True
    assert candidate([9, 4, 1, -6]) == True
    assert candidate([2, 15, 2, 15]) == False
    assert candidate([6, 2, 4, 4]) == False
    assert candidate([3, 3, 2, 4]) == False
    assert candidate([2, 2, 8, 1, 3, 63]) == False
    assert candidate([2, 2, 8, 12]) == True
    assert candidate([3, 4, 2, 1]) == False
    assert candidate([4, 4, 3, 15]) == False
    assert candidate([2, 6, 5, 3]) == False
    assert candidate([6, 5, 7, 7, 6, 55]) == False
    assert candidate([2, 4, 4, 14]) == True
    assert candidate([5, 4, 8, 5]) == False
    assert candidate([4, 5, 1, -7]) == False
    assert candidate([3, 3, 6, 8]) == True
    assert candidate([9, 5, 5, -14]) == True
    assert candidate([2, 1, 4, 4, 5, 55]) == False
    assert candidate([4, 1, 0, -10]) == True
    assert candidate([5, 5, 7, 21]) == True
    assert candidate([1, 1, 3, 18]) == True
    assert candidate([1, 6, 4, -7]) == False
    assert candidate([4, 3, 4, 17]) == False
    assert candidate([7, 2, 1, -6]) == True
    assert candidate([1, 2, 3, 2, 5, 60]) == False
    assert candidate([5, 2, 5, 2]) == False
    assert candidate([2, 3, 8, 8]) == True
    assert candidate([5, 2, 3, 4]) == False
    assert candidate([8, 3, 2, -15]) == True
    assert candidate([3, 4, 3, 15]) == False
    assert candidate([2, 1, 5, 3]) == False
    assert candidate([2, 4, 3, 19]) == False

if __name__ == '__main__':
    check(monotonic)