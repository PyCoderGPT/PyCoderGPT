from case_MBPP_388 import get_Pairs_Count


def check(candidate):
    assert candidate([1,1,1,1],4,2) == 6
    assert candidate([1,5,7,-1,5],5,6) == 3
    assert candidate([1,-2,3],3,1) == 1
    assert candidate([5, 5, 6, 3], 4, 4) == 0
    assert candidate([2, 4, 2, 1], 4, 7) == 0
    assert candidate([4, 3, 2, 5], 3, 4) == 0
    assert candidate([6, 5, 4, 5], 3, 7) == 0
    assert candidate([4, 5, 6, 1], 2, 3) == 0
    assert candidate([4, 2, 6, 6], 2, 6) == 1
    assert candidate([6, 5, 6, 4], 3, 3) == 0
    assert candidate([1, 5, 2, 3], 4, 7) == 1
    assert candidate([6, 4, 4, 5], 3, 4) == 0
    assert candidate([4, 1, 1, 2], 2, 1) == 0
    assert candidate([4, 2, 5, 4], 1, 2) == 0
    assert candidate([3, 3, 5, 1], 3, 3) == 0
    assert candidate([2, 6, 4, 1], 2, 7) == 0
    assert candidate([2, 3, 1, 1], 1, 7) == 0
    assert candidate([3, 4, 4, 4], 3, 1) == 0
    assert candidate([1, 4, 6, 3], 1, 7) == 0
    assert candidate([5, 1, 5, 2], 4, 6) == 2
    assert candidate([3, 3, 1, 6], 3, 6) == 1
    assert candidate([1, 2, 2, 2], 3, 2) == 0
    assert candidate([4, 3, 5, 6], 2, 2) == 0
    assert candidate([6, 3, 1, 5], 2, 6) == 0
    assert candidate([6, 1, 4, 6], 1, 3) == 0
    assert candidate([2, 4, 5, 1], 1, 2) == 0
    assert candidate([6, 4, 5, 6], 2, 4) == 0
    assert candidate([6, 6, 4, 1], 4, 5) == 1
    assert candidate([1, 4, 6, 2], 2, 6) == 0
    assert candidate([3, 2, 3, 1], 4, 4) == 2
    assert candidate([5, 3, 4, 5], 2, 3) == 0
    assert candidate([3, 1, 5, 5], 3, 4) == 1
    assert candidate([6, 1, 5, 3], 2, 7) == 1
    assert candidate([4, 6, 6, 6], 2, 7) == 0
    assert candidate([3, 1, 4, 4], 3, 2) == 0
    assert candidate([6, 5, 1, 5], 3, 2) == 0
    assert candidate([2, 1, 7, 1, 10], 3, 1) == 0
    assert candidate([4, 8, 4, 1, 7], 4, 5) == 2
    assert candidate([6, 10, 11, -3, 5], 2, 10) == 0
    assert candidate([2, 5, 7, -6, 5], 4, 5) == 0
    assert candidate([5, 8, 9, 4, 2], 3, 11) == 0
    assert candidate([1, 1, 10, 0, 4], 1, 3) == 0
    assert candidate([6, 3, 8, 3, 1], 3, 7) == 0
    assert candidate([1, 6, 2, -6, 8], 4, 5) == 0
    assert candidate([6, 9, 11, -3, 9], 5, 4) == 0
    assert candidate([5, 7, 12, -2, 4], 4, 5) == 1
    assert candidate([5, 6, 12, 2, 9], 2, 1) == 0
    assert candidate([5, 9, 12, -6, 10], 3, 8) == 0
    assert candidate([3, 5, 11, 3, 5], 3, 2) == 0
    assert candidate([1, 3, 9, 2, 4], 3, 1) == 0
    assert candidate([4, 8, 11, -2, 3], 3, 3) == 0
    assert candidate([1, 4, 11, 3, 4], 2, 2) == 0
    assert candidate([1, 1, 2, 2, 7], 2, 10) == 0
    assert candidate([3, 10, 5, 2, 9], 4, 5) == 1
    assert candidate([3, 9, 5, -1, 4], 1, 1) == 0
    assert candidate([4, 8, 10, 0, 5], 3, 4) == 0
    assert candidate([3, 3, 6, -6, 5], 1, 10) == 0
    assert candidate([3, 3, 11, 0, 7], 2, 1) == 0
    assert candidate([6, 6, 8, -4, 4], 5, 8) == 0
    assert candidate([1, 2, 7, 4, 2], 3, 2) == 0
    assert candidate([3, 7, 10, -3, 6], 2, 11) == 0
    assert candidate([2, 9, 4, -6, 6], 4, 10) == 0
    assert candidate([6, 7, 5, -3, 1], 3, 11) == 1
    assert candidate([4, 5, 3, -5, 2], 4, 10) == 0
    assert candidate([6, 7, 12, -6, 9], 1, 11) == 0
    assert candidate([5, 7, 9, 4, 7], 2, 11) == 0
    assert candidate([3, 4, 3, -4, 10], 2, 3) == 0
    assert candidate([3, 3, 10, -4, 7], 4, 3) == 0
    assert candidate([6, 2, 11, -5, 9], 4, 3) == 0
    assert candidate([2, -7, 1], 2, 5) == 0
    assert candidate([5, 0, 7], 2, 1) == 0
    assert candidate([3, -3, 7], 3, 5) == 0
    assert candidate([4, -2, 6], 3, 2) == 1
    assert candidate([4, -3, 6], 1, 3) == 0
    assert candidate([1, 3, 3], 1, 3) == 0
    assert candidate([5, -1, 1], 2, 2) == 0
    assert candidate([6, -1, 2], 2, 1) == 0
    assert candidate([1, -6, 8], 2, 5) == 0
    assert candidate([3, 3, 4], 1, 1) == 0
    assert candidate([4, -4, 2], 1, 5) == 0
    assert candidate([3, 1, 4], 3, 4) == 1
    assert candidate([6, -5, 5], 2, 2) == 0
    assert candidate([2, -7, 3], 1, 5) == 0
    assert candidate([5, -5, 1], 2, 2) == 0
    assert candidate([1, -3, 5], 3, 1) == 0
    assert candidate([5, -5, 3], 3, 5) == 0
    assert candidate([1, 2, 3], 3, 5) == 1
    assert candidate([1, 0, 6], 3, 1) == 1
    assert candidate([4, -2, 3], 3, 5) == 0
    assert candidate([2, -7, 1], 2, 2) == 0
    assert candidate([1, -7, 6], 2, 6) == 0
    assert candidate([4, -2, 3], 3, 3) == 0
    assert candidate([3, -6, 2], 1, 4) == 0
    assert candidate([6, -6, 2], 3, 2) == 0
    assert candidate([3, 3, 5], 3, 3) == 0
    assert candidate([2, -2, 8], 2, 2) == 0
    assert candidate([1, -6, 3], 3, 2) == 0
    assert candidate([4, 0, 3], 3, 4) == 1
    assert candidate([6, -6, 7], 1, 6) == 0
    assert candidate([2, -6, 2], 2, 5) == 0
    assert candidate([2, -6, 4], 3, 1) == 0
    assert candidate([5, -3, 3], 3, 5) == 0

if __name__ == '__main__':
    check(get_Pairs_Count)