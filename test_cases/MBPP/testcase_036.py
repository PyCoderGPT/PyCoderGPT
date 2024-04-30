from case_MBPP_036 import volume_sphere


def check(candidate):
    assert math.isclose(candidate(10), 4188.790204786391, rel_tol=0.001)
    assert math.isclose(candidate(25), 65449.84694978735, rel_tol=0.001)
    assert math.isclose(candidate(20), 33510.32163829113, rel_tol=0.001)

if __name__ == '__main__':
    check(volume_sphere)