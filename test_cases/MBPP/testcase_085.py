from case_MBPP_085 import circle_circumference


def check(candidate):
    assert math.isclose(candidate(10), 62.830000000000005, rel_tol=0.001)
    assert math.isclose(candidate(5), 31.415000000000003, rel_tol=0.001)
    assert math.isclose(candidate(4), 25.132, rel_tol=0.001)

if __name__ == '__main__':
    check(circle_circumference)