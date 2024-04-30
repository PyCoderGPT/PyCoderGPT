from case_MBPP_173 import max_sum_increasing_subseq


def check(candidate):
    assert candidate([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert candidate([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert candidate([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

if __name__ == '__main__':
    check(max_sum_increasing_subseq)