from case_MBPP_075 import multiply_int


def check(candidate):
    assert candidate(10,20)==200
    assert candidate(5,10)==50
    assert candidate(4,8)==32

if __name__ == '__main__':
    check(multiply_int)