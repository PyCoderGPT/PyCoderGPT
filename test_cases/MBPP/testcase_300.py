from case_MBPP_300 import diff_even_odd


def check(candidate):
    assert candidate([1,3,5,7,4,1,6,8])==3
    assert candidate([1,2,3,4,5,6,7,8,9,10])==1
    assert candidate([1,5,7,9,10])==9

if __name__ == '__main__':
    check(diff_even_odd)