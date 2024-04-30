from case_MBPP_052 import multiply_num


def check(candidate):
    assert math.isclose(candidate((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
    assert math.isclose(candidate((-10,-20,-30)), -2000.0, rel_tol=0.001)
    assert math.isclose(candidate((19,15,18)), 1710.0, rel_tol=0.001)

if __name__ == '__main__':
    check(multiply_num)