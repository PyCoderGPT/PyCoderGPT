from case_MBPP_049 import Find_Min_Length


def check(candidate):
    assert candidate([[1],[1,2]]) == 1
    assert candidate([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert candidate([[3,3,3],[4,4,4,4]]) == 3

if __name__ == '__main__':
    check(Find_Min_Length)