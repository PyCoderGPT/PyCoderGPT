from case_MBPP_350 import multiply_elements


def check(candidate):
    assert candidate((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
    assert candidate((2, 4, 5, 6, 7)) == (8, 20, 30, 42)
    assert candidate((12, 13, 14, 9, 15)) == (156, 182, 126, 135)
    assert candidate((12,)) == ()

if __name__ == '__main__':
    check(multiply_elements)