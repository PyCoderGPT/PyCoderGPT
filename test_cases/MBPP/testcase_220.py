from case_MBPP_220 import median_trapezium


def check(candidate):
    assert candidate(15,25,35)==20
    assert candidate(10,20,30)==15
    assert candidate(6,9,4)==7.5

if __name__ == '__main__':
    check(median_trapezium)