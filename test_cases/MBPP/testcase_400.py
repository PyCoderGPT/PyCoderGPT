from case_MBPP_400 import count_divisors


def check(candidate):
    assert candidate(10)
    assert not candidate(100)
    assert candidate(125)

if __name__ == '__main__':
    check(count_divisors)