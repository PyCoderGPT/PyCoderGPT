from case_MBPP_204 import overlapping


def check(candidate):
    assert candidate([1,2,3,4,5],[6,7,8,9]) == False
    assert candidate([1,2,3],[4,5,6]) == False
    assert candidate([1,4,5],[1,4,5]) == True

if __name__ == '__main__':
    check(overlapping)