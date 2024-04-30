from case_MBPP_368 import sector_area


def check(candidate):
    assert candidate(4,45)==6.283185307179586
    assert candidate(9,45)==31.808625617596654
    assert candidate(9,361)==None

if __name__ == '__main__':
    check(sector_area)