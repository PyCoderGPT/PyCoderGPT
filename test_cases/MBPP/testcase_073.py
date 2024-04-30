from case_MBPP_073 import find_length


def check(candidate):
    assert candidate("11000010001") == 6
    assert candidate("10111") == 1
    assert candidate("11011101100101") == 2

if __name__ == '__main__':
    check(find_length)