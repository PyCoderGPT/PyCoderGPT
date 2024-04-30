from case_MBPP_292 import split_Arr


def check(candidate):
    assert candidate([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
    assert candidate([1,2,3,4],1) == [2,3,4,1]
    assert candidate([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]

if __name__ == '__main__':
    check(split_Arr)