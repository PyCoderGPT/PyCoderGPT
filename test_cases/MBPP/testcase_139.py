from case_MBPP_139 import lateralsurface_cube


def check(candidate):
    assert candidate(5)==100
    assert candidate(9)==324
    assert candidate(10)==400

if __name__ == '__main__':
    check(lateralsurface_cube)