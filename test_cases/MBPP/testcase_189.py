from case_MBPP_189 import median_numbers


def check(candidate):
    assert candidate(25,55,65)==55.0
    assert candidate(20,10,30)==20.0
    assert candidate(15,45,75)==45.0

if __name__ == '__main__':
    check(median_numbers)