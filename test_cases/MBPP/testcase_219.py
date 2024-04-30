from case_MBPP_219 import common_element


def check(candidate):
    assert candidate([1,2,3,4,5], [5,6,7,8,9])==True
    assert candidate([1,2,3,4,5], [6,7,8,9])==None
    assert candidate(['a','b','c'], ['d','b','e'])==True

if __name__ == '__main__':
    check(common_element)