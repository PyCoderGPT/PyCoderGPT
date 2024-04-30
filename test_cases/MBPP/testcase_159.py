from case_MBPP_159 import square_Sum


def check(candidate):
    assert candidate(2) == 20
    assert candidate(3) == 56
    assert candidate(4) == 120

if __name__ == '__main__':
    check(square_Sum)