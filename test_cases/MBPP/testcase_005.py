from case_MBPP_005 import square_nums


def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert candidate([10,20,30])==([100,400,900])
    assert candidate([12,15])==([144,225])

if __name__ == '__main__':
    check(square_nums)