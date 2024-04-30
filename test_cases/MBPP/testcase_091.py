from case_MBPP_091 import find_solution


def check(candidate):
    assert candidate(2, 3, 7) == (2, 1)
    assert candidate(4, 2, 7) == None
    assert candidate(1, 13, 17) == (4, 1)

if __name__ == '__main__':
    check(find_solution)