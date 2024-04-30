from case_MBPP_044 import len_log


def check(candidate):
    assert candidate(["python","PHP","bigdata"]) == 7
    assert candidate(["a","ab","abc"]) == 3
    assert candidate(["small","big","tall"]) == 5

if __name__ == '__main__':
    check(len_log)