from case_MBPP_317 import cummulative_sum


def check(candidate):
    assert candidate([(1, 3), (5, 6, 7), (2, 6)]) == 30
    assert candidate([(2, 4), (6, 7, 8), (3, 7)]) == 37
    assert candidate([(3, 5), (7, 8, 9), (4, 8)]) == 44
    assert candidate([(3, 7), (8, 7, 4), (6, 7)]) == 42
    assert candidate([(6, 5), (3, 9, 3), (6, 10)]) == 42
    assert candidate([(3, 5), (8, 4, 9), (3, 6)]) == 38
    assert candidate([(4, 8), (2, 4, 5), (5, 6)]) == 34
    assert candidate([(4, 3), (8, 7, 4), (4, 5)]) == 35
    assert candidate([(2, 5), (10, 10, 4), (6, 1)]) == 38
    assert candidate([(5, 3), (9, 1, 2), (2, 2)]) == 24
    assert candidate([(1, 8), (10, 3, 8), (7, 3)]) == 40
    assert candidate([(5, 5), (7, 10, 7), (1, 1)]) == 36
    assert candidate([(5, 6), (3, 3, 7), (3, 5)]) == 32
    assert candidate([(1, 4), (2, 10, 6), (5, 7)]) == 35
    assert candidate([(6, 2), (5, 9, 11), (7, 6)]) == 46
    assert candidate([(3, 3), (2, 8, 3), (3, 7)]) == 29
    assert candidate([(5, 6), (3, 10, 11), (6, 4)]) == 45
    assert candidate([(2, 4), (8, 2, 9), (6, 6)]) == 37
    assert candidate([(4, 2), (9, 3, 3), (3, 4)]) == 28
    assert candidate([(6, 4), (4, 9, 9), (3, 5)]) == 40
    assert candidate([(1, 3), (8, 2, 2), (7, 5)]) == 28
    assert candidate([(1, 2), (2, 7, 2), (2, 8)]) == 24
    assert candidate([(6, 6), (8, 2, 10), (2, 4)]) == 38
    assert candidate([(3, 4), (4, 2, 12), (1, 7)]) == 33
    assert candidate([(1, 3), (10, 6, 7), (5, 9)]) == 41
    assert candidate([(6, 8), (5, 6, 7), (4, 9)]) == 45
    assert candidate([(1, 2), (6, 1, 5), (2, 2)]) == 19
    assert candidate([(1, 1), (8, 1, 10), (1, 11)]) == 33
    assert candidate([(3, 3), (4, 9, 12), (5, 5)]) == 41
    assert candidate([(2, 4), (6, 2, 11), (3, 9)]) == 37
    assert candidate([(4, 5), (7, 6, 8), (7, 10)]) == 47
    assert candidate([(6, 4), (9, 1, 8), (4, 8)]) == 40
    assert candidate([(3, 1), (9, 3, 9), (1, 4)]) == 30
    assert candidate([(3, 8), (2, 6, 5), (1, 4)]) == 29
    assert candidate([(1, 4), (6, 5, 6), (2, 5)]) == 29
    assert candidate([(1, 2), (7, 3, 3), (7, 10)]) == 33
    assert candidate([(5, 3), (7, 2, 12), (7, 11)]) == 47
    assert candidate([(3, 5), (7, 4, 8), (2, 3)]) == 32
    assert candidate([(7, 3), (11, 10, 7), (3, 3)]) == 44
    assert candidate([(2, 6), (6, 12, 12), (3, 5)]) == 46
    assert candidate([(2, 9), (11, 7, 3), (6, 10)]) == 48
    assert candidate([(7, 5), (8, 5, 6), (3, 8)]) == 42
    assert candidate([(3, 7), (1, 3, 5), (2, 6)]) == 27
    assert candidate([(7, 8), (9, 10, 3), (5, 9)]) == 51
    assert candidate([(7, 3), (8, 7, 11), (1, 3)]) == 40
    assert candidate([(2, 2), (5, 10, 7), (8, 10)]) == 44
    assert candidate([(1, 3), (4, 9, 9), (7, 3)]) == 36
    assert candidate([(1, 9), (6, 2, 13), (6, 6)]) == 43
    assert candidate([(2, 7), (6, 9, 12), (3, 4)]) == 43
    assert candidate([(5, 8), (4, 8, 9), (7, 9)]) == 50
    assert candidate([(7, 5), (10, 11, 4), (4, 12)]) == 53
    assert candidate([(5, 6), (7, 9, 13), (4, 4)]) == 48
    assert candidate([(5, 5), (9, 10, 12), (4, 5)]) == 50
    assert candidate([(7, 7), (10, 4, 4), (6, 2)]) == 40
    assert candidate([(6, 9), (9, 7, 3), (2, 9)]) == 45
    assert candidate([(1, 7), (11, 10, 9), (2, 3)]) == 43
    assert candidate([(6, 9), (9, 10, 6), (8, 7)]) == 55
    assert candidate([(1, 5), (8, 11, 3), (1, 7)]) == 36
    assert candidate([(3, 9), (7, 11, 5), (8, 5)]) == 48
    assert candidate([(1, 4), (11, 10, 12), (6, 7)]) == 51
    assert candidate([(6, 5), (10, 8, 3), (2, 7)]) == 41
    assert candidate([(4, 4), (5, 11, 10), (3, 6)]) == 43
    assert candidate([(4, 7), (2, 12, 6), (3, 8)]) == 42
    assert candidate([(2, 1), (6, 6, 13), (6, 5)]) == 39
    assert candidate([(7, 6), (10, 3, 8), (3, 6)]) == 43
    assert candidate([(4, 7), (5, 2, 8), (8, 12)]) == 46
    assert candidate([(3, 1), (5, 4, 3), (7, 11)]) == 34
    assert candidate([(5, 8), (9, 5, 3), (5, 12)]) == 47
    assert candidate([(1, 7), (1, 10, 5), (5, 10)]) == 39
    assert candidate([(7, 2), (11, 9, 13), (2, 4)]) == 48
    assert candidate([(1, 8), (10, 9, 14), (2, 6)]) == 50
    assert candidate([(5, 7), (5, 12, 10), (6, 3)]) == 48
    assert candidate([(1, 8), (10, 13, 10), (2, 9)]) == 53
    assert candidate([(7, 4), (6, 4, 4), (4, 7)]) == 36
    assert candidate([(6, 2), (7, 5, 13), (1, 8)]) == 42
    assert candidate([(1, 6), (2, 12, 13), (3, 8)]) == 45
    assert candidate([(2, 8), (8, 12, 7), (7, 8)]) == 52
    assert candidate([(3, 9), (2, 4, 9), (8, 12)]) == 47
    assert candidate([(3, 2), (7, 9, 7), (3, 7)]) == 38
    assert candidate([(3, 2), (6, 9, 12), (5, 11)]) == 48
    assert candidate([(4, 3), (11, 7, 11), (6, 12)]) == 54
    assert candidate([(6, 6), (5, 7, 11), (1, 8)]) == 44
    assert candidate([(4, 10), (9, 13, 10), (5, 7)]) == 58
    assert candidate([(1, 7), (2, 4, 4), (3, 13)]) == 34
    assert candidate([(4, 3), (2, 5, 6), (8, 12)]) == 40
    assert candidate([(8, 7), (11, 11, 11), (7, 9)]) == 64
    assert candidate([(5, 7), (3, 10, 12), (4, 6)]) == 47
    assert candidate([(2, 8), (6, 11, 5), (7, 12)]) == 51
    assert candidate([(3, 4), (5, 3, 12), (9, 13)]) == 49
    assert candidate([(7, 2), (6, 8, 8), (1, 12)]) == 44
    assert candidate([(2, 1), (9, 5, 14), (1, 10)]) == 42
    assert candidate([(6, 7), (7, 3, 4), (2, 5)]) == 34
    assert candidate([(8, 1), (8, 10, 7), (2, 7)]) == 43
    assert candidate([(3, 6), (7, 10, 12), (9, 8)]) == 55
    assert candidate([(8, 7), (12, 12, 11), (7, 5)]) == 62
    assert candidate([(2, 5), (2, 3, 5), (6, 12)]) == 35
    assert candidate([(4, 1), (10, 11, 4), (3, 6)]) == 39
    assert candidate([(3, 2), (10, 9, 9), (1, 6)]) == 40
    assert candidate([(2, 7), (2, 7, 11), (7, 6)]) == 42
    assert candidate([(3, 2), (5, 5, 8), (6, 5)]) == 34
    assert candidate([(4, 6), (2, 9, 8), (2, 5)]) == 36
    assert candidate([(2, 7), (8, 6, 7), (5, 13)]) == 48

if __name__ == '__main__':
    check(cummulative_sum)