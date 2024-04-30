from case_MBPP_364 import area_tetrahedron


def check(candidate):
    assert candidate(3)==15.588457268119894
    assert candidate(20)==692.8203230275509
    assert candidate(10)==173.20508075688772

if __name__ == '__main__':
    check(area_tetrahedron)