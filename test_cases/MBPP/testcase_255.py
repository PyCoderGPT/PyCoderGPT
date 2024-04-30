from case_MBPP_255 import find_remainder


def check(candidate):
    assert candidate([ 100, 10, 5, 25, 35, 14 ],11) ==9
    assert candidate([1,1,1],1) == 0
    assert candidate([1,2,1],2) == 0

if __name__ == '__main__':
    check(find_remainder)