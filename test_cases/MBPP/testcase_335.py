from case_MBPP_335 import pair_xor_Sum


def check(candidate):
    assert candidate([5,9,7,6],4) == 47
    assert candidate([7,3,5],3) == 12
    assert candidate([7,3],2) == 4

if __name__ == '__main__':
    check(pair_xor_Sum)