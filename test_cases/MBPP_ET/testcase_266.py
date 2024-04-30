from case_MBPP_266 import find_Odd_Pair


def check(candidate):
    assert candidate([5,4,7,2,1],5) == 6
    assert candidate([7,2,8,1,0,5,11],7) == 12
    assert candidate([1,2,3],3) == 2
    assert candidate([7, 6, 11, 1, 3], 3) == 2
    assert candidate([2, 9, 11, 7, 4], 2) == 1
    assert candidate([1, 7, 6, 4, 6], 4) == 4
    assert candidate([7, 2, 10, 5, 4], 2) == 1
    assert candidate([7, 1, 2, 3, 1], 4) == 3
    assert candidate([7, 3, 6, 7, 2], 4) == 3
    assert candidate([5, 2, 6, 4, 2], 3) == 2
    assert candidate([10, 4, 5, 6, 2], 1) == 0
    assert candidate([6, 9, 7, 2, 5], 4) == 4
    assert candidate([1, 2, 12, 5, 3], 3) == 2
    assert candidate([5, 4, 3, 1, 6], 3) == 2
    assert candidate([9, 1, 6, 2, 5], 5) == 6
    assert candidate([5, 2, 12, 1, 4], 3) == 2
    assert candidate([7, 8, 11, 3, 5], 4) == 3
    assert candidate([5, 5, 5, 5, 6], 2) == 0
    assert candidate([6, 7, 4, 1, 2], 4) == 4
    assert candidate([9, 4, 2, 7, 1], 5) == 6
    assert candidate([5, 4, 3, 2, 2], 4) == 4
    assert candidate([5, 1, 8, 6, 2], 5) == 6
    assert candidate([10, 9, 11, 3, 2], 5) == 6
    assert candidate([7, 7, 3, 4, 6], 5) == 6
    assert candidate([10, 4, 11, 5, 4], 2) == 0
    assert candidate([7, 5, 3, 1, 3], 4) == 0
    assert candidate([1, 1, 5, 2, 2], 4) == 3
    assert candidate([7, 9, 2, 6, 1], 5) == 6
    assert candidate([6, 6, 5, 5, 5], 4) == 4
    assert candidate([3, 2, 6, 3, 4], 5) == 6
    assert candidate([2, 9, 5, 2, 4], 3) == 2
    assert candidate([4, 1, 4, 5, 1], 1) == 0
    assert candidate([8, 1, 3, 4, 2], 5) == 6
    assert candidate([8, 7, 5, 2, 2], 4) == 4
    assert candidate([3, 6, 8, 2, 5], 2) == 1
    assert candidate([4, 8, 11, 4, 6], 3) == 2
    assert candidate([10, 7, 3, 6, 5, 9, 12], 3) == 2
    assert candidate([10, 7, 10, 2, 4, 9, 6], 3) == 2
    assert candidate([4, 3, 7, 2, 1, 6, 10], 6) == 9
    assert candidate([9, 4, 5, 6, 2, 3, 14], 5) == 6
    assert candidate([7, 2, 11, 2, 1, 10, 11], 2) == 1
    assert candidate([5, 7, 8, 2, 3, 1, 13], 4) == 4
    assert candidate([11, 5, 9, 1, 4, 5, 14], 5) == 4
    assert candidate([8, 6, 4, 2, 3, 7, 14], 5) == 4
    assert candidate([8, 3, 6, 1, 4, 7, 13], 7) == 12
    assert candidate([2, 2, 4, 5, 2, 1, 11], 6) == 8
    assert candidate([3, 6, 4, 2, 1, 9, 12], 4) == 3
    assert candidate([11, 7, 8, 5, 4, 2, 12], 3) == 2
    assert candidate([6, 7, 12, 2, 3, 7, 8], 7) == 12
    assert candidate([10, 7, 11, 2, 1, 4, 7], 5) == 6
    assert candidate([11, 6, 7, 5, 4, 8, 11], 4) == 3
    assert candidate([4, 7, 10, 3, 2, 8, 8], 7) == 10
    assert candidate([11, 7, 13, 2, 1, 3, 12], 7) == 10
    assert candidate([11, 2, 9, 4, 2, 1, 11], 5) == 6
    assert candidate([9, 6, 11, 6, 3, 4, 14], 5) == 6
    assert candidate([10, 6, 4, 3, 4, 9, 6], 5) == 4
    assert candidate([9, 5, 5, 4, 3, 10, 16], 7) == 12
    assert candidate([3, 1, 3, 1, 1, 6, 11], 2) == 0
    assert candidate([8, 3, 12, 6, 3, 7, 11], 6) == 9
    assert candidate([10, 5, 7, 4, 4, 4, 11], 2) == 1
    assert candidate([10, 5, 10, 5, 4, 6, 13], 6) == 8
    assert candidate([6, 7, 3, 1, 3, 6, 15], 5) == 4
    assert candidate([8, 5, 3, 6, 3, 5, 7], 5) == 6
    assert candidate([5, 4, 9, 1, 5, 5, 10], 3) == 2
    assert candidate([11, 5, 13, 4, 5, 5, 6], 3) == 0
    assert candidate([9, 5, 4, 4, 3, 6, 10], 3) == 2
    assert candidate([11, 6, 9, 3, 2, 3, 8], 7) == 12
    assert candidate([3, 3, 3, 3, 1, 1, 13], 6) == 0
    assert candidate([7, 2, 9, 5, 4, 3, 15], 7) == 10
    assert candidate([5, 2, 5], 2) == 1
    assert candidate([3, 2, 6], 1) == 0
    assert candidate([3, 3, 4], 3) == 2
    assert candidate([5, 5, 8], 1) == 0
    assert candidate([3, 2, 8], 1) == 0
    assert candidate([5, 1, 7], 3) == 0
    assert candidate([3, 1, 8], 1) == 0
    assert candidate([3, 6, 8], 1) == 0
    assert candidate([5, 7, 1], 3) == 0
    assert candidate([1, 4, 8], 2) == 1
    assert candidate([1, 3, 2], 1) == 0
    assert candidate([2, 3, 7], 1) == 0
    assert candidate([5, 3, 2], 2) == 0
    assert candidate([3, 5, 4], 2) == 0
    assert candidate([6, 1, 2], 3) == 2
    assert candidate([6, 3, 1], 2) == 1
    assert candidate([5, 5, 8], 1) == 0
    assert candidate([1, 4, 7], 3) == 2
    assert candidate([6, 2, 8], 2) == 0
    assert candidate([4, 6, 4], 1) == 0
    assert candidate([5, 6, 7], 2) == 1
    assert candidate([5, 2, 5], 1) == 0
    assert candidate([1, 3, 5], 3) == 0
    assert candidate([5, 5, 1], 3) == 0
    assert candidate([6, 3, 2], 2) == 1
    assert candidate([3, 7, 1], 2) == 0
    assert candidate([6, 7, 8], 3) == 2
    assert candidate([5, 4, 1], 3) == 2
    assert candidate([6, 5, 3], 3) == 2
    assert candidate([6, 2, 2], 3) == 0
    assert candidate([4, 5, 3], 1) == 0
    assert candidate([5, 3, 6], 1) == 0
    assert candidate([2, 1, 4], 1) == 0

if __name__ == '__main__':
    check(find_Odd_Pair)