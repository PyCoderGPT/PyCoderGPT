from case_MBPP_384 import find_min_diff


def check(candidate):
    assert candidate((1,5,3,19,18,25),6) == 1
    assert candidate((4,3,2,6),4) == 1
    assert candidate((30,5,20,9),4) == 4

if __name__ == '__main__':
    check(find_min_diff)