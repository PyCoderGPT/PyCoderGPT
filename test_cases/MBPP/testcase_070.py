from case_MBPP_070 import max_product_tuple


def check(candidate):
    assert candidate([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
    assert candidate([(10,20), (15,2), (5,10)] )==200
    assert candidate([(11,44), (10,15), (20,5), (12, 9)] )==484

if __name__ == '__main__':
    check(max_product_tuple)