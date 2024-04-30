from case_MBPP_072 import angle_complex


def check(candidate):
    assert math.isclose(candidate(0,1j), 1.5707963267948966, rel_tol=0.001)
    assert math.isclose(candidate(2,1j), 0.4636476090008061, rel_tol=0.001)
    assert math.isclose(candidate(0,2j), 1.5707963267948966, rel_tol=0.001)

if __name__ == '__main__':
    check(angle_complex)