from case_HE_039 import prime_fib


def check(candidate):
    assert candidate(2) == 3
    assert candidate(12) == 99194853094755497
    assert candidate(6) == 233
    assert candidate(10) == 433494437
    assert candidate(3) == 5
    assert candidate(5) == 89
    assert candidate(8) == 28657
    assert candidate(11) == 2971215073
    assert candidate(1) == 2
    assert candidate(4) == 13
    assert candidate(9) == 514229
    assert candidate(7) == 1597

if __name__ == '__main__':
    check(prime_fib)