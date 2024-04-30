from case_MBPP_039 import surfacearea_sphere


def check(candidate):
    assert math.isclose(candidate(10), 1256.6370614359173, rel_tol=0.001)
    assert math.isclose(candidate(15), 2827.4333882308138, rel_tol=0.001)
    assert math.isclose(candidate(20), 5026.548245743669, rel_tol=0.001)

if __name__ == '__main__':
    check(surfacearea_sphere)