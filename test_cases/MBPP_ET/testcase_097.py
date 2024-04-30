from case_MBPP_097 import find_even_Pair


def check(candidate):
    assert candidate([5,4,7,2,1],5) == 4
    assert candidate([7,2,8,1,0,5,11],7) == 9
    assert candidate([1,2,3],3) == 1
    assert candidate([3, 1, 7, 5, 3], 4) == 6
    assert candidate([4, 5, 6, 6, 1], 3) == 1
    assert candidate([5, 7, 9, 1, 6], 2) == 1
    assert candidate([10, 4, 4, 2, 1], 4) == 6
    assert candidate([9, 1, 4, 6, 2], 2) == 1
    assert candidate([3, 7, 10, 4, 6], 4) == 2
    assert candidate([3, 2, 8, 4, 6], 4) == 3
    assert candidate([8, 1, 7, 2, 6], 4) == 2
    assert candidate([8, 6, 2, 7, 4], 5) == 6
    assert candidate([8, 5, 2, 1, 5], 2) == 0
    assert candidate([10, 9, 8, 2, 4], 4) == 3
    assert candidate([6, 4, 4, 4, 4], 5) == 10
    assert candidate([2, 1, 5, 3, 2], 2) == 0
    assert candidate([10, 4, 7, 7, 1], 4) == 2
    assert candidate([5, 7, 10, 5, 5], 2) == 1
    assert candidate([3, 6, 8, 6, 6], 2) == 0
    assert candidate([2, 5, 9, 1, 6], 3) == 1
    assert candidate([7, 3, 9, 5, 3], 4) == 6
    assert candidate([2, 8, 6, 3, 4], 4) == 3
    assert candidate([8, 5, 5, 3, 3], 3) == 1
    assert candidate([1, 2, 12, 6, 2], 1) == 0
    assert candidate([4, 3, 5, 4, 6], 5) == 4
    assert candidate([2, 1, 8, 2, 5], 4) == 3
    assert candidate([2, 9, 12, 2, 5], 4) == 3
    assert candidate([3, 6, 8, 6, 4], 3) == 1
    assert candidate([1, 8, 2, 3, 1], 5) == 4
    assert candidate([6, 7, 8, 4, 6], 5) == 6
    assert candidate([9, 6, 2, 3, 1], 5) == 4
    assert candidate([10, 1, 12, 2, 1], 1) == 0
    assert candidate([1, 3, 8, 5, 2], 4) == 3
    assert candidate([5, 2, 11, 5, 1], 2) == 0
    assert candidate([10, 3, 3, 7, 5], 4) == 3
    assert candidate([2, 7, 4, 1, 4], 4) == 2
    assert candidate([11, 2, 4, 4, 4, 9, 7], 7) == 9
    assert candidate([6, 2, 4, 4, 1, 2, 9], 4) == 6
    assert candidate([9, 6, 8, 6, 4, 2, 13], 4) == 3
    assert candidate([9, 4, 10, 5, 4, 8, 11], 4) == 2
    assert candidate([2, 3, 7, 2, 4, 2, 8], 2) == 0
    assert candidate([3, 2, 4, 4, 5, 5, 13], 7) == 9
    assert candidate([8, 3, 10, 3, 3, 9, 7], 3) == 1
    assert candidate([4, 3, 8, 6, 1, 8, 16], 4) == 3
    assert candidate([7, 6, 5, 3, 2, 1, 15], 5) == 4
    assert candidate([2, 4, 4, 6, 2, 9, 8], 3) == 3
    assert candidate([3, 3, 4, 6, 3, 5, 11], 5) == 4
    assert candidate([8, 6, 8, 1, 2, 9, 13], 3) == 3
    assert candidate([12, 3, 13, 2, 3, 5, 15], 3) == 1
    assert candidate([3, 5, 8, 2, 1, 10, 11], 6) == 6
    assert candidate([6, 3, 4, 5, 3, 6, 12], 2) == 0
    assert candidate([10, 3, 4, 1, 4, 5, 8], 2) == 0
    assert candidate([11, 5, 8, 5, 3, 6, 16], 4) == 3
    assert candidate([5, 6, 8, 6, 2, 1, 16], 6) == 7
    assert candidate([9, 4, 13, 4, 1, 4, 16], 7) == 9
    assert candidate([8, 4, 10, 4, 4, 1, 10], 5) == 10
    assert candidate([6, 6, 6, 3, 3, 7, 11], 3) == 3
    assert candidate([9, 5, 5, 1, 1, 6, 7], 7) == 15
    assert candidate([10, 4, 11, 4, 5, 5, 7], 5) == 4
    assert candidate([5, 5, 8, 5, 1, 3, 15], 4) == 3
    assert candidate([5, 1, 12, 2, 1, 9, 7], 2) == 1
    assert candidate([7, 4, 13, 1, 3, 9, 7], 6) == 10
    assert candidate([2, 7, 9, 5, 2, 7, 14], 7) == 9
    assert candidate([10, 2, 10, 2, 4, 10, 7], 4) == 6
    assert candidate([8, 5, 7, 2, 4, 2, 14], 5) == 4
    assert candidate([10, 1, 6, 3, 1, 1, 11], 7) == 11
    assert candidate([2, 1, 12, 2, 4, 4, 11], 7) == 11
    assert candidate([8, 2, 4, 4, 5, 8, 7], 5) == 6
    assert candidate([7, 6, 3, 1, 3, 1, 8], 7) == 11
    assert candidate([4, 5, 7], 3) == 1
    assert candidate([6, 7, 2], 3) == 1
    assert candidate([1, 3, 4], 1) == 0
    assert candidate([2, 7, 7], 2) == 0
    assert candidate([5, 3, 4], 1) == 0
    assert candidate([5, 3, 2], 3) == 1
    assert candidate([1, 6, 2], 1) == 0
    assert candidate([1, 7, 8], 3) == 1
    assert candidate([3, 2, 4], 3) == 1
    assert candidate([4, 4, 7], 1) == 0
    assert candidate([2, 7, 5], 3) == 1
    assert candidate([5, 7, 4], 1) == 0
    assert candidate([3, 7, 2], 2) == 1
    assert candidate([4, 2, 3], 2) == 1
    assert candidate([2, 7, 7], 1) == 0
    assert candidate([1, 2, 6], 2) == 0
    assert candidate([2, 1, 4], 2) == 0
    assert candidate([3, 4, 4], 2) == 0
    assert candidate([1, 2, 7], 3) == 1
    assert candidate([5, 3, 3], 1) == 0
    assert candidate([4, 3, 5], 2) == 0
    assert candidate([5, 4, 7], 1) == 0
    assert candidate([1, 5, 6], 3) == 1
    assert candidate([3, 3, 5], 3) == 3
    assert candidate([1, 3, 5], 3) == 3
    assert candidate([1, 7, 3], 2) == 1
    assert candidate([5, 6, 7], 3) == 1
    assert candidate([6, 3, 6], 3) == 1
    assert candidate([5, 1, 2], 3) == 1
    assert candidate([5, 2, 3], 3) == 1
    assert candidate([4, 4, 5], 2) == 1
    assert candidate([5, 1, 6], 1) == 0
    assert candidate([4, 4, 6], 2) == 1

if __name__ == '__main__':
    check(find_even_Pair)