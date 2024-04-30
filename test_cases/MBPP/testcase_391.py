from case_MBPP_391 import check_expression


def check(candidate):
    assert candidate("{()}[{}]") == True
    assert candidate("{()}[{]") == False
    assert candidate("{()}[{}][]({})") == True

if __name__ == '__main__':
    check(check_expression)