from case_HE_055 import fib


def check(candidate):
    assert candidate(29) == 514229
    assert candidate(25) == 75025
    assert candidate(34) == 5702887
    assert candidate(7) == 13
    assert candidate(32) == 2178309
    assert candidate(27) == 196418
    assert candidate(16) == 987
    assert candidate(14) == 377
    assert candidate(33) == 3524578
    assert candidate(20) == 6765
    assert candidate(8) == 21
    assert candidate(31) == 1346269
    assert candidate(6) == 8
    assert candidate(17) == 1597
    assert candidate(2) == 1
    assert candidate(1) == 1
    assert candidate(30) == 832040
    assert candidate(11) == 89
    assert candidate(3) == 2
    assert candidate(19) == 4181
    assert candidate(21) == 10946
    assert candidate(4) == 3
    assert candidate(10) == 55
    assert candidate(12) == 144
    assert candidate(9) == 34
    assert candidate(13) == 233
    assert candidate(0) == 0
    assert candidate(15) == 610
    assert candidate(22) == 17711
    assert candidate(24) == 46368
    assert candidate(18) == 2584
    assert candidate(28) == 317811
    assert candidate(35) == 9227465

if __name__ == '__main__':
    check(fib)