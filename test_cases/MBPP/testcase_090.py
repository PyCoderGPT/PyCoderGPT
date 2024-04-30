from case_MBPP_090 import max_Abs_Diff


def check(candidate):
    assert candidate((2,1,5,3)) == 4
    assert candidate((9,3,2,5,1)) == 8
    assert candidate((3,2,1)) == 2

if __name__ == '__main__':
    check(max_Abs_Diff)