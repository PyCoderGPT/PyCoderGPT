from case_HE_052 import below_threshold


def check(candidate):
    assert candidate([2, 24, 5, 9], 5) == False
    assert candidate([6, 7, 7, 5], 103) == True
    assert candidate([4, 23, 8, 12], 6) == False
    assert candidate([6, 21, 9, 5], 17) == False
    assert candidate([6, 15, 6, 7], 26) == True
    assert candidate([3, 7, 7, 6], 104) == True
    assert candidate([1, 6, 8, 11], 11) == False
    assert candidate([2, 4, 3, 15], 105) == True
    assert not candidate([1, 8, 4, 10], 10)
    assert candidate([2, 24, 8, 14], 20) == False
    assert candidate([1, 5, 5, 8], 97) == True
    assert candidate([2, 7, 4, 8], 104) == True
    assert candidate([4, 17, 9, 5], 20) == True
    assert candidate([6, 3, 2, 13], 105) == True
    assert candidate([2, 3, 2, 10], 11) == True
    assert candidate([2, 3, 5, 5], 6) == True
    assert candidate([3, 24, 8, 8], 2) == False
    assert candidate([4, 25, 4, 9], 26) == True
    assert candidate([6, 8, 5, 6], 9) == True
    assert candidate([6, 18, 3, 6], 18) == False
    assert candidate([2, 7, 5, 13], 100) == True
    assert candidate([2, 11, 4, 8], 11) == False
    assert candidate([1, 10, 5, 8], 13) == True
    assert candidate([2, 3, 3, 5], 105) == True
    assert candidate([2, 16, 2, 10], 23) == True
    assert candidate([1, 11, 7, 6], 14) == True
    assert candidate([6, 21, 9, 10], 8) == False
    assert candidate([2, 21, 6, 10], 18) == False
    assert candidate([1, 12, 7, 13], 9) == False
    assert candidate([5, 20, 7, 8], 17) == False
    assert candidate([6, 20, 8, 9], 4) == False
    assert candidate([3, 1, 5, 14], 97) == True
    assert candidate([6, 3, 8, 13], 12) == False
    assert candidate([2, 24, 7, 11], 23) == False
    assert candidate([3, 24, 4, 14], 20) == False
    assert candidate([3, 18, 5, 15], 25) == True
    assert candidate([1, 6, 4, 14], 10) == False
    assert candidate([4, 19, 6, 12], 26) == True
    assert candidate([5, 9, 5, 13], 12) == False
    assert candidate([6, 17, 1, 9], 19) == True
    assert candidate([1, 8, 4, 10], 11)
    assert candidate([2, 13, 8, 13], 5) == False
    assert candidate([3, 7, 2, 11], 7) == False
    assert candidate([4, 15, 5, 7], 8) == False
    assert candidate([4, 16, 1, 5], 24) == True
    assert candidate([3, 5, 1, 12], 9) == False
    assert candidate([4, 4, 5, 5], 95) == True
    assert candidate([2, 23, 2, 5], 3) == False
    assert candidate([6, 3, 5, 11], 15) == True
    assert candidate([1, 18, 9, 14], 8) == False
    assert candidate([1, 20, 5, 15], 4) == False
    assert candidate([3, 5, 4, 7], 14) == True
    assert candidate([6, 17, 8, 9], 7) == False
    assert candidate([1, 18, 2, 9], 20) == True
    assert candidate([3, 3, 6, 12], 10) == False
    assert candidate([5, 21, 5, 12], 7) == False
    assert candidate([2, 4, 7, 9], 105) == True
    assert candidate([1, 20, 4, 10], 22)
    assert candidate([6, 24, 9, 11], 24) == False
    assert candidate([1, 22, 2, 14], 23) == True
    assert candidate([5, 23, 5, 15], 7) == False
    assert candidate([1, 24, 5, 6], 19) == False
    assert candidate([4, 7, 5, 9], 97) == True
    assert candidate([2, 25, 4, 12], 16) == False
    assert candidate([2, 7, 4, 8], 96) == True
    assert candidate([6, 13, 8, 15], 9) == False
    assert candidate([5, 23, 9, 15], 25) == True
    assert candidate([6, 25, 8, 13], 7) == False
    assert candidate([1, 2, 4, 10], 100)
    assert candidate([3, 19, 4, 12], 22) == True
    assert candidate([4, 15, 6, 7], 19) == True
    assert candidate([3, 16, 6, 14], 18) == True
    assert candidate([3, 16, 1, 11], 6) == False
    assert candidate([5, 6, 7, 15], 13) == False
    assert candidate([2, 6, 4, 10], 12) == True
    assert candidate([4, 6, 3, 5], 12) == True
    assert candidate([4, 9, 3, 9], 8) == False
    assert candidate([3, 18, 3, 11], 21) == True
    assert candidate([3, 15, 5, 7], 20) == True
    assert candidate([1, 5, 8, 12], 12) == False
    assert candidate([6, 16, 4, 13], 25) == True
    assert candidate([6, 19, 1, 14], 21) == True
    assert candidate([4, 3, 9, 15], 97) == True
    assert candidate([5, 21, 1, 8], 18) == False
    assert candidate([6, 15, 5, 12], 23) == True
    assert candidate([4, 2, 8, 10], 104) == True
    assert candidate([2, 1, 1, 11], 99) == True
    assert candidate([2, 25, 2, 12], 4) == False
    assert candidate([6, 3, 4, 12], 101) == True
    assert candidate([5, 4, 8, 7], 100) == True
    assert candidate([5, 16, 3, 13], 24) == True
    assert candidate([6, 21, 7, 8], 19) == False
    assert candidate([1, 6, 6, 15], 11) == False
    assert candidate([4, 24, 9, 10], 6) == False
    assert candidate([5, 22, 8, 13], 20) == False
    assert candidate([5, 7, 4, 12], 6) == False
    assert candidate([6, 10, 9, 12], 11) == False
    assert candidate([5, 11, 8, 12], 8) == False
    assert candidate([5, 11, 6, 14], 15) == True
    assert candidate([5, 4, 6, 10], 16) == True
    assert candidate([4, 21, 5, 7], 6) == False
    assert candidate([3, 4, 2, 13], 12) == False
    assert candidate([1, 20, 4, 10], 21)
    assert candidate([2, 19, 9, 5], 17) == False
    assert not candidate([1, 20, 4, 10], 5)
    assert candidate([5, 23, 9, 14], 7) == False
    assert candidate([6, 3, 8, 8], 11) == True
    assert candidate([2, 21, 6, 13], 20) == False
    assert candidate([5, 7, 2, 8], 98) == True
    assert candidate([1, 16, 3, 11], 19) == True
    assert candidate([6, 20, 1, 13], 2) == False
    assert candidate([3, 11, 4, 6], 8) == False
    assert candidate([3, 4, 8, 9], 95) == True
    assert candidate([5, 9, 4, 12], 10) == False
    assert candidate([4, 24, 9, 11], 2) == False
    assert candidate([1, 9, 8, 6], 14) == True
    assert candidate([4, 7, 5, 5], 15) == True
    assert candidate([4, 12, 7, 13], 11) == False
    assert candidate([6, 17, 5, 5], 22) == True
    assert candidate([4, 22, 6, 12], 21) == False
    assert candidate([1, 3, 8, 5], 11) == True
    assert candidate([5, 7, 7, 7], 12) == True
    assert candidate([6, 10, 6, 15], 16) == True
    assert candidate([2, 9, 6, 6], 10) == True
    assert candidate([5, 25, 3, 8], 20) == False
    assert candidate([3, 20, 1, 6], 19) == False

if __name__ == '__main__':
    check(below_threshold)