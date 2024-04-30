from case_MBPP_337 import noprofit_noloss


def check(candidate):
    assert candidate(1500,1200)==False
    assert candidate(100,100)==True
    assert candidate(2000,5000)==False

if __name__ == '__main__':
    check(noprofit_noloss)