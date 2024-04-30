from case_MBPP_152 import sequential_search


def check(candidate):
    assert candidate([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
    assert candidate([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)
    assert candidate([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6)
    assert candidate([9, 22, 55, 30, 51, 81, 47, 16, 67, 22], 31) == (False, 10)
    assert candidate([14, 22, 60, 34, 58, 79, 40, 17, 66, 17], 32) == (False, 10)
    assert candidate([12, 22, 62, 36, 58, 72, 41, 12, 64, 24], 36) == (True, 3)
    assert candidate([15, 24, 61, 31, 59, 73, 41, 11, 60, 23], 31) == (True, 3)
    assert candidate([9, 19, 62, 29, 57, 80, 48, 8, 70, 16], 27) == (False, 10)
    assert candidate([11, 18, 59, 29, 51, 76, 48, 10, 69, 16], 34) == (False, 10)
    assert candidate([11, 20, 54, 36, 54, 78, 43, 14, 65, 22], 36) == (True, 3)
    assert candidate([11, 23, 58, 29, 58, 80, 47, 9, 68, 23], 26) == (False, 10)
    assert candidate([6, 24, 62, 27, 60, 73, 38, 15, 60, 16], 28) == (False, 10)
    assert candidate([10, 18, 58, 28, 57, 80, 45, 13, 69, 17], 34) == (False, 10)
    assert candidate([6, 27, 55, 28, 59, 76, 38, 7, 61, 15], 36) == (False, 10)
    assert candidate([11, 18, 57, 34, 56, 81, 48, 15, 66, 22], 26) == (False, 10)
    assert candidate([15, 21, 57, 26, 59, 73, 48, 10, 69, 19], 33) == (False, 10)
    assert candidate([9, 28, 56, 36, 52, 76, 44, 10, 60, 19], 34) == (False, 10)
    assert candidate([12, 20, 56, 27, 61, 78, 40, 16, 66, 19], 35) == (False, 10)
    assert candidate([12, 24, 55, 31, 60, 81, 39, 14, 68, 15], 33) == (False, 10)
    assert candidate([11, 19, 53, 30, 54, 80, 42, 15, 65, 19], 29) == (False, 10)
    assert candidate([11, 21, 58, 26, 53, 80, 40, 15, 60, 14], 26) == (True, 3)
    assert candidate([14, 22, 58, 29, 59, 81, 47, 16, 69, 18], 29) == (True, 3)
    assert candidate([14, 21, 55, 34, 55, 78, 41, 8, 62, 22], 34) == (True, 3)
    assert candidate([15, 18, 62, 29, 52, 72, 47, 13, 62, 17], 29) == (True, 3)
    assert candidate([15, 26, 62, 30, 54, 76, 48, 12, 62, 24], 28) == (False, 10)
    assert candidate([9, 21, 56, 27, 57, 78, 46, 10, 65, 24], 26) == (False, 10)
    assert candidate([15, 21, 54, 30, 53, 78, 41, 10, 70, 19], 34) == (False, 10)
    assert candidate([15, 25, 56, 32, 56, 73, 38, 10, 66, 23], 31) == (False, 10)
    assert candidate([6, 22, 58, 34, 60, 72, 45, 16, 63, 22], 30) == (False, 10)
    assert candidate([15, 27, 57, 33, 54, 82, 46, 8, 63, 23], 33) == (True, 3)
    assert candidate([6, 26, 60, 31, 51, 80, 39, 7, 69, 24], 33) == (False, 10)
    assert candidate([10, 18, 54, 35, 52, 82, 48, 9, 60, 20], 27) == (False, 10)
    assert candidate([11, 23, 59, 29, 55, 75, 40, 11, 61, 18], 29) == (True, 3)
    assert candidate([11, 28, 59, 29, 56, 77, 47, 12, 65, 17], 29) == (True, 3)
    assert candidate([13, 22, 56, 36, 52, 78, 41, 14, 68, 15], 36) == (True, 3)
    assert candidate([15, 25, 58, 31, 59, 77, 40, 15, 64, 23], 28) == (False, 10)
    assert candidate([16, 34, 40, 64, 31, 52, 48, 56], 58) == (False, 8)
    assert candidate([9, 36, 48, 59, 30, 51, 40, 56], 57) == (False, 8)
    assert candidate([12, 32, 49, 67, 33, 46, 42, 62], 61) == (False, 8)
    assert candidate([13, 28, 44, 59, 40, 44, 42, 57], 66) == (False, 8)
    assert candidate([15, 37, 42, 65, 35, 47, 48, 65], 65) == (True, 3)
    assert candidate([11, 30, 41, 57, 40, 49, 40, 56], 60) == (False, 8)
    assert candidate([15, 37, 46, 61, 31, 52, 40, 57], 64) == (False, 8)
    assert candidate([12, 34, 42, 67, 40, 46, 43, 60], 59) == (False, 8)
    assert candidate([14, 31, 50, 58, 32, 42, 42, 60], 62) == (False, 8)
    assert candidate([16, 35, 43, 58, 37, 50, 46, 66], 56) == (False, 8)
    assert candidate([13, 33, 47, 66, 33, 45, 45, 66], 64) == (False, 8)
    assert candidate([12, 30, 44, 62, 31, 44, 45, 58], 56) == (False, 8)
    assert candidate([16, 29, 50, 58, 39, 50, 47, 62], 63) == (False, 8)
    assert candidate([16, 36, 44, 61, 32, 42, 48, 60], 66) == (False, 8)
    assert candidate([8, 36, 43, 59, 32, 47, 45, 65], 60) == (False, 8)
    assert candidate([16, 33, 47, 58, 38, 50, 46, 63], 62) == (False, 8)
    assert candidate([17, 35, 45, 61, 36, 49, 43, 58], 60) == (False, 8)
    assert candidate([9, 37, 44, 58, 36, 48, 46, 61], 63) == (False, 8)
    assert candidate([7, 31, 48, 59, 38, 52, 44, 59], 66) == (False, 8)
    assert candidate([10, 36, 46, 67, 34, 46, 41, 59], 63) == (False, 8)
    assert candidate([12, 32, 44, 61, 39, 49, 48, 63], 60) == (False, 8)
    assert candidate([12, 30, 43, 63, 30, 49, 48, 66], 57) == (False, 8)
    assert candidate([8, 34, 42, 67, 34, 48, 48, 59], 61) == (False, 8)
    assert candidate([11, 35, 40, 66, 34, 45, 49, 63], 66) == (True, 3)
    assert candidate([10, 27, 50, 66, 31, 43, 45, 64], 60) == (False, 8)
    assert candidate([17, 35, 41, 57, 38, 47, 44, 63], 64) == (False, 8)
    assert candidate([8, 36, 43, 59, 35, 48, 45, 60], 59) == (True, 3)
    assert candidate([8, 27, 50, 57, 38, 43, 45, 60], 65) == (False, 8)
    assert candidate([14, 34, 46, 60, 39, 47, 42, 58], 63) == (False, 8)
    assert candidate([17, 36, 46, 57, 35, 52, 48, 57], 62) == (False, 8)
    assert candidate([15, 27, 47, 60, 37, 45, 46, 64], 60) == (True, 3)
    assert candidate([17, 35, 46, 59, 34, 43, 45, 57], 60) == (False, 8)
    assert candidate([17, 33, 50, 61, 38, 42, 48, 58], 59) == (False, 8)
    assert candidate([9, 10, 20, 21, 22, 35, 53, 53], 51) == (False, 8)
    assert candidate([4, 14, 17, 15, 21, 38, 52, 51], 44) == (False, 8)
    assert candidate([12, 7, 15, 15, 19, 41, 45, 57], 50) == (False, 8)
    assert candidate([6, 9, 12, 16, 19, 44, 53, 53], 43) == (False, 8)
    assert candidate([5, 5, 19, 21, 22, 35, 46, 58], 50) == (False, 8)
    assert candidate([13, 7, 15, 15, 21, 41, 46, 55], 44) == (False, 8)
    assert candidate([12, 14, 13, 16, 20, 38, 50, 61], 47) == (False, 8)
    assert candidate([10, 6, 15, 23, 18, 35, 52, 56], 50) == (False, 8)
    assert candidate([8, 8, 12, 14, 19, 34, 50, 56], 53) == (False, 8)
    assert candidate([6, 5, 19, 18, 18, 40, 48, 56], 45) == (False, 8)
    assert candidate([13, 12, 19, 15, 27, 34, 52, 61], 45) == (False, 8)
    assert candidate([14, 12, 20, 23, 23, 44, 47, 59], 50) == (False, 8)
    assert candidate([12, 12, 12, 24, 24, 35, 51, 57], 44) == (False, 8)
    assert candidate([5, 14, 14, 14, 17, 40, 51, 56], 46) == (False, 8)
    assert candidate([11, 5, 14, 15, 25, 44, 50, 60], 46) == (False, 8)
    assert candidate([9, 6, 18, 16, 25, 36, 53, 57], 46) == (False, 8)
    assert candidate([13, 9, 21, 14, 21, 39, 49, 61], 51) == (False, 8)
    assert candidate([7, 12, 15, 15, 24, 37, 44, 55], 46) == (False, 8)
    assert candidate([6, 13, 19, 23, 20, 37, 50, 56], 52) == (False, 8)
    assert candidate([8, 10, 19, 23, 23, 40, 52, 58], 47) == (False, 8)
    assert candidate([7, 6, 19, 18, 23, 40, 53, 58], 47) == (False, 8)
    assert candidate([8, 6, 16, 18, 25, 38, 44, 58], 45) == (False, 8)
    assert candidate([9, 13, 17, 22, 18, 39, 49, 57], 48) == (False, 8)
    assert candidate([12, 15, 19, 20, 19, 36, 43, 56], 44) == (False, 8)
    assert candidate([10, 11, 19, 14, 22, 35, 48, 53], 53) == (True, 7)
    assert candidate([13, 5, 14, 19, 25, 34, 45, 57], 44) == (False, 8)
    assert candidate([4, 5, 20, 18, 26, 36, 51, 57], 52) == (False, 8)
    assert candidate([8, 7, 21, 22, 22, 34, 47, 58], 50) == (False, 8)
    assert candidate([7, 15, 21, 18, 22, 35, 48, 60], 44) == (False, 8)
    assert candidate([11, 6, 18, 18, 19, 40, 51, 61], 45) == (False, 8)
    assert candidate([13, 13, 15, 14, 18, 37, 48, 60], 53) == (False, 8)
    assert candidate([11, 5, 16, 24, 21, 35, 51, 60], 48) == (False, 8)
    assert candidate([9, 12, 16, 24, 22, 40, 47, 56], 50) == (False, 8)

if __name__ == '__main__':
    check(sequential_search)