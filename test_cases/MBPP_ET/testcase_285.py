from case_MBPP_285 import find_dissimilar


def check(candidate):
    assert candidate((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
    assert candidate((1, 2, 3, 4), (7, 2, 3, 9)) == (1, 4, 7, 9)
    assert candidate((21, 11, 25, 26), (26, 34, 21, 36)) == (34, 36, 11, 25)
    assert candidate((1, 1, 5, 6), (1, 4, 9, 13)) == (4, 5, 6, 9, 13)
    assert candidate((5, 5, 3, 1), (2, 8, 6, 15)) == (1, 2, 3, 5, 6, 8, 15)
    assert candidate((5, 1, 8, 4), (2, 2, 5, 14)) == (1, 2, 4, 8, 14)
    assert candidate((1, 6, 5, 3), (10, 3, 4, 5)) == (1, 4, 6, 10)
    assert candidate((4, 7, 10, 4), (1, 10, 7, 5)) == (1, 4, 5)
    assert candidate((4, 3, 6, 3), (9, 12, 5, 6)) == (3, 4, 5, 9, 12)
    assert candidate((7, 8, 5, 9), (10, 6, 2, 6)) == (2, 5, 6, 7, 8, 9, 10)
    assert candidate((7, 3, 4, 5), (4, 6, 7, 13)) == (3, 5, 6, 13)
    assert candidate((4, 3, 1, 3), (2, 9, 3, 13)) == (1, 2, 4, 9, 13)
    assert candidate((4, 1, 9, 10), (3, 8, 9, 11)) == (1, 3, 4, 8, 10, 11)
    assert candidate((7, 2, 2, 8), (2, 8, 2, 10)) == (10, 7)
    assert candidate((2, 2, 9, 11), (1, 3, 4, 6)) == (1, 2, 3, 4, 6, 9, 11)
    assert candidate((3, 3, 9, 7), (6, 4, 7, 10)) == (3, 4, 6, 9, 10)
    assert candidate((8, 9, 8, 5), (8, 6, 6, 9)) == (5, 6)
    assert candidate((6, 8, 10, 8), (7, 6, 8, 7)) == (10, 7)
    assert candidate((2, 3, 3, 11), (3, 9, 4, 6)) == (2, 4, 6, 9, 11)
    assert candidate((1, 3, 4, 9), (8, 9, 5, 8)) == (1, 3, 4, 5, 8)
    assert candidate((3, 9, 1, 5), (8, 11, 3, 6)) == (1, 5, 6, 8, 9, 11)
    assert candidate((4, 4, 2, 1), (7, 7, 6, 11)) == (1, 2, 4, 6, 7, 11)
    assert candidate((8, 9, 3, 3), (4, 6, 6, 9)) == (3, 4, 6, 8)
    assert candidate((7, 2, 6, 5), (3, 7, 4, 5)) == (2, 3, 4, 6)
    assert candidate((8, 3, 2, 9), (2, 3, 7, 5)) == (5, 7, 8, 9)
    assert candidate((5, 4, 7, 6), (2, 4, 4, 8)) == (2, 5, 6, 7, 8)
    assert candidate((2, 2, 4, 10), (2, 12, 1, 11)) == (1, 4, 10, 11, 12)
    assert candidate((8, 6, 8, 9), (8, 5, 2, 12)) == (2, 5, 6, 9, 12)
    assert candidate((5, 2, 2, 3), (8, 9, 3, 8)) == (2, 5, 8, 9)
    assert candidate((4, 1, 2, 2), (3, 9, 2, 15)) == (1, 3, 4, 9, 15)
    assert candidate((1, 1, 2, 5), (4, 4, 3, 15)) == (1, 2, 3, 4, 5, 15)
    assert candidate((4, 5, 9, 11), (2, 5, 8, 5)) == (2, 4, 8, 9, 11)
    assert candidate((1, 9, 3, 7), (9, 5, 1, 5)) == (3, 5, 7)
    assert candidate((4, 9, 1, 3), (1, 12, 7, 14)) == (3, 4, 7, 9, 12, 14)
    assert candidate((2, 6, 10, 4), (5, 11, 6, 10)) == (2, 4, 5, 11)
    assert candidate((4, 6, 6, 7), (9, 9, 4, 5)) == (5, 6, 7, 9)
    assert candidate((3, 5, 4, 8), (3, 7, 8, 5)) == (4, 7)
    assert candidate((6, 5, 2, 7), (2, 7, 3, 5)) == (3, 6)
    assert candidate((6, 3, 8, 7), (3, 3, 4, 11)) == (4, 6, 7, 8, 11)
    assert candidate((4, 6, 6, 8), (10, 7, 7, 10)) == (4, 6, 7, 8, 10)
    assert candidate((5, 7, 6, 9), (5, 4, 7, 8)) == (4, 6, 8, 9)
    assert candidate((3, 2, 8, 5), (11, 6, 2, 10)) == (3, 5, 6, 8, 10, 11)
    assert candidate((5, 3, 2, 2), (11, 2, 5, 8)) == (3, 8, 11)
    assert candidate((5, 6, 3, 4), (8, 2, 3, 14)) == (2, 4, 5, 6, 8, 14)
    assert candidate((5, 7, 7, 9), (10, 4, 1, 14)) == (1, 4, 5, 7, 9, 10, 14)
    assert candidate((6, 4, 2, 2), (9, 1, 1, 12)) == (1, 2, 4, 6, 9, 12)
    assert candidate((4, 2, 3, 5), (9, 3, 5, 13)) == (2, 4, 9, 13)
    assert candidate((2, 3, 5, 1), (11, 1, 3, 13)) == (2, 5, 11, 13)
    assert candidate((4, 6, 5, 6), (8, 6, 7, 8)) == (4, 5, 7, 8)
    assert candidate((2, 1, 7, 3), (8, 2, 2, 4)) == (1, 3, 4, 7, 8)
    assert candidate((3, 6, 4, 2), (2, 5, 4, 10)) == (3, 5, 6, 10)
    assert candidate((4, 4, 3, 9), (3, 5, 2, 4)) == (2, 5, 9)
    assert candidate((1, 2, 5, 7), (4, 7, 7, 12)) == (1, 2, 4, 5, 12)
    assert candidate((1, 2, 1, 1), (4, 2, 1, 9)) == (4, 9)
    assert candidate((4, 1, 5, 5), (12, 3, 3, 11)) == (1, 3, 4, 5, 11, 12)
    assert candidate((5, 6, 4, 5), (12, 3, 6, 11)) == (3, 4, 5, 11, 12)
    assert candidate((6, 5, 2, 3), (4, 7, 5, 13)) == (2, 3, 4, 6, 7, 13)
    assert candidate((3, 5, 4, 3), (3, 4, 1, 11)) == (1, 5, 11)
    assert candidate((5, 3, 7, 5), (2, 6, 2, 8)) == (2, 3, 5, 6, 7, 8)
    assert candidate((4, 5, 4, 5), (4, 2, 2, 12)) == (2, 5, 12)
    assert candidate((4, 5, 7, 3), (10, 5, 1, 14)) == (1, 3, 4, 7, 10, 14)
    assert candidate((1, 1, 7, 5), (10, 1, 6, 7)) == (5, 6, 10)
    assert candidate((2, 2, 1, 6), (9, 2, 7, 4)) == (1, 4, 6, 7, 9)
    assert candidate((3, 2, 1, 7), (3, 4, 3, 8)) == (1, 2, 4, 7, 8)
    assert candidate((1, 5, 6, 2), (8, 1, 5, 12)) == (2, 6, 8, 12)
    assert candidate((4, 1, 8, 4), (4, 3, 4, 9)) == (1, 3, 8, 9)
    assert candidate((5, 7, 6, 8), (6, 5, 1, 6)) == (1, 7, 8)
    assert candidate((4, 1, 6, 4), (7, 1, 8, 7)) == (4, 6, 7, 8)
    assert candidate((1, 2, 6, 2), (5, 6, 3, 14)) == (1, 2, 3, 5, 14)
    assert candidate((26, 11, 23, 29), (21, 38, 18, 34)) == (34, 38, 11, 18, 21, 23, 26, 29)
    assert candidate((19, 14, 29, 31), (27, 29, 21, 37)) == (37, 14, 19, 21, 27, 31)
    assert candidate((16, 16, 29, 28), (26, 32, 22, 39)) == (32, 39, 16, 22, 26, 28, 29)
    assert candidate((26, 6, 27, 28), (26, 39, 16, 41)) == (6, 39, 41, 16, 27, 28)
    assert candidate((24, 13, 29, 31), (23, 29, 23, 34)) == (34, 13, 23, 24, 31)
    assert candidate((24, 9, 23, 30), (21, 39, 17, 31)) == (39, 9, 17, 21, 23, 24, 30, 31)
    assert candidate((16, 13, 21, 30), (28, 37, 18, 35)) == (35, 37, 13, 16, 18, 21, 28, 30)
    assert candidate((18, 7, 26, 31), (27, 29, 21, 41)) == (7, 41, 18, 21, 26, 27, 29, 31)
    assert candidate((21, 12, 22, 22), (27, 39, 21, 37)) == (37, 39, 12, 22, 27)
    assert candidate((20, 6, 30, 25), (26, 32, 22, 31)) == (32, 6, 20, 22, 25, 26, 30, 31)
    assert candidate((23, 9, 20, 23), (30, 33, 19, 36)) == (33, 36, 9, 19, 20, 23, 30)
    assert candidate((21, 9, 24, 21), (25, 38, 25, 32)) == (32, 38, 9, 21, 24, 25)
    assert candidate((18, 9, 21, 24), (28, 31, 26, 33)) == (33, 9, 18, 21, 24, 26, 28, 31)
    assert candidate((22, 8, 20, 25), (22, 29, 18, 34)) == (34, 8, 18, 20, 25, 29)
    assert candidate((25, 8, 24, 29), (28, 33, 16, 31)) == (33, 8, 16, 24, 25, 28, 29, 31)
    assert candidate((17, 15, 25, 27), (22, 38, 16, 38)) == (38, 15, 16, 17, 22, 25, 27)
    assert candidate((23, 6, 27, 27), (25, 39, 25, 34)) == (34, 6, 39, 23, 25, 27)
    assert candidate((21, 13, 24, 22), (23, 38, 23, 36)) == (36, 38, 13, 21, 22, 23, 24)
    assert candidate((23, 11, 27, 24), (21, 29, 19, 33)) == (33, 11, 19, 21, 23, 24, 27, 29)
    assert candidate((23, 11, 25, 27), (21, 35, 16, 34)) == (34, 35, 11, 16, 21, 23, 25, 27)
    assert candidate((19, 11, 24, 25), (22, 39, 25, 36)) == (36, 39, 11, 19, 22, 24)
    assert candidate((16, 14, 28, 24), (24, 34, 26, 35)) == (34, 35, 14, 16, 26, 28)
    assert candidate((17, 9, 20, 30), (23, 38, 18, 41)) == (38, 41, 9, 17, 18, 20, 23, 30)
    assert candidate((26, 14, 25, 25), (22, 29, 23, 37)) == (37, 14, 22, 23, 25, 26, 29)
    assert candidate((16, 11, 24, 24), (21, 38, 18, 41)) == (38, 41, 11, 16, 18, 21, 24)
    assert candidate((20, 8, 20, 28), (27, 29, 23, 31)) == (8, 20, 23, 27, 28, 29, 31)
    assert candidate((22, 6, 30, 29), (27, 35, 18, 34)) == (34, 35, 6, 18, 22, 27, 29, 30)
    assert candidate((25, 15, 27, 30), (21, 36, 23, 41)) == (36, 41, 15, 21, 23, 25, 27, 30)
    assert candidate((23, 11, 25, 27), (27, 34, 18, 35)) == (34, 35, 11, 18, 23, 25)
    assert candidate((19, 12, 26, 27), (21, 31, 18, 31)) == (12, 18, 19, 21, 26, 27, 31)
    assert candidate((21, 15, 28, 24), (27, 34, 19, 35)) == (34, 35, 15, 19, 21, 24, 27, 28)
    assert candidate((25, 13, 23, 25), (25, 35, 26, 40)) == (35, 40, 13, 23, 26)
    assert candidate((19, 14, 30, 28), (22, 35, 26, 36)) == (35, 36, 14, 19, 22, 26, 28, 30)

if __name__ == '__main__':
    check(find_dissimilar)