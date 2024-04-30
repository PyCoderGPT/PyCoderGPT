from case_MBPP_113 import volume_cube


def check(candidate):
    assert candidate(3)==27
    assert candidate(2)==8
    assert candidate(5)==125

if __name__ == '__main__':
    check(volume_cube)