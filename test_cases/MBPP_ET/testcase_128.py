from case_MBPP_128 import convert


def check(candidate):
    assert candidate(1) == (1.0, 0.0)
    assert candidate(4) == (4.0,0.0)
    assert candidate(5) == (5.0,0.0)
    assert candidate(1) == (1.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(4) == (4.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(4) == (4.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(1) == (1.0, 0.0)
    assert candidate(1) == (1.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(6) == (6.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(6) == (6.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(1) == (1.0, 0.0)
    assert candidate(1) == (1.0, 0.0)
    assert candidate(6) == (6.0, 0.0)
    assert candidate(4) == (4.0, 0.0)
    assert candidate(1) == (1.0, 0.0)
    assert candidate(1) == (1.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(7) == (7.0, 0.0)
    assert candidate(6) == (6.0, 0.0)
    assert candidate(8) == (8.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(9) == (9.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(6) == (6.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(7) == (7.0, 0.0)
    assert candidate(9) == (9.0, 0.0)
    assert candidate(9) == (9.0, 0.0)
    assert candidate(8) == (8.0, 0.0)
    assert candidate(7) == (7.0, 0.0)
    assert candidate(1) == (1.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(4) == (4.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(9) == (9.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(6) == (6.0, 0.0)
    assert candidate(8) == (8.0, 0.0)
    assert candidate(8) == (8.0, 0.0)
    assert candidate(4) == (4.0, 0.0)
    assert candidate(4) == (4.0, 0.0)
    assert candidate(1) == (1.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(7) == (7.0, 0.0)
    assert candidate(9) == (9.0, 0.0)
    assert candidate(8) == (8.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(4) == (4.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(6) == (6.0, 0.0)
    assert candidate(1) == (1.0, 0.0)
    assert candidate(4) == (4.0, 0.0)
    assert candidate(7) == (7.0, 0.0)
    assert candidate(10) == (10.0, 0.0)
    assert candidate(2) == (2.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(6) == (6.0, 0.0)
    assert candidate(1) == (1.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(8) == (8.0, 0.0)
    assert candidate(10) == (10.0, 0.0)
    assert candidate(7) == (7.0, 0.0)
    assert candidate(9) == (9.0, 0.0)
    assert candidate(10) == (10.0, 0.0)
    assert candidate(10) == (10.0, 0.0)
    assert candidate(6) == (6.0, 0.0)
    assert candidate(9) == (9.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(4) == (4.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(9) == (9.0, 0.0)
    assert candidate(8) == (8.0, 0.0)
    assert candidate(9) == (9.0, 0.0)
    assert candidate(5) == (5.0, 0.0)
    assert candidate(3) == (3.0, 0.0)
    assert candidate(4) == (4.0, 0.0)
    assert candidate(7) == (7.0, 0.0)
    assert candidate(7) == (7.0, 0.0)

if __name__ == '__main__':
    check(convert)