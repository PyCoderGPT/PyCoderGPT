from case_MBPP_328 import triangle_area


def check(candidate):
    assert candidate(0) == 0
    assert candidate(-1) == -1
    assert candidate(2) == 4
    assert candidate(1) == 1
    assert candidate(5) == 25
    assert candidate(3) == 9
    assert candidate(2) == 4
    assert candidate(2) == 4
    assert candidate(5) == 25
    assert candidate(2) == 4
    assert candidate(4) == 16
    assert candidate(3) == 9
    assert candidate(3) == 9
    assert candidate(5) == 25
    assert candidate(5) == 25
    assert candidate(3) == 9
    assert candidate(1) == 1
    assert candidate(4) == 16
    assert candidate(3) == 9
    assert candidate(5) == 25
    assert candidate(1) == 1
    assert candidate(2) == 4
    assert candidate(4) == 16
    assert candidate(3) == 9
    assert candidate(2) == 4
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(5) == 25
    assert candidate(3) == 9
    assert candidate(2) == 4
    assert candidate(4) == 16
    assert candidate(2) == 4
    assert candidate(1) == 1
    assert candidate(1) == 1
    assert candidate(4) == 16
    assert candidate(-2) == -1
    assert candidate(2) == 4
    assert candidate(1) == 1
    assert candidate(-4) == -1
    assert candidate(-1) == -1
    assert candidate(3) == 9
    assert candidate(3) == 9
    assert candidate(-6) == -1
    assert candidate(0) == 0
    assert candidate(-4) == -1
    assert candidate(4) == 16
    assert candidate(-5) == -1
    assert candidate(0) == 0
    assert candidate(1) == 1
    assert candidate(-6) == -1
    assert candidate(-1) == -1
    assert candidate(4) == 16
    assert candidate(0) == 0
    assert candidate(-6) == -1
    assert candidate(4) == 16
    assert candidate(4) == 16
    assert candidate(-3) == -1
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(3) == 9
    assert candidate(-1) == -1
    assert candidate(-2) == -1
    assert candidate(-4) == -1
    assert candidate(0) == 0
    assert candidate(-6) == -1
    assert candidate(-5) == -1
    assert candidate(1) == 1
    assert candidate(4) == 16
    assert candidate(1) == 1
    assert candidate(6) == 36
    assert candidate(3) == 9
    assert candidate(2) == 4
    assert candidate(1) == 1
    assert candidate(1) == 1
    assert candidate(5) == 25
    assert candidate(1) == 1
    assert candidate(4) == 16
    assert candidate(3) == 9
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(1) == 1
    assert candidate(6) == 36
    assert candidate(4) == 16
    assert candidate(4) == 16
    assert candidate(5) == 25
    assert candidate(2) == 4
    assert candidate(2) == 4
    assert candidate(7) == 49
    assert candidate(7) == 49
    assert candidate(1) == 1
    assert candidate(7) == 49
    assert candidate(4) == 16
    assert candidate(1) == 1
    assert candidate(2) == 4
    assert candidate(5) == 25
    assert candidate(5) == 25
    assert candidate(2) == 4
    assert candidate(4) == 16
    assert candidate(4) == 16

if __name__ == '__main__':
    check(triangle_area)