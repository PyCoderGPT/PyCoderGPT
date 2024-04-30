from case_MBPP_280 import unique_product


def check(candidate):
    assert candidate([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
    assert candidate([1, 2, 3, 1,]) == 6
    assert candidate([7, 8, 9, 0, 1, 1]) == 0

if __name__ == '__main__':
    check(unique_product)