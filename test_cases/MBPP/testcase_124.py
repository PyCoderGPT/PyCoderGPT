from case_MBPP_124 import harmonic_sum


def check(candidate):
    assert math.isclose(candidate(7), 2.5928571428571425, rel_tol=0.001)
    assert math.isclose(candidate(4), 2.083333333333333, rel_tol=0.001)
    assert math.isclose(candidate(19), 3.547739657143682, rel_tol=0.001)

if __name__ == '__main__':
    check(harmonic_sum)