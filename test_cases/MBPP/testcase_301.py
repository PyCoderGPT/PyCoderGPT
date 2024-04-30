from case_MBPP_301 import min_Swaps


def check(candidate):
    assert candidate("1101","1110") == 1
    assert candidate("111","000") == "Not Possible"
    assert candidate("111","110") == "Not Possible"

if __name__ == '__main__':
    check(min_Swaps)