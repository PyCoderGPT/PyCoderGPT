from case_MBPP_313 import bell_Number


def check(candidate):
    assert candidate(2) == 2
    assert candidate(3) == 5
    assert candidate(4) == 15
    assert candidate(2) == 2
    assert candidate(4) == 15
    assert candidate(7) == 877
    assert candidate(5) == 52
    assert candidate(3) == 5
    assert candidate(3) == 5
    assert candidate(3) == 5
    assert candidate(6) == 203
    assert candidate(6) == 203
    assert candidate(2) == 2
    assert candidate(1) == 1
    assert candidate(4) == 15
    assert candidate(1) == 1
    assert candidate(5) == 52
    assert candidate(6) == 203
    assert candidate(5) == 52
    assert candidate(5) == 52
    assert candidate(2) == 2
    assert candidate(2) == 2
    assert candidate(1) == 1
    assert candidate(7) == 877
    assert candidate(1) == 1
    assert candidate(7) == 877
    assert candidate(1) == 1
    assert candidate(3) == 5
    assert candidate(7) == 877
    assert candidate(6) == 203
    assert candidate(3) == 5
    assert candidate(1) == 1
    assert candidate(4) == 15
    assert candidate(4) == 15
    assert candidate(4) == 15
    assert candidate(4) == 15
    assert candidate(6) == 203
    assert candidate(7) == 877
    assert candidate(5) == 52
    assert candidate(7) == 877
    assert candidate(4) == 15
    assert candidate(4) == 15
    assert candidate(3) == 5
    assert candidate(5) == 52
    assert candidate(3) == 5
    assert candidate(8) == 4140
    assert candidate(4) == 15
    assert candidate(6) == 203
    assert candidate(6) == 203
    assert candidate(6) == 203
    assert candidate(2) == 2
    assert candidate(4) == 15
    assert candidate(1) == 1
    assert candidate(7) == 877
    assert candidate(5) == 52
    assert candidate(3) == 5
    assert candidate(7) == 877
    assert candidate(2) == 2
    assert candidate(5) == 52
    assert candidate(6) == 203
    assert candidate(5) == 52
    assert candidate(3) == 5
    assert candidate(8) == 4140
    assert candidate(1) == 1
    assert candidate(2) == 2
    assert candidate(2) == 2
    assert candidate(5) == 52
    assert candidate(5) == 52
    assert candidate(1) == 1
    assert candidate(2) == 2
    assert candidate(7) == 877
    assert candidate(3) == 5
    assert candidate(2) == 2
    assert candidate(6) == 203
    assert candidate(5) == 52
    assert candidate(5) == 52
    assert candidate(5) == 52
    assert candidate(8) == 4140
    assert candidate(5) == 52
    assert candidate(9) == 21147
    assert candidate(9) == 21147
    assert candidate(8) == 4140
    assert candidate(7) == 877
    assert candidate(9) == 21147
    assert candidate(6) == 203
    assert candidate(2) == 2
    assert candidate(4) == 15
    assert candidate(5) == 52
    assert candidate(5) == 52
    assert candidate(1) == 1
    assert candidate(7) == 877
    assert candidate(2) == 2
    assert candidate(3) == 5
    assert candidate(6) == 203
    assert candidate(4) == 15
    assert candidate(6) == 203
    assert candidate(4) == 15
    assert candidate(7) == 877
    assert candidate(1) == 1
    assert candidate(5) == 52
    assert candidate(5) == 52
    assert candidate(9) == 21147

if __name__ == '__main__':
    check(bell_Number)