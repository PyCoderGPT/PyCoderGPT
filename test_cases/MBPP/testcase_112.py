from case_MBPP_112 import lateralsuface_cylinder


def check(candidate):
    assert math.isclose(candidate(10,5), 314.15000000000003, rel_tol=0.001)
    assert math.isclose(candidate(4,5), 125.66000000000001, rel_tol=0.001)
    assert math.isclose(candidate(4,10), 251.32000000000002, rel_tol=0.001)

if __name__ == '__main__':
    check(lateralsuface_cylinder)