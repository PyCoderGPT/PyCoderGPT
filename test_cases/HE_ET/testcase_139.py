from case_HE_139 import special_factorial


def check(candidate):
    assert candidate(7) == 125411328000
    assert candidate(9) == 1834933472251084800000
    assert candidate(1) == 1, "Test 1"
    assert candidate(3) == 12
    assert candidate(10) == 6658606584104736522240000000
    assert candidate(12) == 127313963299399416749559771247411200000000000
    assert candidate(4) == 288
    assert candidate(1) == 1
    assert candidate(6) == 24883200
    assert candidate(8) == 5056584744960000
    assert candidate(5) == 34560
    assert candidate(4) == 288, "Test 4"
    assert candidate(2) == 2
    assert candidate(5) == 34560, "Test 5"
    assert candidate(11) == 265790267296391946810949632000000000
    assert candidate(7) == 125411328000, "Test 7"

    # Check some edge cases that are easy to work out by hand.

if __name__ == '__main__':
    check(special_factorial)