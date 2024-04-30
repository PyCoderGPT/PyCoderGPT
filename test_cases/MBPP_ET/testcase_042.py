from case_MBPP_042 import freq_count


def check(candidate):
    assert candidate([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1}) 
    assert candidate([1,2,3,4,3,2,4,1,3,1,4])==({1:3, 2:2,3:3,4:3}) 
    assert candidate([5,6,7,4,9,10,4,5,6,7,9,5])==({10:1,5:3,6:2,7:2,4:2,9:2}) 
    assert candidate([11, 6, 14, 10, 18, 17, 18, 20, 42, 45, 52, 46, 35]) == Counter({18: 2, 11: 1, 6: 1, 14: 1, 10: 1, 17: 1, 20: 1, 42: 1, 45: 1, 52: 1, 46: 1, 35: 1})
    assert candidate([14, 6, 9, 7, 15, 20, 18, 18, 35, 43, 55, 46, 35]) == Counter({18: 2, 35: 2, 14: 1, 6: 1, 9: 1, 7: 1, 15: 1, 20: 1, 43: 1, 55: 1, 46: 1})
    assert candidate([5, 7, 15, 5, 18, 25, 15, 15, 39, 35, 45, 48, 28]) == Counter({15: 3, 5: 2, 7: 1, 18: 1, 25: 1, 39: 1, 35: 1, 45: 1, 48: 1, 28: 1})
    assert candidate([9, 11, 12, 12, 16, 21, 21, 16, 42, 44, 46, 48, 25]) == Counter({12: 2, 16: 2, 21: 2, 9: 1, 11: 1, 42: 1, 44: 1, 46: 1, 48: 1, 25: 1})
    assert candidate([6, 9, 9, 12, 17, 21, 18, 25, 37, 45, 45, 52, 27]) == Counter({9: 2, 45: 2, 6: 1, 12: 1, 17: 1, 21: 1, 18: 1, 25: 1, 37: 1, 52: 1, 27: 1})
    assert candidate([6, 15, 6, 15, 22, 16, 18, 20, 38, 40, 45, 52, 26]) == Counter({6: 2, 15: 2, 22: 1, 16: 1, 18: 1, 20: 1, 38: 1, 40: 1, 45: 1, 52: 1, 26: 1})
    assert candidate([5, 11, 10, 5, 15, 16, 22, 18, 42, 43, 46, 54, 31]) == Counter({5: 2, 11: 1, 10: 1, 15: 1, 16: 1, 22: 1, 18: 1, 42: 1, 43: 1, 46: 1, 54: 1, 31: 1})
    assert candidate([9, 6, 6, 7, 15, 19, 15, 25, 35, 43, 49, 45, 25]) == Counter({6: 2, 15: 2, 25: 2, 9: 1, 7: 1, 19: 1, 35: 1, 43: 1, 49: 1, 45: 1})
    assert candidate([11, 9, 12, 9, 23, 16, 22, 15, 44, 40, 55, 47, 29]) == Counter({9: 2, 11: 1, 12: 1, 23: 1, 16: 1, 22: 1, 15: 1, 44: 1, 40: 1, 55: 1, 47: 1, 29: 1})
    assert candidate([5, 13, 9, 8, 21, 20, 23, 23, 39, 45, 45, 53, 32]) == Counter({23: 2, 45: 2, 5: 1, 13: 1, 9: 1, 8: 1, 21: 1, 20: 1, 39: 1, 53: 1, 32: 1})
    assert candidate([15, 11, 7, 13, 19, 21, 24, 15, 35, 37, 45, 45, 30]) == Counter({15: 2, 45: 2, 11: 1, 7: 1, 13: 1, 19: 1, 21: 1, 24: 1, 35: 1, 37: 1, 30: 1})
    assert candidate([11, 8, 8, 5, 20, 22, 23, 15, 44, 38, 52, 50, 29]) == Counter({8: 2, 11: 1, 5: 1, 20: 1, 22: 1, 23: 1, 15: 1, 44: 1, 38: 1, 52: 1, 50: 1, 29: 1})
    assert candidate([15, 9, 10, 13, 23, 23, 18, 15, 41, 41, 49, 55, 33]) == Counter({15: 2, 23: 2, 41: 2, 9: 1, 10: 1, 13: 1, 18: 1, 49: 1, 55: 1, 33: 1})
    assert candidate([7, 9, 7, 14, 24, 16, 22, 18, 37, 40, 55, 50, 31]) == Counter({7: 2, 9: 1, 14: 1, 24: 1, 16: 1, 22: 1, 18: 1, 37: 1, 40: 1, 55: 1, 50: 1, 31: 1})
    assert candidate([7, 8, 9, 13, 17, 17, 17, 18, 44, 40, 51, 55, 25]) == Counter({17: 3, 7: 1, 8: 1, 9: 1, 13: 1, 18: 1, 44: 1, 40: 1, 51: 1, 55: 1, 25: 1})
    assert candidate([8, 12, 9, 10, 24, 16, 21, 22, 38, 45, 50, 52, 33]) == Counter({8: 1, 12: 1, 9: 1, 10: 1, 24: 1, 16: 1, 21: 1, 22: 1, 38: 1, 45: 1, 50: 1, 52: 1, 33: 1})
    assert candidate([6, 9, 8, 11, 19, 18, 16, 18, 45, 45, 55, 51, 28]) == Counter({18: 2, 45: 2, 6: 1, 9: 1, 8: 1, 11: 1, 19: 1, 16: 1, 55: 1, 51: 1, 28: 1})
    assert candidate([9, 5, 12, 15, 21, 15, 16, 20, 41, 41, 51, 55, 31]) == Counter({15: 2, 41: 2, 9: 1, 5: 1, 12: 1, 21: 1, 16: 1, 20: 1, 51: 1, 55: 1, 31: 1})
    assert candidate([15, 7, 10, 8, 18, 25, 15, 23, 38, 38, 49, 48, 34]) == Counter({15: 2, 38: 2, 7: 1, 10: 1, 8: 1, 18: 1, 25: 1, 23: 1, 49: 1, 48: 1, 34: 1})
    assert candidate([14, 14, 14, 11, 18, 15, 15, 15, 38, 41, 45, 49, 32]) == Counter({14: 3, 15: 3, 11: 1, 18: 1, 38: 1, 41: 1, 45: 1, 49: 1, 32: 1})
    assert candidate([10, 15, 13, 15, 21, 16, 20, 23, 44, 35, 49, 46, 29]) == Counter({15: 2, 10: 1, 13: 1, 21: 1, 16: 1, 20: 1, 23: 1, 44: 1, 35: 1, 49: 1, 46: 1, 29: 1})
    assert candidate([7, 12, 10, 14, 22, 24, 17, 23, 35, 43, 54, 47, 34]) == Counter({7: 1, 12: 1, 10: 1, 14: 1, 22: 1, 24: 1, 17: 1, 23: 1, 35: 1, 43: 1, 54: 1, 47: 1, 34: 1})
    assert candidate([6, 12, 7, 10, 20, 21, 19, 25, 42, 42, 46, 54, 34]) == Counter({42: 2, 6: 1, 12: 1, 7: 1, 10: 1, 20: 1, 21: 1, 19: 1, 25: 1, 46: 1, 54: 1, 34: 1})
    assert candidate([15, 9, 5, 9, 16, 20, 22, 17, 41, 36, 48, 49, 33]) == Counter({9: 2, 15: 1, 5: 1, 16: 1, 20: 1, 22: 1, 17: 1, 41: 1, 36: 1, 48: 1, 49: 1, 33: 1})
    assert candidate([5, 5, 7, 13, 20, 17, 18, 17, 40, 37, 50, 53, 25]) == Counter({5: 2, 17: 2, 7: 1, 13: 1, 20: 1, 18: 1, 40: 1, 37: 1, 50: 1, 53: 1, 25: 1})
    assert candidate([12, 13, 8, 7, 20, 24, 24, 19, 44, 43, 45, 50, 35]) == Counter({24: 2, 12: 1, 13: 1, 8: 1, 7: 1, 20: 1, 19: 1, 44: 1, 43: 1, 45: 1, 50: 1, 35: 1})
    assert candidate([8, 5, 15, 7, 25, 19, 17, 16, 42, 35, 45, 53, 33]) == Counter({8: 1, 5: 1, 15: 1, 7: 1, 25: 1, 19: 1, 17: 1, 16: 1, 42: 1, 35: 1, 45: 1, 53: 1, 33: 1})
    assert candidate([7, 13, 8, 7, 16, 19, 20, 18, 44, 36, 49, 45, 31]) == Counter({7: 2, 13: 1, 8: 1, 16: 1, 19: 1, 20: 1, 18: 1, 44: 1, 36: 1, 49: 1, 45: 1, 31: 1})
    assert candidate([15, 5, 10, 12, 16, 18, 24, 15, 39, 45, 54, 50, 25]) == Counter({15: 2, 5: 1, 10: 1, 12: 1, 16: 1, 18: 1, 24: 1, 39: 1, 45: 1, 54: 1, 50: 1, 25: 1})
    assert candidate([10, 9, 13, 8, 23, 17, 15, 24, 38, 42, 54, 54, 29]) == Counter({54: 2, 10: 1, 9: 1, 13: 1, 8: 1, 23: 1, 17: 1, 15: 1, 24: 1, 38: 1, 42: 1, 29: 1})
    assert candidate([5, 8, 15, 15, 20, 21, 17, 22, 44, 38, 51, 48, 26]) == Counter({15: 2, 5: 1, 8: 1, 20: 1, 21: 1, 17: 1, 22: 1, 44: 1, 38: 1, 51: 1, 48: 1, 26: 1})
    assert candidate([6, 13, 9, 7, 25, 22, 23, 19, 43, 37, 52, 48, 32]) == Counter({6: 1, 13: 1, 9: 1, 7: 1, 25: 1, 22: 1, 23: 1, 19: 1, 43: 1, 37: 1, 52: 1, 48: 1, 32: 1})
    assert candidate([15, 5, 6, 7, 16, 22, 22, 16, 39, 40, 51, 52, 26]) == Counter({16: 2, 22: 2, 15: 1, 5: 1, 6: 1, 7: 1, 39: 1, 40: 1, 51: 1, 52: 1, 26: 1})
    assert candidate([6, 7, 1, 2, 4, 3, 7, 1, 7, 5, 6]) == Counter({7: 3, 6: 2, 1: 2, 2: 1, 4: 1, 3: 1, 5: 1})
    assert candidate([6, 3, 3, 2, 1, 7, 6, 2, 3, 4, 2]) == Counter({3: 3, 2: 3, 6: 2, 1: 1, 7: 1, 4: 1})
    assert candidate([3, 7, 7, 3, 4, 6, 8, 1, 3, 5, 5]) == Counter({3: 3, 7: 2, 5: 2, 4: 1, 6: 1, 8: 1, 1: 1})
    assert candidate([2, 3, 3, 7, 3, 3, 5, 2, 6, 5, 2]) == Counter({3: 4, 2: 3, 5: 2, 7: 1, 6: 1})
    assert candidate([1, 2, 8, 4, 3, 2, 4, 4, 5, 2, 3]) == Counter({2: 3, 4: 3, 3: 2, 1: 1, 8: 1, 5: 1})
    assert candidate([3, 2, 5, 9, 4, 1, 7, 5, 7, 3, 1]) == Counter({3: 2, 5: 2, 1: 2, 7: 2, 2: 1, 9: 1, 4: 1})
    assert candidate([6, 5, 8, 2, 7, 7, 8, 4, 7, 1, 8]) == Counter({8: 3, 7: 3, 6: 1, 5: 1, 2: 1, 4: 1, 1: 1})
    assert candidate([4, 3, 5, 7, 7, 7, 5, 5, 6, 3, 7]) == Counter({7: 4, 5: 3, 3: 2, 4: 1, 6: 1})
    assert candidate([5, 3, 4, 3, 7, 4, 3, 5, 1, 3, 8]) == Counter({3: 4, 5: 2, 4: 2, 7: 1, 1: 1, 8: 1})
    assert candidate([6, 6, 1, 5, 4, 1, 8, 6, 2, 3, 6]) == Counter({6: 4, 1: 2, 5: 1, 4: 1, 8: 1, 2: 1, 3: 1})
    assert candidate([5, 5, 8, 3, 6, 6, 9, 1, 2, 5, 4]) == Counter({5: 3, 6: 2, 8: 1, 3: 1, 9: 1, 1: 1, 2: 1, 4: 1})
    assert candidate([1, 7, 6, 3, 3, 4, 5, 1, 1, 6, 9]) == Counter({1: 3, 6: 2, 3: 2, 7: 1, 4: 1, 5: 1, 9: 1})
    assert candidate([6, 2, 8, 6, 7, 7, 5, 2, 6, 3, 6]) == Counter({6: 4, 2: 2, 7: 2, 8: 1, 5: 1, 3: 1})
    assert candidate([3, 5, 5, 9, 3, 1, 1, 3, 3, 5, 3]) == Counter({3: 5, 5: 3, 1: 2, 9: 1})
    assert candidate([1, 5, 3, 2, 3, 7, 6, 5, 8, 6, 1]) == Counter({1: 2, 5: 2, 3: 2, 6: 2, 2: 1, 7: 1, 8: 1})
    assert candidate([2, 2, 8, 3, 3, 6, 9, 1, 5, 6, 4]) == Counter({2: 2, 3: 2, 6: 2, 8: 1, 9: 1, 1: 1, 5: 1, 4: 1})
    assert candidate([1, 1, 8, 7, 4, 2, 4, 6, 2, 5, 8]) == Counter({1: 2, 8: 2, 4: 2, 2: 2, 7: 1, 6: 1, 5: 1})
    assert candidate([3, 3, 8, 9, 1, 7, 2, 1, 8, 6, 5]) == Counter({3: 2, 8: 2, 1: 2, 9: 1, 7: 1, 2: 1, 6: 1, 5: 1})
    assert candidate([1, 3, 2, 6, 2, 5, 4, 5, 1, 1, 4]) == Counter({1: 3, 2: 2, 5: 2, 4: 2, 3: 1, 6: 1})
    assert candidate([4, 6, 2, 4, 1, 4, 9, 3, 2, 2, 5]) == Counter({4: 3, 2: 3, 6: 1, 1: 1, 9: 1, 3: 1, 5: 1})
    assert candidate([1, 5, 2, 6, 8, 7, 4, 4, 5, 2, 6]) == Counter({5: 2, 2: 2, 6: 2, 4: 2, 1: 1, 8: 1, 7: 1})
    assert candidate([1, 3, 7, 9, 5, 7, 7, 1, 4, 5, 6]) == Counter({7: 3, 1: 2, 5: 2, 3: 1, 9: 1, 4: 1, 6: 1})
    assert candidate([2, 2, 7, 9, 8, 3, 9, 4, 1, 1, 5]) == Counter({2: 2, 9: 2, 1: 2, 7: 1, 8: 1, 3: 1, 4: 1, 5: 1})
    assert candidate([3, 5, 7, 6, 5, 2, 4, 2, 1, 3, 9]) == Counter({3: 2, 5: 2, 2: 2, 7: 1, 6: 1, 4: 1, 1: 1, 9: 1})
    assert candidate([3, 5, 5, 2, 2, 3, 7, 6, 3, 3, 4]) == Counter({3: 4, 5: 2, 2: 2, 7: 1, 6: 1, 4: 1})
    assert candidate([4, 5, 3, 6, 4, 3, 5, 4, 8, 4, 5]) == Counter({4: 4, 5: 3, 3: 2, 6: 1, 8: 1})
    assert candidate([6, 2, 8, 3, 3, 2, 6, 5, 8, 1, 9]) == Counter({6: 2, 2: 2, 8: 2, 3: 2, 5: 1, 1: 1, 9: 1})
    assert candidate([5, 5, 5, 7, 5, 2, 7, 2, 5, 4, 2]) == Counter({5: 5, 2: 3, 7: 2, 4: 1})
    assert candidate([1, 2, 7, 4, 4, 6, 9, 5, 2, 4, 9]) == Counter({4: 3, 2: 2, 9: 2, 1: 1, 7: 1, 6: 1, 5: 1})
    assert candidate([5, 2, 2, 4, 1, 2, 5, 5, 5, 1, 3]) == Counter({5: 4, 2: 3, 1: 2, 4: 1, 3: 1})
    assert candidate([1, 3, 3, 2, 4, 4, 7, 5, 3, 3, 7]) == Counter({3: 4, 4: 2, 7: 2, 1: 1, 2: 1, 5: 1})
    assert candidate([1, 1, 1, 9, 4, 7, 2, 4, 4, 2, 1]) == Counter({1: 4, 4: 3, 2: 2, 9: 1, 7: 1})
    assert candidate([2, 5, 8, 3, 2, 1, 5, 6, 3, 4, 9]) == Counter({2: 2, 5: 2, 3: 2, 8: 1, 1: 1, 6: 1, 4: 1, 9: 1})
    assert candidate([5, 6, 11, 9, 4, 12, 3, 8, 11, 7, 7, 1]) == Counter({11: 2, 7: 2, 5: 1, 6: 1, 9: 1, 4: 1, 12: 1, 3: 1, 8: 1, 1: 1})
    assert candidate([9, 6, 9, 6, 6, 7, 8, 1, 1, 3, 5, 10]) == Counter({6: 3, 9: 2, 1: 2, 7: 1, 8: 1, 3: 1, 5: 1, 10: 1})
    assert candidate([5, 1, 6, 7, 8, 13, 8, 6, 4, 11, 14, 7]) == Counter({6: 2, 7: 2, 8: 2, 5: 1, 1: 1, 13: 1, 4: 1, 11: 1, 14: 1})
    assert candidate([9, 7, 10, 3, 4, 12, 2, 3, 5, 5, 4, 2]) == Counter({3: 2, 4: 2, 2: 2, 5: 2, 9: 1, 7: 1, 10: 1, 12: 1})
    assert candidate([6, 7, 2, 2, 6, 15, 6, 7, 8, 7, 11, 6]) == Counter({6: 4, 7: 3, 2: 2, 15: 1, 8: 1, 11: 1})
    assert candidate([4, 2, 9, 5, 7, 13, 3, 5, 9, 11, 7, 8]) == Counter({9: 2, 5: 2, 7: 2, 4: 1, 2: 1, 13: 1, 3: 1, 11: 1, 8: 1})
    assert candidate([8, 4, 7, 5, 6, 15, 3, 9, 8, 4, 12, 3]) == Counter({8: 2, 4: 2, 3: 2, 7: 1, 5: 1, 6: 1, 15: 1, 9: 1, 12: 1})
    assert candidate([4, 9, 5, 7, 6, 10, 5, 1, 7, 5, 9, 8]) == Counter({5: 3, 9: 2, 7: 2, 4: 1, 6: 1, 10: 1, 1: 1, 8: 1})
    assert candidate([4, 6, 12, 6, 9, 5, 9, 5, 4, 11, 4, 8]) == Counter({4: 3, 6: 2, 9: 2, 5: 2, 12: 1, 11: 1, 8: 1})
    assert candidate([3, 11, 7, 4, 11, 8, 3, 2, 4, 6, 10, 4]) == Counter({4: 3, 3: 2, 11: 2, 7: 1, 8: 1, 2: 1, 6: 1, 10: 1})
    assert candidate([4, 7, 2, 9, 4, 10, 5, 2, 8, 11, 6, 2]) == Counter({2: 3, 4: 2, 7: 1, 9: 1, 10: 1, 5: 1, 8: 1, 11: 1, 6: 1})
    assert candidate([8, 6, 2, 7, 5, 11, 5, 8, 11, 6, 13, 9]) == Counter({8: 2, 6: 2, 5: 2, 11: 2, 2: 1, 7: 1, 13: 1, 9: 1})
    assert candidate([8, 6, 3, 9, 5, 11, 7, 3, 9, 2, 13, 6]) == Counter({6: 2, 3: 2, 9: 2, 8: 1, 5: 1, 11: 1, 7: 1, 2: 1, 13: 1})
    assert candidate([9, 8, 3, 9, 11, 5, 1, 7, 5, 12, 9, 3]) == Counter({9: 3, 3: 2, 5: 2, 8: 1, 11: 1, 1: 1, 7: 1, 12: 1})
    assert candidate([10, 6, 2, 1, 4, 15, 8, 2, 8, 6, 14, 10]) == Counter({10: 2, 6: 2, 2: 2, 8: 2, 1: 1, 4: 1, 15: 1, 14: 1})
    assert candidate([1, 10, 4, 3, 10, 9, 7, 3, 3, 3, 4, 4]) == Counter({3: 4, 4: 3, 10: 2, 1: 1, 9: 1, 7: 1})
    assert candidate([1, 5, 5, 3, 4, 8, 5, 7, 8, 7, 9, 2]) == Counter({5: 3, 8: 2, 7: 2, 1: 1, 3: 1, 4: 1, 9: 1, 2: 1})
    assert candidate([4, 3, 10, 5, 6, 10, 2, 6, 6, 8, 4, 3]) == Counter({6: 3, 4: 2, 3: 2, 10: 2, 5: 1, 2: 1, 8: 1})
    assert candidate([3, 5, 3, 3, 4, 14, 1, 9, 8, 4, 13, 1]) == Counter({3: 3, 4: 2, 1: 2, 5: 1, 14: 1, 9: 1, 8: 1, 13: 1})
    assert candidate([2, 4, 3, 3, 4, 10, 6, 7, 1, 12, 7, 3]) == Counter({3: 3, 4: 2, 7: 2, 2: 1, 10: 1, 6: 1, 1: 1, 12: 1})
    assert candidate([5, 1, 4, 9, 5, 11, 4, 8, 1, 12, 4, 3]) == Counter({4: 3, 5: 2, 1: 2, 9: 1, 11: 1, 8: 1, 12: 1, 3: 1})
    assert candidate([10, 9, 9, 6, 5, 13, 8, 7, 1, 6, 5, 10]) == Counter({10: 2, 9: 2, 6: 2, 5: 2, 13: 1, 8: 1, 7: 1, 1: 1})
    assert candidate([10, 3, 2, 6, 6, 8, 4, 4, 4, 10, 7, 4]) == Counter({4: 4, 10: 2, 6: 2, 3: 1, 2: 1, 8: 1, 7: 1})
    assert candidate([7, 2, 8, 9, 10, 12, 6, 5, 3, 11, 11, 1]) == Counter({11: 2, 7: 1, 2: 1, 8: 1, 9: 1, 10: 1, 12: 1, 6: 1, 5: 1, 3: 1, 1: 1})
    assert candidate([4, 1, 7, 4, 4, 12, 3, 9, 4, 9, 11, 8]) == Counter({4: 4, 9: 2, 1: 1, 7: 1, 12: 1, 3: 1, 11: 1, 8: 1})
    assert candidate([7, 6, 11, 4, 10, 5, 5, 7, 4, 2, 12, 10]) == Counter({7: 2, 4: 2, 10: 2, 5: 2, 6: 1, 11: 1, 2: 1, 12: 1})
    assert candidate([3, 2, 11, 8, 4, 14, 9, 8, 7, 10, 7, 1]) == Counter({8: 2, 7: 2, 3: 1, 2: 1, 11: 1, 4: 1, 14: 1, 9: 1, 10: 1, 1: 1})
    assert candidate([7, 3, 8, 2, 14, 7, 8, 4, 1, 6, 10, 6]) == Counter({7: 2, 8: 2, 6: 2, 3: 1, 2: 1, 14: 1, 4: 1, 1: 1, 10: 1})
    assert candidate([9, 11, 4, 7, 8, 12, 9, 8, 4, 9, 9, 1]) == Counter({9: 4, 4: 2, 8: 2, 11: 1, 7: 1, 12: 1, 1: 1})
    assert candidate([4, 9, 9, 8, 7, 10, 6, 3, 9, 5, 13, 1]) == Counter({9: 3, 4: 1, 8: 1, 7: 1, 10: 1, 6: 1, 3: 1, 5: 1, 13: 1, 1: 1})
    assert candidate([5, 1, 6, 3, 14, 6, 9, 2, 10, 2, 4, 8]) == Counter({6: 2, 2: 2, 5: 1, 1: 1, 3: 1, 14: 1, 9: 1, 10: 1, 4: 1, 8: 1})
    assert candidate([8, 10, 11, 2, 5, 6, 6, 8, 2, 3, 14, 8]) == Counter({8: 3, 2: 2, 6: 2, 10: 1, 11: 1, 5: 1, 3: 1, 14: 1})
    assert candidate([3, 2, 5, 9, 10, 5, 6, 8, 10, 12, 8, 9]) == Counter({5: 2, 9: 2, 10: 2, 8: 2, 3: 1, 2: 1, 6: 1, 12: 1})

if __name__ == '__main__':
    check(freq_count)