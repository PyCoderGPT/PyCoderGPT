from case_MBPP_147 import even_binomial_Coeff_Sum


def check(candidate):
    assert candidate(4) == 8
    assert candidate(6) == 32
    assert candidate(2) == 2

if __name__ == '__main__':
    check(even_binomial_Coeff_Sum)