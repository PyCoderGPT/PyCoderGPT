from case_MBPP_094 import area_polygon


def check(candidate):
    assert math.isclose(candidate(4, 20), 400., rel_tol=0.001)
    assert math.isclose(candidate(10, 15), 1731.197, rel_tol=0.001)
    assert math.isclose(candidate(9, 7), 302.909, rel_tol=0.001)

if __name__ == '__main__':
    check(area_polygon)