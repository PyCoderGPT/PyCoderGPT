from case_MBPP_111 import larg_nnum


def check(candidate):
    assert set(candidate([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
    assert set(candidate([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])
    assert set(candidate([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80])

if __name__ == '__main__':
    check(larg_nnum)