from case_MBPP_336 import heap_sort


def check(candidate):
    assert candidate([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate([25, 35, 22, 85, 14, 65, 75, 25, 58])==[14, 22, 25, 25, 35, 58, 65, 75, 85]
    assert candidate( [7, 1, 9, 5])==[1,5,7,9]

if __name__ == '__main__':
    check(heap_sort)