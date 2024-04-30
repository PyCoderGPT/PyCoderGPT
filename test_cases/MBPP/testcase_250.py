from case_MBPP_250 import max_subarray_product


def check(candidate):
    assert candidate([1, -2, -3, 0, 7, -8, -2]) == 112
    assert candidate([6, -3, -10, 0, 2]) == 180
    assert candidate([-2, -40, 0, -2, -3]) == 80

if __name__ == '__main__':
    check(max_subarray_product)