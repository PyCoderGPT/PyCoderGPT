from case_MBPP_158 import max_sub_array_sum_repeated


def check(candidate):
    assert candidate([10, 20, -30, -1], 4, 3) == 30
    assert candidate([-1, 10, 20], 3, 2) == 59
    assert candidate([-1, -2, -3], 3, 3) == -1

if __name__ == '__main__':
    check(max_sub_array_sum_repeated)