from case_MBPP_084 import is_Sum_Of_Powers_Of_Two


def check(candidate):
    assert candidate(10) == True
    assert candidate(7) == False
    assert candidate(14) == True

if __name__ == '__main__':
    check(is_Sum_Of_Powers_Of_Two)