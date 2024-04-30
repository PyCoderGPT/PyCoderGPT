from case_HE_035 import max_element


def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

if __name__ == '__main__':
    check(max_element)