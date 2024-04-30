from case_MBPP_129 import count_integer


def check(candidate):
    assert candidate([1,2,'abc',1.2]) == 2
    assert candidate([1,2,3]) == 3
    assert candidate([1,1.2,4,5.1]) == 2

if __name__ == '__main__':
    check(count_integer)