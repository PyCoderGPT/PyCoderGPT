from case_MBPP_009 import find_Volume


def check(candidate):
    assert candidate(10,8,6) == 240
    assert candidate(3,2,2) == 6
    assert candidate(1,2,1) == 1

if __name__ == '__main__':
    check(find_Volume)