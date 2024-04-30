from case_MBPP_312 import find_literals


def check(candidate):
    assert candidate('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
    assert candidate('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
    assert candidate('Hardest choices required strongest will', 'will') == ('will', 35, 39)

if __name__ == '__main__':
    check(find_literals)