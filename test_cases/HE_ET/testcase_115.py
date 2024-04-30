from case_HE_115 import max_fill


def check(candidate):
    assert candidate([[1, 1, 5, 2], [4, 2, 4, 3], [1, 2, 5, 2]], 2) == 17
    assert candidate([[4, 3, 4], [3, 1, 5]], 2) == 11
    assert candidate([[4, 3, 4], [1, 2, 5]], 4) == 5
    assert candidate([[5, 2, 2, 4], [1, 3, 3, 4], [5, 3, 5, 5], [4, 5, 1, 1]], 1) == 53
    assert candidate([[3, 3, 3], [5, 4, 5]], 4) == 7
    assert candidate([[3, 2, 1, 5], [6, 3, 3, 2]], 3) == 9
    assert candidate([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5, "Error"
    assert candidate([[3, 1, 5, 6], [4, 5, 4, 3], [1, 1, 4, 4], [2, 1, 2, 6]], 7) == 10
    assert candidate([[5, 2, 2, 1], [5, 2, 1, 1], [3, 5, 4, 6], [1, 6, 6, 4]], 7) == 10
    assert candidate([[4, 4, 3, 6], [4, 4, 6, 6]], 5) == 8
    assert candidate([[5, 2, 6, 4], [1, 2, 2, 2], [2, 1, 1, 2]], 5) == 8
    assert candidate([[2, 3, 5], [4, 4, 3]], 3) == 8
    assert candidate([[2, 3, 1], [1, 4, 3]], 2) == 7
    assert candidate([[1, 4, 1, 1], [1, 2, 3, 5], [5, 4, 6, 5], [5, 1, 5, 3]], 5) == 12
    assert candidate([[3, 5, 1, 5], [4, 4, 1, 5], [1, 4, 5, 6]], 6) == 9
    assert candidate([[1, 6, 5, 2], [4, 5, 6, 1]], 8) == 4
    assert candidate([[5, 3, 6, 6], [4, 6, 4, 5]], 11) == 4
    assert candidate([[2, 1, 1, 1], [2, 1, 1, 2], [3, 5, 2, 5]], 3) == 9
    assert candidate([[3, 6, 1, 5], [1, 2, 5, 3]], 7) == 5
    assert candidate([[3, 1, 2, 4], [3, 1, 1, 6]], 3) == 8
    assert candidate([[2, 5, 2, 4], [1, 4, 2, 1], [3, 1, 6, 4], [3, 4, 2, 3]], 6) == 10
    assert candidate([[5, 1, 1], [2, 5, 5]], 2) == 10
    assert candidate([[1, 1, 5, 6], [4, 1, 3, 5], [3, 4, 6, 1], [3, 2, 5, 5]], 3) == 20
    assert candidate([[4, 5, 1, 5], [3, 2, 2, 3], [5, 3, 4, 2]], 4) == 11
    assert candidate([[5, 5, 3, 2], [3, 2, 2, 4], [5, 3, 1, 1]], 1) == 36
    assert candidate([[3, 4, 4, 2], [2, 4, 4, 5], [5, 3, 2, 4]], 5) == 9
    assert candidate([[4, 3, 2, 1], [1, 2, 5, 2]], 6) == 4
    assert candidate([[5, 5, 3], [4, 3, 1]], 4) == 6
    assert candidate([[5, 6, 4, 6], [1, 6, 2, 1]], 7) == 5
    assert candidate([[2, 3, 1, 4], [5, 6, 2, 4], [1, 5, 4, 5]], 1) == 42
    assert candidate([[1, 5, 4], [3, 3, 3]], 6) == 4
    assert candidate([[1, 6, 4, 2], [1, 3, 2, 6]], 7) == 4
    assert candidate([[2, 1, 2, 5], [4, 3, 2, 5], [6, 5, 5, 6], [2, 5, 5, 1]], 2) == 30
    assert candidate([[5, 4, 2], [3, 5, 1]], 7) == 4
    assert candidate([[3, 2, 3], [5, 1, 2]], 7) == 4
    assert candidate([[2, 5, 2, 6], [4, 1, 1, 1]], 8) == 3
    assert candidate([[2, 5, 6, 1], [2, 4, 5, 5]], 5) == 7
    assert candidate([[2, 2, 1, 1], [4, 1, 2, 4]], 8) == 3
    assert candidate([[3, 4, 5, 6], [4, 5, 3, 2], [5, 3, 1, 1], [5, 6, 6, 5]], 2) == 32
    assert candidate([[5, 2, 6, 2], [3, 1, 5, 2], [1, 1, 5, 6]], 1) == 39
    assert candidate([[2, 5, 5, 1], [5, 6, 4, 1]], 4) == 8
    assert candidate([[4, 5, 1, 3], [2, 4, 1, 5], [4, 6, 5, 5]], 1) == 45
    assert candidate([[1, 4, 6, 4], [5, 4, 2, 3], [5, 6, 4, 2]], 5) == 10
    assert candidate([[4, 4, 6, 3], [3, 3, 2, 4], [3, 3, 6, 4], [4, 1, 1, 2]], 1) == 53
    assert candidate([[6, 3, 3, 1], [4, 3, 6, 2]], 3) == 10
    assert candidate([[1, 2, 6, 3], [5, 5, 6, 3]], 1) == 31
    assert candidate([[6, 3, 3, 6], [5, 4, 6, 5]], 6) == 7
    assert candidate([[5, 2, 1], [5, 5, 4]], 8) == 3
    assert candidate([[1,1,1,1], [1,1,1,1]], 2) == 4, "Error"
    assert candidate([[1, 5, 2, 4], [2, 4, 4, 2]], 7) == 4
    assert candidate([[5, 3, 2], [4, 4, 4]], 7) == 4
    assert candidate([[4, 1, 5, 5], [2, 3, 4, 2], [3, 3, 5, 2], [2, 1, 3, 4]], 1) == 49
    assert candidate([[3, 2, 5, 1], [3, 2, 2, 5], [4, 3, 1, 3], [3, 1, 4, 5]], 3) == 17
    assert candidate([[5, 4, 2, 4], [5, 2, 2, 1]], 11) == 3
    assert candidate([[6, 6, 3, 3], [2, 4, 6, 6]], 13) == 4
    assert candidate([[3, 3, 5, 2], [2, 4, 5, 5]], 6) == 6
    assert candidate([[3, 1, 3, 1], [4, 4, 2, 2], [5, 6, 6, 1]], 2) == 19
    assert candidate([[5, 2, 3, 2], [6, 6, 5, 3]], 7) == 5
    assert candidate([[1, 2, 2, 1], [2, 3, 2, 1]], 5) == 4
    assert candidate([[1, 1, 5, 4], [5, 6, 5, 2]], 1) == 29
    assert candidate([[4, 3, 1, 2], [3, 4, 1, 3], [1, 1, 2, 4], [5, 2, 6, 3]], 7) == 9
    assert candidate([[2, 6, 5, 4], [5, 5, 6, 5]], 7) == 6
    assert candidate([[4, 1, 2, 5], [3, 4, 4, 3], [6, 5, 2, 3], [5, 2, 6, 5]], 3) == 21
    assert candidate([[1, 2, 3, 3], [3, 3, 6, 4]], 7) == 5
    assert candidate([[1, 6, 4, 2], [2, 4, 5, 5]], 1) == 29
    assert candidate([[4, 1, 2, 4], [5, 2, 1, 5], [5, 6, 5, 1], [3, 3, 4, 4]], 7) == 9
    assert candidate([[6, 4, 3, 3], [5, 3, 3, 4]], 7) == 6
    assert candidate([[4, 3, 4], [3, 1, 1]], 9) == 3
    assert candidate([[4, 3, 1], [5, 5, 1]], 7) == 4
    assert candidate([[2, 2, 3, 3], [3, 3, 5, 4], [3, 6, 2, 4], [4, 4, 4, 5]], 4) == 16
    assert candidate([[5, 4, 1], [3, 1, 4]], 1) == 18
    assert candidate([[1, 5, 1, 5], [1, 3, 5, 3], [6, 2, 3, 4]], 2) == 20
    assert candidate([[1,1,1,1], [1,1,1,1]], 9) == 2, "Error"
    assert candidate([[2, 4, 5], [5, 3, 5]], 3) == 9
    assert candidate([[1, 5, 4, 1], [2, 2, 4, 1], [6, 1, 6, 5]], 5) == 9
    assert candidate([[1, 1, 5, 2], [5, 2, 1, 5]], 4) == 7
    assert candidate([[1, 6, 6, 3], [5, 1, 5, 2]], 4) == 8
    assert candidate([[6, 5, 6, 6], [2, 3, 3, 6]], 7) == 6
    assert candidate([[3, 3, 2, 3], [4, 1, 3, 3]], 3) == 8
    assert candidate([[1, 1, 5, 1], [3, 1, 2, 4], [1, 1, 1, 3], [3, 1, 5, 1]], 5) == 8
    assert candidate([[4, 1, 5, 2], [1, 6, 4, 5]], 1) == 28
    assert candidate([[5, 4, 6, 2], [2, 2, 2, 6]], 6) == 5
    assert candidate([[4, 4, 4, 1], [4, 1, 3, 5]], 11) == 4
    assert candidate([[4, 1, 1, 5], [3, 2, 3, 3]], 11) == 2
    assert candidate([[3, 5, 3, 3], [2, 2, 4, 1], [6, 3, 3, 5]], 3) == 14
    assert candidate([[2, 4, 1, 2], [2, 5, 3, 1], [1, 4, 6, 2], [2, 5, 3, 5]], 6) == 10
    assert candidate([[4, 2, 3, 1], [3, 6, 1, 1], [1, 3, 5, 5]], 3) == 13
    assert candidate([[5, 2, 4], [2, 1, 4]], 3) == 7
    assert candidate([[5, 1, 2, 5], [4, 1, 3, 4]], 5) == 6
    assert candidate([[4, 2, 2, 4], [2, 2, 1, 1], [3, 5, 2, 5]], 1) == 33
    assert candidate([[4, 1, 5], [3, 4, 1]], 5) == 4
    assert candidate([[5, 4, 3, 4], [6, 6, 3, 1]], 5) == 8
    assert candidate([[2, 4, 4, 4], [2, 6, 4, 2]], 7) == 4
    assert candidate([[5, 4, 4, 1], [2, 4, 1, 1], [6, 1, 3, 3], [2, 2, 2, 3]], 2) == 23
    assert candidate([[5, 4, 1, 1], [1, 3, 1, 4], [6, 2, 2, 5], [5, 3, 1, 5]], 3) == 17
    assert candidate([[2, 2, 6, 4], [5, 2, 1, 5], [5, 4, 5, 1]], 1) == 42
    assert candidate([[6, 1, 4, 4], [6, 5, 2, 1]], 12) == 4
    assert candidate([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6, "Error"
    assert candidate([[5, 1, 3, 4], [1, 2, 4, 2], [2, 5, 1, 1], [5, 5, 1, 5]], 4) == 14
    assert candidate([[1, 4, 5, 3], [3, 5, 4, 5], [1, 6, 6, 5]], 5) == 11
    assert candidate([[5, 1, 2, 4], [5, 1, 1, 5], [4, 3, 6, 2]], 1) == 39
    assert candidate([[4, 5, 5, 5], [3, 5, 1, 4], [1, 2, 6, 3], [2, 3, 4, 5]], 7) == 9
    assert candidate([[4, 4, 2], [3, 2, 4]], 4) == 6
    assert candidate([[4, 1, 1], [4, 2, 3]], 6) == 3
    assert candidate([[5, 4, 4, 4], [1, 2, 4, 3]], 13) == 3
    assert candidate([[4, 1, 1, 3], [1, 2, 2, 1], [1, 3, 5, 2], [3, 2, 3, 2]], 2) == 19
    assert candidate([[4, 4, 1], [2, 1, 3]], 8) == 3
    assert candidate([[3, 6, 4, 1], [2, 6, 3, 1]], 3) == 9
    assert candidate([[2, 3, 4], [2, 1, 1]], 9) == 2
    assert candidate([[5, 4, 6, 6], [4, 6, 4, 6]], 10) == 5
    assert candidate([[1, 1, 2, 6], [3, 4, 2, 2], [3, 2, 6, 4], [4, 1, 3, 4]], 5) == 11
    assert candidate([[5, 5, 3, 3], [2, 1, 6, 6]], 8) == 4
    assert candidate([[3, 1, 4], [5, 3, 2]], 10) == 2
    assert candidate([[5, 2, 6, 2], [2, 1, 1, 6]], 3) == 9
    assert candidate([[1, 3, 2, 4], [4, 2, 5, 5], [2, 2, 5, 6]], 2) == 21
    assert candidate([[5, 6, 3, 6], [5, 1, 4, 3]], 8) == 5
    assert candidate([[4, 3, 3, 4], [5, 6, 1, 5]], 6) == 6
    assert candidate([[4, 1, 3, 6], [4, 5, 2, 2], [3, 5, 3, 4], [5, 1, 5, 5]], 3) == 21
    assert candidate([[3, 5, 4, 3], [4, 3, 1, 5], [5, 3, 4, 2]], 4) == 12
    assert candidate([[1, 3, 5, 4], [5, 1, 1, 4], [2, 2, 2, 5], [4, 5, 6, 2]], 2) == 28
    assert candidate([[4, 4, 5, 1], [5, 5, 1, 2], [1, 1, 6, 1]], 1) == 36
    assert candidate([[3, 3, 4, 4], [1, 3, 4, 5]], 14) == 2
    assert candidate([[0,0,0], [0,0,0]], 5) == 0, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([[2, 3, 6, 3], [3, 5, 1, 2]], 3) == 9
    assert candidate([[4, 4, 3, 3], [1, 6, 4, 2], [1, 1, 6, 3]], 1) == 38
    assert candidate([[5, 2, 5], [2, 3, 3]], 2) == 10
    assert candidate([[2, 4, 1, 6], [1, 2, 1, 6]], 8) == 4
    assert candidate([[2, 5, 2, 4], [5, 4, 1, 2], [6, 5, 5, 4]], 3) == 16
    assert candidate([[5, 4, 6, 3], [1, 1, 3, 5]], 4) == 8
    assert candidate([[4, 1, 1], [3, 3, 4]], 7) == 3

if __name__ == '__main__':
    check(max_fill)