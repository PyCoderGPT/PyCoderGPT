from case_HE_059 import largest_prime_factor


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


if __name__ == '__main__':
    check(largest_prime_factor)