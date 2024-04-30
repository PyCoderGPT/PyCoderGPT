from case_MBPP_186 import check_distinct


def check(candidate):
    assert candidate((1, 4, 5, 6, 1, 4)) == False
    assert candidate((1, 4, 5, 6)) == True
    assert candidate((2, 3, 4, 5, 6)) == True

if __name__ == '__main__':
    check(check_distinct)