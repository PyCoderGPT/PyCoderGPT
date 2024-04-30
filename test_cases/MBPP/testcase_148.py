from case_MBPP_148 import volume_cylinder


def check(candidate):
    assert math.isclose(candidate(10,5), 1570.7500000000002, rel_tol=0.001)
    assert math.isclose(candidate(4,5), 251.32000000000002, rel_tol=0.001)
    assert math.isclose(candidate(4,10), 502.64000000000004, rel_tol=0.001)

if __name__ == '__main__':
    check(volume_cylinder)