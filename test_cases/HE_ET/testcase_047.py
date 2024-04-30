from case_HE_047 import median


def check(candidate):
    assert candidate([-6, 3, 8, 1002, 14, 16]) == 11.0
    assert candidate([2, 10]) == 6.0
    assert candidate([12, 3, 5, 11, 7, 4, 5]) == 5
    assert candidate([-15, 4, 5, 1001, 15, 23]) == 10.0
    assert candidate([-15, 3, 4, 1000, 13, 23]) == 8.5
    assert candidate([-5, 9, 2, 996, 15, 22]) == 12.0
    assert candidate([6, 2, 1, 8, 1]) == 2
    assert candidate([7, 7]) == 7.0
    assert candidate([4, 2, 2, 12, 10, 4, 10]) == 4
    assert candidate([-12, 8, 9, 997, 14, 17]) == 11.5
    assert candidate([1, 1, 3, 1, 10]) == 1
    assert candidate([-8, 4, 8, 997, 15, 20]) == 11.5
    assert candidate([8]) == 8
    assert candidate([5]) == 5
    assert candidate([8, 3, 2, 9, 6, 5, 2]) == 5
    assert candidate([-15, 8, 4, 997, 7, 19]) == 7.5
    assert candidate([-7, 4, 10, 998, 10, 22]) == 10.0
    assert candidate([10]) == 10
    assert candidate([5, 4]) == 4.5
    assert candidate([3, 6, 6, 2, 6]) == 6
    assert candidate([1, 8]) == 4.5
    assert candidate([12, 1, 6, 11, 13, 6, 6]) == 6
    assert candidate([8, 5, 7, 6, 3]) == 6
    assert candidate([6, 2, 7, 8, 8, 5, 4]) == 6
    assert candidate([7, 4]) == 5.5
    assert candidate([-7, 6, 6, 996, 6, 15]) == 6.0
    assert candidate([-15, 8, 1, 1004, 6, 19]) == 7.0
    assert candidate([5, 5, 5, 7, 3]) == 5
    assert candidate([6, 6, 2, 7, 6]) == 6
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([4]) == 4
    assert candidate([11, 2]) == 6.5
    assert candidate([1, 3, 6, 4, 10]) == 4
    assert candidate([-5, 9, 10, 1000, 12, 18]) == 11.0
    assert candidate([10, 6, 4, 8, 4, 3, 11]) == 6
    assert candidate([6, 5]) == 5.5
    assert candidate([6, 6, 6, 9, 7, 4, 10]) == 6
    assert candidate([6, 5, 5, 7, 10, 6, 8]) == 6
    assert candidate([7, 4, 7, 1, 7]) == 7
    assert candidate([-6, 9, 6, 997, 14, 25]) == 11.5
    assert candidate([7, 8]) == 7.5
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-11, 3, 10, 1005, 10, 22]) == 10.0
    assert candidate([6, 9]) == 7.5
    assert candidate([11, 3, 6, 13, 6, 4, 9]) == 6
    assert candidate([-10, 3, 3, 997, 15, 22]) == 9.0
    assert candidate([-8, 5, 4, 1001, 14, 22]) == 9.5
    assert candidate([11, 3, 1, 8, 5, 1, 8]) == 5
    assert candidate([-15, 3, 2, 1002, 8, 22]) == 5.5
    assert candidate([8, 5, 3, 2, 10]) == 5
    assert candidate([11, 1, 3, 8, 13, 2, 7]) == 7
    assert candidate([3, 6, 1, 4, 3]) == 3
    assert candidate([10, 10]) == 10.0
    assert candidate([1]) == 1
    assert candidate([11, 6, 7, 6, 6, 1, 12]) == 6
    assert candidate([1, 5, 6, 6, 3]) == 5
    assert candidate([2, 6, 6, 7, 3]) == 6
    assert candidate([3, 10]) == 6.5
    assert candidate([-11, 5, 11, 1002, 10, 20]) == 10.5
    assert candidate([6, 6, 6, 7, 10]) == 6
    assert candidate([3, 5, 7, 4, 8]) == 5
    assert candidate([13, 5, 6, 7, 14, 7, 9]) == 7
    assert candidate([6, 4, 4, 11, 11, 2, 2]) == 4
    assert candidate([12, 2, 2, 11, 11, 4, 2]) == 4
    assert candidate([3, 9]) == 6.0
    assert candidate([5, 6, 6, 7, 5, 2, 9]) == 6
    assert candidate([4, 6]) == 5.0
    assert candidate([1, 2]) == 1.5
    assert candidate([3, 4, 5, 9, 7, 2, 3]) == 4
    assert candidate([10, 4, 7, 11, 11, 3, 3]) == 7
    assert candidate([6, 10]) == 8.0
    assert candidate([-6, 6, 9, 1005, 8, 25]) == 8.5
    assert candidate([8, 5, 5, 7, 10]) == 7
    assert candidate([-13, 8, 6, 998, 13, 19]) == 10.5
    assert candidate([7, 2, 7, 6, 6]) == 6
    assert candidate([9]) == 9
    assert candidate([7]) == 7
    assert candidate([8, 1, 3, 9, 3]) == 3
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7
    assert candidate([-9, 4, 2, 1002, 6, 23]) == 5.0
    assert candidate([8, 2, 7, 6, 7]) == 7
    assert candidate([1, 6, 7, 5, 4]) == 5
    assert candidate([2, 2]) == 2.0
    assert candidate([6]) == 6
    assert candidate([-7, 7, 8, 1000, 13, 25]) == 10.5
    assert candidate([-5, 1, 10, 1003, 10, 25]) == 10.0
    assert candidate([9, 2]) == 5.5
    assert candidate([3]) == 3
    assert candidate([6, 1, 5, 7, 11, 6, 5]) == 6
    assert candidate([7, 3, 6, 5, 2]) == 5
    assert candidate([-11, 3, 3, 998, 15, 15]) == 9.0
    assert candidate([5, 5]) == 5.0
    assert candidate([9, 5, 2, 6, 13, 7, 2]) == 6
    assert candidate([8, 6, 3, 5, 12, 5, 5]) == 5
    assert candidate([11, 3]) == 7.0
    assert candidate([3, 6, 5, 11, 5, 4, 6]) == 5
    assert candidate([5, 1]) == 3.0
    assert candidate([8, 8]) == 8.0
    assert candidate([7, 2, 7, 1, 4]) == 4
    assert candidate([9, 9]) == 9.0
    assert candidate([3, 6, 2, 6, 9]) == 6
    assert candidate([-11, 1, 3, 1004, 12, 17]) == 7.5
    assert candidate([5, 2, 3, 9, 5, 7, 7]) == 5
    assert candidate([6, 2, 4, 2, 6]) == 4
    assert candidate([3, 1, 7, 4, 3]) == 3
    assert candidate([5, 2, 2, 5, 6, 1, 3]) == 3
    assert candidate([-15, 8, 4, 1000, 6, 16]) == 7.0
    assert candidate([1, 6]) == 3.5
    assert candidate([3, 2, 7, 8, 11, 5, 12]) == 7
    assert candidate([8, 3, 5, 9, 10]) == 8
    assert candidate([2, 9]) == 5.5

if __name__ == '__main__':
    check(median)