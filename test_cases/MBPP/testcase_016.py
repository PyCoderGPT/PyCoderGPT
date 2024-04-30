from case_MBPP_016 import find_Max_Num


def check(candidate):
    assert candidate([1,2,3]) == 321
    assert candidate([4,5,6,1]) == 6541
    assert candidate([1,2,3,9]) == 9321

if __name__ == '__main__':
    check(find_Max_Num)