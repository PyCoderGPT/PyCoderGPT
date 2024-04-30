from case_HE_146 import specialFilter


def check(candidate):
    assert candidate([10, -5, 6, -5]) == 0
    assert candidate([66, -6, -30, 73, 16, 21]) == 1
    assert candidate([35, -3, -4, 45, 16, 104]) == 1
    assert candidate([15, -75, 14, -17]) == 1
    assert candidate([48, -12, 97, 129, 117, 107]) == 4
    assert candidate([70, 2, -34, 78, 25, 23]) == 0
    assert candidate([36, -6, 2, 49, 22, 111]) == 1
    assert candidate([11, -78, 9, -19]) == 1
    assert candidate([70, -3, -34, 78, 21, 21]) == 0
    assert candidate([34, -2, -2, 44, 18, 105]) == 1
    assert candidate([12, -78, 18, -19]) == 0
    assert candidate([66, 2, -29, 71, 19, 15]) == 3
    assert candidate([6]) == 0
    assert candidate([7, -5, 3, -2]) == 0
    assert candidate([32, 3, -6, 45, 16, 108]) == 0
    assert candidate([14, -74, 18, -20]) == 0
    assert candidate([]) == 0
    assert candidate([3, -7, 5, -5]) == 0
    assert candidate([17, -71, 11, -14]) == 2
    assert candidate([35, 1, 1, 49, 16, 114]) == 1
    assert candidate([69, -5, -33, 80, 16, 17]) == 1
    assert candidate([7, -4, 3, -2]) == 0
    assert candidate([4, 1, 6, -2]) == 0
    assert candidate([43, -12, 96, 128, 120, 104]) == 0
    assert candidate([12, -73, 19, -10]) == 1
    assert candidate([37, 3, 1, 45, 22, 113]) == 2
    assert candidate([10, 2, 2, -5]) == 0
    assert candidate([18, -71, 10, -15]) == 0
    assert candidate([31, -7, -4, 48, 20, 108]) == 1
    assert candidate([40, -10, 88, 126, 117, 112]) == 1
    assert candidate([33, -2, -3, 45, 21, 109]) == 2
    assert candidate([48, -15, 88, 128, 122, 112]) == 0
    assert candidate([16, -74, 18, -13]) == 0
    assert candidate([76, 1, -31, 70, 17, 18]) == 1
    assert candidate([73, 2, -31, 70, 25, 18]) == 1
    assert candidate([45, -7, 91, 125, 122, 106]) == 2
    assert candidate([71, -2, -33, 75, 21, 19]) == 3


    # Check some edge cases that are easy to work out by hand.
    assert candidate([47, -9, 90, 130, 121, 109]) == 2
    assert candidate([15, -73, 17, -15]) == 2
    assert candidate([71, -5, -36, 75, 21, 23]) == 2
    assert candidate([47, -17, 95, 124, 122, 113]) == 2
    assert candidate([74, -7, -29, 80, 22, 18]) == 0
    assert candidate([33, -2, -7, 40, 21, 105]) == 2
    assert candidate([18, -73, 11, -11]) == 1
    assert candidate([43, -12, 93, 125, 121, 109]) == 4
    assert candidate([3, 2, 6, -6]) == 0
    assert candidate([2]) == 0
    assert candidate([1, -7, 2, -10]) == 0
    assert candidate([31, 1, 1, 50, 26, 114]) == 1
    assert candidate([1, -7, 1, -9]) == 0
    assert candidate([40, -12, 94, 130, 117, 110]) == 1
    assert candidate([20, -78, 16, -20]) == 0
    assert candidate([28, -3, -5, 41, 19, 110]) == 1
    assert candidate([12, -73, 13, -15]) == 1
    assert candidate([73, 1, -28, 75, 22, 14]) == 2
    assert candidate([67, -5, -32, 74, 24, 19]) == 1
    assert candidate([5, -2, 1, -5]) == 0
    assert candidate([13, -71, 10, -20]) == 1
    assert candidate([43, -7, 94, 120, 122, 114]) == 0
    assert candidate([72, 1, -30, 80, 21, 24]) == 0
    assert candidate([31, -2, 0, 48, 26, 112]) == 1
    assert candidate([8, -2, 3, -1]) == 0
    assert candidate([19, -74, 19, -12]) == 2
    assert candidate([39, -11, 91, 125, 117, 107]) == 5
    assert candidate([75, 1, -36, 70, 21, 21]) == 1
    assert candidate([1, -5, 5, -5]) == 0
    assert candidate([68, -1, -28, 73, 24, 15]) == 2
    assert candidate([41, -12, 98, 128, 121, 104]) == 1
    assert candidate([30, -4, -8, 42, 23, 112]) == 0
    assert candidate([13, -70, 16, -15]) == 1
    assert candidate([11, -70, 16, -15]) == 1
    assert candidate([1, 0, 6, -7]) == 0
    assert candidate([28, 2, 0, 49, 26, 107]) == 1
    assert candidate([73, 2, -32, 71, 18, 19]) == 3
    assert candidate([5]) == 0
    assert candidate([1]) == 0
    assert candidate([6, -4, 1, -10]) == 0
    assert candidate([8, -2, 4, -7]) == 0
    assert candidate([4]) == 0
    assert candidate([33, 1, -3, 41, 21, 107]) == 2
    assert candidate([74, 1, -31, 79, 16, 17]) == 2
    assert candidate([3, -2, 4, -3]) == 0
    assert candidate([1, 1, 5, -5]) == 0
    assert candidate([41, -8, 96, 130, 118, 109]) == 1
    assert candidate([38, -3, 0, 49, 24, 110]) == 0
    assert candidate([12, -73, 14, -15]) == 0
    assert candidate([16, -72, 9, -20]) == 0
    assert candidate([5, 3, 1, -7]) == 0
    assert candidate([3]) == 0
    assert candidate([38, -6, 2, 43, 21, 105]) == 1
    assert candidate([32, 2, -1, 45, 16, 107]) == 1
    assert candidate([39, -11, 96, 126, 125, 111]) == 3
    assert candidate([31, 1, -3, 41, 16, 110]) == 1
    assert candidate([46, -12, 92, 122, 123, 108]) == 1
    assert candidate([44, -7, 97, 126, 116, 106]) == 1
    assert candidate([39, -15, 91, 120, 121, 107]) == 4
    assert candidate([4, 2, 3, -6]) == 0
    assert candidate([15, -73, 14, -15]) == 1
    assert candidate([74, 0, -35, 74, 19, 16]) == 1
    assert candidate([46, -7, 89, 129, 121, 109]) == 3
    assert candidate([66, 3, -33, 78, 18, 21]) == 0
    assert candidate([47, -9, 97, 128, 118, 111]) == 2

if __name__ == '__main__':
    check(specialFilter)