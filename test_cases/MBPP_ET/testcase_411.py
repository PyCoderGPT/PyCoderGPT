from case_MBPP_411 import last


def check(candidate):
    assert candidate([1,2,3],1,3) == 0
    assert candidate([1,1,1,2,3,4],1,6) == 2
    assert candidate([2,3,2,3,6,8,9],3,8) == 3
    assert candidate([4, 1, 3], 3, 2) == -1
    assert candidate([6, 7, 1], 5, 3) == -1
    assert candidate([4, 3, 1], 6, 3) == -1
    assert candidate([2, 7, 4], 5, 4) == -1
    assert candidate([6, 1, 5], 6, 1) == 0
    assert candidate([3, 6, 6], 4, 3) == -1
    assert candidate([5, 3, 7], 5, 4) == -1
    assert candidate([3, 3, 7], 3, 4) == 1
    assert candidate([2, 4, 1], 3, 2) == -1
    assert candidate([6, 7, 3], 5, 2) == -1
    assert candidate([3, 3, 3], 5, 3) == -1
    assert candidate([2, 1, 6], 4, 5) == -1
    assert candidate([2, 1, 5], 5, 3) == 2
    assert candidate([4, 2, 6], 5, 3) == -1
    assert candidate([4, 2, 7], 3, 6) == -1
    assert candidate([3, 6, 8], 2, 6) == -1
    assert candidate([4, 7, 8], 6, 3) == -1
    assert candidate([3, 5, 3], 4, 1) == -1
    assert candidate([5, 2, 5], 2, 5) == -1
    assert candidate([3, 4, 3], 2, 3) == -1
    assert candidate([2, 6, 1], 5, 3) == -1
    assert candidate([2, 5, 5], 2, 1) == 0
    assert candidate([2, 6, 1], 1, 4) == -1
    assert candidate([5, 6, 7], 6, 1) == -1
    assert candidate([1, 5, 7], 2, 1) == -1
    assert candidate([3, 6, 7], 5, 6) == -1
    assert candidate([2, 3, 8], 3, 1) == -1
    assert candidate([4, 7, 4], 5, 2) == -1
    assert candidate([2, 6, 8], 5, 3) == -1
    assert candidate([6, 6, 8], 1, 3) == -1
    assert candidate([4, 1, 7], 5, 2) == -1
    assert candidate([3, 7, 7], 6, 2) == -1
    assert candidate([3, 4, 1], 4, 3) == 1
    assert candidate([5, 4, 1, 4, 3, 9], 5, 11) == -1
    assert candidate([4, 3, 6, 1, 6, 6], 4, 9) == -1
    assert candidate([1, 2, 6, 4, 6, 3], 4, 6) == -1
    assert candidate([4, 6, 6, 7, 5, 4], 3, 6) == -1
    assert candidate([6, 4, 6, 7, 1, 5], 2, 4) == -1
    assert candidate([6, 3, 5, 6, 7, 8], 3, 9) == 1
    assert candidate([6, 4, 3, 6, 3, 6], 1, 6) == -1
    assert candidate([4, 5, 4, 1, 5, 4], 5, 3) == 1
    assert candidate([6, 5, 1, 5, 8, 3], 3, 5) == -1
    assert candidate([3, 1, 1, 2, 3, 6], 1, 7) == 2
    assert candidate([3, 3, 6, 3, 8, 5], 1, 3) == -1
    assert candidate([3, 4, 6, 3, 1, 7], 2, 11) == -1
    assert candidate([3, 2, 3, 2, 4, 9], 4, 4) == -1
    assert candidate([2, 2, 6, 3, 2, 7], 2, 1) == 0
    assert candidate([1, 5, 6, 1, 3, 7], 4, 4) == -1
    assert candidate([6, 3, 5, 2, 3, 2], 5, 2) == -1
    assert candidate([3, 1, 3, 2, 4, 6], 2, 5) == -1
    assert candidate([5, 3, 4, 5, 3, 4], 3, 5) == -1
    assert candidate([1, 4, 2, 6, 6, 4], 6, 2) == -1
    assert candidate([5, 3, 1, 7, 5, 4], 4, 3) == -1
    assert candidate([2, 5, 2, 7, 7, 3], 1, 5) == -1
    assert candidate([2, 5, 6, 3, 8, 9], 4, 2) == -1
    assert candidate([5, 6, 2, 6, 5, 4], 1, 11) == -1
    assert candidate([3, 5, 2, 4, 2, 7], 1, 4) == -1
    assert candidate([1, 3, 5, 7, 7, 8], 5, 9) == 2
    assert candidate([1, 2, 4, 2, 3, 5], 1, 2) == 0
    assert candidate([3, 3, 1, 4, 2, 2], 4, 5) == 3
    assert candidate([5, 3, 6, 4, 1, 4], 5, 5) == 0
    assert candidate([6, 5, 6, 1, 7, 9], 2, 9) == -1
    assert candidate([6, 4, 5, 3, 5, 1], 2, 9) == -1
    assert candidate([4, 6, 1, 3, 7, 3], 1, 10) == -1
    assert candidate([3, 6, 3, 6, 8, 1], 4, 4) == -1
    assert candidate([6, 4, 5, 4, 6, 8], 5, 6) == 2
    assert candidate([1, 7, 5, 5, 5, 5, 11], 5, 9) == 5
    assert candidate([6, 5, 6, 8, 5, 4, 8], 4, 7) == -1
    assert candidate([4, 4, 2, 4, 3, 5, 12], 1, 13) == -1
    assert candidate([5, 8, 6, 3, 9, 5, 13], 4, 13) == -1
    assert candidate([5, 4, 6, 2, 2, 3, 10], 1, 13) == -1
    assert candidate([3, 5, 1, 6, 9, 6, 4], 7, 9) == -1
    assert candidate([5, 2, 4, 4, 6, 12, 7], 1, 7) == -1
    assert candidate([6, 5, 1, 1, 5, 5, 4], 4, 12) == -1
    assert candidate([7, 4, 5, 1, 7, 5, 11], 6, 6) == -1
    assert candidate([4, 2, 2, 4, 4, 5, 11], 6, 7) == -1
    assert candidate([7, 5, 4, 4, 1, 6, 4], 8, 7) == -1
    assert candidate([2, 5, 1, 6, 8, 9, 6], 2, 4) == 0
    assert candidate([3, 4, 1, 3, 2, 4, 6], 8, 6) == -1
    assert candidate([3, 8, 1, 3, 9, 12, 9], 7, 5) == -1
    assert candidate([4, 3, 6, 7, 11, 11, 5], 8, 8) == -1
    assert candidate([5, 4, 2, 8, 8, 7, 13], 4, 8) == 1
    assert candidate([4, 3, 3, 7, 1, 11, 11], 5, 3) == -1
    assert candidate([4, 7, 5, 2, 3, 5, 8], 1, 12) == -1
    assert candidate([2, 5, 4, 1, 2, 4, 12], 8, 6) == -1
    assert candidate([7, 2, 2, 6, 3, 5, 8], 2, 12) == 2
    assert candidate([1, 4, 2, 4, 10, 12, 10], 7, 8) == -1
    assert candidate([2, 2, 6, 8, 6, 3, 7], 6, 5) == 2
    assert candidate([5, 3, 6, 4, 9, 5, 4], 8, 9) == -1
    assert candidate([5, 6, 7, 5, 2, 5, 9], 5, 5) == 0
    assert candidate([6, 5, 3, 4, 2, 12, 11], 6, 6) == -1
    assert candidate([1, 1, 2, 2, 4, 4, 7], 8, 4) == -1
    assert candidate([7, 6, 5, 8, 10, 7, 4], 1, 9) == -1
    assert candidate([1, 7, 2, 4, 11, 5, 11], 4, 7) == 3
    assert candidate([1, 5, 4, 7, 2, 9, 4], 3, 5) == -1
    assert candidate([2, 3, 1, 7, 7, 10, 5], 4, 5) == -1
    assert candidate([6, 1, 5, 2, 6, 13, 8], 7, 6) == -1
    assert candidate([1, 4, 3, 8, 8, 13, 13], 6, 8) == -1
    assert candidate([2, 1, 7, 8, 4, 5, 7], 1, 4) == 1

if __name__ == '__main__':
    check(last)