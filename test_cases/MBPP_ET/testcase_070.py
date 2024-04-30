from case_MBPP_070 import max_product_tuple


def check(candidate):
    assert candidate([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
    assert candidate([(10,20), (15,2), (5,10)] )==200
    assert candidate([(11,44), (10,15), (20,5), (12, 9)] )==484
    assert candidate([(5, 12), (2, 4), (1, 9), (6, 6)]) == 60
    assert candidate([(3, 9), (3, 4), (6, 5), (2, 4)]) == 30
    assert candidate([(2, 2), (3, 11), (2, 12), (4, 14)]) == 56
    assert candidate([(7, 10), (4, 5), (5, 12), (3, 12)]) == 70
    assert candidate([(3, 2), (1, 8), (4, 8), (8, 12)]) == 96
    assert candidate([(3, 6), (2, 9), (2, 3), (2, 10)]) == 20
    assert candidate([(7, 2), (1, 10), (1, 6), (5, 10)]) == 50
    assert candidate([(2, 6), (1, 8), (6, 4), (9, 4)]) == 36
    assert candidate([(2, 10), (5, 3), (6, 10), (7, 7)]) == 60
    assert candidate([(6, 7), (5, 2), (5, 12), (9, 14)]) == 126
    assert candidate([(1, 3), (2, 9), (3, 9), (2, 8)]) == 27
    assert candidate([(3, 3), (4, 5), (2, 5), (7, 10)]) == 70
    assert candidate([(2, 10), (3, 9), (6, 9), (7, 4)]) == 54
    assert candidate([(3, 7), (4, 8), (5, 13), (2, 7)]) == 65
    assert candidate([(7, 12), (4, 6), (3, 8), (6, 6)]) == 84
    assert candidate([(3, 3), (4, 5), (1, 9), (8, 7)]) == 56
    assert candidate([(3, 9), (6, 1), (3, 9), (3, 14)]) == 42
    assert candidate([(3, 9), (2, 4), (4, 6), (6, 11)]) == 66
    assert candidate([(2, 9), (3, 5), (1, 11), (6, 12)]) == 72
    assert candidate([(6, 10), (3, 1), (4, 12), (7, 9)]) == 63
    assert candidate([(2, 5), (4, 7), (2, 8), (5, 11)]) == 55
    assert candidate([(4, 8), (5, 9), (3, 7), (3, 6)]) == 45
    assert candidate([(5, 3), (2, 7), (5, 4), (5, 11)]) == 55
    assert candidate([(2, 3), (3, 8), (5, 7), (7, 12)]) == 84
    assert candidate([(6, 10), (4, 7), (4, 7), (1, 10)]) == 60
    assert candidate([(3, 12), (4, 3), (4, 8), (9, 7)]) == 63
    assert candidate([(7, 11), (6, 9), (1, 11), (5, 12)]) == 77
    assert candidate([(7, 6), (2, 8), (1, 12), (6, 14)]) == 84
    assert candidate([(7, 6), (6, 9), (2, 9), (9, 4)]) == 54
    assert candidate([(3, 10), (4, 8), (2, 5), (3, 4)]) == 32
    assert candidate([(2, 4), (2, 3), (1, 5), (8, 11)]) == 88
    assert candidate([(4, 11), (4, 11), (3, 3), (1, 9)]) == 44
    assert candidate([(4, 12), (1, 8), (4, 8), (5, 4)]) == 48
    assert candidate([(13, 15), (11, 5), (9, 6)]) == 195
    assert candidate([(9, 15), (17, 7), (1, 10)]) == 135
    assert candidate([(9, 18), (12, 5), (5, 14)]) == 162
    assert candidate([(15, 15), (15, 4), (10, 5)]) == 225
    assert candidate([(12, 17), (15, 1), (8, 6)]) == 204
    assert candidate([(13, 23), (15, 7), (2, 9)]) == 299
    assert candidate([(7, 19), (16, 7), (3, 9)]) == 133
    assert candidate([(14, 17), (20, 7), (5, 13)]) == 238
    assert candidate([(7, 25), (19, 1), (6, 5)]) == 175
    assert candidate([(7, 25), (11, 4), (2, 11)]) == 175
    assert candidate([(14, 18), (12, 4), (6, 14)]) == 252
    assert candidate([(13, 20), (14, 5), (4, 11)]) == 260
    assert candidate([(10, 20), (16, 2), (2, 7)]) == 200
    assert candidate([(7, 20), (18, 4), (2, 9)]) == 140
    assert candidate([(5, 18), (17, 2), (9, 11)]) == 99
    assert candidate([(14, 23), (13, 1), (5, 11)]) == 322
    assert candidate([(12, 23), (16, 6), (7, 7)]) == 276
    assert candidate([(10, 19), (12, 1), (7, 10)]) == 190
    assert candidate([(10, 20), (19, 6), (8, 10)]) == 200
    assert candidate([(15, 18), (12, 3), (10, 10)]) == 270
    assert candidate([(8, 24), (18, 3), (8, 11)]) == 192
    assert candidate([(10, 15), (17, 6), (3, 7)]) == 150
    assert candidate([(6, 25), (18, 5), (6, 10)]) == 150
    assert candidate([(15, 20), (13, 6), (10, 10)]) == 300
    assert candidate([(9, 22), (12, 2), (9, 11)]) == 198
    assert candidate([(5, 18), (13, 2), (7, 15)]) == 105
    assert candidate([(15, 24), (10, 7), (9, 11)]) == 360
    assert candidate([(8, 19), (12, 5), (3, 5)]) == 152
    assert candidate([(12, 18), (10, 1), (6, 7)]) == 216
    assert candidate([(14, 18), (16, 7), (6, 7)]) == 252
    assert candidate([(15, 24), (17, 3), (1, 15)]) == 360
    assert candidate([(5, 22), (11, 4), (4, 13)]) == 110
    assert candidate([(15, 21), (13, 6), (8, 11)]) == 315
    assert candidate([(10, 42), (13, 15), (25, 8), (8, 5)]) == 420
    assert candidate([(14, 45), (12, 10), (23, 8), (15, 5)]) == 630
    assert candidate([(16, 43), (14, 18), (20, 9), (12, 13)]) == 688
    assert candidate([(9, 46), (13, 16), (23, 2), (13, 9)]) == 414
    assert candidate([(6, 40), (8, 16), (21, 8), (7, 14)]) == 240
    assert candidate([(14, 46), (11, 15), (17, 4), (8, 11)]) == 644
    assert candidate([(15, 42), (9, 20), (17, 10), (10, 4)]) == 630
    assert candidate([(9, 43), (5, 15), (20, 3), (7, 6)]) == 387
    assert candidate([(14, 44), (15, 18), (20, 2), (11, 9)]) == 616
    assert candidate([(10, 43), (13, 11), (25, 3), (10, 6)]) == 430
    assert candidate([(14, 42), (11, 18), (19, 4), (10, 8)]) == 588
    assert candidate([(11, 46), (13, 11), (19, 1), (11, 10)]) == 506
    assert candidate([(14, 47), (14, 15), (17, 10), (10, 5)]) == 658
    assert candidate([(14, 40), (15, 17), (17, 10), (11, 7)]) == 560
    assert candidate([(8, 40), (8, 15), (25, 6), (8, 11)]) == 320
    assert candidate([(13, 40), (11, 11), (22, 8), (16, 7)]) == 520
    assert candidate([(13, 42), (13, 14), (25, 1), (13, 10)]) == 546
    assert candidate([(13, 45), (12, 15), (25, 6), (15, 5)]) == 585
    assert candidate([(7, 48), (12, 16), (16, 9), (14, 4)]) == 336
    assert candidate([(15, 44), (11, 16), (25, 1), (11, 14)]) == 660
    assert candidate([(13, 44), (8, 13), (18, 9), (13, 4)]) == 572
    assert candidate([(15, 45), (5, 18), (17, 6), (11, 14)]) == 675
    assert candidate([(10, 41), (14, 10), (21, 10), (11, 11)]) == 410
    assert candidate([(15, 45), (9, 18), (17, 7), (13, 6)]) == 675
    assert candidate([(10, 49), (10, 17), (15, 5), (16, 12)]) == 490
    assert candidate([(12, 48), (9, 16), (20, 6), (11, 14)]) == 576
    assert candidate([(9, 47), (9, 12), (23, 7), (16, 8)]) == 423
    assert candidate([(14, 44), (12, 19), (21, 1), (15, 12)]) == 616
    assert candidate([(12, 40), (5, 18), (23, 10), (10, 7)]) == 480
    assert candidate([(16, 40), (6, 20), (18, 3), (12, 5)]) == 640
    assert candidate([(6, 48), (13, 15), (16, 5), (10, 10)]) == 288
    assert candidate([(7, 44), (9, 20), (19, 8), (17, 5)]) == 308
    assert candidate([(13, 46), (14, 16), (25, 10), (9, 10)]) == 598

if __name__ == '__main__':
    check(max_product_tuple)