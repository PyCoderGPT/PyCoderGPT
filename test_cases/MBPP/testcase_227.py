from case_MBPP_227 import multiple_to_single


def check(candidate):
    assert candidate([11, 33, 50])==113350
    assert candidate([-1,2,3,4,5,6])==-123456
    assert candidate([10,15,20,25])==10152025

if __name__ == '__main__':
    check(multiple_to_single)