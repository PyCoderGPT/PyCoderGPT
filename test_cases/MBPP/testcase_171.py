from case_MBPP_171 import find_Element


def check(candidate):
    assert candidate([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
    assert candidate([1,2,3,4],[[0,1],[0,2]],1,2) == 3
    assert candidate([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1

if __name__ == '__main__':
    check(find_Element)