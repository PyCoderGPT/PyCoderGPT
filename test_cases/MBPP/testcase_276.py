from case_MBPP_276 import issort_list


def check(candidate):
    assert candidate([1,2,4,6,8,10,12,14,16,17])==True
    assert candidate([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False
    assert candidate([1, 2, 4, 6, 8, 10,15,14,20])==False

if __name__ == '__main__':
    check(issort_list)