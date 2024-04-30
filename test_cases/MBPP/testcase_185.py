from case_MBPP_185 import max_length_list


def check(candidate):
    assert candidate([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
    assert candidate([[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]])==(5,[1,2,3,4,5])
    assert candidate([[3,4,5],[6,7,8,9],[10,11,12]])==(4,[6,7,8,9])

if __name__ == '__main__':
    check(max_length_list)