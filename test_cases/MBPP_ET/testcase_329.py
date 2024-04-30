from case_MBPP_329 import find_First_Missing


def check(candidate):
    assert candidate([0,1,2,3],0,3) == 4
    assert candidate([0,1,2,6,9],0,4) == 3
    assert candidate([2,3,5,8,9],0,4) == 0
    assert candidate([3, 2, 6, 7], 1, 5) == 1
    assert candidate([5, 1, 6, 2], 5, 3) == 4
    assert candidate([5, 3, 5, 3], 3, 1) == 2
    assert candidate([1, 1, 4, 6], 1, 4) == 2
    assert candidate([5, 1, 2, 3], 5, 4) == 5
    assert candidate([5, 5, 1, 3], 4, 2) == 3
    assert candidate([5, 3, 7, 7], 2, 3) == 2
    assert candidate([3, 4, 7, 5], 3, 7) == 3
    assert candidate([4, 5, 4, 8], 5, 3) == 4
    assert candidate([1, 3, 5, 5], 2, 2) == 2
    assert candidate([5, 5, 3, 6], 2, 1) == 2
    assert candidate([4, 4, 1, 6], 2, 6) == 2
    assert candidate([3, 6, 3, 6], 2, 1) == 2
    assert candidate([2, 4, 2, 3], 1, 5) == 1
    assert candidate([2, 4, 2, 4], 1, 7) == 1
    assert candidate([1, 3, 3, 8], 3, 2) == 3
    assert candidate([4, 1, 6, 1], 3, 5) == 3
    assert candidate([1, 1, 6, 5], 3, 3) == 3
    assert candidate([2, 1, 5, 7], 5, 2) == 3
    assert candidate([2, 2, 5, 5], 2, 3) == 2
    assert candidate([2, 1, 6, 1], 1, 5) == 2
    assert candidate([1, 3, 4, 6], 4, 2) == 3
    assert candidate([4, 1, 7, 1], 2, 1) == 2
    assert candidate([3, 5, 6, 4], 5, 4) == 5
    assert candidate([5, 5, 5, 6], 2, 6) == 2
    assert candidate([5, 5, 6, 4], 4, 2) == 3
    assert candidate([2, 2, 1, 2], 2, 3) == 2
    assert candidate([5, 6, 4, 8], 3, 4) == 3
    assert candidate([1, 3, 6, 1], 3, 4) == 3
    assert candidate([5, 3, 2, 2], 1, 6) == 1
    assert candidate([4, 5, 4, 6], 1, 4) == 1
    assert candidate([5, 5, 2, 7], 2, 2) == 3
    assert candidate([1, 1, 5, 3], 1, 2) == 2
    assert candidate([5, 1, 5, 7, 9], 1, 6) == 2
    assert candidate([3, 5, 1, 1, 12], 3, 3) == 3
    assert candidate([4, 5, 1, 10, 13], 1, 1) == 1
    assert candidate([2, 3, 1, 1, 12], 2, 4) == 2
    assert candidate([4, 4, 1, 7, 5], 1, 8) == 1
    assert candidate([4, 1, 6, 8, 5], 4, 8) == 4
    assert candidate([5, 4, 5, 3, 12], 1, 2) == 1
    assert candidate([5, 3, 4, 7, 5], 4, 8) == 4
    assert candidate([4, 1, 2, 4, 10], 4, 7) == 4
    assert candidate([4, 4, 7, 8, 13], 4, 9) == 4
    assert candidate([1, 4, 6, 5, 8], 1, 1) == 1
    assert candidate([4, 3, 2, 6, 6], 2, 4) == 3
    assert candidate([2, 6, 4, 3, 7], 5, 4) == 5
    assert candidate([1, 6, 5, 6, 5], 4, 5) == 4
    assert candidate([4, 3, 4, 2, 6], 3, 8) == 3
    assert candidate([5, 6, 1, 2, 9], 1, 2) == 1
    assert candidate([2, 4, 1, 9, 6], 2, 3) == 2
    assert candidate([2, 1, 3, 2, 12], 4, 6) == 4
    assert candidate([3, 3, 5, 1, 6], 4, 7) == 4
    assert candidate([1, 2, 5, 9, 10], 4, 8) == 4
    assert candidate([5, 6, 2, 10, 6], 2, 1) == 2
    assert candidate([4, 6, 6, 5, 10], 2, 6) == 2
    assert candidate([4, 5, 2, 11, 11], 4, 9) == 4
    assert candidate([4, 5, 6, 4, 10], 5, 2) == 3
    assert candidate([5, 5, 3, 7, 11], 1, 3) == 1
    assert candidate([5, 2, 2, 8, 11], 4, 6) == 4
    assert candidate([3, 3, 5, 8, 7], 4, 8) == 4
    assert candidate([4, 4, 3, 4, 5], 4, 1) == 2
    assert candidate([3, 4, 3, 6, 7], 2, 8) == 2
    assert candidate([1, 3, 7, 5, 4], 4, 2) == 3
    assert candidate([2, 4, 3, 7, 11], 1, 6) == 1
    assert candidate([2, 6, 2, 9, 10], 3, 1) == 2
    assert candidate([5, 6, 4, 7, 9], 2, 3) == 2
    assert candidate([4, 1, 8, 9, 9], 1, 5) == 2
    assert candidate([4, 3, 8, 6, 4], 5, 1) == 2
    assert candidate([3, 8, 8, 6, 11], 1, 7) == 1
    assert candidate([2, 4, 8, 4, 10], 1, 4) == 1
    assert candidate([5, 1, 2, 11, 10], 3, 2) == 3
    assert candidate([7, 8, 5, 8, 12], 2, 4) == 2
    assert candidate([1, 5, 10, 13, 9], 5, 3) == 4
    assert candidate([3, 2, 3, 6, 14], 2, 5) == 2
    assert candidate([2, 7, 5, 8, 9], 4, 8) == 4
    assert candidate([2, 6, 5, 9, 7], 4, 3) == 4
    assert candidate([2, 3, 4, 5, 14], 3, 2) == 3
    assert candidate([5, 4, 1, 13, 11], 3, 8) == 3
    assert candidate([2, 5, 10, 3, 4], 1, 7) == 1
    assert candidate([3, 5, 4, 5, 10], 2, 7) == 2
    assert candidate([7, 1, 5, 13, 12], 4, 7) == 4
    assert candidate([4, 4, 5, 10, 8], 4, 8) == 4
    assert candidate([1, 8, 8, 8, 10], 1, 7) == 1
    assert candidate([3, 7, 7, 5, 12], 2, 8) == 2
    assert candidate([5, 3, 10, 12, 6], 4, 2) == 3
    assert candidate([4, 3, 5, 12, 7], 1, 5) == 1
    assert candidate([1, 2, 3, 12, 11], 1, 2) == 1
    assert candidate([5, 2, 7, 13, 5], 1, 6) == 1
    assert candidate([6, 8, 8, 13, 7], 4, 7) == 4
    assert candidate([3, 5, 6, 10, 7], 4, 1) == 2
    assert candidate([3, 2, 8, 12, 6], 3, 2) == 3
    assert candidate([5, 3, 4, 7, 7], 2, 3) == 2
    assert candidate([1, 6, 2, 6, 5], 1, 2) == 1
    assert candidate([5, 3, 4, 7, 13], 1, 1) == 1
    assert candidate([5, 2, 3, 5, 13], 1, 2) == 1
    assert candidate([7, 6, 9, 10, 9], 2, 3) == 2
    assert candidate([5, 7, 8, 12, 14], 3, 1) == 2
    assert candidate([1, 7, 4, 3, 13], 5, 4) == 5
    assert candidate([1, 2, 1, 13, 6], 5, 1) == 2

if __name__ == '__main__':
    check(find_First_Missing)