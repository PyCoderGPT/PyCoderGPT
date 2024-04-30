from case_MBPP_405 import right_insertion


def check(candidate):
    assert candidate([1,2,4,5],6)==4
    assert candidate([1,2,4,5],3)==2
    assert candidate([1,2,4,5],7)==4

if __name__ == '__main__':
    check(right_insertion)