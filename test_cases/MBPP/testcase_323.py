from case_MBPP_323 import largest_subset


def check(candidate):
    assert candidate([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert candidate([10, 5, 3, 15, 20]) == 3
    assert candidate([18, 1, 3, 6, 13, 17]) == 4

if __name__ == '__main__':
    check(largest_subset)