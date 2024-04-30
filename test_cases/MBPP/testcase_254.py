from case_MBPP_254 import add_pairwise


def check(candidate):
    assert candidate((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
    assert candidate((2, 6, 8, 9, 11)) == (8, 14, 17, 20)
    assert candidate((3, 7, 9, 10, 12)) == (10, 16, 19, 22)

if __name__ == '__main__':
    check(add_pairwise)