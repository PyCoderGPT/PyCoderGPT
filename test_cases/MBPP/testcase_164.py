from case_MBPP_164 import max_val


def check(candidate):
    assert candidate(['Python', 3, 2, 4, 5, 'version'])==5
    assert candidate(['Python', 15, 20, 25])==25
    assert candidate(['Python', 30, 20, 40, 50, 'version'])==50

if __name__ == '__main__':
    check(max_val)