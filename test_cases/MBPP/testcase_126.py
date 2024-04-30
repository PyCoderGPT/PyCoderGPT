from case_MBPP_126 import count_X


def check(candidate):
    assert candidate((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
    assert candidate((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 3
    assert candidate((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 4

if __name__ == '__main__':
    check(count_X)