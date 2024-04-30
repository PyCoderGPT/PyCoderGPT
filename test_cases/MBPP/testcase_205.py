from case_MBPP_205 import max_Product


def check(candidate):
    assert candidate([1,2,3,4,7,0,8,4]) == (7,8)
    assert candidate([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert candidate([1,2,3]) == (2,3)

if __name__ == '__main__':
    check(max_Product)