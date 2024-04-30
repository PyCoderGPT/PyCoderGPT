from case_MBPP_026 import is_Monotonic


def check(candidate):
    assert candidate([6, 5, 4, 4]) == True
    assert candidate([1, 2, 2, 3]) == True
    assert candidate([1, 3, 2]) == False

if __name__ == '__main__':
    check(is_Monotonic)