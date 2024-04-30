from case_MBPP_169 import count_binary_seq


def check(candidate):
    assert math.isclose(candidate(1), 2.0, rel_tol=0.001)
    assert math.isclose(candidate(2), 6.0, rel_tol=0.001)
    assert math.isclose(candidate(3), 20.0, rel_tol=0.001)

if __name__ == '__main__':
    check(count_binary_seq)