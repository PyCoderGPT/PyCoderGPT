from case_MBPP_021 import max_difference


def check(candidate):
    assert candidate([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
    assert candidate([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
    assert candidate([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23
    assert candidate([(7, 8), (2, 8), (13, 2), (5, 1)]) == 11
    assert candidate([(3, 7), (6, 12), (15, 1), (6, 2)]) == 14
    assert candidate([(1, 3), (6, 11), (10, 2), (6, 4)]) == 8
    assert candidate([(3, 5), (4, 10), (14, 8), (5, 6)]) == 6
    assert candidate([(5, 6), (4, 9), (8, 3), (3, 6)]) == 5
    assert candidate([(2, 6), (6, 6), (13, 2), (3, 4)]) == 11
    assert candidate([(2, 4), (1, 7), (7, 2), (3, 7)]) == 6
    assert candidate([(1, 8), (2, 12), (7, 4), (2, 3)]) == 10
    assert candidate([(3, 5), (4, 10), (11, 8), (2, 7)]) == 6
    assert candidate([(4, 1), (6, 7), (7, 2), (6, 3)]) == 5
    assert candidate([(1, 10), (6, 12), (7, 3), (4, 2)]) == 9
    assert candidate([(7, 1), (1, 9), (8, 5), (2, 6)]) == 8
    assert candidate([(3, 2), (1, 12), (13, 2), (1, 5)]) == 11
    assert candidate([(2, 7), (4, 2), (10, 8), (6, 3)]) == 5
    assert candidate([(6, 8), (4, 8), (9, 6), (5, 3)]) == 4
    assert candidate([(5, 10), (1, 2), (13, 7), (4, 4)]) == 6
    assert candidate([(1, 8), (5, 2), (13, 4), (2, 7)]) == 9
    assert candidate([(4, 1), (4, 7), (8, 2), (3, 1)]) == 6
    assert candidate([(6, 1), (4, 11), (9, 2), (2, 4)]) == 7
    assert candidate([(5, 2), (4, 9), (11, 1), (6, 6)]) == 10
    assert candidate([(5, 5), (2, 6), (6, 4), (1, 5)]) == 4
    assert candidate([(3, 8), (4, 5), (12, 2), (2, 7)]) == 10
    assert candidate([(4, 5), (6, 6), (12, 8), (2, 3)]) == 4
    assert candidate([(8, 10), (5, 9), (15, 4), (2, 2)]) == 11
    assert candidate([(2, 9), (4, 8), (11, 5), (1, 2)]) == 7
    assert candidate([(2, 9), (1, 12), (13, 1), (1, 7)]) == 12
    assert candidate([(3, 8), (6, 8), (13, 4), (6, 1)]) == 9
    assert candidate([(7, 2), (5, 5), (12, 5), (5, 3)]) == 7
    assert candidate([(6, 8), (4, 3), (10, 6), (3, 2)]) == 4
    assert candidate([(3, 5), (2, 8), (5, 3), (5, 2)]) == 6
    assert candidate([(7, 5), (4, 12), (15, 1), (1, 2)]) == 14
    assert candidate([(3, 5), (3, 12), (13, 3), (2, 3)]) == 10
    assert candidate([(2, 7), (5, 5), (10, 3), (1, 7)]) == 7
    assert candidate([(5, 10), (2, 19), (7, 8), (8, 12)]) == 17
    assert candidate([(7, 1), (7, 17), (10, 13), (11, 13)]) == 10
    assert candidate([(8, 2), (3, 19), (11, 9), (12, 16)]) == 16
    assert candidate([(7, 9), (7, 17), (10, 18), (7, 7)]) == 10
    assert candidate([(4, 4), (5, 22), (9, 8), (6, 8)]) == 17
    assert candidate([(6, 6), (5, 18), (11, 11), (9, 16)]) == 13
    assert candidate([(5, 2), (3, 16), (5, 11), (9, 10)]) == 13
    assert candidate([(6, 3), (1, 12), (10, 8), (16, 12)]) == 11
    assert candidate([(7, 7), (3, 12), (8, 16), (16, 17)]) == 9
    assert candidate([(8, 7), (5, 19), (12, 11), (13, 11)]) == 14
    assert candidate([(8, 4), (3, 17), (6, 10), (10, 11)]) == 14
    assert candidate([(1, 4), (5, 19), (9, 12), (10, 17)]) == 14
    assert candidate([(3, 3), (5, 22), (5, 9), (14, 15)]) == 17
    assert candidate([(4, 4), (7, 18), (4, 11), (9, 16)]) == 11
    assert candidate([(2, 9), (1, 14), (13, 12), (14, 16)]) == 13
    assert candidate([(3, 2), (2, 16), (8, 12), (6, 15)]) == 14
    assert candidate([(4, 8), (3, 22), (5, 8), (13, 16)]) == 19
    assert candidate([(9, 2), (1, 20), (9, 16), (8, 11)]) == 19
    assert candidate([(4, 6), (5, 18), (8, 13), (6, 14)]) == 13
    assert candidate([(9, 5), (4, 17), (11, 15), (16, 8)]) == 13
    assert candidate([(1, 10), (4, 21), (9, 12), (12, 13)]) == 17
    assert candidate([(6, 9), (6, 21), (12, 13), (9, 9)]) == 15
    assert candidate([(1, 7), (2, 12), (11, 9), (13, 14)]) == 10
    assert candidate([(3, 9), (4, 12), (8, 17), (16, 8)]) == 9
    assert candidate([(1, 8), (3, 17), (6, 18), (8, 16)]) == 14
    assert candidate([(5, 10), (3, 12), (7, 8), (15, 9)]) == 9
    assert candidate([(4, 5), (7, 13), (12, 8), (13, 8)]) == 6
    assert candidate([(1, 2), (4, 22), (6, 18), (8, 12)]) == 18
    assert candidate([(2, 10), (3, 21), (12, 8), (14, 15)]) == 18
    assert candidate([(3, 6), (2, 15), (9, 11), (8, 13)]) == 13
    assert candidate([(3, 10), (5, 19), (14, 17), (13, 11)]) == 14
    assert candidate([(7, 11), (6, 15), (11, 16), (12, 7)]) == 9
    assert candidate([(1, 5), (2, 18), (13, 17), (16, 12)]) == 16
    assert candidate([(7, 35), (25, 23), (13, 23), (39, 23)]) == 28
    assert candidate([(12, 32), (19, 25), (11, 21), (46, 23)]) == 23
    assert candidate([(13, 36), (18, 24), (9, 27), (42, 20)]) == 23
    assert candidate([(13, 37), (21, 26), (18, 21), (43, 23)]) == 24
    assert candidate([(16, 39), (17, 32), (16, 18), (43, 24)]) == 23
    assert candidate([(8, 36), (26, 24), (17, 26), (44, 19)]) == 28
    assert candidate([(9, 38), (24, 23), (14, 27), (40, 27)]) == 29
    assert candidate([(16, 38), (25, 28), (16, 18), (42, 18)]) == 24
    assert candidate([(11, 39), (25, 29), (8, 24), (43, 17)]) == 28
    assert candidate([(13, 37), (18, 28), (13, 20), (40, 24)]) == 24
    assert candidate([(13, 30), (20, 22), (9, 20), (45, 18)]) == 27
    assert candidate([(11, 36), (23, 24), (17, 19), (46, 24)]) == 25
    assert candidate([(17, 33), (22, 29), (17, 23), (42, 23)]) == 19
    assert candidate([(11, 34), (16, 27), (16, 26), (42, 22)]) == 23
    assert candidate([(16, 40), (26, 30), (18, 24), (37, 18)]) == 24
    assert candidate([(15, 32), (17, 25), (9, 24), (41, 19)]) == 22
    assert candidate([(12, 37), (21, 29), (13, 25), (36, 24)]) == 25
    assert candidate([(14, 31), (19, 24), (15, 20), (45, 20)]) == 25
    assert candidate([(16, 33), (22, 26), (11, 18), (38, 23)]) == 17
    assert candidate([(14, 31), (24, 23), (16, 21), (44, 21)]) == 23
    assert candidate([(10, 34), (23, 25), (11, 24), (38, 23)]) == 24
    assert candidate([(10, 34), (25, 31), (13, 28), (45, 17)]) == 28
    assert candidate([(8, 30), (16, 22), (10, 22), (38, 17)]) == 22
    assert candidate([(8, 40), (19, 32), (8, 21), (38, 27)]) == 32
    assert candidate([(17, 37), (20, 26), (18, 21), (40, 24)]) == 20
    assert candidate([(16, 32), (18, 25), (18, 25), (38, 22)]) == 16
    assert candidate([(8, 40), (18, 27), (17, 18), (40, 23)]) == 32
    assert candidate([(10, 36), (25, 28), (10, 25), (37, 20)]) == 26
    assert candidate([(10, 30), (26, 28), (11, 20), (45, 19)]) == 26
    assert candidate([(16, 30), (24, 23), (9, 19), (40, 18)]) == 22
    assert candidate([(13, 35), (21, 26), (18, 19), (46, 25)]) == 22
    assert candidate([(13, 38), (26, 26), (10, 26), (44, 26)]) == 25
    assert candidate([(11, 33), (22, 27), (14, 21), (42, 23)]) == 22

if __name__ == '__main__':
    check(max_difference)