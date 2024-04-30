from case_MBPP_011 import square_perimeter


def check(candidate):
    assert candidate(10)==40
    assert candidate(5)==20
    assert candidate(4)==16

if __name__ == '__main__':
    check(square_perimeter)