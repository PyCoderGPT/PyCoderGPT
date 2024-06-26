from case_MBPP_171 import find_Element


def check(candidate):
    assert candidate([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert candidate([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert candidate([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1
    assert candidate([1, 6, 7, 6, 1], [[4, 6], [1, 4]], 1, 2) == 7
    assert candidate([1, 1, 6, 9, 9], [[1, 3], [2, 2]], 2, 1) == 9
    assert candidate([1, 3, 6, 3, 7], [[4, 5], [3, 5]], 1, 3) == 3
    assert candidate([1, 5, 6, 4, 10], [[2, 2], [3, 6]], 2, 4) == 4
    assert candidate([4, 7, 4, 8, 1], [[5, 7], [4, 3]], 2, 3) == 8
    assert candidate([6, 6, 8, 1, 9], [[2, 4], [2, 2]], 2, 2) == 9
    assert candidate([2, 7, 4, 8, 9], [[3, 1], [3, 8]], 2, 4) == 8
    assert candidate([2, 7, 1, 1, 9], [[3, 2], [2, 1]], 1, 3) == 1
    assert candidate([3, 2, 4, 8, 1], [[1, 7], [5, 5]], 2, 5) == 1
    assert candidate([5, 2, 3, 8, 10], [[1, 7], [1, 4]], 2, 5) == 10
    assert candidate([1, 4, 4, 8, 6], [[4, 3], [5, 3]], 1, 1) == 4
    assert candidate([2, 1, 2, 4, 5], [[4, 5], [2, 1]], 2, 3) == 4
    assert candidate([6, 7, 3, 4, 7], [[2, 5], [5, 8]], 2, 1) == 7
    assert candidate([3, 6, 2, 6, 9], [[4, 7], [1, 7]], 1, 2) == 2
    assert candidate([3, 4, 4, 1, 3], [[4, 1], [5, 5]], 2, 4) == 3
    assert candidate([4, 5, 5, 7, 2], [[5, 3], [5, 1]], 2, 2) == 5
    assert candidate([4, 5, 4, 1, 1], [[5, 7], [4, 1]], 2, 2) == 4
    assert candidate([2, 6, 8, 3, 3], [[2, 3], [1, 7]], 1, 4) == 3
    assert candidate([4, 6, 4, 7, 5], [[3, 7], [2, 1]], 1, 2) == 4
    assert candidate([5, 2, 3, 5, 1], [[1, 2], [1, 5]], 2, 2) == 3
    assert candidate([6, 2, 5, 5, 4], [[3, 4], [4, 4]], 2, 1) == 2
    assert candidate([6, 5, 4, 7, 10], [[4, 3], [3, 1]], 2, 1) == 5
    assert candidate([5, 3, 1, 3, 2], [[1, 5], [2, 1]], 1, 5) == 2
    assert candidate([2, 1, 4, 3, 1], [[2, 4], [3, 6]], 2, 5) == 3
    assert candidate([1, 5, 5, 2, 9], [[5, 1], [3, 4]], 2, 1) == 5
    assert candidate([6, 2, 4, 1, 2], [[1, 1], [1, 3]], 2, 4) == 2
    assert candidate([6, 6, 2, 7, 10], [[3, 5], [2, 8]], 2, 1) == 6
    assert candidate([1, 1, 7, 9, 3], [[3, 1], [1, 4]], 2, 1) == 3
    assert candidate([5, 3, 6, 6, 10], [[1, 1], [1, 4]], 1, 2) == 6
    assert candidate([5, 5, 8, 9, 1], [[2, 3], [5, 4]], 2, 3) == 8
    assert candidate([1, 5, 1, 4, 6], [[5, 6], [1, 1]], 1, 1) == 5
    assert candidate([2, 3, 7, 4, 4], [[5, 6], [3, 4]], 2, 4) == 4
    assert candidate([6, 7, 4, 1, 3], [[3, 4], [4, 2]], 1, 4) == 1
    assert candidate([3, 2, 5, 2], [[2, 2], [1, 4]], 1, 1) == 2
    assert candidate([6, 2, 5, 1], [[4, 5], [2, 1]], 2, 2) == 5
    assert candidate([5, 4, 5, 3], [[3, 3], [4, 2]], 1, 1) == 4
    assert candidate([2, 7, 8, 2], [[4, 4], [4, 1]], 1, 2) == 8
    assert candidate([6, 7, 3, 5], [[5, 6], [5, 5]], 2, 2) == 3
    assert candidate([4, 3, 2, 3], [[1, 1], [3, 3]], 2, 3) == 3
    assert candidate([6, 5, 1, 3], [[5, 2], [2, 7]], 2, 4) == 3
    assert candidate([1, 3, 7, 4], [[2, 2], [4, 7]], 2, 3) == 4
    assert candidate([4, 7, 5, 9], [[2, 6], [4, 1]], 2, 1) == 7
    assert candidate([5, 3, 3, 4], [[2, 5], [2, 5]], 2, 1) == 3
    assert candidate([3, 4, 8, 8], [[3, 2], [2, 1]], 2, 1) == 4
    assert candidate([5, 7, 1, 2], [[4, 4], [4, 2]], 1, 2) == 1
    assert candidate([5, 7, 4, 5], [[1, 6], [4, 1]], 2, 3) == 4
    assert candidate([5, 4, 1, 8], [[2, 5], [3, 4]], 2, 4) == 1
    assert candidate([2, 7, 3, 5], [[1, 3], [4, 1]], 1, 3) == 3
    assert candidate([3, 5, 8, 4], [[3, 1], [4, 6]], 1, 1) == 5
    assert candidate([1, 5, 6, 3], [[2, 1], [3, 6]], 2, 1) == 5
    assert candidate([3, 3, 5, 3], [[4, 3], [4, 6]], 1, 1) == 3
    assert candidate([5, 7, 6, 3], [[4, 6], [5, 2]], 1, 1) == 7
    assert candidate([5, 4, 7, 7], [[4, 2], [5, 6]], 2, 2) == 7
    assert candidate([2, 4, 4, 6], [[1, 2], [4, 5]], 2, 1) == 4
    assert candidate([1, 6, 1, 7], [[2, 6], [3, 2]], 2, 1) == 6
    assert candidate([5, 2, 5, 6], [[3, 6], [2, 5]], 1, 4) == 6
    assert candidate([6, 1, 8, 5], [[3, 6], [1, 7]], 2, 5) == 5
    assert candidate([6, 1, 5, 3], [[1, 4], [2, 1]], 1, 3) == 5
    assert candidate([2, 2, 4, 1], [[1, 4], [4, 3]], 2, 3) == 4
    assert candidate([1, 4, 2, 2], [[1, 6], [4, 7]], 2, 2) == 4
    assert candidate([2, 1, 5, 5], [[1, 5], [2, 4]], 1, 4) == 5
    assert candidate([5, 4, 1, 9], [[2, 5], [4, 7]], 1, 4) == 9
    assert candidate([1, 1, 4, 4], [[5, 2], [1, 2]], 2, 1) == 4
    assert candidate([3, 5, 4, 6], [[1, 4], [4, 6]], 1, 3) == 4
    assert candidate([6, 2, 1, 5], [[2, 3], [1, 5]], 2, 4) == 1
    assert candidate([6, 1, 7, 9], [[3, 4], [5, 7]], 2, 1) == 1
    assert candidate([5, 5, 1, 2, 1, 6], [[4, 1], [2, 7]], 2, 6) == 6
    assert candidate([4, 5, 1, 4, 6, 2], [[4, 6], [5, 7]], 2, 6) == 6
    assert candidate([6, 3, 4, 4, 5, 7], [[4, 2], [5, 3]], 1, 4) == 5
    assert candidate([4, 3, 4, 8, 6, 3], [[4, 6], [2, 3]], 2, 3) == 4
    assert candidate([2, 1, 3, 6, 4, 11], [[1, 4], [2, 7]], 2, 6) == 11
    assert candidate([4, 2, 1, 5, 8, 10], [[4, 6], [2, 4]], 1, 5) == 8
    assert candidate([6, 7, 6, 3, 10, 10], [[5, 1], [3, 2]], 2, 4) == 10
    assert candidate([6, 2, 2, 1, 2, 11], [[1, 1], [5, 1]], 1, 1) == 2
    assert candidate([3, 7, 7, 2, 5, 11], [[1, 3], [2, 4]], 1, 1) == 2
    assert candidate([6, 6, 8, 2, 1, 3], [[3, 3], [1, 3]], 1, 4) == 1
    assert candidate([5, 4, 6, 8, 9, 8], [[1, 2], [4, 6]], 2, 5) == 9
    assert candidate([2, 5, 7, 2, 2, 2], [[2, 2], [3, 2]], 2, 5) == 2
    assert candidate([3, 3, 5, 1, 7, 2], [[1, 3], [3, 4]], 1, 3) == 5
    assert candidate([2, 4, 3, 9, 1, 1], [[3, 6], [5, 6]], 2, 6) == 1
    assert candidate([6, 2, 3, 1, 6, 6], [[3, 4], [4, 7]], 1, 4) == 1
    assert candidate([4, 6, 6, 4, 2, 10], [[1, 5], [1, 4]], 2, 3) == 6
    assert candidate([2, 1, 4, 1, 6, 6], [[2, 1], [1, 2]], 2, 1) == 4
    assert candidate([1, 4, 1, 3, 9, 4], [[3, 6], [4, 6]], 1, 5) == 9
    assert candidate([1, 2, 1, 2, 3, 2], [[1, 3], [1, 7]], 1, 5) == 2
    assert candidate([6, 6, 3, 4, 8, 1], [[1, 3], [4, 2]], 2, 2) == 6
    assert candidate([1, 5, 1, 2, 6, 9], [[5, 2], [4, 1]], 1, 3) == 2
    assert candidate([3, 2, 3, 2, 8, 6], [[5, 5], [5, 1]], 1, 2) == 3
    assert candidate([6, 3, 4, 4, 1, 2], [[5, 4], [3, 5]], 1, 5) == 2
    assert candidate([2, 2, 4, 1, 3, 11], [[1, 1], [3, 3]], 1, 2) == 4
    assert candidate([1, 2, 1, 7, 1, 10], [[4, 2], [1, 1]], 2, 5) == 10
    assert candidate([3, 1, 2, 9, 7, 5], [[5, 3], [4, 7]], 2, 5) == 7
    assert candidate([2, 4, 1, 7, 9, 7], [[5, 6], [5, 4]], 2, 4) == 9
    assert candidate([2, 1, 4, 7, 7, 1], [[1, 4], [1, 1]], 2, 5) == 1
    assert candidate([4, 6, 8, 3, 3, 10], [[4, 5], [5, 3]], 2, 5) == 3
    assert candidate([2, 5, 4, 5, 9, 6], [[1, 5], [2, 4]], 1, 1) == 6
    assert candidate([4, 7, 2, 8, 5, 1], [[1, 6], [2, 6]], 1, 4) == 8
    assert candidate([4, 3, 6, 6, 2, 1], [[3, 2], [4, 2]], 2, 4) == 2
    assert candidate([2, 1, 4, 9, 7, 9], [[5, 2], [5, 5]], 2, 2) == 4

if __name__ == '__main__':
    check(find_Element)