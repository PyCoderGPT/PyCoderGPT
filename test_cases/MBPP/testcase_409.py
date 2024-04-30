from case_MBPP_409 import remove_nested


def check(candidate):
    assert candidate((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
    assert candidate((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)
    assert candidate((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)
    assert candidate((3, 7, 9, (6, 8), (5,12), 12)) == (3, 7, 9, 12)

if __name__ == '__main__':
    check(remove_nested)