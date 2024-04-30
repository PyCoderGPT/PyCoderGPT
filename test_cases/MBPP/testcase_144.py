from case_MBPP_144 import even_Power_Sum


def check(candidate):
    assert candidate(2) == 1056
    assert candidate(3) == 8832
    assert candidate(1) == 32

if __name__ == '__main__':
    check(even_Power_Sum)