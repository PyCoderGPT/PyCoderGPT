from case_MBPP_245 import rectangle_area


def check(candidate):
    assert candidate(10,20)==200
    assert candidate(10,5)==50
    assert candidate(4,2)==8

if __name__ == '__main__':
    check(rectangle_area)