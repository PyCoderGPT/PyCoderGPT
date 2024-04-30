from case_MBPP_382 import unique_Element


def check(candidate):
    assert candidate([1,1,1]) == True
    assert candidate([1,2,1,2]) == False
    assert candidate([1,2,3,4,5]) == False

if __name__ == '__main__':
    check(unique_Element)