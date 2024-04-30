from case_MBPP_314 import remove_kth_element


def check(candidate):
    assert candidate([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
    assert candidate([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4],4)==[0, 0, 1, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    assert candidate([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10],5)==[10,10,15,19, 18, 17, 26, 26, 17, 18, 10]
    assert candidate([1, 2, 5, 2, 5, 3, 4, 2], 4) == [1, 2, 5, 5, 3, 4, 2]
    assert candidate([2, 1, 3, 8, 3, 9, 8, 1], 6) == [2, 1, 3, 8, 3, 8, 1]
    assert candidate([2, 6, 4, 7, 3, 4, 9, 1], 7) == [2, 6, 4, 7, 3, 4, 1]
    assert candidate([2, 1, 7, 7, 4, 4, 1, 3], 2) == [2, 7, 7, 4, 4, 1, 3]
    assert candidate([5, 1, 3, 4, 4, 8, 3, 2], 8) == [5, 1, 3, 4, 4, 8, 3]
    assert candidate([4, 5, 2, 2, 5, 8, 7, 2], 1) == [5, 2, 2, 5, 8, 7, 2]
    assert candidate([6, 2, 4, 2, 5, 8, 10, 5], 2) == [6, 4, 2, 5, 8, 10, 5]
    assert candidate([3, 5, 2, 2, 6, 3, 5, 1], 8) == [3, 5, 2, 2, 6, 3, 5]
    assert candidate([4, 2, 3, 6, 2, 4, 7, 3], 5) == [4, 2, 3, 6, 4, 7, 3]
    assert candidate([6, 4, 5, 8, 5, 8, 1, 2], 5) == [6, 4, 5, 8, 8, 1, 2]
    assert candidate([1, 1, 6, 2, 7, 1, 1, 2], 2) == [1, 6, 2, 7, 1, 1, 2]
    assert candidate([4, 2, 4, 4, 3, 7, 2, 6], 8) == [4, 2, 4, 4, 3, 7, 2]
    assert candidate([1, 2, 1, 4, 6, 3, 2, 1], 8) == [1, 2, 1, 4, 6, 3, 2]
    assert candidate([6, 5, 3, 1, 7, 9, 5, 3], 3) == [6, 5, 1, 7, 9, 5, 3]
    assert candidate([2, 4, 1, 2, 3, 6, 8, 3], 8) == [2, 4, 1, 2, 3, 6, 8]
    assert candidate([6, 4, 7, 6, 5, 9, 1, 6], 8) == [6, 4, 7, 6, 5, 9, 1]
    assert candidate([5, 1, 5, 6, 7, 9, 9, 6], 1) == [1, 5, 6, 7, 9, 9, 6]
    assert candidate([1, 6, 2, 3, 7, 2, 5, 1], 8) == [1, 6, 2, 3, 7, 2, 5]
    assert candidate([4, 3, 7, 2, 8, 5, 9, 4], 1) == [3, 7, 2, 8, 5, 9, 4]
    assert candidate([1, 3, 5, 8, 4, 9, 9, 6], 8) == [1, 3, 5, 8, 4, 9, 9]
    assert candidate([2, 4, 4, 8, 8, 3, 2, 3], 7) == [2, 4, 4, 8, 8, 3, 3]
    assert candidate([3, 6, 5, 6, 2, 5, 2, 6], 3) == [3, 6, 6, 2, 5, 2, 6]
    assert candidate([2, 5, 5, 3, 1, 1, 10, 3], 1) == [5, 5, 3, 1, 1, 10, 3]
    assert candidate([1, 4, 4, 8, 1, 2, 9, 5], 5) == [1, 4, 4, 8, 2, 9, 5]
    assert candidate([6, 5, 5, 7, 3, 1, 1, 3], 3) == [6, 5, 7, 3, 1, 1, 3]
    assert candidate([5, 3, 5, 4, 8, 7, 10, 4], 6) == [5, 3, 5, 4, 8, 10, 4]
    assert candidate([6, 3, 7, 5, 5, 1, 4, 3], 5) == [6, 3, 7, 5, 1, 4, 3]
    assert candidate([5, 1, 6, 1, 8, 7, 8, 4], 8) == [5, 1, 6, 1, 8, 7, 8]
    assert candidate([5, 6, 7, 5, 6, 4, 5, 1], 4) == [5, 6, 7, 6, 4, 5, 1]
    assert candidate([1, 2, 3, 2, 3, 1, 8, 1], 1) == [2, 3, 2, 3, 1, 8, 1]
    assert candidate([4, 3, 4, 1, 2, 3, 5, 4], 8) == [4, 3, 4, 1, 2, 3, 5]
    assert candidate([3, 2, 7, 6, 6, 1, 5, 1], 8) == [3, 2, 7, 6, 6, 1, 5]
    assert candidate([5, 4, 2, 7, 4, 5, 6, 4], 7) == [5, 4, 2, 7, 4, 5, 4]
    assert candidate([2, 5, 5, 3, 5, 6, 9, 1, 4, 7, 2, 7, 9, 6, 5, 2], 8) == [2, 5, 5, 3, 5, 6, 9, 4, 7, 2, 7, 9, 6, 5, 2]
    assert candidate([5, 3, 6, 7, 2, 9, 6, 5, 4, 6, 2, 6, 7, 13, 9, 6], 3) == [5, 3, 7, 2, 9, 6, 5, 4, 6, 2, 6, 7, 13, 9, 6]
    assert candidate([5, 4, 3, 2, 2, 1, 5, 3, 8, 7, 8, 8, 4, 5, 1, 8], 2) == [5, 3, 2, 2, 1, 5, 3, 8, 7, 8, 8, 4, 5, 1, 8]
    assert candidate([5, 5, 6, 2, 1, 8, 6, 6, 9, 6, 4, 4, 3, 7, 6, 4], 5) == [5, 5, 6, 2, 8, 6, 6, 9, 6, 4, 4, 3, 7, 6, 4]
    assert candidate([1, 3, 5, 4, 6, 2, 6, 9, 5, 7, 1, 9, 3, 5, 4, 6], 8) == [1, 3, 5, 4, 6, 2, 6, 5, 7, 1, 9, 3, 5, 4, 6]
    assert candidate([2, 5, 4, 5, 8, 1, 5, 2, 7, 4, 8, 3, 11, 7, 8, 6], 8) == [2, 5, 4, 5, 8, 1, 5, 7, 4, 8, 3, 11, 7, 8, 6]
    assert candidate([4, 2, 2, 4, 3, 2, 8, 9, 1, 9, 9, 6, 10, 13, 1, 4], 9) == [4, 2, 2, 4, 3, 2, 8, 9, 9, 9, 6, 10, 13, 1, 4]
    assert candidate([3, 5, 6, 4, 6, 5, 3, 7, 6, 1, 6, 8, 3, 7, 8, 8], 6) == [3, 5, 6, 4, 6, 3, 7, 6, 1, 6, 8, 3, 7, 8, 8]
    assert candidate([3, 2, 5, 2, 2, 5, 5, 6, 4, 4, 2, 8, 3, 11, 6, 1], 8) == [3, 2, 5, 2, 2, 5, 5, 4, 4, 2, 8, 3, 11, 6, 1]
    assert candidate([4, 2, 2, 1, 5, 5, 6, 9, 8, 2, 7, 10, 12, 6, 7, 8], 1) == [2, 2, 1, 5, 5, 6, 9, 8, 2, 7, 10, 12, 6, 7, 8]
    assert candidate([1, 3, 5, 7, 7, 7, 2, 5, 11, 7, 8, 10, 8, 9, 6, 2], 1) == [3, 5, 7, 7, 7, 2, 5, 11, 7, 8, 10, 8, 9, 6, 2]
    assert candidate([5, 4, 2, 1, 4, 9, 1, 3, 5, 11, 1, 10, 10, 6, 1, 1], 6) == [5, 4, 2, 1, 4, 1, 3, 5, 11, 1, 10, 10, 6, 1, 1]
    assert candidate([4, 5, 5, 4, 1, 8, 3, 1, 9, 2, 7, 9, 9, 7, 3, 1], 5) == [4, 5, 5, 4, 8, 3, 1, 9, 2, 7, 9, 9, 7, 3, 1]
    assert candidate([4, 2, 2, 1, 6, 7, 3, 8, 1, 7, 7, 10, 10, 12, 5, 9], 5) == [4, 2, 2, 1, 7, 3, 8, 1, 7, 7, 10, 10, 12, 5, 9]
    assert candidate([2, 3, 3, 3, 6, 3, 2, 10, 9, 9, 8, 5, 7, 5, 7, 4], 7) == [2, 3, 3, 3, 6, 3, 10, 9, 9, 8, 5, 7, 5, 7, 4]
    assert candidate([2, 4, 3, 3, 7, 7, 3, 5, 5, 6, 10, 12, 8, 4, 9, 8], 9) == [2, 4, 3, 3, 7, 7, 3, 5, 6, 10, 12, 8, 4, 9, 8]
    assert candidate([2, 4, 1, 7, 7, 1, 3, 10, 8, 6, 1, 5, 9, 5, 7, 1], 8) == [2, 4, 1, 7, 7, 1, 3, 8, 6, 1, 5, 9, 5, 7, 1]
    assert candidate([5, 4, 2, 5, 7, 4, 2, 4, 3, 9, 1, 8, 13, 13, 4, 4], 6) == [5, 4, 2, 5, 7, 2, 4, 3, 9, 1, 8, 13, 13, 4, 4]
    assert candidate([3, 2, 1, 5, 3, 7, 2, 2, 2, 1, 3, 11, 8, 12, 4, 9], 5) == [3, 2, 1, 5, 7, 2, 2, 2, 1, 3, 11, 8, 12, 4, 9]
    assert candidate([1, 1, 3, 7, 4, 6, 4, 3, 7, 7, 3, 7, 7, 13, 4, 3], 5) == [1, 1, 3, 7, 6, 4, 3, 7, 7, 3, 7, 7, 13, 4, 3]
    assert candidate([1, 1, 1, 3, 7, 1, 6, 9, 8, 3, 8, 9, 7, 6, 4, 4], 7) == [1, 1, 1, 3, 7, 1, 9, 8, 3, 8, 9, 7, 6, 4, 4]
    assert candidate([3, 2, 1, 5, 1, 4, 8, 5, 9, 10, 6, 2, 3, 6, 1, 3], 1) == [2, 1, 5, 1, 4, 8, 5, 9, 10, 6, 2, 3, 6, 1, 3]
    assert candidate([1, 5, 2, 6, 2, 1, 5, 6, 10, 10, 5, 10, 10, 14, 4, 7], 1) == [5, 2, 6, 2, 1, 5, 6, 10, 10, 5, 10, 10, 14, 4, 7]
    assert candidate([2, 2, 3, 5, 5, 3, 1, 1, 3, 11, 7, 3, 4, 10, 9, 9], 3) == [2, 2, 5, 5, 3, 1, 1, 3, 11, 7, 3, 4, 10, 9, 9]
    assert candidate([1, 2, 2, 4, 2, 6, 3, 5, 11, 6, 3, 6, 13, 14, 8, 6], 1) == [2, 2, 4, 2, 6, 3, 5, 11, 6, 3, 6, 13, 14, 8, 6]
    assert candidate([4, 5, 5, 2, 1, 6, 9, 7, 11, 4, 2, 11, 3, 9, 8, 5], 6) == [4, 5, 5, 2, 1, 9, 7, 11, 4, 2, 11, 3, 9, 8, 5]
    assert candidate([5, 4, 3, 1, 8, 7, 3, 4, 2, 9, 2, 12, 7, 10, 9, 9], 7) == [5, 4, 3, 1, 8, 7, 4, 2, 9, 2, 12, 7, 10, 9, 9]
    assert candidate([3, 3, 3, 5, 3, 4, 7, 6, 11, 2, 8, 3, 13, 10, 3, 7], 6) == [3, 3, 3, 5, 3, 7, 6, 11, 2, 8, 3, 13, 10, 3, 7]
    assert candidate([1, 4, 3, 7, 1, 2, 1, 3, 3, 6, 7, 8, 3, 4, 3, 4], 8) == [1, 4, 3, 7, 1, 2, 1, 3, 6, 7, 8, 3, 4, 3, 4]
    assert candidate([5, 4, 3, 2, 6, 5, 6, 10, 11, 6, 6, 9, 5, 12, 2, 9], 2) == [5, 3, 2, 6, 5, 6, 10, 11, 6, 6, 9, 5, 12, 2, 9]
    assert candidate([2, 2, 3, 7, 3, 4, 5, 5, 4, 10, 2, 5, 5, 9, 5, 7], 7) == [2, 2, 3, 7, 3, 4, 5, 4, 10, 2, 5, 5, 9, 5, 7]
    assert candidate([4, 4, 3, 5, 8, 7, 2, 1, 10, 6, 5, 12, 6, 11, 6, 7], 1) == [4, 3, 5, 8, 7, 2, 1, 10, 6, 5, 12, 6, 11, 6, 7]
    assert candidate([4, 5, 4, 7, 8, 2, 2, 1, 11, 3, 5, 10, 12, 7, 5, 7], 2) == [4, 4, 7, 8, 2, 2, 1, 11, 3, 5, 10, 12, 7, 5, 7]
    assert candidate([15, 10, 12, 14, 18, 19, 17, 28, 27, 14, 22, 9], 9) == [15, 10, 12, 14, 18, 19, 17, 28, 14, 22, 9]
    assert candidate([10, 15, 14, 21, 16, 13, 19, 25, 30, 15, 15, 12], 8) == [10, 15, 14, 21, 16, 13, 19, 30, 15, 15, 12]
    assert candidate([11, 9, 18, 14, 15, 21, 20, 22, 23, 19, 21, 15], 1) == [9, 18, 14, 15, 21, 20, 22, 23, 19, 21, 15]
    assert candidate([5, 8, 18, 23, 20, 16, 14, 30, 31, 12, 19, 12], 10) == [5, 8, 18, 23, 20, 16, 14, 30, 31, 19, 12]
    assert candidate([11, 9, 15, 22, 19, 22, 12, 29, 22, 20, 23, 7], 4) == [11, 9, 15, 19, 22, 12, 29, 22, 20, 23, 7]
    assert candidate([12, 7, 12, 16, 21, 15, 21, 31, 26, 13, 15, 6], 8) == [12, 7, 12, 16, 21, 15, 21, 26, 13, 15, 6]
    assert candidate([13, 12, 19, 19, 15, 20, 21, 26, 21, 16, 20, 12], 7) == [13, 12, 19, 19, 15, 20, 26, 21, 16, 20, 12]
    assert candidate([8, 14, 11, 15, 13, 18, 15, 25, 24, 15, 17, 10], 7) == [8, 14, 11, 15, 13, 18, 25, 24, 15, 17, 10]
    assert candidate([7, 8, 10, 24, 20, 19, 18, 23, 28, 17, 14, 14], 3) == [7, 8, 24, 20, 19, 18, 23, 28, 17, 14, 14]
    assert candidate([7, 9, 19, 14, 19, 15, 12, 24, 23, 13, 22, 11], 4) == [7, 9, 19, 19, 15, 12, 24, 23, 13, 22, 11]
    assert candidate([15, 13, 20, 19, 21, 15, 18, 27, 23, 22, 15, 9], 9) == [15, 13, 20, 19, 21, 15, 18, 27, 22, 15, 9]
    assert candidate([5, 5, 16, 23, 17, 21, 17, 27, 24, 12, 22, 7], 6) == [5, 5, 16, 23, 17, 17, 27, 24, 12, 22, 7]
    assert candidate([13, 13, 15, 23, 23, 23, 12, 31, 29, 12, 23, 5], 7) == [13, 13, 15, 23, 23, 23, 31, 29, 12, 23, 5]
    assert candidate([10, 5, 16, 19, 21, 16, 14, 30, 23, 18, 20, 14], 10) == [10, 5, 16, 19, 21, 16, 14, 30, 23, 20, 14]
    assert candidate([9, 11, 16, 22, 18, 22, 18, 25, 26, 18, 18, 7], 3) == [9, 11, 22, 18, 22, 18, 25, 26, 18, 18, 7]
    assert candidate([14, 15, 11, 24, 14, 15, 12, 30, 28, 17, 15, 13], 4) == [14, 15, 11, 14, 15, 12, 30, 28, 17, 15, 13]
    assert candidate([11, 12, 13, 19, 22, 18, 21, 26, 22, 19, 23, 15], 1) == [12, 13, 19, 22, 18, 21, 26, 22, 19, 23, 15]
    assert candidate([5, 8, 14, 23, 21, 14, 13, 21, 29, 12, 14, 15], 10) == [5, 8, 14, 23, 21, 14, 13, 21, 29, 14, 15]
    assert candidate([10, 7, 11, 16, 13, 23, 20, 21, 28, 18, 16, 6], 3) == [10, 7, 16, 13, 23, 20, 21, 28, 18, 16, 6]
    assert candidate([5, 11, 17, 15, 23, 23, 14, 24, 24, 12, 16, 13], 3) == [5, 11, 15, 23, 23, 14, 24, 24, 12, 16, 13]
    assert candidate([6, 14, 15, 17, 19, 23, 22, 24, 21, 20, 23, 10], 8) == [6, 14, 15, 17, 19, 23, 22, 21, 20, 23, 10]
    assert candidate([13, 12, 15, 15, 20, 17, 22, 30, 31, 22, 16, 13], 9) == [13, 12, 15, 15, 20, 17, 22, 30, 22, 16, 13]
    assert candidate([15, 9, 15, 22, 18, 21, 19, 30, 24, 14, 13, 14], 5) == [15, 9, 15, 22, 21, 19, 30, 24, 14, 13, 14]
    assert candidate([7, 15, 11, 18, 14, 19, 22, 21, 30, 19, 20, 8], 2) == [7, 11, 18, 14, 19, 22, 21, 30, 19, 20, 8]
    assert candidate([10, 8, 10, 16, 17, 17, 15, 21, 25, 19, 22, 13], 7) == [10, 8, 10, 16, 17, 17, 21, 25, 19, 22, 13]
    assert candidate([9, 7, 13, 22, 19, 13, 14, 22, 25, 19, 15, 12], 5) == [9, 7, 13, 22, 13, 14, 22, 25, 19, 15, 12]
    assert candidate([8, 14, 13, 19, 22, 19, 17, 28, 23, 16, 22, 14], 6) == [8, 14, 13, 19, 22, 17, 28, 23, 16, 22, 14]
    assert candidate([11, 12, 10, 21, 17, 18, 13, 22, 25, 17, 13, 14], 7) == [11, 12, 10, 21, 17, 18, 22, 25, 17, 13, 14]
    assert candidate([6, 14, 20, 20, 16, 14, 17, 29, 27, 20, 16, 8], 2) == [6, 20, 20, 16, 14, 17, 29, 27, 20, 16, 8]
    assert candidate([10, 6, 15, 18, 20, 16, 13, 30, 27, 20, 18, 10], 7) == [10, 6, 15, 18, 20, 16, 30, 27, 20, 18, 10]
    assert candidate([7, 14, 12, 19, 22, 23, 17, 27, 30, 21, 18, 11], 7) == [7, 14, 12, 19, 22, 23, 27, 30, 21, 18, 11]
    assert candidate([14, 5, 17, 23, 13, 19, 16, 27, 26, 19, 23, 15], 4) == [14, 5, 17, 13, 19, 16, 27, 26, 19, 23, 15]
    assert candidate([10, 10, 11, 15, 22, 20, 12, 26, 23, 13, 14, 8], 7) == [10, 10, 11, 15, 22, 20, 26, 23, 13, 14, 8]

if __name__ == '__main__':
    check(remove_kth_element)