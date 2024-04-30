from case_MBPP_421 import is_Product_Even


def check(candidate):
    assert candidate([1,2,3],3) == True
    assert candidate([1,2,1,4],4) == True
    assert candidate([1,1],2) == False
    assert candidate([2, 7, 4], 5) == True
    assert candidate([6, 4, 1], 4) == True
    assert candidate([1, 4, 4], 7) == True
    assert candidate([1, 7, 3], 3) == False
    assert candidate([6, 4, 1], 2) == True
    assert candidate([4, 7, 5], 5) == True
    assert candidate([5, 5, 1], 2) == False
    assert candidate([1, 7, 2], 1) == False
    assert candidate([2, 5, 1], 8) == True
    assert candidate([3, 5, 6], 8) == True
    assert candidate([4, 4, 6], 7) == True
    assert candidate([1, 7, 6], 1) == False
    assert candidate([5, 7, 4], 2) == False
    assert candidate([5, 3, 7], 2) == False
    assert candidate([6, 4, 2], 4) == True
    assert candidate([6, 1, 1], 7) == True
    assert candidate([2, 6, 8], 3) == True
    assert candidate([5, 4, 6], 3) == True
    assert candidate([2, 5, 1], 8) == True
    assert candidate([4, 6, 6], 5) == True
    assert candidate([4, 2, 1], 6) == True
    assert candidate([4, 4, 3], 5) == True
    assert candidate([4, 3, 3], 6) == True
    assert candidate([4, 7, 4], 1) == True
    assert candidate([4, 5, 1], 4) == True
    assert candidate([4, 4, 4], 8) == True
    assert candidate([4, 4, 6], 1) == True
    assert candidate([3, 2, 3], 3) == True
    assert candidate([6, 1, 6], 5) == True
    assert candidate([2, 1, 7], 2) == True
    assert candidate([4, 5, 6], 7) == True
    assert candidate([1, 1, 2], 7) == True
    assert candidate([2, 3, 6], 7) == True
    assert candidate([4, 6, 6, 9], 3) == True
    assert candidate([2, 2, 1, 1], 3) == True
    assert candidate([6, 3, 4, 3], 9) == True
    assert candidate([6, 3, 6, 7], 6) == True
    assert candidate([5, 7, 5, 5], 3) == False
    assert candidate([6, 1, 1, 5], 1) == True
    assert candidate([5, 1, 4, 5], 5) == True
    assert candidate([2, 6, 4, 1], 9) == True
    assert candidate([6, 3, 2, 2], 6) == True
    assert candidate([4, 6, 2, 3], 1) == True
    assert candidate([5, 6, 3, 4], 6) == True
    assert candidate([2, 3, 4, 7], 1) == True
    assert candidate([5, 5, 6, 4], 2) == False
    assert candidate([5, 3, 2, 7], 1) == False
    assert candidate([4, 1, 5, 3], 7) == True
    assert candidate([4, 2, 1, 9], 7) == True
    assert candidate([1, 3, 3, 5], 3) == False
    assert candidate([6, 6, 5, 3], 2) == True
    assert candidate([4, 1, 5, 4], 5) == True
    assert candidate([1, 6, 4, 5], 6) == True
    assert candidate([2, 5, 2, 5], 1) == True
    assert candidate([2, 4, 5, 6], 4) == True
    assert candidate([1, 6, 4, 6], 3) == True
    assert candidate([3, 4, 2, 4], 2) == True
    assert candidate([6, 6, 2, 7], 3) == True
    assert candidate([6, 1, 2, 3], 9) == True
    assert candidate([5, 3, 4, 5], 9) == True
    assert candidate([4, 1, 1, 8], 6) == True
    assert candidate([3, 4, 4, 6], 6) == True
    assert candidate([3, 5, 3, 4], 2) == False
    assert candidate([6, 3, 1, 3], 9) == True
    assert candidate([6, 4, 6, 3], 4) == True
    assert candidate([6, 2, 5, 1], 4) == True
    assert candidate([3, 4], 1) == False
    assert candidate([1, 2], 5) == True
    assert candidate([3, 5], 1) == False
    assert candidate([6, 2], 6) == True
    assert candidate([4, 6], 2) == True
    assert candidate([5, 4], 2) == True
    assert candidate([6, 6], 5) == True
    assert candidate([3, 4], 7) == True
    assert candidate([5, 3], 2) == False
    assert candidate([1, 4], 6) == True
    assert candidate([3, 2], 3) == True
    assert candidate([6, 6], 7) == True
    assert candidate([4, 4], 6) == True
    assert candidate([3, 4], 7) == True
    assert candidate([1, 6], 4) == True
    assert candidate([2, 2], 6) == True
    assert candidate([5, 6], 5) == True
    assert candidate([3, 2], 5) == True
    assert candidate([5, 6], 1) == False
    assert candidate([2, 1], 7) == True
    assert candidate([2, 1], 1) == True
    assert candidate([6, 4], 5) == True
    assert candidate([3, 2], 1) == False
    assert candidate([4, 3], 7) == True
    assert candidate([3, 2], 4) == True
    assert candidate([5, 4], 2) == True
    assert candidate([5, 5], 2) == False
    assert candidate([5, 2], 2) == True
    assert candidate([5, 2], 6) == True
    assert candidate([6, 2], 6) == True
    assert candidate([4, 3], 7) == True
    assert candidate([2, 4], 4) == True
    assert candidate([5, 2], 6) == True

if __name__ == '__main__':
    check(is_Product_Even)