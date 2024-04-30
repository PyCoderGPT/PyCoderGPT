from case_MBPP_062 import odd_Equivalent


def check(candidate):
    assert candidate("011001",6) == 3
    assert candidate("11011",5) == 4
    assert candidate("1010",4) == 2

if __name__ == '__main__':
    check(odd_Equivalent)