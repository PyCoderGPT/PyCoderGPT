from case_MBPP_276 import issort_list


def check(candidate):
    assert candidate([1,2,4,6,8,10,12,14,16,17])==True
    assert candidate([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False
    assert candidate([1, 2, 4, 6, 8, 10,15,14,20])==False
    assert candidate([3, 4, 5, 6, 5, 5, 17, 13, 13, 20]) == False
    assert candidate([3, 5, 1, 11, 12, 13, 12, 16, 18, 16]) == False
    assert candidate([1, 2, 9, 2, 7, 9, 12, 10, 21, 21]) == False
    assert candidate([1, 7, 1, 10, 8, 11, 10, 11, 15, 18]) == False
    assert candidate([4, 4, 4, 6, 7, 8, 9, 17, 15, 22]) == False
    assert candidate([2, 6, 2, 1, 6, 11, 14, 15, 19, 16]) == False
    assert candidate([5, 5, 9, 3, 7, 9, 7, 19, 18, 16]) == False
    assert candidate([5, 3, 2, 8, 11, 13, 8, 13, 18, 16]) == False
    assert candidate([1, 6, 9, 7, 4, 10, 8, 15, 16, 17]) == False
    assert candidate([4, 6, 8, 6, 12, 7, 14, 10, 20, 16]) == False
    assert candidate([4, 1, 2, 5, 7, 10, 9, 17, 14, 13]) == False
    assert candidate([5, 6, 7, 3, 13, 12, 11, 10, 12, 22]) == False
    assert candidate([5, 3, 4, 7, 4, 10, 11, 11, 15, 13]) == False
    assert candidate([6, 3, 7, 9, 10, 11, 16, 13, 13, 17]) == False
    assert candidate([5, 3, 4, 10, 10, 12, 14, 17, 17, 18]) == False
    assert candidate([3, 3, 2, 3, 5, 13, 8, 13, 17, 15]) == False
    assert candidate([2, 3, 5, 1, 6, 6, 12, 16, 11, 15]) == False
    assert candidate([2, 2, 8, 4, 7, 12, 15, 9, 19, 19]) == False
    assert candidate([1, 4, 6, 10, 12, 10, 8, 12, 19, 19]) == False
    assert candidate([2, 7, 8, 11, 3, 9, 10, 15, 15, 21]) == False
    assert candidate([5, 1, 9, 1, 10, 14, 8, 15, 19, 12]) == False
    assert candidate([5, 4, 6, 8, 11, 14, 16, 11, 19, 15]) == False
    assert candidate([3, 3, 5, 3, 5, 14, 13, 12, 13, 19]) == False
    assert candidate([3, 3, 5, 4, 10, 12, 8, 15, 11, 12]) == False
    assert candidate([4, 1, 9, 8, 13, 13, 10, 15, 17, 22]) == False
    assert candidate([2, 6, 7, 2, 7, 9, 11, 16, 13, 16]) == False
    assert candidate([3, 2, 2, 8, 9, 10, 9, 19, 17, 13]) == False
    assert candidate([4, 3, 8, 6, 11, 7, 8, 10, 11, 16]) == False
    assert candidate([1, 7, 1, 5, 11, 13, 14, 17, 20, 15]) == False
    assert candidate([1, 7, 8, 2, 13, 8, 7, 12, 12, 18]) == False
    assert candidate([5, 2, 5, 2, 11, 13, 11, 18, 17, 15]) == False
    assert candidate([2, 1, 9, 7, 5, 12, 12, 19, 11, 13]) == False
    assert candidate([3, 6, 8, 2, 8, 10, 13, 11, 19, 15]) == False
    assert candidate([1, 2, 2, 10, 10, 14, 13, 18, 20, 13]) == False
    assert candidate([3, 2, 7, 2, 6, 10, 9, 17, 21, 22]) == False
    assert candidate([5, 6, 7, 7, 12, 6, 15, 10, 21, 20]) == False
    assert candidate([3, 3, 3, 2, 11, 15, 14, 16, 23, 22]) == False
    assert candidate([6, 2, 9, 1, 13, 12, 11, 9, 20, 17]) == False
    assert candidate([1, 7, 1, 7, 13, 12, 16, 12, 22, 22]) == False
    assert candidate([1, 4, 2, 7, 5, 8, 12, 11, 24, 21]) == False
    assert candidate([6, 4, 1, 11, 3, 9, 9, 17, 23, 19]) == False
    assert candidate([4, 7, 4, 2, 12, 7, 9, 13, 15, 12]) == False
    assert candidate([6, 1, 1, 7, 3, 12, 12, 10, 18, 19]) == False
    assert candidate([4, 4, 5, 11, 9, 10, 9, 17, 15, 15]) == False
    assert candidate([6, 6, 7, 1, 9, 14, 14, 17, 15, 21]) == False
    assert candidate([4, 5, 6, 3, 6, 7, 14, 12, 17, 15]) == False
    assert candidate([5, 6, 8, 4, 10, 8, 9, 10, 22, 18]) == False
    assert candidate([2, 6, 2, 10, 3, 13, 15, 10, 17, 12]) == False
    assert candidate([2, 1, 2, 1, 10, 14, 10, 12, 19, 17]) == False
    assert candidate([1, 4, 9, 3, 8, 14, 10, 9, 18, 15]) == False
    assert candidate([2, 2, 4, 5, 13, 12, 7, 15, 25, 15]) == False
    assert candidate([1, 2, 7, 9, 3, 15, 13, 11, 17, 18]) == False
    assert candidate([2, 4, 7, 1, 11, 5, 14, 9, 22, 21]) == False
    assert candidate([4, 6, 9, 10, 11, 11, 12, 12, 20, 21]) == True
    assert candidate([1, 4, 6, 11, 12, 7, 11, 15, 15, 21]) == False
    assert candidate([2, 1, 8, 9, 10, 5, 16, 12, 20, 17]) == False
    assert candidate([4, 3, 3, 10, 12, 14, 9, 17, 17, 21]) == False
    assert candidate([2, 6, 1, 10, 3, 11, 16, 18, 20, 21]) == False
    assert candidate([3, 4, 9, 1, 4, 12, 17, 19, 25, 12]) == False
    assert candidate([5, 7, 7, 6, 3, 11, 16, 17, 21, 12]) == False
    assert candidate([2, 4, 9, 4, 4, 11, 7, 19, 24, 15]) == False
    assert candidate([2, 6, 3, 10, 6, 11, 15, 9, 19, 19]) == False
    assert candidate([3, 5, 1, 11, 4, 15, 8, 15, 17, 19]) == False
    assert candidate([1, 7, 4, 7, 13, 5, 13, 11, 23, 19]) == False
    assert candidate([5, 7, 8, 4, 11, 15, 17, 12, 20, 19]) == False
    assert candidate([3, 1, 3, 2, 7, 12, 9, 17, 19, 20]) == False
    assert candidate([3, 4, 2, 7, 11, 15, 20, 16, 16]) == False
    assert candidate([5, 4, 2, 10, 3, 15, 14, 11, 21]) == False
    assert candidate([6, 7, 2, 3, 7, 6, 13, 9, 25]) == False
    assert candidate([5, 1, 3, 4, 11, 9, 12, 13, 23]) == False
    assert candidate([4, 1, 5, 4, 7, 6, 11, 14, 16]) == False
    assert candidate([3, 5, 4, 1, 10, 7, 18, 16, 22]) == False
    assert candidate([3, 7, 9, 9, 4, 14, 19, 13, 19]) == False
    assert candidate([5, 4, 5, 7, 13, 11, 10, 9, 23]) == False
    assert candidate([6, 1, 8, 4, 13, 12, 19, 13, 19]) == False
    assert candidate([6, 3, 9, 9, 9, 12, 15, 13, 23]) == False
    assert candidate([5, 4, 4, 6, 7, 10, 11, 14, 23]) == False
    assert candidate([4, 6, 6, 6, 3, 7, 18, 17, 23]) == False
    assert candidate([6, 7, 1, 2, 9, 8, 20, 16, 16]) == False
    assert candidate([2, 6, 9, 1, 4, 13, 17, 18, 21]) == False
    assert candidate([6, 4, 8, 4, 6, 7, 16, 9, 17]) == False
    assert candidate([1, 6, 2, 5, 8, 5, 13, 17, 25]) == False
    assert candidate([5, 3, 8, 5, 7, 11, 15, 11, 22]) == False
    assert candidate([5, 3, 5, 10, 8, 11, 17, 11, 24]) == False
    assert candidate([2, 5, 4, 7, 3, 7, 15, 19, 25]) == False
    assert candidate([5, 4, 9, 5, 8, 15, 16, 19, 15]) == False
    assert candidate([4, 5, 8, 6, 6, 7, 20, 11, 16]) == False
    assert candidate([6, 6, 9, 1, 12, 5, 11, 18, 19]) == False
    assert candidate([4, 4, 5, 4, 3, 14, 13, 14, 19]) == False
    assert candidate([2, 1, 6, 3, 4, 10, 11, 15, 23]) == False
    assert candidate([4, 4, 7, 4, 12, 14, 10, 12, 20]) == False
    assert candidate([4, 2, 1, 8, 11, 6, 11, 9, 25]) == False
    assert candidate([2, 1, 3, 1, 9, 7, 15, 18, 17]) == False
    assert candidate([4, 6, 9, 4, 4, 14, 11, 19, 19]) == False
    assert candidate([5, 5, 6, 6, 6, 15, 10, 11, 23]) == False
    assert candidate([3, 2, 8, 2, 13, 10, 11, 15, 18]) == False
    assert candidate([4, 3, 6, 10, 4, 7, 12, 17, 21]) == False
    assert candidate([5, 1, 8, 2, 4, 14, 12, 16, 16]) == False
    assert candidate([5, 2, 5, 1, 10, 7, 20, 11, 15]) == False

if __name__ == '__main__':
    check(issort_list)