from case_MBPP_282 import is_Sub_Array


def check(candidate):
    assert candidate([1,4,3,5],[1,2]) == False
    assert candidate([1,2,1],[1,2,1]) == True
    assert candidate([1,0,2,2],[2,2,0]) ==False

if __name__ == '__main__':
    check(is_Sub_Array)