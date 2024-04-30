from case_MBPP_421 import is_product_even


def check(candidate):
    assert candidate([1,2,3])
    assert candidate([1,2,1,4])
    assert not candidate([1,1])

if __name__ == '__main__':
    check(is_product_even)