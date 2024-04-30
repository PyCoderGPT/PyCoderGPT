from case_MBPP_154 import sub_list


def check(candidate):
    assert candidate([1, 2, 3],[4,5,6])==[-3,-3,-3]
    assert candidate([1,2],[3,4])==[-2,-2]
    assert candidate([90,120],[50,70])==[40,50]

if __name__ == '__main__':
    check(sub_list)