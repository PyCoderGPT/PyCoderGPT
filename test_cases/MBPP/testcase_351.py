from case_MBPP_351 import sum_list


def check(candidate):
    assert candidate([10,20,30],[15,25,35])==[25,45,65]
    assert candidate([1,2,3],[5,6,7])==[6,8,10]
    assert candidate([15,20,30],[15,45,75])==[30,65,105]

if __name__ == '__main__':
    check(sum_list)