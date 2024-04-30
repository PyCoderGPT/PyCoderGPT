from case_MBPP_020 import smallest_num


def check(candidate):
    assert candidate([10, 20, 1, 45, 99]) == 1
    assert candidate([1, 2, 3]) == 1
    assert candidate([45, 46, 50, 60]) == 45
    assert candidate([13, 24, 6, 50, 103]) == 6
    assert candidate([12, 18, 3, 43, 96]) == 3
    assert candidate([6, 21, 4, 47, 94]) == 4
    assert candidate([14, 20, 1, 48, 97]) == 1
    assert candidate([9, 17, 3, 42, 99]) == 3
    assert candidate([9, 15, 6, 47, 100]) == 6
    assert candidate([9, 22, 6, 43, 99]) == 6
    assert candidate([5, 21, 1, 50, 101]) == 1
    assert candidate([7, 25, 3, 48, 101]) == 3
    assert candidate([12, 21, 1, 50, 99]) == 1
    assert candidate([11, 25, 6, 49, 94]) == 6
    assert candidate([14, 18, 2, 48, 103]) == 2
    assert candidate([9, 15, 1, 50, 99]) == 1
    assert candidate([11, 15, 3, 48, 98]) == 3
    assert candidate([12, 17, 2, 46, 102]) == 2
    assert candidate([10, 19, 6, 46, 103]) == 6
    assert candidate([10, 25, 2, 40, 99]) == 2
    assert candidate([7, 17, 1, 41, 101]) == 1
    assert candidate([9, 23, 5, 49, 104]) == 5
    assert candidate([10, 25, 1, 41, 97]) == 1
    assert candidate([6, 21, 2, 44, 104]) == 2
    assert candidate([9, 16, 4, 45, 101]) == 4
    assert candidate([11, 20, 3, 50, 97]) == 3
    assert candidate([11, 17, 4, 48, 101]) == 4
    assert candidate([13, 17, 1, 44, 98]) == 1
    assert candidate([11, 21, 3, 45, 100]) == 3
    assert candidate([14, 17, 4, 50, 98]) == 4
    assert candidate([6, 25, 3, 44, 103]) == 3
    assert candidate([6, 21, 2, 43, 103]) == 2
    assert candidate([7, 20, 6, 48, 101]) == 6
    assert candidate([12, 24, 1, 44, 101]) == 1
    assert candidate([9, 20, 2, 46, 101]) == 2
    assert candidate([12, 20, 6, 41, 102]) == 6
    assert candidate([2, 5, 2]) == 2
    assert candidate([3, 4, 5]) == 3
    assert candidate([3, 5, 3]) == 3
    assert candidate([4, 7, 7]) == 4
    assert candidate([1, 7, 8]) == 1
    assert candidate([1, 2, 4]) == 1
    assert candidate([3, 7, 2]) == 2
    assert candidate([2, 1, 6]) == 1
    assert candidate([5, 7, 8]) == 5
    assert candidate([2, 5, 4]) == 2
    assert candidate([1, 7, 3]) == 1
    assert candidate([3, 5, 6]) == 3
    assert candidate([5, 3, 6]) == 3
    assert candidate([2, 1, 4]) == 1
    assert candidate([5, 7, 3]) == 3
    assert candidate([6, 3, 2]) == 2
    assert candidate([4, 5, 4]) == 4
    assert candidate([3, 1, 3]) == 1
    assert candidate([5, 3, 2]) == 2
    assert candidate([3, 3, 4]) == 3
    assert candidate([1, 2, 8]) == 1
    assert candidate([3, 3, 2]) == 2
    assert candidate([4, 7, 5]) == 4
    assert candidate([1, 1, 6]) == 1
    assert candidate([6, 4, 6]) == 4
    assert candidate([4, 5, 3]) == 3
    assert candidate([6, 2, 6]) == 2
    assert candidate([1, 4, 5]) == 1
    assert candidate([1, 7, 3]) == 1
    assert candidate([4, 4, 6]) == 4
    assert candidate([4, 5, 5]) == 4
    assert candidate([2, 2, 1]) == 1
    assert candidate([4, 1, 2]) == 1
    assert candidate([50, 50, 52, 56]) == 50
    assert candidate([49, 43, 48, 62]) == 43
    assert candidate([46, 47, 50, 62]) == 46
    assert candidate([48, 51, 49, 55]) == 48
    assert candidate([50, 44, 46, 63]) == 44
    assert candidate([41, 46, 47, 65]) == 41
    assert candidate([47, 44, 53, 64]) == 44
    assert candidate([43, 47, 53, 55]) == 43
    assert candidate([43, 47, 46, 61]) == 43
    assert candidate([42, 49, 54, 55]) == 42
    assert candidate([41, 46, 47, 62]) == 41
    assert candidate([48, 51, 49, 59]) == 48
    assert candidate([44, 51, 49, 63]) == 44
    assert candidate([47, 43, 52, 61]) == 43
    assert candidate([47, 49, 46, 61]) == 46
    assert candidate([47, 41, 50, 64]) == 41
    assert candidate([46, 51, 51, 55]) == 46
    assert candidate([45, 49, 53, 61]) == 45
    assert candidate([41, 41, 54, 63]) == 41
    assert candidate([42, 47, 51, 57]) == 42
    assert candidate([45, 50, 50, 60]) == 45
    assert candidate([46, 51, 54, 55]) == 46
    assert candidate([43, 49, 47, 56]) == 43
    assert candidate([42, 51, 52, 60]) == 42
    assert candidate([43, 48, 55, 57]) == 43
    assert candidate([47, 43, 55, 63]) == 43
    assert candidate([45, 50, 49, 60]) == 45
    assert candidate([50, 50, 45, 57]) == 45
    assert candidate([49, 41, 45, 57]) == 41
    assert candidate([48, 45, 46, 57]) == 45
    assert candidate([50, 48, 51, 63]) == 48
    assert candidate([44, 49, 53, 60]) == 44
    assert candidate([47, 46, 53, 59]) == 46

if __name__ == '__main__':
    check(smallest_num)