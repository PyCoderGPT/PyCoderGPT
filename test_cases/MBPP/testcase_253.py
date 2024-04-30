from case_MBPP_253 import max_product


def check(candidate):
    assert candidate([3, 100, 4, 5, 150, 6]) == 3000
    assert candidate([4, 42, 55, 68, 80]) == 50265600
    assert candidate([10, 22, 9, 33, 21, 50, 41, 60]) == 2460

if __name__ == '__main__':
    check(max_product)