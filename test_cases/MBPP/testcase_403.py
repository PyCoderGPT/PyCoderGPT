from case_MBPP_403 import mul_even_odd


def check(candidate):
    assert candidate([1,3,5,7,4,1,6,8])==4
    assert candidate([1,2,3,4,5,6,7,8,9,10])==2
    assert candidate([1,5,7,9,10])==10

if __name__ == '__main__':
    check(mul_even_odd)