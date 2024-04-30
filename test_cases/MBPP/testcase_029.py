from case_MBPP_029 import comb_sort


def check(candidate):
    assert candidate([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    assert candidate([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
    assert candidate([99, 15, 13, 47]) == [13, 15, 47, 99]

if __name__ == '__main__':
    check(comb_sort)