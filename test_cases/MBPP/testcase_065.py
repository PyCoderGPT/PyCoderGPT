from case_MBPP_065 import empty_dit


def check(candidate):
    assert candidate([{},{},{}])==True
    assert candidate([{1,2},{},{}])==False
    assert candidate({})==True

if __name__ == '__main__':
    check(empty_dit)