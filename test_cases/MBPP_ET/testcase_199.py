from case_MBPP_199 import min_product_tuple


def check(candidate):
    assert candidate([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
    assert candidate([(10,20), (15,2), (5,10)] )==30
    assert candidate([(11,44), (10,15), (20,5), (12, 9)] )==100
    assert candidate([(4, 2), (6, 11), (5, 5), (7, 14)]) == 8
    assert candidate([(6, 5), (2, 10), (5, 4), (6, 9)]) == 20
    assert candidate([(3, 11), (5, 8), (5, 8), (6, 7)]) == 33
    assert candidate([(5, 3), (5, 5), (3, 10), (4, 9)]) == 15
    assert candidate([(6, 2), (6, 4), (1, 5), (1, 7)]) == 5
    assert candidate([(4, 6), (2, 3), (6, 9), (9, 9)]) == 6
    assert candidate([(2, 7), (1, 3), (2, 8), (2, 7)]) == 3
    assert candidate([(6, 11), (4, 11), (4, 13), (6, 7)]) == 42
    assert candidate([(5, 6), (3, 3), (4, 13), (1, 14)]) == 9
    assert candidate([(7, 6), (3, 3), (6, 12), (6, 11)]) == 9
    assert candidate([(7, 11), (6, 9), (5, 5), (1, 7)]) == 7
    assert candidate([(4, 11), (3, 10), (1, 5), (2, 14)]) == 5
    assert candidate([(3, 2), (2, 6), (4, 5), (6, 4)]) == 6
    assert candidate([(3, 6), (2, 6), (2, 6), (3, 8)]) == 12
    assert candidate([(5, 2), (1, 4), (5, 5), (7, 13)]) == 4
    assert candidate([(1, 10), (4, 10), (2, 6), (3, 10)]) == 10
    assert candidate([(4, 2), (1, 9), (1, 10), (3, 9)]) == 8
    assert candidate([(7, 11), (5, 6), (6, 8), (8, 11)]) == 30
    assert candidate([(5, 2), (7, 6), (4, 5), (4, 10)]) == 10
    assert candidate([(2, 9), (4, 6), (2, 12), (7, 6)]) == 18
    assert candidate([(7, 2), (7, 8), (2, 8), (9, 9)]) == 14
    assert candidate([(6, 12), (7, 6), (1, 7), (1, 7)]) == 7
    assert candidate([(4, 2), (7, 11), (4, 7), (1, 12)]) == 8
    assert candidate([(2, 3), (5, 11), (4, 13), (1, 7)]) == 6
    assert candidate([(6, 3), (5, 8), (4, 13), (1, 6)]) == 6
    assert candidate([(6, 4), (7, 3), (3, 11), (1, 12)]) == 12
    assert candidate([(7, 11), (7, 11), (6, 10), (6, 12)]) == 60
    assert candidate([(5, 8), (4, 8), (1, 8), (4, 9)]) == 8
    assert candidate([(2, 3), (2, 5), (2, 6), (2, 14)]) == 6
    assert candidate([(6, 7), (1, 11), (6, 4), (7, 6)]) == 11
    assert candidate([(4, 9), (7, 9), (1, 6), (5, 10)]) == 6
    assert candidate([(1, 10), (3, 4), (5, 3), (7, 9)]) == 10
    assert candidate([(3, 4), (6, 11), (4, 3), (7, 10)]) == 12
    assert candidate([(15, 17), (15, 7), (9, 14)]) == 105
    assert candidate([(12, 18), (11, 3), (8, 10)]) == 33
    assert candidate([(6, 15), (11, 6), (9, 5)]) == 45
    assert candidate([(5, 23), (15, 5), (2, 13)]) == 26
    assert candidate([(7, 22), (16, 3), (1, 10)]) == 10
    assert candidate([(8, 24), (16, 5), (6, 8)]) == 48
    assert candidate([(10, 16), (15, 3), (6, 6)]) == 36
    assert candidate([(7, 16), (17, 6), (3, 14)]) == 42
    assert candidate([(5, 20), (18, 2), (6, 9)]) == 36
    assert candidate([(5, 23), (10, 2), (10, 14)]) == 20
    assert candidate([(14, 15), (12, 2), (6, 8)]) == 24
    assert candidate([(5, 15), (16, 5), (10, 6)]) == 60
    assert candidate([(14, 19), (14, 5), (10, 14)]) == 70
    assert candidate([(14, 23), (11, 5), (10, 9)]) == 55
    assert candidate([(14, 18), (20, 1), (1, 15)]) == 15
    assert candidate([(14, 15), (12, 6), (10, 14)]) == 72
    assert candidate([(13, 15), (14, 1), (8, 14)]) == 14
    assert candidate([(13, 23), (16, 5), (6, 12)]) == 72
    assert candidate([(7, 20), (10, 6), (2, 13)]) == 26
    assert candidate([(9, 18), (12, 7), (8, 9)]) == 72
    assert candidate([(13, 25), (15, 5), (10, 11)]) == 75
    assert candidate([(7, 17), (12, 1), (7, 14)]) == 12
    assert candidate([(12, 25), (20, 7), (7, 15)]) == 105
    assert candidate([(12, 18), (11, 2), (9, 7)]) == 22
    assert candidate([(10, 19), (15, 7), (4, 8)]) == 32
    assert candidate([(14, 25), (14, 7), (10, 10)]) == 98
    assert candidate([(10, 24), (11, 3), (8, 6)]) == 33
    assert candidate([(13, 18), (20, 2), (3, 5)]) == 15
    assert candidate([(8, 21), (18, 1), (7, 5)]) == 18
    assert candidate([(14, 16), (18, 7), (8, 7)]) == 56
    assert candidate([(15, 19), (19, 2), (7, 13)]) == 38
    assert candidate([(7, 21), (14, 4), (10, 11)]) == 56
    assert candidate([(7, 20), (14, 6), (6, 14)]) == 84
    assert candidate([(14, 45), (6, 20), (21, 4), (8, 5)]) == 40
    assert candidate([(14, 47), (6, 20), (25, 8), (14, 6)]) == 84
    assert candidate([(12, 46), (6, 14), (21, 8), (15, 11)]) == 84
    assert candidate([(8, 44), (13, 10), (15, 7), (17, 10)]) == 105
    assert candidate([(6, 46), (9, 18), (25, 2), (14, 14)]) == 50
    assert candidate([(11, 46), (15, 20), (22, 6), (8, 7)]) == 56
    assert candidate([(14, 44), (8, 13), (15, 4), (9, 12)]) == 60
    assert candidate([(6, 41), (14, 16), (19, 4), (12, 13)]) == 76
    assert candidate([(12, 43), (12, 19), (17, 5), (16, 10)]) == 85
    assert candidate([(6, 48), (7, 13), (23, 8), (15, 4)]) == 60
    assert candidate([(6, 47), (8, 11), (25, 10), (17, 12)]) == 88
    assert candidate([(13, 43), (6, 10), (19, 4), (16, 11)]) == 60
    assert candidate([(11, 42), (12, 18), (22, 1), (16, 11)]) == 22
    assert candidate([(14, 48), (14, 18), (19, 10), (10, 8)]) == 80
    assert candidate([(8, 42), (10, 18), (17, 8), (11, 5)]) == 55
    assert candidate([(7, 49), (6, 10), (17, 6), (17, 4)]) == 60
    assert candidate([(13, 46), (8, 12), (20, 7), (12, 10)]) == 96
    assert candidate([(16, 42), (14, 11), (25, 6), (9, 5)]) == 45
    assert candidate([(14, 45), (14, 17), (25, 6), (14, 11)]) == 150
    assert candidate([(11, 47), (7, 14), (18, 8), (12, 12)]) == 98
    assert candidate([(7, 47), (15, 13), (24, 7), (13, 4)]) == 52
    assert candidate([(11, 49), (14, 10), (22, 7), (15, 4)]) == 60
    assert candidate([(7, 44), (5, 17), (20, 6), (11, 7)]) == 77
    assert candidate([(16, 40), (10, 19), (18, 6), (16, 12)]) == 108
    assert candidate([(12, 39), (11, 15), (15, 10), (13, 5)]) == 65
    assert candidate([(13, 40), (11, 16), (15, 3), (12, 5)]) == 45
    assert candidate([(8, 47), (9, 10), (22, 2), (16, 9)]) == 44
    assert candidate([(12, 45), (9, 17), (22, 2), (13, 9)]) == 44
    assert candidate([(14, 47), (9, 11), (24, 7), (12, 5)]) == 60
    assert candidate([(15, 48), (15, 19), (20, 2), (15, 14)]) == 40
    assert candidate([(6, 40), (5, 14), (25, 4), (15, 8)]) == 70
    assert candidate([(8, 46), (6, 16), (21, 1), (16, 12)]) == 21
    assert candidate([(14, 41), (11, 19), (23, 2), (15, 11)]) == 46

if __name__ == '__main__':
    check(min_product_tuple)