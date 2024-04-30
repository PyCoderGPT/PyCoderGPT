from case_MBPP_165 import sum_div


def check(candidate):
    assert candidate(8)==7
    assert candidate(12)==16
    assert candidate(7)==1

if __name__ == '__main__':
    check(sum_div)