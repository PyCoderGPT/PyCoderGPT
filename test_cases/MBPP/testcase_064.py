from case_MBPP_064 import check_integer


def check(candidate):
    assert candidate("python")==False
    assert candidate("1")==True
    assert candidate("12345")==True

if __name__ == '__main__':
    check(check_integer)