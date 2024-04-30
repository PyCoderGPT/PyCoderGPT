from case_MBPP_066 import tuple_to_int


def check(candidate):
    assert candidate((1,2,3))==123
    assert candidate((4,5,6))==456
    assert candidate((5,6,7))==567

if __name__ == '__main__':
    check(tuple_to_int)