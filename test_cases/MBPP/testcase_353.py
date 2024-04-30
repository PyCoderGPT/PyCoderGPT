from case_MBPP_353 import lateralsurface_cone


def check(candidate):
    assert candidate(5,12)==204.20352248333654
    assert candidate(10,15)==566.3586699569488
    assert candidate(19,17)==1521.8090132193388

if __name__ == '__main__':
    check(lateralsurface_cone)