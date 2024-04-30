from case_MBPP_422 import max_sum_list


def check(candidate):
    assert candidate([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
    assert candidate([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10]
    assert candidate([[2,3,1]])==[2,3,1]

if __name__ == '__main__':
    check(max_sum_list)