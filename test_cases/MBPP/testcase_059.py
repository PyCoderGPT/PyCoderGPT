from case_MBPP_059 import count


def check(candidate):
    assert candidate([True,False,True]) == 2
    assert candidate([False,False]) == 0
    assert candidate([True,True,True]) == 3

if __name__ == '__main__':
    check(count)