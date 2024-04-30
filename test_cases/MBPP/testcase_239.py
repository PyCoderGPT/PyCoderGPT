from case_MBPP_239 import loss_amount


def check(candidate):
    assert candidate(1500,1200)==0
    assert candidate(100,200)==100
    assert candidate(2000,5000)==3000

if __name__ == '__main__':
    check(loss_amount)