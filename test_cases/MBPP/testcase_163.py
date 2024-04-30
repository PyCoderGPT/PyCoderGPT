from case_MBPP_163 import otherside_rightangle


def check(candidate):
    assert candidate(7,8)==10.63014581273465
    assert candidate(3,4)==5
    assert candidate(7,15)==16.55294535724685

if __name__ == '__main__':
    check(otherside_rightangle)