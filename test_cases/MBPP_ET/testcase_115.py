from case_MBPP_115 import check_occurences


def check(candidate):
    assert candidate([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
    assert candidate([(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)] ) == {(2, 4): 2, (3, 6): 2, (4, 7): 1}
    assert candidate([(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)] ) == {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}
    assert candidate([(1, 6), (5, 7), (2, 4), (2, 5), (9, 2)]) == {(1, 6): 1, (5, 7): 1, (2, 4): 1, (2, 5): 1, (2, 9): 1}
    assert candidate([(2, 2), (2, 4), (4, 8), (8, 4), (7, 1)]) == {(2, 2): 1, (2, 4): 1, (4, 8): 2, (1, 7): 1}
    assert candidate([(8, 2), (4, 3), (5, 8), (5, 1), (8, 4)]) == {(2, 8): 1, (3, 4): 1, (5, 8): 1, (1, 5): 1, (4, 8): 1}
    assert candidate([(1, 2), (2, 6), (6, 5), (4, 6), (6, 4)]) == {(1, 2): 1, (2, 6): 1, (5, 6): 1, (4, 6): 2}
    assert candidate([(2, 4), (4, 8), (1, 10), (2, 5), (3, 2)]) == {(2, 4): 1, (4, 8): 1, (1, 10): 1, (2, 5): 1, (2, 3): 1}
    assert candidate([(1, 6), (5, 6), (2, 7), (2, 3), (9, 7)]) == {(1, 6): 1, (5, 6): 1, (2, 7): 1, (2, 3): 1, (7, 9): 1}
    assert candidate([(3, 2), (3, 3), (7, 8), (5, 1), (6, 6)]) == {(2, 3): 1, (3, 3): 1, (7, 8): 1, (1, 5): 1, (6, 6): 1}
    assert candidate([(8, 2), (2, 1), (1, 6), (9, 4), (6, 2)]) == {(2, 8): 1, (1, 2): 1, (1, 6): 1, (4, 9): 1, (2, 6): 1}
    assert candidate([(3, 1), (2, 5), (3, 5), (8, 3), (11, 5)]) == {(1, 3): 1, (2, 5): 1, (3, 5): 1, (3, 8): 1, (5, 11): 1}
    assert candidate([(2, 6), (4, 1), (1, 4), (8, 1), (9, 1)]) == {(2, 6): 1, (1, 4): 2, (1, 8): 1, (1, 9): 1}
    assert candidate([(3, 2), (3, 3), (3, 7), (3, 1), (5, 8)]) == {(2, 3): 1, (3, 3): 1, (3, 7): 1, (1, 3): 1, (5, 8): 1}
    assert candidate([(6, 5), (2, 4), (2, 7), (9, 7), (6, 3)]) == {(5, 6): 1, (2, 4): 1, (2, 7): 1, (7, 9): 1, (3, 6): 1}
    assert candidate([(3, 1), (5, 4), (1, 4), (8, 4), (5, 5)]) == {(1, 3): 1, (4, 5): 1, (1, 4): 1, (4, 8): 1, (5, 5): 1}
    assert candidate([(5, 3), (4, 6), (4, 5), (10, 3), (11, 3)]) == {(3, 5): 1, (4, 6): 1, (4, 5): 1, (3, 10): 1, (3, 11): 1}
    assert candidate([(4, 4), (1, 7), (3, 8), (4, 3), (5, 7)]) == {(4, 4): 1, (1, 7): 1, (3, 8): 1, (3, 4): 1, (5, 7): 1}
    assert candidate([(8, 5), (6, 6), (2, 2), (9, 7), (3, 4)]) == {(5, 8): 1, (6, 6): 1, (2, 2): 1, (7, 9): 1, (3, 4): 1}
    assert candidate([(5, 4), (1, 7), (6, 10), (4, 5), (9, 1)]) == {(4, 5): 2, (1, 7): 1, (6, 10): 1, (1, 9): 1}
    assert candidate([(5, 1), (2, 1), (4, 3), (5, 3), (2, 5)]) == {(1, 5): 1, (1, 2): 1, (3, 4): 1, (3, 5): 1, (2, 5): 1}
    assert candidate([(3, 2), (1, 6), (1, 4), (10, 6), (9, 2)]) == {(2, 3): 1, (1, 6): 1, (1, 4): 1, (6, 10): 1, (2, 9): 1}
    assert candidate([(8, 4), (5, 3), (1, 5), (1, 3), (11, 7)]) == {(4, 8): 1, (3, 5): 1, (1, 5): 1, (1, 3): 1, (7, 11): 1}
    assert candidate([(3, 3), (3, 5), (6, 8), (1, 4), (11, 2)]) == {(3, 3): 1, (3, 5): 1, (6, 8): 1, (1, 4): 1, (2, 11): 1}
    assert candidate([(2, 1), (1, 2), (1, 4), (1, 7), (3, 7)]) == {(1, 2): 2, (1, 4): 1, (1, 7): 1, (3, 7): 1}
    assert candidate([(2, 1), (3, 8), (3, 10), (7, 3), (7, 6)]) == {(1, 2): 1, (3, 8): 1, (3, 10): 1, (3, 7): 1, (6, 7): 1}
    assert candidate([(7, 6), (6, 5), (6, 4), (5, 3), (10, 3)]) == {(6, 7): 1, (5, 6): 1, (4, 6): 1, (3, 5): 1, (3, 10): 1}
    assert candidate([(5, 5), (1, 7), (2, 1), (1, 1), (11, 1)]) == {(5, 5): 1, (1, 7): 1, (1, 2): 1, (1, 1): 1, (1, 11): 1}
    assert candidate([(5, 4), (2, 8), (7, 5), (9, 3), (3, 2)]) == {(4, 5): 1, (2, 8): 1, (5, 7): 1, (3, 9): 1, (2, 3): 1}
    assert candidate([(5, 4), (4, 7), (3, 9), (1, 6), (10, 2)]) == {(4, 5): 1, (4, 7): 1, (3, 9): 1, (1, 6): 1, (2, 10): 1}
    assert candidate([(5, 6), (4, 3), (5, 9), (8, 7), (2, 7)]) == {(5, 6): 1, (3, 4): 1, (5, 9): 1, (7, 8): 1, (2, 7): 1}
    assert candidate([(4, 5), (6, 8), (5, 9), (7, 2), (2, 3)]) == {(4, 5): 1, (6, 8): 1, (5, 9): 1, (2, 7): 1, (2, 3): 1}
    assert candidate([(1, 2), (3, 3), (7, 10), (1, 2), (4, 6)]) == {(1, 2): 2, (3, 3): 1, (7, 10): 1, (4, 6): 1}
    assert candidate([(6, 3), (1, 5), (3, 3), (9, 1), (6, 6)]) == {(3, 6): 1, (1, 5): 1, (3, 3): 1, (1, 9): 1, (6, 6): 1}
    assert candidate([(2, 5), (6, 5), (2, 9), (8, 1), (5, 6)]) == {(2, 5): 1, (5, 6): 2, (2, 9): 1, (1, 8): 1}
    assert candidate([(2, 6), (4, 5), (6, 4), (4, 1), (10, 1)]) == {(2, 6): 1, (4, 5): 1, (4, 6): 1, (1, 4): 1, (1, 10): 1}
    assert candidate([(6, 3), (4, 4), (7, 2), (10, 8), (10, 3)]) == {(3, 6): 1, (4, 4): 1, (2, 7): 1, (8, 10): 1, (3, 10): 1}
    assert candidate([(2, 4), (3, 9), (7, 6), (10, 4), (11, 8)]) == {(2, 4): 1, (3, 9): 1, (6, 7): 1, (4, 10): 1, (8, 11): 1}
    assert candidate([(3, 7), (2, 4), (2, 2), (9, 5), (8, 6)]) == {(3, 7): 1, (2, 4): 1, (2, 2): 1, (5, 9): 1, (6, 8): 1}
    assert candidate([(9, 1), (7, 5), (8, 9), (5, 1), (4, 8)]) == {(1, 9): 1, (5, 7): 1, (8, 9): 1, (1, 5): 1, (4, 8): 1}
    assert candidate([(4, 5), (2, 7), (7, 3), (10, 8), (10, 4)]) == {(4, 5): 1, (2, 7): 1, (3, 7): 1, (8, 10): 1, (4, 10): 1}
    assert candidate([(2, 4), (2, 9), (1, 9), (3, 8), (6, 7)]) == {(2, 4): 1, (2, 9): 1, (1, 9): 1, (3, 8): 1, (6, 7): 1}
    assert candidate([(8, 6), (2, 7), (8, 3), (10, 2), (3, 4)]) == {(6, 8): 1, (2, 7): 1, (3, 8): 1, (2, 10): 1, (3, 4): 1}
    assert candidate([(9, 7), (5, 5), (7, 8), (10, 2), (7, 4)]) == {(7, 9): 1, (5, 5): 1, (7, 8): 1, (2, 10): 1, (4, 7): 1}
    assert candidate([(8, 3), (5, 8), (6, 10), (8, 4), (8, 3)]) == {(3, 8): 2, (5, 8): 1, (6, 10): 1, (4, 8): 1}
    assert candidate([(6, 7), (5, 9), (1, 1), (2, 1), (9, 7)]) == {(6, 7): 1, (5, 9): 1, (1, 1): 1, (1, 2): 1, (7, 9): 1}
    assert candidate([(8, 7), (5, 6), (3, 10), (1, 2), (9, 8)]) == {(7, 8): 1, (5, 6): 1, (3, 10): 1, (1, 2): 1, (8, 9): 1}
    assert candidate([(2, 5), (3, 4), (8, 4), (4, 8), (2, 4)]) == {(2, 5): 1, (3, 4): 1, (4, 8): 2, (2, 4): 1}
    assert candidate([(9, 7), (4, 4), (8, 3), (1, 1), (4, 8)]) == {(7, 9): 1, (4, 4): 1, (3, 8): 1, (1, 1): 1, (4, 8): 1}
    assert candidate([(5, 5), (7, 9), (8, 1), (4, 1), (4, 4)]) == {(5, 5): 1, (7, 9): 1, (1, 8): 1, (1, 4): 1, (4, 4): 1}
    assert candidate([(2, 4), (2, 4), (1, 5), (7, 5), (2, 6)]) == {(2, 4): 2, (1, 5): 1, (5, 7): 1, (2, 6): 1}
    assert candidate([(6, 7), (2, 7), (8, 1), (9, 4), (2, 7)]) == {(6, 7): 1, (2, 7): 2, (1, 8): 1, (4, 9): 1}
    assert candidate([(8, 4), (7, 1), (3, 11), (9, 4), (6, 8)]) == {(4, 8): 1, (1, 7): 1, (3, 11): 1, (4, 9): 1, (6, 8): 1}
    assert candidate([(2, 4), (7, 6), (3, 1), (7, 4), (3, 6)]) == {(2, 4): 1, (6, 7): 1, (1, 3): 1, (4, 7): 1, (3, 6): 1}
    assert candidate([(8, 3), (1, 8), (8, 3), (9, 5), (12, 8)]) == {(3, 8): 2, (1, 8): 1, (5, 9): 1, (8, 12): 1}
    assert candidate([(8, 6), (3, 8), (3, 3), (7, 5), (9, 6)]) == {(6, 8): 1, (3, 8): 1, (3, 3): 1, (5, 7): 1, (6, 9): 1}
    assert candidate([(3, 3), (2, 6), (7, 7), (6, 7), (6, 1)]) == {(3, 3): 1, (2, 6): 1, (7, 7): 1, (6, 7): 1, (1, 6): 1}
    assert candidate([(2, 7), (5, 7), (2, 8), (6, 6), (6, 2)]) == {(2, 7): 1, (5, 7): 1, (2, 8): 1, (6, 6): 1, (2, 6): 1}
    assert candidate([(6, 1), (5, 7), (1, 1), (9, 5), (8, 7)]) == {(1, 6): 1, (5, 7): 1, (1, 1): 1, (5, 9): 1, (7, 8): 1}
    assert candidate([(9, 1), (1, 8), (2, 8), (8, 3), (3, 2)]) == {(1, 9): 1, (1, 8): 1, (2, 8): 1, (3, 8): 1, (2, 3): 1}
    assert candidate([(8, 2), (7, 5), (7, 6), (11, 4), (4, 2)]) == {(2, 8): 1, (5, 7): 1, (6, 7): 1, (4, 11): 1, (2, 4): 1}
    assert candidate([(2, 5), (6, 4), (7, 6), (4, 2), (6, 1)]) == {(2, 5): 1, (4, 6): 1, (6, 7): 1, (2, 4): 1, (1, 6): 1}
    assert candidate([(3, 4), (1, 6), (8, 8), (1, 1), (4, 8)]) == {(3, 4): 1, (1, 6): 1, (8, 8): 1, (1, 1): 1, (4, 8): 1}
    assert candidate([(4, 1), (3, 2), (7, 2), (2, 6), (6, 1)]) == {(1, 4): 1, (2, 3): 1, (2, 7): 1, (2, 6): 1, (1, 6): 1}
    assert candidate([(2, 4), (6, 8), (2, 6), (6, 5), (2, 1)]) == {(2, 4): 1, (6, 8): 1, (2, 6): 1, (5, 6): 1, (1, 2): 1}
    assert candidate([(9, 1), (4, 4), (7, 4), (10, 2), (7, 9)]) == {(1, 9): 1, (4, 4): 1, (4, 7): 1, (2, 10): 1, (7, 9): 1}
    assert candidate([(1, 4), (3, 6), (7, 9), (7, 3), (10, 8)]) == {(1, 4): 1, (3, 6): 1, (7, 9): 1, (3, 7): 1, (8, 10): 1}
    assert candidate([(2, 3), (2, 5), (1, 11), (6, 7), (5, 4)]) == {(2, 3): 1, (2, 5): 1, (1, 11): 1, (6, 7): 1, (4, 5): 1}
    assert candidate([(6, 7), (5, 3), (3, 6), (9, 7), (4, 5)]) == {(6, 7): 1, (3, 5): 1, (3, 6): 1, (7, 9): 1, (4, 5): 1}
    assert candidate([(11, 1), (13, 27), (13, 20), (30, 8), (11, 21)]) == {(1, 11): 1, (13, 27): 1, (13, 20): 1, (8, 30): 1, (11, 21): 1}
    assert candidate([(8, 1), (6, 22), (13, 27), (22, 17), (13, 24)]) == {(1, 8): 1, (6, 22): 1, (13, 27): 1, (17, 22): 1, (13, 24): 1}
    assert candidate([(15, 3), (12, 22), (13, 25), (30, 16), (12, 18)]) == {(3, 15): 1, (12, 22): 1, (13, 25): 1, (16, 30): 1, (12, 18): 1}
    assert candidate([(10, 1), (16, 19), (16, 25), (23, 14), (11, 18)]) == {(1, 10): 1, (16, 19): 1, (16, 25): 1, (14, 23): 1, (11, 18): 1}
    assert candidate([(13, 1), (11, 18), (12, 20), (27, 16), (11, 22)]) == {(1, 13): 1, (11, 18): 1, (12, 20): 1, (16, 27): 1, (11, 22): 1}
    assert candidate([(11, 2), (12, 28), (14, 29), (20, 11), (19, 28)]) == {(2, 11): 1, (12, 28): 1, (14, 29): 1, (11, 20): 1, (19, 28): 1}
    assert candidate([(14, 4), (7, 27), (12, 27), (26, 17), (17, 28)]) == {(4, 14): 1, (7, 27): 1, (12, 27): 1, (17, 26): 1, (17, 28): 1}
    assert candidate([(11, 3), (15, 18), (10, 28), (30, 16), (16, 22)]) == {(3, 11): 1, (15, 18): 1, (10, 28): 1, (16, 30): 1, (16, 22): 1}
    assert candidate([(11, 1), (8, 25), (8, 29), (26, 13), (14, 22)]) == {(1, 11): 1, (8, 25): 1, (8, 29): 1, (13, 26): 1, (14, 22): 1}
    assert candidate([(13, 2), (12, 22), (9, 25), (25, 15), (20, 24)]) == {(2, 13): 1, (12, 22): 1, (9, 25): 1, (15, 25): 1, (20, 24): 1}
    assert candidate([(10, 7), (10, 21), (9, 20), (29, 17), (11, 25)]) == {(7, 10): 1, (10, 21): 1, (9, 20): 1, (17, 29): 1, (11, 25): 1}
    assert candidate([(12, 4), (7, 21), (14, 28), (28, 17), (11, 25)]) == {(4, 12): 1, (7, 21): 1, (14, 28): 1, (17, 28): 1, (11, 25): 1}
    assert candidate([(9, 1), (9, 20), (8, 29), (24, 9), (16, 26)]) == {(1, 9): 1, (9, 20): 1, (8, 29): 1, (9, 24): 1, (16, 26): 1}
    assert candidate([(15, 7), (13, 23), (7, 23), (27, 10), (19, 26)]) == {(7, 15): 1, (13, 23): 1, (7, 23): 1, (10, 27): 1, (19, 26): 1}
    assert candidate([(8, 5), (11, 21), (7, 24), (29, 7), (16, 19)]) == {(5, 8): 1, (11, 21): 1, (7, 24): 1, (7, 29): 1, (16, 19): 1}
    assert candidate([(18, 3), (14, 27), (10, 21), (28, 7), (13, 23)]) == {(3, 18): 1, (14, 27): 1, (10, 21): 1, (7, 28): 1, (13, 23): 1}
    assert candidate([(11, 3), (9, 19), (15, 25), (21, 7), (19, 18)]) == {(3, 11): 1, (9, 19): 1, (15, 25): 1, (7, 21): 1, (18, 19): 1}
    assert candidate([(11, 3), (13, 20), (16, 22), (24, 15), (19, 19)]) == {(3, 11): 1, (13, 20): 1, (16, 22): 1, (15, 24): 1, (19, 19): 1}
    assert candidate([(17, 1), (11, 18), (11, 24), (21, 16), (19, 24)]) == {(1, 17): 1, (11, 18): 1, (11, 24): 1, (16, 21): 1, (19, 24): 1}
    assert candidate([(10, 6), (6, 28), (12, 20), (27, 11), (17, 26)]) == {(6, 10): 1, (6, 28): 1, (12, 20): 1, (11, 27): 1, (17, 26): 1}
    assert candidate([(8, 3), (14, 27), (13, 20), (24, 8), (16, 19)]) == {(3, 8): 1, (14, 27): 1, (13, 20): 1, (8, 24): 1, (16, 19): 1}
    assert candidate([(13, 4), (16, 20), (12, 24), (25, 16), (17, 27)]) == {(4, 13): 1, (16, 20): 1, (12, 24): 1, (16, 25): 1, (17, 27): 1}
    assert candidate([(10, 6), (13, 18), (16, 21), (26, 17), (13, 23)]) == {(6, 10): 1, (13, 18): 1, (16, 21): 1, (17, 26): 1, (13, 23): 1}
    assert candidate([(13, 7), (7, 28), (13, 28), (21, 16), (13, 23)]) == {(7, 13): 1, (7, 28): 1, (13, 28): 1, (16, 21): 1, (13, 23): 1}
    assert candidate([(8, 7), (7, 18), (15, 23), (23, 7), (18, 21)]) == {(7, 8): 1, (7, 18): 1, (15, 23): 1, (7, 23): 1, (18, 21): 1}
    assert candidate([(17, 7), (10, 24), (14, 23), (23, 16), (16, 27)]) == {(7, 17): 1, (10, 24): 1, (14, 23): 1, (16, 23): 1, (16, 27): 1}
    assert candidate([(10, 5), (14, 26), (11, 28), (29, 13), (18, 25)]) == {(5, 10): 1, (14, 26): 1, (11, 28): 1, (13, 29): 1, (18, 25): 1}
    assert candidate([(17, 3), (15, 22), (10, 29), (20, 17), (20, 18)]) == {(3, 17): 1, (15, 22): 1, (10, 29): 1, (17, 20): 1, (18, 20): 1}
    assert candidate([(11, 3), (12, 27), (13, 26), (24, 12), (20, 18)]) == {(3, 11): 1, (12, 27): 1, (13, 26): 1, (12, 24): 1, (18, 20): 1}
    assert candidate([(12, 7), (9, 19), (9, 25), (29, 11), (15, 22)]) == {(7, 12): 1, (9, 19): 1, (9, 25): 1, (11, 29): 1, (15, 22): 1}
    assert candidate([(8, 3), (9, 20), (16, 23), (22, 8), (15, 24)]) == {(3, 8): 1, (9, 20): 1, (16, 23): 1, (8, 22): 1, (15, 24): 1}
    assert candidate([(17, 2), (6, 20), (13, 28), (30, 14), (21, 21)]) == {(2, 17): 1, (6, 20): 1, (13, 28): 1, (14, 30): 1, (21, 21): 1}
    assert candidate([(8, 4), (7, 26), (10, 26), (28, 8), (21, 26)]) == {(4, 8): 1, (7, 26): 1, (10, 26): 1, (8, 28): 1, (21, 26): 1}

if __name__ == '__main__':
    check(check_occurences)