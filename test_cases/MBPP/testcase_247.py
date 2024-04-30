from case_MBPP_247 import Extract


def check(candidate):
    assert candidate([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
    assert candidate([[1,2,3],[4, 5]]) == [1,4]
    assert candidate([[9,8,1],[1,2]]) == [9,1]

if __name__ == '__main__':
    check(Extract)