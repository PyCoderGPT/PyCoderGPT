from case_MBPP_244 import Find_Min


def check(candidate):
    assert candidate([[1],[1,2],[1,2,3]]) == [1]
    assert candidate([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert candidate([['x'],['x','y'],['x','y','z']]) == ['x']

if __name__ == '__main__':
    check(Find_Min)