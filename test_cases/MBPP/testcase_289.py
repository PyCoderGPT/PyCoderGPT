from case_MBPP_289 import catalan_number


def check(candidate):
    assert candidate(10)==16796
    assert candidate(9)==4862
    assert candidate(7)==429

if __name__ == '__main__':
    check(catalan_number)