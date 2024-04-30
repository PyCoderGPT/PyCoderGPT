from case_MBPP_410 import count_list


def check(candidate):
    assert candidate([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
    assert candidate([[1,2],[2,3],[4,5]]) == 3
    assert candidate([[1,0],[2,0]]) == 2

if __name__ == '__main__':
    check(count_list)