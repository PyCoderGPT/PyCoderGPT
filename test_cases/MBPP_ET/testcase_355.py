from case_MBPP_355 import find_first_occurrence


def check(candidate):
    assert candidate([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
    assert candidate([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
    assert candidate([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4
    assert candidate([4, 3, 2, 7, 8, 3, 13, 4, 11, 9], 4) == -1
    assert candidate([4, 6, 1, 6, 7, 10, 9, 5, 12, 10], 4) == 0
    assert candidate([5, 1, 8, 10, 7, 11, 6, 12, 6, 13], 3) == -1
    assert candidate([2, 8, 9, 3, 4, 9, 13, 5, 7, 12], 8) == -1
    assert candidate([3, 9, 6, 3, 7, 2, 11, 5, 13, 6], 3) == 0
    assert candidate([1, 4, 8, 4, 7, 10, 12, 10, 14, 13], 5) == -1
    assert candidate([4, 10, 9, 8, 2, 10, 4, 13, 14, 12], 1) == -1
    assert candidate([2, 8, 3, 7, 3, 2, 7, 8, 7, 13], 4) == -1
    assert candidate([4, 10, 9, 8, 1, 4, 13, 10, 4, 9], 6) == -1
    assert candidate([7, 5, 2, 5, 3, 5, 13, 12, 4, 6], 10) == -1
    assert candidate([7, 5, 3, 3, 10, 9, 10, 9, 4, 13], 9) == -1
    assert candidate([3, 5, 1, 5, 9, 6, 6, 13, 12, 10], 4) == -1
    assert candidate([5, 10, 3, 4, 6, 8, 3, 9, 10, 14], 4) == -1
    assert candidate([5, 1, 7, 9, 9, 5, 12, 7, 11, 10], 8) == -1
    assert candidate([1, 5, 5, 10, 5, 9, 11, 4, 5, 7], 10) == -1
    assert candidate([6, 7, 2, 5, 11, 2, 9, 13, 11, 9], 3) == -1
    assert candidate([1, 7, 1, 5, 1, 5, 6, 7, 6, 12], 7) == 7
    assert candidate([2, 8, 9, 6, 10, 7, 10, 6, 5, 5], 10) == 4
    assert candidate([2, 5, 3, 10, 8, 7, 12, 10, 11, 12], 2) == 0
    assert candidate([4, 7, 3, 3, 7, 7, 5, 7, 13, 6], 5) == -1
    assert candidate([3, 7, 4, 1, 4, 9, 6, 14, 13, 8], 4) == 4
    assert candidate([5, 5, 1, 6, 10, 4, 11, 5, 10, 12], 5) == 0
    assert candidate([1, 2, 7, 7, 1, 7, 9, 13, 9, 14], 7) == 5
    assert candidate([5, 8, 1, 2, 3, 5, 7, 10, 4, 10], 6) == -1
    assert candidate([4, 2, 9, 9, 11, 9, 3, 13, 7, 9], 7) == -1
    assert candidate([7, 9, 6, 5, 9, 5, 3, 12, 6, 12], 10) == -1
    assert candidate([1, 4, 5, 6, 11, 8, 11, 10, 14, 10], 9) == -1
    assert candidate([1, 5, 9, 8, 4, 11, 10, 13, 11, 5], 4) == 4
    assert candidate([6, 1, 3, 8, 3, 7, 6, 11, 4, 10], 3) == 2
    assert candidate([4, 1, 8, 3, 10, 6, 5, 10, 11, 9], 10) == 4
    assert candidate([6, 9, 4, 1, 2, 1, 11, 10, 13, 6], 3) == -1
    assert candidate([2, 5, 8, 1, 10, 9, 13, 6, 7, 7], 1) == -1
    assert candidate([2, 5, 1, 5, 10, 5, 10, 6, 11, 12], 4) == -1
    assert candidate([3, 7, 7, 5, 6, 1, 6, 6, 14, 12], 2) == -1
    assert candidate([5, 5, 10, 2, 2, 3, 7, 8, 12, 5], 10) == -1
    assert candidate([6, 1, 5, 8, 3, 1, 12, 8, 5, 5], 8) == 7
    assert candidate([1, 7, 5, 2, 1, 3, 11, 7, 6, 12], 7) == 7
    assert candidate([6, 6, 8, 3, 4, 1, 6, 11, 4, 10], 1) == -1
    assert candidate([4, 5, 10, 8, 1, 9, 13, 8, 14, 10], 8) == 7
    assert candidate([1, 8, 7, 2, 11, 5, 7, 9, 9, 9], 7) == -1
    assert candidate([5, 5, 9, 4, 3, 10, 4, 4, 7, 9], 8) == -1
    assert candidate([6, 4, 3, 9, 10, 9, 11, 14, 14, 9], 6) == -1
    assert candidate([2, 1, 4, 3, 7, 4, 6, 10, 4, 10], 1) == 1
    assert candidate([6, 5, 6, 5, 8, 3, 9, 14, 14, 11], 1) == -1
    assert candidate([7, 1, 1, 9, 9, 10, 13, 10, 11, 5], 5) == -1
    assert candidate([5, 5, 1, 2, 3, 4, 5, 8, 12, 11], 10) == -1
    assert candidate([5, 2, 1, 9, 8, 11, 3, 6, 8, 4], 7) == -1
    assert candidate([3, 8, 8, 7, 8, 3, 5, 11, 14, 12], 8) == 1
    assert candidate([2, 3, 3, 10, 1, 3, 10, 14, 13, 8], 4) == -1
    assert candidate([2, 4, 1, 10, 11, 5, 7, 13, 4, 8], 6) == -1
    assert candidate([6, 4, 9, 8, 2, 10, 10, 11, 8, 5], 10) == 5
    assert candidate([1, 7, 10, 5, 8, 11, 11, 13, 12, 6], 3) == -1
    assert candidate([7, 7, 7, 6, 8, 4, 5, 4, 4, 7], 8) == 4
    assert candidate([5, 2, 4, 10, 11, 8, 3, 6, 10, 12], 2) == 1
    assert candidate([3, 6, 7, 2, 10, 1, 7, 12, 14, 7], 8) == -1
    assert candidate([5, 1, 4, 2, 3, 8, 8, 12, 12, 4], 1) == 1
    assert candidate([7, 1, 10, 9, 3, 11, 7, 8, 11, 5], 3) == 4
    assert candidate([7, 2, 9, 1, 7, 3, 3, 4, 5, 5], 8) == -1
    assert candidate([3, 3, 9, 1, 11, 7, 11, 11, 6, 13], 8) == -1
    assert candidate([5, 7, 5, 1, 2, 1, 11, 5, 11, 11], 9) == -1
    assert candidate([4, 5, 9, 6, 11, 1, 6, 5, 12, 12], 3) == -1
    assert candidate([7, 5, 4, 9, 2, 8, 9, 11, 11, 13], 4) == -1
    assert candidate([7, 5, 9, 9, 6, 11, 3, 9, 8, 5], 7) == -1
    assert candidate([7, 1, 6, 8, 4, 8, 10, 10, 10, 10], 5) == -1
    assert candidate([4, 5, 8, 4, 6, 9, 11, 10, 8, 14], 9) == 5
    assert candidate([2, 2, 1, 5, 4, 3, 9, 4, 12, 11], 4) == 4
    assert candidate([1, 1, 5, 2, 1, 6, 3, 13, 9, 9], 4) == -1
    assert candidate([6, 5, 1, 4, 10, 2, 5, 11, 11, 5], 7) == -1
    assert candidate([6, 5, 3, 8, 1, 5, 11, 9, 8, 4], 3) == -1
    assert candidate([3, 6, 6, 2, 3, 1, 10, 14, 4, 11], 11) == -1
    assert candidate([3, 8, 3, 2, 8, 1, 6, 10, 9, 4], 10) == 7
    assert candidate([2, 8, 1, 4, 3, 3, 4, 14, 7, 13], 8) == -1
    assert candidate([2, 5, 5, 3, 8, 8, 10, 8, 11, 13], 5) == 1
    assert candidate([4, 7, 4, 2, 8, 10, 5, 8, 4, 9], 4) == 0
    assert candidate([3, 9, 2, 5, 10, 1, 3, 5, 13, 6], 8) == -1
    assert candidate([2, 3, 4, 9, 3, 10, 13, 6, 14, 5], 11) == -1
    assert candidate([5, 4, 5, 9, 11, 4, 6, 8, 12, 4], 4) == 1
    assert candidate([1, 3, 2, 1, 7, 8, 12, 10, 9, 5], 8) == 5
    assert candidate([5, 8, 5, 3, 6, 8, 5, 10, 13, 10], 11) == -1
    assert candidate([2, 9, 3, 7, 4, 11, 9, 11, 7, 6], 2) == 0
    assert candidate([7, 3, 5, 4, 7, 10, 5, 5, 14, 13], 2) == -1
    assert candidate([7, 7, 6, 3, 8, 6, 9, 9, 7, 5], 10) == -1
    assert candidate([4, 1, 1, 10, 8, 10, 4, 9, 7, 10], 8) == 4
    assert candidate([6, 1, 4, 4, 3, 10, 9, 9, 11, 13], 6) == -1
    assert candidate([2, 4, 5, 5, 10, 5, 9, 8, 6, 8], 6) == -1
    assert candidate([1, 1, 4, 7, 5, 4, 11, 10, 4, 10], 1) == 0
    assert candidate([7, 2, 4, 2, 11, 4, 11, 12, 7, 10], 7) == -1
    assert candidate([2, 8, 2, 4, 8, 4, 13, 4, 4, 14], 9) == -1
    assert candidate([2, 7, 4, 8, 5, 1, 9, 5, 4, 10], 6) == -1
    assert candidate([7, 7, 4, 3, 8, 8, 7, 13, 11, 14], 3) == -1
    assert candidate([2, 8, 2, 4, 5, 11, 12, 13, 4, 4], 6) == -1
    assert candidate([6, 9, 5, 8, 7, 9, 8, 11, 9, 9], 4) == -1
    assert candidate([5, 8, 4, 1, 3, 8, 10, 14, 7, 13], 2) == -1
    assert candidate([7, 7, 3, 2, 5, 5, 6, 13, 7, 7], 7) == -1
    assert candidate([2, 5, 3, 5, 11, 4, 4, 13, 13, 7], 2) == 0
    assert candidate([7, 3, 5, 8, 11, 7, 7, 4, 7, 5], 3) == 1
    assert candidate([1, 6, 3, 10, 9, 6, 10, 9, 5, 4], 1) == 0
    assert candidate([4, 2, 4, 1, 9, 3, 12, 13, 5, 7], 8) == -1
    assert candidate([7, 6, 1, 5, 9, 5, 9, 12, 13, 11], 5) == -1

if __name__ == '__main__':
    check(find_first_occurrence)