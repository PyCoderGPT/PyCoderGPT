from case_HE_083 import starts_one_ends


def check(candidate):
    assert candidate(12) == 180000000000
    assert candidate(2) == 18
    assert candidate(14) == 18000000000000
    assert candidate(3) == 180
    assert candidate(19) == 1800000000000000000
    assert candidate(1) == 1
    assert candidate(8) == 18000000
    assert candidate(13) == 1800000000000
    assert candidate(16) == 1800000000000000
    assert candidate(11) == 18000000000
    assert candidate(17) == 18000000000000000
    assert candidate(4) == 1800
    assert candidate(20) == 18000000000000000000
    assert candidate(9) == 180000000
    assert candidate(6) == 180000
    assert candidate(15) == 180000000000000
    assert candidate(5) == 18000
    assert candidate(18) == 180000000000000000
    assert candidate(5) == 18000

    # Check some edge cases that are easy to work out by hand.
    assert candidate(7) == 1800000
    assert candidate(10) == 1800000000

if __name__ == '__main__':
    check(starts_one_ends)