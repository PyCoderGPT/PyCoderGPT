from case_MBPP_104 import binary_search


def check(candidate):
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
    assert is_majority([6, 2, 3, 8, 1, 4, 11], 7, 8) == False
    assert is_majority([4, 6, 3, 2, 6, 3, 11], 9, 5) == False
    assert is_majority([4, 4, 4, 6, 6, 7, 12], 7, 4) == False
    assert is_majority([6, 3, 2, 1, 8, 7, 13], 12, 7) == False
    assert is_majority([1, 1, 5, 8, 6, 5, 9], 4, 6) == False
    assert is_majority([3, 4, 8, 6, 6, 8, 8], 11, 2) == False
    assert is_majority([1, 5, 4, 1, 2, 5, 12], 4, 7) == False
    assert is_majority([1, 3, 1, 4, 1, 4, 14], 7, 8) == False
    assert is_majority([2, 7, 3, 4, 1, 4, 12], 4, 7) == False
    assert is_majority([1, 1, 1, 7, 5, 1, 15], 3, 6) == False
    assert is_majority([4, 4, 7, 4, 3, 3, 7], 3, 1) == False
    assert is_majority([4, 3, 7, 1, 7, 4, 12], 8, 8) == False
    assert is_majority([3, 5, 2, 4, 8, 1, 11], 3, 4) == False
    assert is_majority([1, 2, 7, 5, 4, 6, 15], 5, 5) == False
    assert is_majority([3, 4, 4, 5, 8, 3, 7], 6, 7) == False
    assert is_majority([3, 3, 8, 6, 3, 7, 13], 9, 7) == False
    assert is_majority([3, 1, 1, 6, 6, 6, 5], 3, 1) == False
    assert is_majority([6, 2, 3, 4, 7, 2, 9], 2, 5) == False
    assert is_majority([6, 4, 6, 7, 3, 8, 10], 5, 3) == False
    assert is_majority([4, 5, 2, 7, 2, 8, 12], 4, 3) == False
    assert is_majority([3, 4, 1, 1, 6, 5, 13], 4, 2) == False
    assert is_majority([3, 4, 8, 4, 4, 1, 9], 3, 3) == False
    assert is_majority([2, 2, 1, 5, 4, 7, 8], 7, 2) == False
    assert is_majority([2, 3, 1, 4, 1, 4, 10], 4, 2) == False
    assert is_majority([2, 1, 8, 2, 2, 8, 5], 7, 7) == False
    assert is_majority([4, 4, 2, 3, 4, 1, 9], 3, 4) == True
    assert is_majority([4, 3, 7, 3, 1, 4, 5], 11, 1) == False
    assert is_majority([2, 7, 3, 6, 2, 6, 11], 9, 1) == False
    assert is_majority([5, 2, 1, 6, 3, 6, 6], 9, 6) == False
    assert is_majority([2, 2, 6, 7, 2, 3, 8], 2, 7) == False
    assert is_majority([3, 1, 6, 3, 5, 1, 9], 8, 7) == False
    assert is_majority([4, 5, 7, 5, 1, 3, 14], 9, 1) == False
    assert is_majority([4, 3, 3, 2, 6, 1, 6], 10, 2) == False
    assert is_majority([2, 3, 5, 5, 4, 2, 11, 7], 5, 6) == False
    assert is_majority([2, 1, 7, 7, 4, 1, 5, 10], 3, 8) == False
    assert is_majority([2, 6, 6, 2, 9, 3, 7, 9], 3, 7) == False
    assert is_majority([2, 1, 1, 6, 6, 5, 7, 3], 7, 4) == False
    assert is_majority([6, 4, 4, 6, 9, 4, 2, 7], 7, 3) == False
    assert is_majority([3, 1, 4, 4, 1, 9, 7, 1], 11, 3) == False
    assert is_majority([5, 6, 7, 5, 3, 9, 9, 3], 8, 2) == False
    assert is_majority([3, 6, 6, 6, 3, 3, 3, 6], 10, 3) == True
    assert is_majority([6, 4, 1, 3, 6, 5, 7, 7], 6, 9) == False
    assert is_majority([4, 6, 1, 8, 5, 8, 6, 11], 7, 1) == False
    assert is_majority([5, 6, 7, 4, 7, 4, 8, 10], 6, 8) == False
    assert is_majority([5, 3, 4, 8, 2, 7, 6, 6], 13, 6) == False
    assert is_majority([4, 5, 5, 7, 5, 3, 8, 9], 7, 2) == False
    assert is_majority([3, 5, 3, 1, 1, 9, 1, 2], 3, 9) == False
    assert is_majority([2, 5, 6, 8, 6, 9, 1, 4], 7, 7) == False
    assert is_majority([4, 3, 2, 6, 8, 8, 9, 2], 7, 8) == False
    assert is_majority([5, 1, 6, 4, 4, 5, 5, 9], 3, 3) == False
    assert is_majority([6, 2, 5, 5, 2, 2, 2, 9], 7, 4) == False
    assert is_majority([2, 3, 6, 3, 4, 3, 10, 9], 6, 3) == False
    assert is_majority([5, 2, 4, 5, 9, 4, 2, 10], 3, 4) == False
    assert is_majority([2, 3, 4, 5, 5, 9, 8, 10], 4, 1) == False
    assert is_majority([3, 1, 7, 6, 5, 2, 2, 10], 5, 8) == False
    assert is_majority([1, 2, 3, 6, 6, 8, 7, 2], 7, 6) == False
    assert is_majority([5, 2, 6, 3, 3, 2, 3, 11], 8, 2) == False
    assert is_majority([4, 3, 5, 6, 2, 8, 5, 10], 5, 8) == False
    assert is_majority([3, 5, 4, 1, 1, 1, 9, 4], 5, 5) == False
    assert is_majority([1, 1, 2, 3, 2, 8, 8, 8], 11, 2) == False
    assert is_majority([2, 5, 2, 7, 9, 3, 6, 5], 8, 1) == False
    assert is_majority([3, 2, 3, 2, 5, 8, 11, 11], 9, 7) == False
    assert is_majority([4, 4, 1, 8, 2, 6, 1, 10], 9, 2) == False
    assert is_majority([4, 2, 6, 8, 9, 4, 4, 4], 13, 1) == False
    assert is_majority([1, 3, 7, 3, 1, 7, 10, 7], 4, 8) == False
    assert is_majority([6, 1, 7, 8, 4, 1, 3, 9], 7, 3) == False
    assert is_majority([1, 6, 2, 6, 3], 7, 2) == False
    assert is_majority([2, 1, 1, 7, 2], 2, 5) == False
    assert is_majority([5, 1, 6, 5, 7], 5, 5) == False
    assert is_majority([2, 1, 1, 6, 6], 5, 4) == False
    assert is_majority([2, 2, 2, 4, 6], 3, 6) == False
    assert is_majority([2, 1, 6, 3, 1], 6, 3) == False
    assert is_majority([3, 5, 5, 6, 5], 3, 6) == False
    assert is_majority([1, 1, 3, 5, 4], 5, 6) == False
    assert is_majority([1, 6, 4, 3, 1], 6, 2) == False
    assert is_majority([6, 3, 4, 4, 2], 9, 2) == False
    assert is_majority([3, 4, 4, 7, 7], 3, 2) == False
    assert is_majority([5, 3, 4, 6, 3], 1, 2) == False
    assert is_majority([6, 5, 5, 1, 1], 4, 2) == False
    assert is_majority([1, 4, 1, 6, 4], 2, 1) == False
    assert is_majority([2, 5, 2, 2, 7], 6, 5) == False
    assert is_majority([5, 5, 1, 3, 3], 4, 5) == False
    assert is_majority([5, 6, 1, 5, 6], 2, 2) == False
    assert is_majority([4, 2, 5, 3, 5], 6, 1) == False
    assert is_majority([6, 2, 6, 6, 7], 9, 1) == False
    assert is_majority([6, 5, 1, 3, 5], 10, 4) == False
    assert is_majority([6, 5, 6, 6, 3], 3, 3) == False
    assert is_majority([6, 6, 5, 3, 7], 3, 4) == False
    assert is_majority([1, 3, 4, 7, 7], 4, 6) == False
    assert is_majority([2, 2, 6, 7, 6], 9, 1) == False
    assert is_majority([1, 3, 2, 7, 6], 3, 2) == False
    assert is_majority([3, 2, 4, 2, 4], 2, 2) == False
    assert is_majority([1, 4, 4, 1, 4], 2, 6) == False
    assert is_majority([3, 4, 3, 1, 4], 2, 6) == False
    assert is_majority([4, 1, 4, 2, 2], 2, 2) == False
    assert is_majority([1, 3, 3, 3, 7], 5, 2) == False
    assert is_majority([6, 6, 1, 3, 1], 7, 1) == False
    assert is_majority([1, 5, 2, 2, 2], 2, 6) == False
    assert is_majority([2, 2, 4, 6, 5], 2, 4) == False

if __name__ == '__main__':
    check(binary_search)