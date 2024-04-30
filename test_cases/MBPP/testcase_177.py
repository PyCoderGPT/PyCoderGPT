from case_MBPP_177 import string_to_tuple


def check(candidate):
    assert candidate("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
    assert candidate("item1")==('i', 't', 'e', 'm', '1')
    assert candidate("15.10")==('1', '5', '.', '1', '0')

if __name__ == '__main__':
    check(string_to_tuple)