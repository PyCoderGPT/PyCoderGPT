from case_MBPP_031 import is_samepatterns


def check(candidate):
    assert candidate(["red","green","green"], ["a", "b", "b"])==True
    assert candidate(["red","green","greenn"], ["a","b","b"])==False
    assert candidate(["red","green","greenn"], ["a","b"])==False

if __name__ == '__main__':
    check(is_samepatterns)