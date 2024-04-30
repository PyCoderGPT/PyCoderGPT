from case_MBPP_097 import find_even_pair


def check(candidate):
    assert candidate([5, 4, 7, 2, 1]) == 4
    assert candidate([7, 2, 8, 1, 0, 5, 11]) == 9
    assert candidate([1, 2, 3]) == 1

if __name__ == '__main__':
    check(find_even_pair)