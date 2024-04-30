from case_MBPP_083 import zero_count


def check(candidate):
    assert math.isclose(candidate([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
    assert math.isclose(candidate([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]), 0.00, rel_tol=0.001)
    assert math.isclose(candidate([2, 4, -6, -9, 11, -12, 14, -5, 17]), 0.00, rel_tol=0.001)

if __name__ == '__main__':
    check(zero_count)