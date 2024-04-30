from case_MBPP_087 import pancake_sort


def check(candidate):
    assert candidate([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert candidate([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert candidate([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]

if __name__ == '__main__':
    check(pancake_sort)