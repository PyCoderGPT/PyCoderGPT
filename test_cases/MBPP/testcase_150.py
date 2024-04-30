from case_MBPP_150 import count_first_elements


def check(candidate):
    assert candidate((1, 5, 7, (4, 6), 10) ) == 3
    assert candidate((2, 9, (5, 7), 11) ) == 2
    assert candidate((11, 15, 5, 8, (2, 3), 8) ) == 4

if __name__ == '__main__':
    check(count_first_elements)