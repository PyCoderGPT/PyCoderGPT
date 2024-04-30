from case_MBPP_416 import left_rotate


def check(candidate):
    assert candidate(16,2) == 64
    assert candidate(10,2) == 40
    assert candidate(99,3) == 792
    assert candidate(99,3) == 792
    assert candidate(0b0001,3) == 0b1000
    assert candidate(0b0101,3) == 0b101000
    assert candidate(0b11101,3) == 0b11101000

if __name__ == '__main__':
    check(left_rotate)