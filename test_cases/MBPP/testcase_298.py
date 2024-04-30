from case_MBPP_298 import sum_Of_product


def check(candidate):
    assert candidate(3) == 15
    assert candidate(4) == 56
    assert candidate(1) == 1

if __name__ == '__main__':
    check(sum_Of_product)