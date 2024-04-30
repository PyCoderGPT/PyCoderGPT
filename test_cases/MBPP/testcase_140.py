from case_MBPP_140 import square_Sum


def check(candidate):
    assert candidate(2) == 10
    assert candidate(3) == 35
    assert candidate(4) == 84

if __name__ == '__main__':
    check(square_Sum)