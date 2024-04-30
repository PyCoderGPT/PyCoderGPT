from case_MBPP_199 import min_product_tuple


def check(candidate):
    assert candidate([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
    assert candidate([(10,20), (15,2), (5,10)] )==30
    assert candidate([(11,44), (10,15), (20,5), (12, 9)] )==100

if __name__ == '__main__':
    check(min_product_tuple)