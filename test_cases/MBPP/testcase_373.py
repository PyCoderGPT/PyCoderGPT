from case_MBPP_373 import check_min_heap


def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6]) == True
    assert candidate([2, 3, 4, 5, 10, 15]) == True
    assert candidate([2, 10, 4, 5, 3, 15]) == False

if __name__ == '__main__':
    check(check_min_heap)