from case_MBPP_311 import radian_degree


def check(candidate):
    assert candidate(90)==1.5707963267948966
    assert candidate(60)==1.0471975511965976
    assert candidate(120)==2.0943951023931953

if __name__ == '__main__':
    check(radian_degree)