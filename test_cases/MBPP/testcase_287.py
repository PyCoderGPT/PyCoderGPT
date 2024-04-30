from case_MBPP_287 import surface_Area


def check(candidate):
    assert candidate(3,4) == 33
    assert candidate(4,5) == 56
    assert candidate(1,2) == 5

if __name__ == '__main__':
    check(surface_Area)