from case_MBPP_377 import second_smallest


def check(candidate):
    assert candidate([1, 2, -8, -2, 0, -2])==-2
    assert candidate([1, 1, -0.5, 0, 2, -2, -2])==-0.5
    assert candidate([2,2])==None
    assert candidate([2,2,2])==None

if __name__ == '__main__':
    check(second_smallest)