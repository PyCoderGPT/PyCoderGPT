from case_MBPP_207 import Find_Max


def check(candidate):
    assert candidate([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
    assert candidate([[1],[1,2],[1,2,3]]) == [1,2,3]
    assert candidate([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]

if __name__ == '__main__':
    check(Find_Max)