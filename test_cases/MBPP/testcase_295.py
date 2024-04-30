from case_MBPP_295 import perfect_squares


def check(candidate):
    assert candidate(1,30)==[1, 4, 9, 16, 25]
    assert candidate(50,100)==[64, 81, 100]
    assert candidate(100,200)==[100, 121, 144, 169, 196]

if __name__ == '__main__':
    check(perfect_squares)