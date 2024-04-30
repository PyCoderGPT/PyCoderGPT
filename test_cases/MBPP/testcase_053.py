from case_MBPP_053 import decimal_to_binary


def check(candidate):
    assert candidate(8) == '1000'
    assert candidate(18) == '10010'
    assert candidate(7) == '111'

if __name__ == '__main__':
    check(decimal_to_binary)