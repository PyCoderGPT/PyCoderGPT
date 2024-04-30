from case_MBPP_297 import swap_List


def check(candidate):
    assert candidate([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
    assert candidate([1, 2, 3]) == [3, 2, 1]
    assert candidate([4, 5, 6]) == [6, 5, 4]

if __name__ == '__main__':
    check(swap_List)