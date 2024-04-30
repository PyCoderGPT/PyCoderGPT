from case_MBPP_032 import find_tuples


def check(candidate):
    assert candidate([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == '[(6, 24, 12)]'
    assert candidate([(5, 25, 30), (4, 2, 3), (7, 8, 9)], 5) == '[(5, 25, 30)]'
    assert candidate([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == '[(8, 16, 4)]'
    assert candidate([(11, 22, 15), (9, 11, 5), (16, 18, 25)], 11) == []
    assert candidate([(1, 26, 9), (2, 13, 6), (11, 23, 16)], 2) == []
    assert candidate([(5, 28, 10), (2, 6, 6), (9, 21, 21)], 11) == []
    assert candidate([(11, 26, 8), (4, 12, 5), (9, 19, 16)], 4) == []
    assert candidate([(5, 22, 10), (8, 12, 2), (7, 15, 19)], 2) == [(8, 12, 2)]
    assert candidate([(1, 20, 14), (11, 5, 10), (12, 20, 21)], 7) == []
    assert candidate([(1, 27, 14), (6, 12, 7), (10, 14, 23)], 5) == []
    assert candidate([(2, 28, 11), (2, 5, 4), (7, 14, 17)], 6) == []
    assert candidate([(8, 25, 15), (6, 6, 3), (10, 21, 24)], 2) == []
    assert candidate([(11, 23, 8), (12, 6, 4), (17, 16, 25)], 9) == []
    assert candidate([(9, 29, 10), (7, 10, 5), (10, 22, 24)], 1) == [(9, 29, 10), (7, 10, 5), (10, 22, 24)]
    assert candidate([(3, 28, 17), (3, 7, 2), (13, 15, 18)], 8) == []
    assert candidate([(6, 25, 16), (3, 7, 5), (7, 18, 16)], 9) == []
    assert candidate([(10, 23, 17), (6, 8, 6), (17, 19, 21)], 1) == [(10, 23, 17), (6, 8, 6), (17, 19, 21)]
    assert candidate([(8, 20, 10), (8, 14, 8), (14, 14, 19)], 3) == []
    assert candidate([(3, 23, 15), (9, 11, 1), (14, 23, 16)], 2) == []
    assert candidate([(11, 27, 17), (11, 11, 8), (14, 17, 26)], 9) == []
    assert candidate([(7, 21, 13), (6, 4, 2), (10, 20, 16)], 1) == [(7, 21, 13), (6, 4, 2), (10, 20, 16)]
    assert candidate([(7, 19, 8), (7, 6, 5), (13, 22, 20)], 4) == []
    assert candidate([(3, 21, 7), (9, 11, 8), (13, 13, 22)], 8) == []
    assert candidate([(11, 29, 16), (6, 5, 2), (17, 16, 20)], 5) == []
    assert candidate([(9, 20, 10), (8, 14, 1), (16, 15, 21)], 7) == []
    assert candidate([(5, 28, 12), (10, 9, 4), (17, 13, 19)], 11) == []
    assert candidate([(11, 24, 16), (11, 5, 6), (16, 16, 22)], 2) == [(16, 16, 22)]
    assert candidate([(7, 26, 12), (10, 14, 6), (17, 23, 19)], 8) == []
    assert candidate([(8, 28, 11), (5, 12, 3), (8, 14, 19)], 3) == []
    assert candidate([(7, 22, 12), (3, 13, 9), (11, 15, 23)], 4) == []
    assert candidate([(1, 24, 15), (5, 13, 7), (15, 22, 25)], 10) == []
    assert candidate([(5, 24, 13), (2, 12, 4), (17, 14, 23)], 5) == []
    assert candidate([(4, 26, 17), (4, 4, 10), (10, 19, 21)], 7) == []
    assert candidate([(5, 23, 15), (7, 8, 4), (9, 14, 20)], 11) == []
    assert candidate([(3, 29, 16), (9, 12, 8), (17, 18, 25)], 5) == []
    assert candidate([(5, 29, 15), (12, 13, 3), (13, 19, 18)], 8) == []
    assert candidate([(9, 27, 28), (7, 6, 5), (6, 6, 14)], 5) == []
    assert candidate([(3, 30, 34), (1, 7, 6), (4, 8, 9)], 6) == []
    assert candidate([(2, 30, 33), (1, 5, 8), (10, 12, 13)], 1) == [(2, 30, 33), (1, 5, 8), (10, 12, 13)]
    assert candidate([(2, 26, 26), (9, 4, 1), (6, 4, 10)], 2) == [(2, 26, 26), (6, 4, 10)]
    assert candidate([(2, 22, 29), (3, 7, 6), (4, 9, 4)], 7) == []
    assert candidate([(6, 25, 34), (8, 3, 5), (2, 13, 6)], 3) == []
    assert candidate([(4, 21, 25), (6, 2, 4), (5, 9, 9)], 3) == []
    assert candidate([(7, 29, 28), (1, 6, 2), (9, 9, 12)], 3) == [(9, 9, 12)]
    assert candidate([(7, 29, 30), (4, 5, 4), (8, 5, 9)], 6) == []
    assert candidate([(6, 24, 30), (5, 2, 4), (6, 11, 5)], 7) == []
    assert candidate([(3, 24, 33), (6, 2, 7), (8, 13, 9)], 10) == []
    assert candidate([(4, 28, 29), (4, 6, 2), (2, 12, 6)], 3) == []
    assert candidate([(2, 30, 27), (1, 6, 3), (11, 6, 11)], 8) == []
    assert candidate([(4, 21, 32), (6, 6, 6), (10, 12, 9)], 5) == []
    assert candidate([(8, 29, 35), (1, 6, 2), (7, 4, 14)], 1) == [(8, 29, 35), (1, 6, 2), (7, 4, 14)]
    assert candidate([(1, 25, 26), (7, 6, 8), (5, 13, 9)], 9) == []
    assert candidate([(1, 21, 35), (5, 7, 5), (5, 4, 9)], 9) == []
    assert candidate([(10, 25, 31), (8, 1, 8), (11, 7, 11)], 10) == []
    assert candidate([(4, 28, 27), (6, 4, 5), (4, 3, 11)], 1) == [(4, 28, 27), (6, 4, 5), (4, 3, 11)]
    assert candidate([(5, 27, 29), (5, 3, 4), (6, 6, 5)], 2) == []
    assert candidate([(7, 24, 29), (3, 1, 1), (10, 6, 7)], 3) == []
    assert candidate([(4, 22, 25), (9, 2, 8), (10, 13, 9)], 2) == []
    assert candidate([(1, 27, 27), (6, 1, 4), (10, 8, 12)], 10) == []
    assert candidate([(4, 22, 35), (4, 6, 2), (2, 9, 9)], 1) == [(4, 22, 35), (4, 6, 2), (2, 9, 9)]
    assert candidate([(10, 22, 27), (4, 6, 2), (10, 5, 6)], 3) == []
    assert candidate([(4, 26, 30), (4, 6, 5), (11, 3, 11)], 8) == []
    assert candidate([(1, 29, 30), (2, 6, 3), (9, 7, 12)], 9) == []
    assert candidate([(1, 23, 31), (4, 7, 4), (8, 8, 12)], 6) == []
    assert candidate([(2, 28, 32), (3, 3, 1), (9, 8, 11)], 10) == []
    assert candidate([(8, 30, 31), (2, 1, 1), (12, 7, 6)], 8) == []
    assert candidate([(9, 23, 29), (7, 6, 7), (7, 12, 8)], 5) == []
    assert candidate([(2, 29, 32), (8, 4, 8), (5, 6, 13)], 5) == []
    assert candidate([(7, 30, 29), (1, 6, 8), (5, 9, 9)], 7) == []
    assert candidate([(11, 8, 17), (8, 16, 1), (16, 12, 19)], 4) == []
    assert candidate([(11, 10, 13), (10, 14, 3), (18, 12, 18)], 5) == []
    assert candidate([(7, 14, 19), (5, 21, 3), (20, 13, 15)], 8) == []
    assert candidate([(10, 7, 12), (10, 19, 4), (22, 13, 20)], 2) == []
    assert candidate([(11, 13, 20), (11, 14, 8), (16, 16, 23)], 6) == []
    assert candidate([(2, 8, 19), (9, 16, 6), (24, 20, 23)], 6) == []
    assert candidate([(5, 4, 21), (12, 18, 5), (19, 18, 17)], 6) == []
    assert candidate([(9, 7, 17), (11, 16, 5), (23, 12, 21)], 3) == []
    assert candidate([(3, 6, 13), (12, 17, 8), (15, 12, 13)], 4) == []
    assert candidate([(4, 14, 12), (8, 12, 7), (17, 20, 19)], 6) == []
    assert candidate([(11, 5, 14), (10, 14, 8), (21, 20, 18)], 2) == [(10, 14, 8)]
    assert candidate([(11, 10, 21), (9, 17, 5), (20, 20, 15)], 9) == []
    assert candidate([(9, 9, 13), (5, 15, 5), (19, 20, 15)], 6) == []
    assert candidate([(12, 5, 17), (10, 20, 7), (14, 14, 23)], 7) == []
    assert candidate([(10, 8, 18), (6, 19, 7), (19, 13, 16)], 3) == []
    assert candidate([(5, 14, 13), (13, 14, 1), (20, 12, 15)], 2) == []
    assert candidate([(4, 10, 15), (7, 19, 2), (24, 13, 16)], 2) == []
    assert candidate([(4, 5, 16), (10, 20, 4), (23, 19, 15)], 5) == []
    assert candidate([(10, 9, 19), (9, 16, 9), (14, 14, 20)], 5) == []
    assert candidate([(2, 12, 19), (8, 16, 8), (14, 18, 15)], 5) == []
    assert candidate([(10, 13, 14), (5, 18, 2), (24, 21, 13)], 4) == []
    assert candidate([(4, 4, 11), (12, 17, 7), (22, 19, 17)], 6) == []
    assert candidate([(2, 4, 20), (12, 21, 7), (21, 19, 20)], 9) == []
    assert candidate([(11, 14, 12), (11, 20, 3), (14, 22, 15)], 3) == []
    assert candidate([(8, 4, 16), (5, 15, 3), (24, 19, 22)], 7) == []
    assert candidate([(4, 5, 17), (4, 13, 7), (15, 20, 15)], 9) == []
    assert candidate([(7, 7, 12), (9, 19, 3), (17, 18, 13)], 2) == []
    assert candidate([(2, 11, 12), (13, 17, 6), (19, 19, 16)], 2) == []
    assert candidate([(2, 9, 15), (9, 12, 2), (16, 18, 17)], 4) == []
    assert candidate([(2, 8, 15), (13, 12, 2), (14, 20, 18)], 5) == []
    assert candidate([(6, 14, 12), (3, 15, 1), (18, 13, 16)], 9) == []
    assert candidate([(9, 7, 16), (6, 20, 9), (15, 17, 22)], 8) == []
    assert candidate([(6, 10, 16), (11, 18, 1), (15, 13, 22)], 4) == []

if __name__ == '__main__':
    check(find_tuples)