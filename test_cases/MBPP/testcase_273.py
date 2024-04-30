from case_MBPP_273 import count_Pairs


def check(candidate):
    assert candidate([1,2,1],3) == 2
    assert candidate([1,1,1,1],4) == 0
    assert candidate([1,2,3,4,5],5) == 10

if __name__ == '__main__':
    check(count_Pairs)