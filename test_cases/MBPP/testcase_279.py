from case_MBPP_279 import two_unique_nums


def check(candidate):
    assert candidate([1,2,3,2,3,4,5]) == [1, 4, 5]
    assert candidate([1,2,3,2,4,5]) == [1, 3, 4, 5]
    assert candidate([1,2,3,4,5]) == [1, 2, 3, 4, 5]

if __name__ == '__main__':
    check(two_unique_nums)