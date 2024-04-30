from case_MBPP_273 import count_Pairs


def check(candidate):
    assert candidate([1,2,1],3) == 2
    assert candidate([1,1,1,1],4) == 0
    assert candidate([1,2,3,4,5],5) == 10
    assert candidate([3, 2, 5], 1) == 0
    assert candidate([1, 5, 2], 3) == 3
    assert candidate([3, 3, 6], 3) == 2
    assert candidate([4, 1, 3], 1) == 0
    assert candidate([1, 1, 2], 1) == 0
    assert candidate([4, 3, 3], 3) == 2
    assert candidate([3, 5, 4], 3) == 3
    assert candidate([5, 7, 3], 2) == 1
    assert candidate([6, 1, 6], 1) == 0
    assert candidate([3, 3, 5], 2) == 0
    assert candidate([1, 7, 2], 1) == 0
    assert candidate([3, 5, 6], 2) == 1
    assert candidate([1, 6, 2], 3) == 3
    assert candidate([1, 2, 3], 1) == 0
    assert candidate([5, 4, 3], 2) == 1
    assert candidate([4, 7, 2], 1) == 0
    assert candidate([4, 2, 1], 3) == 3
    assert candidate([1, 6, 1], 1) == 0
    assert candidate([4, 7, 5], 1) == 0
    assert candidate([2, 5, 3], 3) == 3
    assert candidate([3, 5, 2], 2) == 1
    assert candidate([5, 4, 4], 2) == 1
    assert candidate([4, 3, 2], 1) == 0
    assert candidate([3, 1, 3], 3) == 2
    assert candidate([3, 6, 6], 2) == 1
    assert candidate([4, 2, 2], 1) == 0
    assert candidate([3, 7, 5], 2) == 1
    assert candidate([3, 2, 5], 1) == 0
    assert candidate([6, 1, 2], 2) == 1
    assert candidate([4, 5, 4], 3) == 2
    assert candidate([6, 7, 2], 2) == 1
    assert candidate([4, 3, 6], 3) == 3
    assert candidate([1, 6, 1], 3) == 2
    assert candidate([1, 1, 3, 1], 1) == 0
    assert candidate([3, 2, 4, 1], 4) == 6
    assert candidate([2, 2, 4, 1], 1) == 0
    assert candidate([5, 3, 5, 4], 3) == 2
    assert candidate([4, 1, 4, 3], 2) == 1
    assert candidate([2, 2, 1, 3], 4) == 5
    assert candidate([4, 5, 5, 1], 4) == 5
    assert candidate([6, 1, 3, 2], 4) == 6
    assert candidate([3, 6, 2, 4], 3) == 3
    assert candidate([2, 1, 5, 5], 1) == 0
    assert candidate([1, 4, 2, 2], 4) == 5
    assert candidate([1, 1, 6, 1], 4) == 3
    assert candidate([1, 2, 1, 4], 4) == 5
    assert candidate([1, 1, 3, 5], 4) == 5
    assert candidate([1, 5, 5, 3], 2) == 1
    assert candidate([5, 4, 1, 3], 2) == 1
    assert candidate([1, 2, 6, 2], 2) == 1
    assert candidate([5, 4, 5, 6], 4) == 5
    assert candidate([2, 6, 2, 6], 4) == 4
    assert candidate([3, 3, 5, 3], 4) == 3
    assert candidate([4, 3, 2, 1], 2) == 1
    assert candidate([5, 4, 3, 5], 1) == 0
    assert candidate([6, 4, 6, 6], 2) == 1
    assert candidate([4, 4, 5, 2], 2) == 0
    assert candidate([1, 2, 5, 6], 3) == 3
    assert candidate([6, 2, 5, 1], 3) == 3
    assert candidate([1, 5, 5, 6], 4) == 5
    assert candidate([3, 5, 5, 2], 3) == 2
    assert candidate([5, 3, 1, 6], 1) == 0
    assert candidate([5, 4, 2, 5], 4) == 5
    assert candidate([5, 3, 1, 1], 1) == 0
    assert candidate([2, 1, 4, 1], 3) == 3
    assert candidate([2, 3, 4, 5], 3) == 3
    assert candidate([3, 6, 1, 9, 8], 5) == 10
    assert candidate([1, 6, 8, 9, 2], 5) == 10
    assert candidate([6, 2, 4, 4, 1], 2) == 1
    assert candidate([6, 2, 4, 4, 2], 4) == 5
    assert candidate([6, 5, 5, 8, 7], 2) == 1
    assert candidate([5, 4, 7, 4, 3], 2) == 1
    assert candidate([3, 6, 1, 7, 7], 1) == 0
    assert candidate([5, 6, 5, 2, 5], 2) == 1
    assert candidate([5, 5, 4, 5, 2], 4) == 3
    assert candidate([4, 3, 4, 6, 9], 3) == 2
    assert candidate([6, 2, 4, 8, 8], 3) == 3
    assert candidate([3, 5, 3, 1, 4], 4) == 5
    assert candidate([4, 3, 1, 2, 3], 4) == 6
    assert candidate([3, 3, 2, 4, 10], 5) == 9
    assert candidate([1, 6, 3, 5, 10], 2) == 1
    assert candidate([5, 3, 6, 4, 2], 5) == 10
    assert candidate([5, 1, 4, 5, 5], 2) == 1
    assert candidate([4, 7, 5, 3, 7], 3) == 3
    assert candidate([5, 5, 3, 8, 9], 3) == 2
    assert candidate([4, 6, 8, 5, 6], 5) == 9
    assert candidate([3, 3, 6, 3, 1], 5) == 7
    assert candidate([6, 1, 5, 5, 10], 4) == 5
    assert candidate([4, 5, 4, 8, 5], 5) == 8
    assert candidate([1, 1, 5, 9, 5], 5) == 8
    assert candidate([1, 6, 5, 9, 2], 2) == 1
    assert candidate([3, 7, 8, 7, 9], 1) == 0
    assert candidate([6, 1, 1, 4, 7], 3) == 2
    assert candidate([1, 2, 2, 6, 7], 4) == 5
    assert candidate([6, 2, 6, 3, 4], 4) == 5
    assert candidate([2, 5, 1, 4, 5], 1) == 0
    assert candidate([4, 1, 7, 6, 8], 3) == 3
    assert candidate([5, 5, 4, 7, 6], 4) == 5
    assert candidate([1, 6, 1, 2, 5], 2) == 1

if __name__ == '__main__':
    check(count_Pairs)