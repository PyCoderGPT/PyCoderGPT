from case_MBPP_096 import count_char_position


def check(candidate):
    assert candidate("xbcefg") == 2
    assert candidate("ABcED") == 3
    assert candidate("AbgdeF") == 5

if __name__ == '__main__':
    check(count_char_position)