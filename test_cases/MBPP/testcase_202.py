from case_MBPP_202 import remove_odd


def check(candidate):
    assert candidate([1,2,3]) == [2]
    assert candidate([2,4,6]) == [2,4,6]
    assert candidate([10,20,3]) == [10,20]

if __name__ == '__main__':
    check(remove_odd)