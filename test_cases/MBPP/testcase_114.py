from case_MBPP_114 import even_bit_set_number


def check(candidate):
    assert candidate(10) == 10
    assert candidate(20) == 30
    assert candidate(30) == 30

if __name__ == '__main__':
    check(even_bit_set_number)