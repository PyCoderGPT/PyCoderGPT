from case_MBPP_358 import left_insertion


def check(candidate):
    assert candidate([1,2,4,5],6)==4
    assert candidate([1,2,4,5],3)==2
    assert candidate([1,2,4,5],7)==4

if __name__ == '__main__':
    check(left_insertion)