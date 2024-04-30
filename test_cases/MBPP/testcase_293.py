from case_MBPP_293 import list_tuple


def check(candidate):
    assert candidate([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
    assert candidate([2, 4, 5, 6, 2, 3, 4, 4, 7])==(2, 4, 5, 6, 2, 3, 4, 4, 7)
    assert candidate([58,44,56])==(58,44,56)

if __name__ == '__main__':
    check(list_tuple)