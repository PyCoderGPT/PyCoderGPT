from case_MBPP_387 import pair_wise


def check(candidate):
    assert candidate([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
    assert candidate([1,5,7,9,10])==[(1, 5), (5, 7), (7, 9), (9, 10)]
    assert candidate([5,1,9,7,10])==[(5, 1), (1, 9), (9, 7), (7, 10)]
    assert candidate([1,2,3,4,5,6,7,8,9,10])==[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]

if __name__ == '__main__':
    check(pair_wise)