from case_MBPP_134 import newman_prime


def check(candidate):
    assert candidate(3) == 7
    assert candidate(4) == 17
    assert candidate(5) == 41

if __name__ == '__main__':
    check(newman_prime)