from case_MBPP_266 import find_Odd_Pair


def check(candidate):
    assert candidate([5,4,7,2,1],5) == 6
    assert candidate([7,2,8,1,0,5,11],7) == 12
    assert candidate([1,2,3],3) == 2

if __name__ == '__main__':
    check(find_Odd_Pair)