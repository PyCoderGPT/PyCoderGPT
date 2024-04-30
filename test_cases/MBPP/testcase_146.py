from case_MBPP_146 import substract_elements


def check(candidate):
    assert candidate((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
    assert candidate((11, 2, 3), (24, 45 ,16)) == (-13, -43, -13)
    assert candidate((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)

if __name__ == '__main__':
    check(substract_elements)