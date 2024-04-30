from case_MBPP_310 import prime_num


def check(candidate):
    assert candidate(13)==True
    assert candidate(7)==True
    assert candidate(-1010)==False

if __name__ == '__main__':
    check(prime_num)