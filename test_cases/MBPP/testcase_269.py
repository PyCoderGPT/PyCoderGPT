from case_MBPP_269 import max_sub_array_sum


def check(candidate):
    assert candidate([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert candidate([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
    assert candidate([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10

if __name__ == '__main__':
    check(max_sub_array_sum)