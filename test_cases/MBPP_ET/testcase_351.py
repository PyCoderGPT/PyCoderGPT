from case_MBPP_351 import sum_list


def check(candidate):
    assert candidate([10,20,30],[15,25,35])==[25,45,65]
    assert candidate([1,2,3],[5,6,7])==[6,8,10]
    assert candidate([15,20,30],[15,45,75])==[30,65,105]
    assert candidate([11, 19, 31], [20, 29, 39]) == [31, 48, 70]
    assert candidate([15, 19, 31], [18, 26, 30]) == [33, 45, 61]
    assert candidate([11, 23, 29], [15, 20, 40]) == [26, 43, 69]
    assert candidate([11, 25, 35], [13, 27, 32]) == [24, 52, 67]
    assert candidate([6, 20, 25], [11, 29, 36]) == [17, 49, 61]
    assert candidate([10, 18, 26], [11, 27, 30]) == [21, 45, 56]
    assert candidate([6, 16, 31], [19, 21, 36]) == [25, 37, 67]
    assert candidate([8, 17, 30], [17, 30, 40]) == [25, 47, 70]
    assert candidate([12, 22, 26], [17, 27, 32]) == [29, 49, 58]
    assert candidate([12, 20, 34], [14, 22, 37]) == [26, 42, 71]
    assert candidate([8, 21, 26], [15, 23, 36]) == [23, 44, 62]
    assert candidate([5, 19, 27], [13, 22, 39]) == [18, 41, 66]
    assert candidate([6, 15, 25], [15, 28, 32]) == [21, 43, 57]
    assert candidate([8, 22, 27], [11, 28, 35]) == [19, 50, 62]
    assert candidate([5, 25, 33], [13, 30, 38]) == [18, 55, 71]
    assert candidate([12, 18, 34], [17, 23, 36]) == [29, 41, 70]
    assert candidate([5, 20, 30], [20, 28, 39]) == [25, 48, 69]
    assert candidate([12, 21, 30], [15, 22, 36]) == [27, 43, 66]
    assert candidate([14, 15, 27], [18, 25, 36]) == [32, 40, 63]
    assert candidate([7, 15, 33], [16, 30, 35]) == [23, 45, 68]
    assert candidate([7, 22, 33], [12, 27, 30]) == [19, 49, 63]
    assert candidate([13, 25, 35], [18, 21, 35]) == [31, 46, 70]
    assert candidate([9, 23, 35], [11, 28, 35]) == [20, 51, 70]
    assert candidate([14, 24, 27], [11, 26, 37]) == [25, 50, 64]
    assert candidate([9, 24, 34], [20, 23, 35]) == [29, 47, 69]
    assert candidate([11, 24, 33], [14, 29, 31]) == [25, 53, 64]
    assert candidate([13, 24, 28], [10, 25, 34]) == [23, 49, 62]
    assert candidate([15, 21, 28], [10, 20, 30]) == [25, 41, 58]
    assert candidate([9, 17, 28], [17, 22, 32]) == [26, 39, 60]
    assert candidate([7, 25, 28], [13, 29, 31]) == [20, 54, 59]
    assert candidate([6, 25, 26], [12, 26, 34]) == [18, 51, 60]
    assert candidate([9, 21, 34], [10, 26, 40]) == [19, 47, 74]
    assert candidate([13, 18, 25], [12, 26, 39]) == [25, 44, 64]
    assert candidate([2, 1, 2], [10, 8, 6]) == [12, 9, 8]
    assert candidate([1, 7, 5], [1, 9, 2]) == [2, 16, 7]
    assert candidate([1, 2, 6], [4, 11, 2]) == [5, 13, 8]
    assert candidate([4, 6, 4], [1, 6, 6]) == [5, 12, 10]
    assert candidate([6, 3, 2], [3, 8, 7]) == [9, 11, 9]
    assert candidate([5, 3, 2], [10, 4, 7]) == [15, 7, 9]
    assert candidate([2, 5, 5], [7, 10, 3]) == [9, 15, 8]
    assert candidate([6, 7, 4], [9, 5, 8]) == [15, 12, 12]
    assert candidate([4, 3, 1], [8, 11, 7]) == [12, 14, 8]
    assert candidate([1, 7, 8], [1, 10, 4]) == [2, 17, 12]
    assert candidate([5, 2, 1], [2, 9, 9]) == [7, 11, 10]
    assert candidate([1, 5, 2], [2, 4, 9]) == [3, 9, 11]
    assert candidate([1, 4, 2], [8, 5, 7]) == [9, 9, 9]
    assert candidate([4, 4, 1], [4, 5, 5]) == [8, 9, 6]
    assert candidate([6, 2, 4], [5, 10, 12]) == [11, 12, 16]
    assert candidate([3, 2, 6], [7, 1, 4]) == [10, 3, 10]
    assert candidate([2, 7, 3], [9, 5, 2]) == [11, 12, 5]
    assert candidate([2, 3, 4], [9, 6, 12]) == [11, 9, 16]
    assert candidate([2, 6, 6], [1, 3, 10]) == [3, 9, 16]
    assert candidate([4, 7, 7], [6, 7, 8]) == [10, 14, 15]
    assert candidate([1, 3, 7], [10, 8, 6]) == [11, 11, 13]
    assert candidate([1, 3, 6], [3, 1, 6]) == [4, 4, 12]
    assert candidate([2, 7, 1], [9, 4, 4]) == [11, 11, 5]
    assert candidate([4, 2, 1], [8, 2, 5]) == [12, 4, 6]
    assert candidate([6, 2, 5], [3, 4, 10]) == [9, 6, 15]
    assert candidate([5, 3, 2], [5, 1, 4]) == [10, 4, 6]
    assert candidate([4, 5, 5], [9, 10, 8]) == [13, 15, 13]
    assert candidate([3, 4, 3], [3, 5, 11]) == [6, 9, 14]
    assert candidate([1, 5, 2], [5, 1, 11]) == [6, 6, 13]
    assert candidate([2, 3, 8], [3, 7, 3]) == [5, 10, 11]
    assert candidate([3, 5, 7], [5, 8, 8]) == [8, 13, 15]
    assert candidate([4, 3, 6], [8, 11, 11]) == [12, 14, 17]
    assert candidate([3, 7, 8], [6, 9, 2]) == [9, 16, 10]
    assert candidate([14, 18, 32], [14, 49, 80]) == [28, 67, 112]
    assert candidate([15, 21, 33], [13, 47, 78]) == [28, 68, 111]
    assert candidate([14, 15, 27], [17, 49, 79]) == [31, 64, 106]
    assert candidate([10, 20, 33], [19, 41, 75]) == [29, 61, 108]
    assert candidate([19, 21, 32], [11, 48, 80]) == [30, 69, 112]
    assert candidate([18, 18, 28], [10, 50, 76]) == [28, 68, 104]
    assert candidate([19, 17, 25], [19, 44, 79]) == [38, 61, 104]
    assert candidate([16, 21, 26], [15, 44, 72]) == [31, 65, 98]
    assert candidate([11, 19, 32], [10, 44, 77]) == [21, 63, 109]
    assert candidate([20, 21, 34], [14, 50, 74]) == [34, 71, 108]
    assert candidate([18, 23, 34], [10, 41, 72]) == [28, 64, 106]
    assert candidate([17, 23, 28], [20, 49, 71]) == [37, 72, 99]
    assert candidate([16, 17, 33], [12, 41, 74]) == [28, 58, 107]
    assert candidate([13, 16, 29], [19, 40, 70]) == [32, 56, 99]
    assert candidate([19, 18, 29], [12, 46, 79]) == [31, 64, 108]
    assert candidate([20, 16, 33], [13, 47, 80]) == [33, 63, 113]
    assert candidate([16, 24, 34], [17, 41, 76]) == [33, 65, 110]
    assert candidate([19, 24, 34], [11, 50, 80]) == [30, 74, 114]
    assert candidate([14, 24, 28], [18, 43, 76]) == [32, 67, 104]
    assert candidate([11, 15, 29], [19, 46, 80]) == [30, 61, 109]
    assert candidate([14, 18, 31], [11, 41, 78]) == [25, 59, 109]
    assert candidate([16, 18, 32], [13, 46, 72]) == [29, 64, 104]
    assert candidate([13, 23, 30], [19, 41, 78]) == [32, 64, 108]
    assert candidate([16, 18, 33], [17, 44, 80]) == [33, 62, 113]
    assert candidate([13, 22, 33], [12, 48, 77]) == [25, 70, 110]
    assert candidate([13, 18, 29], [14, 50, 76]) == [27, 68, 105]
    assert candidate([15, 18, 29], [12, 43, 80]) == [27, 61, 109]
    assert candidate([12, 16, 35], [11, 46, 74]) == [23, 62, 109]
    assert candidate([14, 16, 32], [18, 40, 75]) == [32, 56, 107]
    assert candidate([14, 21, 29], [10, 41, 80]) == [24, 62, 109]
    assert candidate([13, 18, 25], [16, 45, 75]) == [29, 63, 100]
    assert candidate([18, 25, 35], [19, 47, 79]) == [37, 72, 114]
    assert candidate([18, 25, 29], [16, 48, 73]) == [34, 73, 102]

if __name__ == '__main__':
    check(sum_list)