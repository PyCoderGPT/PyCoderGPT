from case_MBPP_361 import find_Index


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 14
    assert candidate(4) == 45

if __name__ == '__main__':
    check(find_Index)