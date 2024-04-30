from case_MBPP_156 import check_element


def check(candidate):
    assert candidate(["green", "orange", "black", "white"],'blue')==False
    assert candidate([1,2,3,4],7)==False
    assert candidate(["green", "green", "green", "green"],'green')==True

if __name__ == '__main__':
    check(check_element)