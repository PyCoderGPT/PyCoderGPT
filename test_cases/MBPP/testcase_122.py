from case_MBPP_122 import babylonian_squareroot


def check(candidate):
    assert math.isclose(candidate(10), 3.162277660168379, rel_tol=0.001)
    assert math.isclose(candidate(2), 1.414213562373095, rel_tol=0.001)
    assert math.isclose(candidate(9), 3.0, rel_tol=0.001)

if __name__ == '__main__':
    check(babylonian_squareroot)