from case_MBPP_367 import divisible_by_digits


def check(candidate):
    assert candidate(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert candidate(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
    assert candidate(20,25)==[22, 24]

if __name__ == '__main__':
    check(divisible_by_digits)