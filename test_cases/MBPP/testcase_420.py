from case_MBPP_420 import is_perfect_square


def check(candidate):
    assert not candidate(10)
    assert candidate(36)
    assert not candidate(14)
    assert candidate(14*14)
    assert not candidate(125)
    assert candidate(125*125)

if __name__ == '__main__':
    check(is_perfect_square)