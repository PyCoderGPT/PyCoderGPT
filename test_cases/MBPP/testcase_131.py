from case_MBPP_131 import count_Primes_nums


def check(candidate):
    assert candidate(5) == 2
    assert candidate(10) == 4
    assert candidate(100) == 25

if __name__ == '__main__':
    check(count_Primes_nums)