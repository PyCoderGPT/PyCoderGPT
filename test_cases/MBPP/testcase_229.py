from case_MBPP_229 import surfacearea_cube


def check(candidate):
    assert candidate(5)==150
    assert candidate(3)==54
    assert candidate(10)==600

if __name__ == '__main__':
    check(surfacearea_cube)