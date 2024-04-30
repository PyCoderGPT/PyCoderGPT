from case_MBPP_071 import amicable_numbers_sum


def check(candidate):
    assert candidate(999)==504
    assert candidate(9999)==31626
    assert candidate(99)==0

if __name__ == '__main__':
    check(amicable_numbers_sum)