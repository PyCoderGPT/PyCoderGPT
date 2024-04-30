from case_MBPP_069 import search


def check(candidate):
    assert candidate([1,1,2,2,3],5) == 3
    assert candidate([1,1,3,3,4,4,5,5,7,7,8],11) == 8
    assert candidate([1,2,2,3,3,4,4],7) == 1
    assert candidate([1, 6, 2, 3, 7], 4) == 6
    assert candidate([4, 2, 7, 5, 7], 2) == 6
    assert candidate([5, 2, 3, 1, 5], 5) == 0
    assert candidate([6, 3, 5, 4, 1], 4) == 4
    assert candidate([2, 3, 3, 6, 2], 1) == 2
    assert candidate([5, 6, 6, 1, 8], 2) == 3
    assert candidate([6, 4, 5, 6, 1], 5) == 0
    assert candidate([5, 4, 1, 1, 8], 2) == 1
    assert candidate([1, 5, 5, 1, 2], 1) == 1
    assert candidate([5, 6, 6, 3, 1], 5) == 7
    assert candidate([5, 6, 5, 2, 7], 1) == 5
    assert candidate([2, 4, 7, 2, 2], 1) == 2
    assert candidate([1, 1, 6, 1, 4], 4) == 7
    assert candidate([5, 2, 2, 5, 4], 5) == 4
    assert candidate([4, 4, 1, 4, 7], 3) == 1
    assert candidate([4, 3, 6, 1, 2], 1) == 4
    assert candidate([2, 5, 7, 4, 7], 1) == 2
    assert candidate([2, 2, 5, 4, 5], 2) == 0
    assert candidate([1, 1, 3, 2, 3], 3) == 3
    assert candidate([3, 3, 7, 6, 3], 5) == 2
    assert candidate([1, 2, 3, 7, 4], 5) == 3
    assert candidate([1, 1, 7, 4, 1], 1) == 1
    assert candidate([2, 2, 5, 5, 5], 1) == 2
    assert candidate([2, 1, 4, 1, 3], 2) == 3
    assert candidate([5, 6, 3, 3, 5], 4) == 3
    assert candidate([6, 2, 3, 6, 3], 2) == 4
    assert candidate([5, 3, 7, 2, 4], 3) == 1
    assert candidate([1, 3, 7, 3, 7], 4) == 6
    assert candidate([4, 4, 3, 7, 5], 3) == 3
    assert candidate([1, 1, 4, 3, 4], 3) == 4
    assert candidate([4, 4, 4, 4, 7], 2) == 0
    assert candidate([3, 2, 6, 6, 7], 2) == 1
    assert candidate([3, 1, 1, 6, 2], 1) == 3
    assert candidate([3, 6, 7, 7, 3, 2, 1, 4, 6, 9, 4], 9) == 7
    assert candidate([4, 5, 7, 2, 7, 5, 3, 7, 3, 12, 7], 9) == 1
    assert candidate([1, 3, 5, 6, 9, 7, 4, 10, 3, 11, 13], 11) == 4
    assert candidate([4, 5, 3, 6, 4, 1, 10, 10, 5, 11, 6], 10) == 15
    assert candidate([6, 6, 2, 5, 1, 1, 5, 2, 12, 6, 10], 8) == 0
    assert candidate([5, 3, 5, 3, 7, 7, 6, 2, 4, 6, 10], 6) == 0
    assert candidate([6, 3, 1, 2, 7, 5, 7, 5, 5, 11, 11], 8) == 6
    assert candidate([5, 2, 3, 4, 5, 3, 7, 10, 9, 6, 12], 8) == 11
    assert candidate([2, 1, 5, 7, 5, 1, 4, 8, 4, 11, 8], 11) == 14
    assert candidate([6, 3, 8, 4, 5, 6, 1, 4, 3, 8, 8], 8) == 15
    assert candidate([3, 5, 2, 3, 5, 6, 9, 5, 12, 6, 11], 11) == 9
    assert candidate([4, 1, 8, 1, 2, 1, 4, 8, 2, 4, 4], 9) == 1
    assert candidate([5, 6, 7, 8, 4, 6, 4, 6, 12, 2, 11], 9) == 0
    assert candidate([4, 2, 4, 6, 3, 2, 4, 3, 2, 2, 6], 7) == 1
    assert candidate([6, 2, 3, 5, 7, 5, 2, 5, 10, 7, 5], 7) == 2
    assert candidate([4, 6, 2, 1, 3, 6, 3, 1, 10, 4, 12], 7) == 7
    assert candidate([6, 5, 1, 1, 7, 5, 10, 4, 5, 6, 8], 7) == 11
    assert candidate([3, 6, 1, 6, 3, 4, 3, 10, 2, 7, 4], 8) == 12
    assert candidate([5, 2, 1, 7, 2, 2, 7, 6, 9, 12, 11], 7) == 6
    assert candidate([5, 5, 8, 1, 1, 2, 8, 10, 9, 4, 9], 7) == 2
    assert candidate([6, 5, 3, 3, 1, 5, 2, 8, 7, 7, 4], 9) == 10
    assert candidate([5, 6, 8, 7, 9, 8, 3, 4, 5, 10, 10], 8) == 10
    assert candidate([4, 6, 1, 2, 1, 5, 8, 7, 7, 9, 7], 7) == 13
    assert candidate([2, 5, 2, 4, 3, 9, 2, 1, 11, 5, 6], 9) == 3
    assert candidate([5, 6, 2, 1, 8, 6, 10, 3, 6, 5, 7], 8) == 7
    assert candidate([2, 1, 6, 7, 4, 4, 5, 6, 8, 12, 6], 6) == 2
    assert candidate([4, 3, 2, 4, 7, 2, 8, 1, 5, 11, 13], 7) == 12
    assert candidate([2, 2, 3, 3, 6, 1, 1, 6, 9, 9, 9], 9) == 9
    assert candidate([3, 4, 8, 3, 5, 6, 7, 10, 4, 6, 6], 8) == 2
    assert candidate([1, 6, 8, 1, 3, 2, 6, 9, 12, 9, 13], 9) == 12
    assert candidate([4, 5, 1, 4, 6, 1, 10, 3, 5, 6, 5], 6) == 3
    assert candidate([6, 1, 3, 8, 8, 6, 10, 10, 10, 10, 7], 7) == 8
    assert candidate([1, 6, 8, 3, 7, 7, 6, 10, 11, 9, 5], 9) == 11
    assert candidate([2, 2, 1, 8, 3, 3, 8], 2) == 0
    assert candidate([4, 5, 6, 3, 7, 8, 5], 6) == 11
    assert candidate([6, 5, 6, 5, 4, 3, 6], 2) == 3
    assert candidate([2, 3, 7, 2, 3, 1, 4], 5) == 7
    assert candidate([1, 4, 3, 4, 3, 1, 3], 3) == 6
    assert candidate([3, 6, 4, 1, 3, 6, 8], 4) == 0
    assert candidate([1, 1, 2, 7, 3, 9, 7], 6) == 15
    assert candidate([4, 5, 7, 1, 1, 1, 3], 5) == 6
    assert candidate([3, 5, 4, 3, 5, 8, 9], 5) == 4
    assert candidate([4, 3, 2, 2, 7, 1, 6], 5) == 0
    assert candidate([3, 3, 7, 3, 7, 8, 5], 7) == 14
    assert candidate([1, 3, 5, 1, 7, 1, 3], 4) == 6
    assert candidate([6, 6, 4, 8, 5, 3, 5], 3) == 4
    assert candidate([1, 7, 7, 1, 8, 5, 4], 2) == 6
    assert candidate([1, 6, 1, 8, 7, 5, 1], 7) == 13
    assert candidate([5, 1, 7, 1, 3, 8, 4], 5) == 1
    assert candidate([1, 2, 7, 7, 4, 6, 7], 3) == 4
    assert candidate([6, 1, 1, 2, 2, 5, 5], 7) == 6
    assert candidate([4, 5, 7, 4, 4, 3, 5], 3) == 6
    assert candidate([5, 4, 2, 3, 1, 8, 7], 6) == 9
    assert candidate([1, 1, 6, 1, 1, 6, 5], 6) == 0
    assert candidate([6, 6, 1, 1, 8, 7, 2], 7) == 13
    assert candidate([4, 2, 1, 7, 1, 7, 6], 5) == 1
    assert candidate([6, 3, 2, 4, 5, 8, 4], 7) == 10
    assert candidate([5, 2, 4, 4, 4, 9, 7], 4) == 7
    assert candidate([2, 2, 1, 3, 6, 6, 8], 6) == 2
    assert candidate([4, 2, 2, 4, 8, 5, 3], 3) == 4
    assert candidate([4, 7, 2, 3, 6, 7, 6], 7) == 5
    assert candidate([4, 2, 5, 7, 2, 4, 6], 7) == 4
    assert candidate([3, 4, 4, 8, 8, 1, 6], 3) == 3
    assert candidate([1, 5, 5, 3, 1, 5, 4], 2) == 4
    assert candidate([6, 6, 3, 6, 5, 5, 8], 7) == 13
    assert candidate([6, 2, 3, 6, 1, 1, 5], 6) == 1

if __name__ == '__main__':
    check(search)