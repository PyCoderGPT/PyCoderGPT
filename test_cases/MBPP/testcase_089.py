from case_MBPP_089 import find_lists


def check(candidate):
    assert candidate(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
    assert candidate(([1, 2], [3, 4], [5, 6]))  == 3
    assert candidate(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1

if __name__ == '__main__':
    check(find_lists)