from case_MBPP_356 import sum_Of_Subarray_Prod


def check(candidate):
    assert candidate([1,2,3]) == 20
    assert candidate([1,2]) == 5
    assert candidate([1,2,3,4]) == 84

if __name__ == '__main__':
    check(sum_Of_Subarray_Prod)