from case_MBPP_191 import bitwise_xor


def check(candidate):
    assert candidate((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
    assert candidate((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
    assert candidate((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)

if __name__ == '__main__':
    check(bitwise_xor)