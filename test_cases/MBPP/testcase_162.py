from case_MBPP_162 import find


def check(candidate):
    assert candidate(10,3) == 3
    assert candidate(4,2) == 2
    assert candidate(20,5) == 4

if __name__ == '__main__':
    check(find)