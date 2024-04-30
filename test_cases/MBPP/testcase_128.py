from case_MBPP_128 import convert


def check(candidate):
    assert candidate(1) == (1.0, 0.0)
    assert candidate(4) == (4.0,0.0)
    assert candidate(5) == (5.0,0.0)

if __name__ == '__main__':
    check(convert)