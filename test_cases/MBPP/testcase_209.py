from case_MBPP_209 import cube_Sum


def check(candidate):
    assert candidate(2) == 72
    assert candidate(3) == 288
    assert candidate(4) == 800

if __name__ == '__main__':
    check(cube_Sum)