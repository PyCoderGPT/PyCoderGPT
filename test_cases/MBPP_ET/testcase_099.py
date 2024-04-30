from case_MBPP_099 import frequency


def check(candidate):
    assert candidate([1,2,3],4) == 0
    assert candidate([1,2,2,3,3,3,4],3) == 3
    assert candidate([0,1,2,3,1,2],1) == 2
    assert candidate([1, 1, 7], 2) == 0
    assert candidate([6, 6, 4], 9) == 0
    assert candidate([3, 1, 6], 6) == 1
    assert candidate([4, 3, 6], 5) == 0
    assert candidate([5, 4, 1], 4) == 1
    assert candidate([5, 6, 2], 8) == 0
    assert candidate([5, 4, 4], 9) == 0
    assert candidate([1, 6, 8], 6) == 1
    assert candidate([2, 7, 1], 2) == 1
    assert candidate([4, 1, 1], 3) == 0
    assert candidate([5, 4, 5], 2) == 0
    assert candidate([3, 1, 3], 8) == 0
    assert candidate([3, 7, 3], 3) == 2
    assert candidate([4, 6, 1], 7) == 0
    assert candidate([5, 6, 5], 7) == 0
    assert candidate([1, 1, 3], 5) == 0
    assert candidate([1, 5, 6], 1) == 1
    assert candidate([2, 2, 7], 2) == 2
    assert candidate([3, 5, 7], 3) == 1
    assert candidate([5, 7, 6], 5) == 1
    assert candidate([4, 7, 4], 5) == 0
    assert candidate([3, 1, 5], 8) == 0
    assert candidate([5, 3, 2], 2) == 1
    assert candidate([1, 7, 4], 6) == 0
    assert candidate([5, 4, 8], 5) == 1
    assert candidate([5, 4, 4], 4) == 2
    assert candidate([5, 4, 5], 5) == 2
    assert candidate([4, 7, 3], 6) == 0
    assert candidate([3, 2, 7], 5) == 0
    assert candidate([1, 3, 8], 6) == 0
    assert candidate([1, 4, 6], 5) == 0
    assert candidate([1, 1, 8], 3) == 0
    assert candidate([3, 2, 7], 4) == 0
    assert candidate([4, 2, 4, 6, 2, 3, 3], 5) == 0
    assert candidate([3, 7, 6, 7, 7, 8, 6], 5) == 0
    assert candidate([6, 5, 2, 1, 4, 4, 9], 5) == 1
    assert candidate([5, 6, 7, 7, 8, 5, 9], 7) == 2
    assert candidate([5, 7, 4, 7, 8, 7, 4], 6) == 0
    assert candidate([2, 7, 4, 5, 2, 2, 4], 7) == 1
    assert candidate([2, 2, 2, 7, 5, 8, 3], 6) == 0
    assert candidate([2, 3, 1, 2, 2, 5, 2], 3) == 1
    assert candidate([2, 3, 6, 7, 5, 7, 9], 8) == 0
    assert candidate([3, 6, 3, 8, 6, 8, 3], 5) == 0
    assert candidate([4, 5, 6, 7, 2, 3, 9], 3) == 1
    assert candidate([4, 2, 1, 5, 4, 6, 6], 4) == 2
    assert candidate([2, 7, 2, 6, 3, 5, 2], 2) == 3
    assert candidate([6, 7, 4, 5, 2, 5, 3], 8) == 0
    assert candidate([3, 1, 2, 4, 1, 4, 6], 2) == 1
    assert candidate([2, 2, 2, 3, 4, 2, 5], 7) == 0
    assert candidate([5, 6, 2, 3, 7, 7, 5], 8) == 0
    assert candidate([5, 3, 3, 7, 4, 3, 6], 8) == 0
    assert candidate([1, 5, 1, 3, 5, 1, 3], 6) == 0
    assert candidate([6, 4, 2, 8, 4, 8, 5], 2) == 1
    assert candidate([1, 3, 6, 3, 1, 5, 1], 2) == 0
    assert candidate([4, 5, 7, 3, 3, 1, 6], 8) == 0
    assert candidate([4, 4, 5, 6, 5, 5, 1], 4) == 2
    assert candidate([4, 7, 6, 7, 5, 3, 2], 5) == 1
    assert candidate([6, 2, 1, 4, 6, 3, 3], 4) == 1
    assert candidate([3, 6, 1, 3, 3, 6, 7], 8) == 0
    assert candidate([5, 1, 2, 8, 5, 7, 1], 6) == 0
    assert candidate([4, 2, 3, 5, 2, 3, 6], 5) == 1
    assert candidate([5, 3, 7, 2, 6, 7, 1], 4) == 0
    assert candidate([3, 7, 3, 7, 2, 2, 3], 8) == 0
    assert candidate([3, 1, 2, 2, 2, 2, 9], 4) == 0
    assert candidate([1, 2, 6, 8, 2, 2, 7], 3) == 0
    assert candidate([1, 4, 2, 3, 5, 2, 8], 4) == 1
    assert candidate([1, 4, 1, 1, 6, 4], 3) == 0
    assert candidate([4, 5, 3, 3, 1, 4], 6) == 0
    assert candidate([1, 3, 1, 2, 2, 3], 1) == 2
    assert candidate([3, 3, 1, 2, 6, 7], 5) == 0
    assert candidate([1, 6, 5, 4, 6, 3], 1) == 1
    assert candidate([4, 5, 5, 8, 3, 6], 2) == 0
    assert candidate([5, 3, 6, 1, 4, 5], 5) == 2
    assert candidate([5, 1, 7, 5, 6, 7], 1) == 1
    assert candidate([2, 5, 1, 5, 1, 3], 1) == 2
    assert candidate([5, 3, 4, 3, 4, 2], 5) == 1
    assert candidate([5, 5, 4, 5, 2, 4], 6) == 0
    assert candidate([3, 1, 2, 7, 2, 1], 3) == 1
    assert candidate([1, 3, 1, 4, 1, 5], 2) == 0
    assert candidate([1, 5, 2, 7, 3, 6], 5) == 1
    assert candidate([4, 5, 2, 4, 4, 3], 2) == 1
    assert candidate([3, 6, 4, 4, 2, 2], 5) == 0
    assert candidate([3, 6, 2, 8, 2, 2], 4) == 0
    assert candidate([1, 4, 6, 5, 2, 1], 6) == 1
    assert candidate([5, 6, 2, 5, 6, 7], 5) == 2
    assert candidate([4, 5, 1, 4, 6, 5], 4) == 2
    assert candidate([5, 5, 2, 8, 1, 7], 2) == 1
    assert candidate([4, 2, 1, 1, 1, 7], 6) == 0
    assert candidate([3, 4, 3, 1, 1, 1], 3) == 2
    assert candidate([3, 4, 5, 2, 1, 2], 4) == 1
    assert candidate([3, 5, 2, 6, 3, 2], 6) == 1
    assert candidate([3, 2, 6, 5, 3, 6], 3) == 2
    assert candidate([2, 2, 3, 8, 1, 6], 2) == 2
    assert candidate([2, 4, 3, 5, 5, 1], 1) == 1
    assert candidate([4, 5, 1, 5, 6, 6], 4) == 1
    assert candidate([1, 6, 6, 3, 1, 7], 6) == 2
    assert candidate([1, 2, 3, 2, 6, 3], 3) == 2
    assert candidate([2, 6, 1, 3, 1, 3], 2) == 1
    assert candidate([4, 3, 4, 7, 3, 2], 2) == 1

if __name__ == '__main__':
    check(frequency)