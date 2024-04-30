from case_MBPP_190 import sum_of_digits


def check(candidate):
    assert candidate([10,2,56])==14
    assert candidate([[10,20,4,5,'b',70,'a']])==19
    assert candidate([10,20,-4,5,-70])==19

if __name__ == '__main__':
    check(sum_of_digits)