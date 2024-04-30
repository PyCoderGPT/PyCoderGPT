from case_MBPP_235 import cube_nums


def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    assert candidate([10,20,30])==([1000, 8000, 27000])
    assert candidate([12,15])==([1728, 3375])

if __name__ == '__main__':
    check(cube_nums)