from case_MBPP_401 import odd_length_sum


def check(candidate):
    assert candidate([1,2,4]) == 14
    assert candidate([1,2,1,2]) == 15
    assert candidate([1,7]) == 8

if __name__ == '__main__':
    check(odd_length_sum)