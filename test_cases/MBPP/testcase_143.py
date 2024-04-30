from case_MBPP_143 import sum_even_and_even_index


def check(candidate):
    assert candidate([5, 6, 12, 1, 18, 8]) == 30
    assert candidate([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
    assert candidate([5, 6, 12, 1]) == 12

if __name__ == '__main__':
    check(sum_even_and_even_index)