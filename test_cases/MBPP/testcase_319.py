from case_MBPP_319 import tuple_modulo


def check(candidate):
    assert candidate((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
    assert candidate((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
    assert candidate((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)

if __name__ == '__main__':
    check(tuple_modulo)