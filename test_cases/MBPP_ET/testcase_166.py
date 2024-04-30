from case_MBPP_166 import get_Inv_Count


def check(candidate):
    assert candidate([1,20,6,4,5],5) == 5
    assert candidate([1,2,1],3) == 1
    assert candidate([1,2,5,6,1],5) == 3
    assert candidate([1, 22, 8, 3, 10], 1) == 0
    assert candidate([6, 22, 10, 6, 3], 3) == 1
    assert candidate([2, 16, 4, 6, 10], 1) == 0
    assert candidate([2, 16, 7, 1, 4], 4) == 4
    assert candidate([4, 18, 4, 9, 6], 3) == 1
    assert candidate([2, 24, 2, 3, 2], 2) == 0
    assert candidate([4, 16, 7, 2, 3], 1) == 0
    assert candidate([3, 24, 3, 5, 5], 4) == 2
    assert candidate([5, 25, 11, 1, 4], 3) == 1
    assert candidate([4, 20, 2, 5, 2], 3) == 2
    assert candidate([4, 23, 5, 5, 2], 2) == 0
    assert candidate([1, 17, 4, 7, 2], 2) == 0
    assert candidate([5, 17, 8, 1, 6], 4) == 4
    assert candidate([2, 22, 9, 5, 2], 1) == 0
    assert candidate([5, 23, 11, 6, 1], 2) == 0
    assert candidate([4, 20, 5, 6, 5], 2) == 0
    assert candidate([6, 21, 10, 8, 1], 2) == 0
    assert candidate([3, 17, 5, 4, 8], 5) == 4
    assert candidate([6, 19, 5, 4, 8], 3) == 2
    assert candidate([6, 15, 7, 4, 2], 1) == 0
    assert candidate([3, 21, 7, 9, 3], 3) == 1
    assert candidate([6, 25, 3, 3, 4], 4) == 4
    assert candidate([5, 16, 8, 4, 7], 1) == 0
    assert candidate([3, 17, 9, 9, 8], 4) == 2
    assert candidate([5, 25, 11, 8, 9], 5) == 5
    assert candidate([2, 16, 3, 1, 2], 1) == 0
    assert candidate([6, 15, 1, 3, 5], 3) == 2
    assert candidate([6, 17, 6, 3, 1], 5) == 8
    assert candidate([2, 25, 11, 6, 9], 1) == 0
    assert candidate([5, 20, 3, 4, 5], 1) == 0
    assert candidate([3, 17, 1, 5, 3], 3) == 2
    assert candidate([6, 19, 6, 7, 10], 1) == 0
    assert candidate([2, 15, 8, 3, 2], 5) == 6
    assert candidate([4, 6, 1], 3) == 2
    assert candidate([2, 3, 6], 1) == 0
    assert candidate([2, 5, 4], 2) == 0
    assert candidate([1, 2, 1], 2) == 0
    assert candidate([2, 2, 6], 1) == 0
    assert candidate([6, 5, 2], 2) == 1
    assert candidate([1, 5, 6], 1) == 0
    assert candidate([4, 3, 4], 3) == 1
    assert candidate([2, 2, 5], 1) == 0
    assert candidate([2, 2, 2], 2) == 0
    assert candidate([5, 6, 5], 3) == 1
    assert candidate([2, 4, 1], 2) == 0
    assert candidate([1, 2, 6], 1) == 0
    assert candidate([2, 7, 2], 3) == 1
    assert candidate([6, 6, 4], 3) == 2
    assert candidate([1, 4, 6], 1) == 0
    assert candidate([5, 7, 1], 3) == 2
    assert candidate([6, 3, 3], 1) == 0
    assert candidate([6, 2, 6], 1) == 0
    assert candidate([6, 3, 4], 2) == 1
    assert candidate([2, 2, 3], 3) == 0
    assert candidate([2, 2, 6], 3) == 0
    assert candidate([2, 5, 2], 3) == 1
    assert candidate([4, 3, 6], 2) == 1
    assert candidate([5, 7, 2], 3) == 2
    assert candidate([4, 1, 4], 1) == 0
    assert candidate([6, 1, 2], 1) == 0
    assert candidate([5, 7, 5], 3) == 1
    assert candidate([3, 4, 5], 1) == 0
    assert candidate([6, 3, 2], 3) == 3
    assert candidate([1, 4, 6], 2) == 0
    assert candidate([3, 5, 3], 3) == 1
    assert candidate([3, 1, 2], 2) == 1
    assert candidate([4, 6, 7, 11, 4], 3) == 0
    assert candidate([5, 2, 1, 2, 6], 3) == 3
    assert candidate([1, 3, 3, 7, 4], 1) == 0
    assert candidate([3, 6, 2, 1, 1], 5) == 8
    assert candidate([3, 4, 8, 6, 4], 2) == 0
    assert candidate([1, 7, 4, 8, 3], 1) == 0
    assert candidate([4, 5, 2, 7, 2], 3) == 2
    assert candidate([5, 2, 2, 10, 6], 4) == 2
    assert candidate([1, 7, 8, 3, 2], 4) == 2
    assert candidate([4, 5, 8, 6, 5], 5) == 3
    assert candidate([2, 3, 7, 3, 2], 2) == 0
    assert candidate([3, 5, 5, 2, 5], 2) == 0
    assert candidate([6, 3, 7, 8, 6], 3) == 1
    assert candidate([3, 2, 7, 8, 1], 1) == 0
    assert candidate([5, 3, 3, 3, 3], 3) == 2
    assert candidate([4, 1, 1, 7, 4], 2) == 1
    assert candidate([3, 3, 1, 2, 6], 3) == 2
    assert candidate([1, 7, 5, 1, 6], 5) == 4
    assert candidate([5, 6, 2, 10, 4], 2) == 0
    assert candidate([6, 6, 2, 2, 3], 3) == 2
    assert candidate([4, 2, 3, 9, 3], 3) == 2
    assert candidate([3, 2, 1, 4, 5], 3) == 3
    assert candidate([2, 6, 4, 5, 5], 1) == 0
    assert candidate([6, 3, 10, 1, 6], 1) == 0
    assert candidate([6, 3, 6, 3, 2], 2) == 1
    assert candidate([1, 3, 4, 9, 6], 4) == 0
    assert candidate([3, 5, 5, 11, 6], 2) == 0
    assert candidate([2, 6, 9, 8, 6], 1) == 0
    assert candidate([4, 4, 6, 3, 3], 4) == 3
    assert candidate([5, 4, 10, 1, 3], 4) == 4
    assert candidate([1, 2, 8, 1, 3], 2) == 0
    assert candidate([6, 1, 9, 11, 6], 1) == 0
    assert candidate([2, 6, 2, 5, 1], 3) == 1

if __name__ == '__main__':
    check(get_Inv_Count)