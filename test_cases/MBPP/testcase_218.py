from case_MBPP_218 import parabola_directrix


def check(candidate):
    assert candidate(5,3,2)==-198
    assert candidate(9,8,4)==-2336
    assert candidate(2,4,6)==-130

if __name__ == '__main__':
    check(parabola_directrix)