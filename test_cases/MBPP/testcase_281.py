from case_MBPP_281 import surfacearea_cylinder


def check(candidate):
    assert candidate(10,5)==942.45
    assert candidate(4,5)==226.18800000000002
    assert candidate(4,10)==351.848

if __name__ == '__main__':
    check(surfacearea_cylinder)