from case_MBPP_125 import intersection_array


def check(candidate):
    assert candidate([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
    assert candidate([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
    assert candidate([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]

if __name__ == '__main__':
    check(intersection_array)