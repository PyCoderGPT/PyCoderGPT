from case_HE_046 import fib4


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


if __name__ == '__main__':
    check(fib4)