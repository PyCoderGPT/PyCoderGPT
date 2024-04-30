from case_MBPP_054 import next_smallest_palindrome


def check(candidate):
    assert candidate(99)==101
    assert candidate(1221)==1331
    assert candidate(120)==121

if __name__ == '__main__':
    check(next_smallest_palindrome)