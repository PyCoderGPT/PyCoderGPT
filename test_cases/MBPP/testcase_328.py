from case_MBPP_328 import triangle_area


def check(candidate):
    assert candidate(-1) == None
    assert candidate(0) == 0
    assert candidate(2) == 4

if __name__ == '__main__':
    check(triangle_area)