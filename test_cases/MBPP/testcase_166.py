from case_MBPP_166 import get_Inv_Count


def check(candidate):
    assert candidate([1,20,6,4,5]) == 5
    assert candidate([1,2,1]) == 1
    assert candidate([1,2,5,6,1]) == 3

if __name__ == '__main__':
    check(get_Inv_Count)