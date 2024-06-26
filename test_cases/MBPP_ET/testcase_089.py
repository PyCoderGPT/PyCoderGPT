from case_MBPP_089 import find_lists


def check(candidate):
    assert candidate(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
    assert candidate(([1, 2], [3, 4], [5, 6]))  == 3
    assert candidate(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1
    assert candidate(([3, 3, 3, 2], [9, 2, 11, 8])) == 2
    assert candidate(([5, 5, 4, 4], [9, 2, 6, 13])) == 2
    assert candidate(([6, 2, 1, 5], [1, 3, 6, 11])) == 2
    assert candidate(([4, 2, 2, 7], [6, 2, 3, 11])) == 2
    assert candidate(([4, 1, 2, 7], [3, 3, 5, 3])) == 2
    assert candidate(([2, 5, 4, 2], [9, 6, 7, 10])) == 2
    assert candidate(([1, 6, 2, 5], [8, 7, 8, 10])) == 2
    assert candidate(([5, 3, 4, 5], [7, 9, 8, 3])) == 2
    assert candidate(([1, 4, 3, 9], [10, 10, 2, 13])) == 2
    assert candidate(([2, 5, 3, 3], [3, 1, 5, 12])) == 2
    assert candidate(([1, 7, 2, 4], [9, 10, 10, 12])) == 2
    assert candidate(([4, 1, 8, 1], [1, 6, 2, 3])) == 2
    assert candidate(([5, 2, 8, 4], [9, 3, 7, 6])) == 2
    assert candidate(([6, 3, 7, 6], [6, 3, 6, 9])) == 2
    assert candidate(([4, 5, 5, 5], [4, 10, 12, 10])) == 2
    assert candidate(([4, 4, 4, 3], [3, 1, 12, 13])) == 2
    assert candidate(([2, 4, 6, 2], [10, 9, 11, 4])) == 2
    assert candidate(([2, 2, 3, 8], [7, 1, 8, 12])) == 2
    assert candidate(([1, 4, 8, 1], [3, 5, 9, 11])) == 2
    assert candidate(([1, 7, 1, 3], [10, 10, 4, 12])) == 2
    assert candidate(([3, 4, 2, 9], [10, 5, 11, 10])) == 2
    assert candidate(([4, 3, 5, 3], [1, 3, 7, 7])) == 2
    assert candidate(([6, 1, 8, 2], [2, 2, 7, 9])) == 2
    assert candidate(([1, 4, 3, 8], [5, 11, 6, 3])) == 2
    assert candidate(([6, 2, 2, 1], [8, 9, 4, 11])) == 2
    assert candidate(([3, 5, 5, 5], [3, 7, 10, 7])) == 2
    assert candidate(([2, 3, 5, 6], [3, 9, 7, 6])) == 2
    assert candidate(([4, 3, 2, 9], [4, 1, 2, 11])) == 2
    assert candidate(([6, 3, 2, 6], [5, 3, 7, 4])) == 2
    assert candidate(([6, 3, 5, 9], [5, 1, 7, 3])) == 2
    assert candidate(([5, 2, 3, 7], [6, 10, 6, 3])) == 2
    assert candidate(([1, 4, 7, 4], [5, 3, 11, 9])) == 2
    assert candidate(([3, 6, 2, 7], [2, 8, 5, 6])) == 2
    assert candidate(([3, 6], [8, 5], [1, 7])) == 3
    assert candidate(([4, 2], [3, 6], [10, 7])) == 3
    assert candidate(([3, 2], [6, 9], [4, 6])) == 3
    assert candidate(([6, 7], [1, 8], [9, 4])) == 3
    assert candidate(([4, 4], [8, 2], [6, 7])) == 3
    assert candidate(([1, 5], [8, 9], [10, 8])) == 3
    assert candidate(([5, 1], [4, 2], [8, 6])) == 3
    assert candidate(([3, 2], [4, 2], [1, 10])) == 3
    assert candidate(([3, 1], [1, 7], [4, 1])) == 3
    assert candidate(([6, 6], [1, 9], [10, 3])) == 3
    assert candidate(([1, 4], [5, 5], [6, 2])) == 3
    assert candidate(([2, 1], [7, 9], [10, 8])) == 3
    assert candidate(([5, 1], [2, 7], [9, 2])) == 3
    assert candidate(([3, 7], [1, 4], [3, 9])) == 3
    assert candidate(([2, 2], [2, 8], [9, 1])) == 3
    assert candidate(([1, 4], [5, 8], [4, 10])) == 3
    assert candidate(([3, 6], [6, 5], [5, 5])) == 3
    assert candidate(([3, 1], [1, 1], [4, 7])) == 3
    assert candidate(([6, 3], [7, 9], [10, 3])) == 3
    assert candidate(([1, 7], [8, 4], [1, 5])) == 3
    assert candidate(([2, 1], [5, 3], [6, 9])) == 3
    assert candidate(([3, 3], [6, 1], [9, 6])) == 3
    assert candidate(([3, 2], [2, 4], [5, 8])) == 3
    assert candidate(([4, 7], [6, 7], [10, 9])) == 3
    assert candidate(([5, 3], [2, 1], [4, 10])) == 3
    assert candidate(([6, 6], [3, 3], [7, 7])) == 3
    assert candidate(([6, 2], [5, 7], [8, 2])) == 3
    assert candidate(([5, 6], [7, 4], [7, 1])) == 3
    assert candidate(([4, 5], [3, 8], [6, 4])) == 3
    assert candidate(([6, 4], [6, 4], [3, 7])) == 3
    assert candidate(([5, 1], [3, 5], [7, 8])) == 3
    assert candidate(([6, 5], [1, 1], [3, 2])) == 3
    assert candidate(([3, 1], [7, 5], [1, 6])) == 3
    assert candidate([12, 4, 8, 2, 1, 2, 1, 1, 3]) == 1
    assert candidate([13, 12, 6, 8, 9, 2, 1, 5, 6]) == 1
    assert candidate([11, 7, 8, 6, 10, 1, 2, 2, 2]) == 1
    assert candidate([13, 4, 10, 11, 7, 9, 8, 6, 4]) == 1
    assert candidate([10, 8, 2, 8, 3, 2, 2, 1, 6]) == 1
    assert candidate([5, 11, 5, 7, 9, 8, 4, 7, 4]) == 1
    assert candidate([6, 7, 8, 3, 2, 4, 3, 2, 5]) == 1
    assert candidate([5, 4, 9, 11, 6, 4, 5, 2, 6]) == 1
    assert candidate([7, 4, 5, 6, 5, 5, 3, 1, 6]) == 1
    assert candidate([12, 9, 5, 3, 3, 1, 6, 4, 1]) == 1
    assert candidate([7, 3, 10, 11, 10, 5, 5, 1, 1]) == 1
    assert candidate([11, 5, 10, 10, 10, 8, 8, 4, 3]) == 1
    assert candidate([7, 5, 12, 4, 8, 7, 7, 3, 2]) == 1
    assert candidate([11, 11, 4, 7, 2, 2, 1, 1, 5]) == 1
    assert candidate([7, 3, 6, 10, 8, 9, 5, 3, 2]) == 1
    assert candidate([10, 11, 2, 5, 6, 9, 3, 3, 4]) == 1
    assert candidate([11, 3, 10, 6, 1, 3, 5, 4, 1]) == 1
    assert candidate([7, 9, 2, 10, 6, 9, 5, 6, 5]) == 1
    assert candidate([6, 10, 6, 4, 3, 3, 5, 5, 6]) == 1
    assert candidate([13, 12, 9, 2, 4, 1, 4, 3, 4]) == 1
    assert candidate([14, 9, 2, 3, 3, 6, 4, 1, 3]) == 1
    assert candidate([4, 13, 9, 6, 5, 6, 7, 5, 6]) == 1
    assert candidate([4, 4, 4, 4, 2, 4, 6, 4, 5]) == 1
    assert candidate([4, 4, 12, 8, 1, 4, 5, 6, 4]) == 1
    assert candidate([6, 12, 7, 11, 3, 8, 3, 7, 4]) == 1
    assert candidate([7, 6, 5, 9, 1, 4, 1, 4, 1]) == 1
    assert candidate([7, 3, 11, 2, 7, 7, 4, 7, 3]) == 1
    assert candidate([5, 10, 2, 3, 4, 7, 2, 3, 5]) == 1
    assert candidate([8, 8, 12, 6, 8, 3, 8, 5, 3]) == 1
    assert candidate([5, 4, 12, 9, 1, 3, 2, 6, 4]) == 1
    assert candidate([5, 11, 7, 2, 9, 6, 6, 3, 2]) == 1
    assert candidate([10, 4, 7, 10, 5, 6, 4, 4, 4]) == 1
    assert candidate([5, 12, 8, 7, 10, 5, 6, 1, 1]) == 1

if __name__ == '__main__':
    check(find_lists)