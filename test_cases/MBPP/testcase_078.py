from case_MBPP_078 import max_occurrences


def check(candidate):
    assert candidate([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    assert candidate([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8
    assert candidate([10,20,20,30,40,90,80,50,30,20,50,10])==20

if __name__ == '__main__':
    check(max_occurrences)