from case_MBPP_282 import is_Sub_Array


def check(candidate):
    assert candidate([1,4,3,5],[1,2],4,2) == False
    assert candidate([1,2,1],[1,2,1],3,3) == True
    assert candidate([1,0,2,2],[2,2,0],4,3) ==False
    assert candidate([3, 3, 4, 8], [2, 2], 1, 3) == False
    assert candidate([6, 3, 5, 9], [5, 3], 4, 7) == False
    assert candidate([1, 5, 3, 2], [5, 3], 1, 3) == False
    assert candidate([5, 9, 7, 10], [1, 1], 4, 2) == False
    assert candidate([4, 7, 5, 1], [1, 7], 3, 3) == False
    assert candidate([1, 4, 8, 10], [5, 4], 3, 2) == False
    assert candidate([6, 3, 3, 5], [4, 4], 2, 4) == False
    assert candidate([2, 4, 4, 10], [1, 6], 3, 1) == False
    assert candidate([2, 1, 4, 10], [6, 6], 1, 3) == False
    assert candidate([4, 4, 3, 8], [4, 1], 4, 2) == False
    assert candidate([4, 4, 5, 1], [2, 3], 1, 3) == False
    assert candidate([1, 2, 6, 7], [5, 3], 3, 5) == False
    assert candidate([4, 3, 7, 10], [2, 7], 3, 3) == False
    assert candidate([6, 7, 3, 10], [2, 3], 4, 5) == False
    assert candidate([1, 8, 2, 3], [4, 7], 3, 2) == False
    assert candidate([3, 6, 6, 5], [6, 7], 1, 7) == False
    assert candidate([1, 6, 3, 4], [4, 1], 2, 4) == False
    assert candidate([6, 4, 4, 10], [2, 3], 2, 7) == False
    assert candidate([4, 8, 1, 10], [4, 6], 2, 7) == False
    assert candidate([5, 9, 1, 3], [6, 5], 2, 6) == False
    assert candidate([2, 4, 6, 6], [1, 6], 4, 3) == False
    assert candidate([5, 2, 6, 5], [3, 5], 4, 4) == False
    assert candidate([1, 4, 8, 2], [2, 7], 3, 7) == False
    assert candidate([3, 6, 5, 2], [2, 6], 1, 3) == False
    assert candidate([2, 1, 1, 5], [2, 3], 6, 1) == True
    assert candidate([1, 8, 8, 4], [4, 4], 4, 5) == False
    assert candidate([4, 4, 6, 2], [4, 1], 2, 6) == False
    assert candidate([6, 8, 3, 5], [6, 2], 3, 4) == False
    assert candidate([2, 9, 1, 4], [2, 7], 3, 3) == False
    assert candidate([3, 7, 4, 7], [5, 7], 1, 5) == False
    assert candidate([4, 3, 4, 8], [2, 4], 3, 4) == False
    assert candidate([1, 5, 3, 2], [4, 1], 2, 2) == False
    assert candidate([1, 8, 2, 10], [1, 1], 1, 2) == False
    assert candidate([1, 5, 1], [6, 6, 3], 1, 6) == False
    assert candidate([5, 4, 1], [4, 1, 2], 6, 1) == True
    assert candidate([3, 6, 5], [4, 2, 2], 3, 6) == False
    assert candidate([4, 7, 6], [5, 1, 3], 2, 7) == False
    assert candidate([2, 6, 3], [1, 3, 4], 1, 3) == False
    assert candidate([6, 4, 3], [4, 3, 3], 7, 1) == True
    assert candidate([1, 1, 5], [5, 1, 1], 3, 5) == False
    assert candidate([4, 5, 1], [4, 3, 6], 2, 8) == False
    assert candidate([5, 7, 6], [6, 3, 6], 2, 3) == False
    assert candidate([2, 2, 3], [6, 5, 2], 3, 4) == False
    assert candidate([3, 3, 3], [5, 2, 5], 2, 3) == False
    assert candidate([1, 2, 5], [4, 5, 2], 2, 3) == False
    assert candidate([6, 1, 4], [4, 5, 3], 3, 4) == False
    assert candidate([3, 3, 4], [2, 2, 6], 1, 6) == False
    assert candidate([1, 7, 5], [2, 7, 1], 1, 4) == False
    assert candidate([6, 4, 3], [6, 7, 5], 2, 2) == False
    assert candidate([3, 5, 3], [2, 7, 1], 1, 7) == False
    assert candidate([4, 5, 2], [1, 2, 4], 2, 6) == False
    assert candidate([4, 6, 5], [5, 4, 4], 2, 5) == False
    assert candidate([3, 3, 6], [5, 7, 2], 1, 4) == False
    assert candidate([4, 7, 4], [1, 4, 5], 3, 2) == False
    assert candidate([1, 1, 6], [2, 2, 3], 1, 3) == False
    assert candidate([4, 6, 2], [6, 4, 2], 3, 5) == False
    assert candidate([2, 5, 3], [4, 3, 1], 1, 2) == False
    assert candidate([1, 5, 5], [2, 6, 6], 1, 6) == False
    assert candidate([6, 1, 1], [6, 2, 5], 1, 1) == True
    assert candidate([6, 3, 6], [2, 5, 1], 3, 2) == False
    assert candidate([1, 3, 4], [3, 6, 4], 1, 2) == False
    assert candidate([6, 6, 6], [4, 2, 2], 3, 4) == False
    assert candidate([6, 2, 2], [4, 1, 4], 1, 2) == False
    assert candidate([1, 7, 1], [1, 5, 1], 3, 7) == False
    assert candidate([5, 2, 5], [3, 1, 2], 1, 7) == False
    assert candidate([5, 1, 1], [1, 3, 1], 3, 6) == False
    assert candidate([1, 4, 5, 7], [3, 7, 4], 4, 1) == False
    assert candidate([5, 3, 1, 6], [3, 6, 2], 1, 6) == False
    assert candidate([6, 4, 7, 3], [6, 4, 5], 2, 8) == False
    assert candidate([5, 1, 5, 3], [6, 4, 3], 3, 4) == False
    assert candidate([5, 1, 3, 3], [5, 2, 3], 5, 1) == True
    assert candidate([5, 5, 5, 4], [7, 6, 3], 4, 1) == False
    assert candidate([1, 3, 5, 6], [1, 5, 1], 3, 2) == False
    assert candidate([6, 3, 1, 7], [1, 3, 1], 4, 4) == False
    assert candidate([2, 1, 5, 7], [1, 3, 3], 3, 6) == False
    assert candidate([6, 5, 5, 4], [1, 3, 1], 4, 3) == False
    assert candidate([5, 1, 5, 1], [6, 5, 1], 4, 4) == False
    assert candidate([1, 2, 5, 7], [3, 3, 2], 3, 3) == False
    assert candidate([1, 5, 4, 2], [7, 4, 2], 1, 6) == False
    assert candidate([1, 3, 3, 7], [7, 1, 1], 4, 5) == False
    assert candidate([6, 2, 2, 1], [4, 1, 4], 3, 8) == False
    assert candidate([5, 5, 2, 4], [7, 5, 4], 4, 1) == False
    assert candidate([5, 1, 7, 6], [3, 3, 1], 2, 5) == False
    assert candidate([1, 3, 4, 6], [3, 3, 2], 4, 7) == False
    assert candidate([5, 3, 4, 2], [1, 7, 4], 3, 8) == False
    assert candidate([4, 3, 4, 1], [7, 7, 5], 4, 2) == False
    assert candidate([1, 3, 5, 6], [2, 2, 2], 1, 1) == False
    assert candidate([5, 1, 4, 1], [7, 4, 4], 3, 1) == False
    assert candidate([2, 5, 1, 6], [4, 1, 5], 2, 6) == False
    assert candidate([5, 5, 6, 5], [5, 3, 5], 4, 7) == False
    assert candidate([4, 1, 4, 2], [7, 5, 1], 1, 6) == False
    assert candidate([6, 4, 1, 5], [1, 3, 3], 1, 6) == False
    assert candidate([1, 1, 6, 2], [1, 3, 5], 2, 3) == False
    assert candidate([5, 3, 7, 5], [1, 7, 3], 1, 3) == False
    assert candidate([5, 4, 3, 5], [4, 4, 5], 2, 7) == False
    assert candidate([6, 5, 2, 2], [5, 7, 5], 5, 1) == True
    assert candidate([6, 4, 3, 2], [2, 3, 2], 1, 5) == False
    assert candidate([6, 4, 1, 6], [4, 7, 1], 4, 3) == False
    assert candidate([5, 2, 5, 6], [4, 6, 5], 1, 5) == False

if __name__ == '__main__':
    check(is_Sub_Array)