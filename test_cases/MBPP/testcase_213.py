from case_MBPP_213 import count_element_in_list


def check(candidate):
    assert candidate([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
    assert candidate([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A')==3
    assert candidate([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'E')==1

if __name__ == '__main__':
    check(count_element_in_list)