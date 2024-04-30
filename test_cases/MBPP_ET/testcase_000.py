from case_MBPP_000 import similar_elements


def check(candidate):
    assert candidate((3, 4, 5, 6),(5, 7, 4, 10)) == (4, 5)
    assert candidate((1, 2, 3, 4),(5, 4, 3, 7)) == (3, 4)
    assert candidate((11, 12, 14, 13),(17, 15, 14, 13)) == (13, 14)
    assert candidate((7, 1, 6, 7), (7, 2, 5, 7)) == (7,)
    assert candidate((1, 7, 5, 11), (7, 10, 7, 8)) == (7,)
    assert candidate((7, 6, 6, 2), (3, 2, 4, 13)) == (2,)
    assert candidate((3, 1, 6, 9), (3, 7, 6, 8)) == (3, 6)
    assert candidate((8, 5, 4, 9), (7, 3, 8, 7)) == (8,)
    assert candidate((2, 8, 2, 1), (3, 4, 4, 12)) == ()
    assert candidate((3, 9, 9, 3), (4, 11, 6, 14)) == ()
    assert candidate((1, 8, 8, 1), (4, 12, 5, 7)) == ()
    assert candidate((6, 3, 6, 11), (7, 6, 7, 14)) == (6,)
    assert candidate((4, 1, 3, 10), (6, 5, 7, 13)) == ()
    assert candidate((7, 8, 7, 7), (2, 6, 7, 7)) == (7,)
    assert candidate((6, 2, 4, 1), (9, 9, 2, 9)) == (2,)
    assert candidate((2, 2, 5, 6), (3, 12, 3, 9)) == ()
    assert candidate((5, 1, 2, 11), (1, 4, 3, 13)) == (1,)
    assert candidate((6, 8, 9, 3), (6, 2, 7, 8)) == (8, 6)
    assert candidate((6, 1, 4, 3), (6, 4, 3, 9)) == (3, 4, 6)
    assert candidate((3, 3, 4, 3), (7, 3, 4, 10)) == (3, 4)
    assert candidate((5, 4, 3, 10), (8, 4, 4, 15)) == (4,)
    assert candidate((4, 5, 9, 3), (4, 7, 7, 15)) == (4,)
    assert candidate((3, 3, 3, 7), (9, 4, 7, 11)) == (7,)
    assert candidate((3, 7, 1, 1), (8, 6, 8, 7)) == (7,)
    assert candidate((6, 2, 4, 10), (3, 10, 4, 14)) == (10, 4)
    assert candidate((2, 8, 5, 9), (2, 6, 7, 11)) == (2,)
    assert candidate((2, 2, 10, 5), (10, 5, 5, 13)) == (10, 5)
    assert candidate((5, 9, 2, 7), (10, 2, 5, 9)) == (9, 2, 5)
    assert candidate((3, 7, 6, 11), (1, 8, 2, 14)) == ()
    assert candidate((4, 2, 5, 8), (6, 5, 5, 11)) == (5,)
    assert candidate((3, 5, 4, 9), (10, 3, 1, 7)) == (3,)
    assert candidate((5, 5, 6, 4), (5, 4, 1, 5)) == (4, 5)
    assert candidate((7, 1, 1, 11), (2, 7, 3, 10)) == (7,)
    assert candidate((4, 7, 5, 1), (1, 8, 5, 6)) == (1, 5)
    assert candidate((5, 4, 1, 4), (10, 11, 1, 6)) == (1,)
    assert candidate((3, 5, 1, 5), (5, 10, 8, 10)) == (5,)
    assert candidate((6, 4, 3, 1), (1, 2, 3, 3)) == (1, 3)
    assert candidate((6, 6, 7, 2), (7, 6, 6, 6)) == (6, 7)
    assert candidate((5, 7, 5, 6), (1, 9, 6, 12)) == (6,)
    assert candidate((1, 4, 8, 2), (6, 4, 8, 5)) == (8, 4)
    assert candidate((5, 2, 8, 4), (5, 8, 8, 7)) == (8, 5)
    assert candidate((3, 7, 3, 6), (9, 1, 2, 8)) == ()
    assert candidate((4, 3, 1, 8), (1, 8, 6, 12)) == (8, 1)
    assert candidate((5, 2, 4, 7), (9, 9, 4, 10)) == (4,)
    assert candidate((2, 1, 3, 2), (9, 1, 2, 9)) == (1, 2)
    assert candidate((4, 3, 4, 9), (9, 1, 4, 11)) == (9, 4)
    assert candidate((3, 6, 8, 8), (4, 9, 4, 7)) == ()
    assert candidate((2, 5, 4, 9), (8, 9, 6, 2)) == (9, 2)
    assert candidate((5, 3, 4, 5), (3, 4, 1, 12)) == (3, 4)
    assert candidate((6, 4, 5, 2), (1, 7, 4, 2)) == (2, 4)
    assert candidate((1, 7, 4, 6), (8, 2, 1, 8)) == (1,)
    assert candidate((4, 7, 6, 4), (5, 4, 7, 8)) == (4, 7)
    assert candidate((6, 7, 1, 2), (3, 9, 8, 6)) == (6,)
    assert candidate((2, 5, 3, 3), (2, 4, 6, 10)) == (2,)
    assert candidate((6, 7, 7, 5), (1, 1, 7, 4)) == (7,)
    assert candidate((1, 3, 7, 7), (6, 8, 8, 10)) == ()
    assert candidate((6, 5, 6, 3), (9, 4, 1, 9)) == ()
    assert candidate((5, 6, 5, 9), (5, 9, 7, 5)) == (9, 5)
    assert candidate((4, 7, 4, 4), (10, 8, 1, 7)) == (7,)
    assert candidate((1, 1, 2, 4), (7, 9, 6, 6)) == ()
    assert candidate((5, 3, 2, 6), (8, 5, 6, 7)) == (5, 6)
    assert candidate((2, 2, 2, 2), (6, 6, 2, 4)) == (2,)
    assert candidate((3, 2, 6, 3), (8, 7, 2, 8)) == (2,)
    assert candidate((2, 1, 1, 3), (6, 5, 5, 2)) == (2,)
    assert candidate((2, 3, 3, 9), (8, 1, 8, 11)) == ()
    assert candidate((5, 6, 2, 5), (6, 8, 4, 8)) == (6,)
    assert candidate((2, 4, 6, 3), (1, 1, 3, 4)) == (3, 4)
    assert candidate((5, 5, 5, 9), (7, 2, 1, 7)) == ()
    assert candidate((2, 1, 5, 3), (4, 2, 3, 11)) == (2, 3)
    assert candidate((6, 7, 18, 15), (21, 10, 11, 12)) == ()
    assert candidate((14, 8, 18, 11), (17, 13, 18, 16)) == (18,)
    assert candidate((13, 12, 10, 10), (18, 20, 10, 8)) == (10,)
    assert candidate((14, 15, 19, 14), (21, 19, 17, 11)) == (19,)
    assert candidate((9, 7, 9, 14), (22, 16, 10, 15)) == ()
    assert candidate((10, 10, 16, 8), (16, 14, 16, 12)) == (16,)
    assert candidate((6, 7, 10, 10), (12, 13, 10, 15)) == (10,)
    assert candidate((7, 7, 19, 17), (14, 20, 19, 13)) == (19,)
    assert candidate((14, 11, 11, 8), (21, 14, 14, 17)) == (14,)
    assert candidate((15, 9, 17, 15), (19, 19, 10, 15)) == (15,)
    assert candidate((8, 17, 11, 14), (14, 15, 19, 12)) == (14,)
    assert candidate((13, 11, 9, 11), (20, 13, 14, 15)) == (13,)
    assert candidate((8, 12, 13, 18), (14, 16, 19, 9)) == ()
    assert candidate((9, 17, 13, 18), (21, 15, 17, 15)) == (17,)
    assert candidate((6, 10, 9, 8), (17, 10, 10, 18)) == (10,)
    assert candidate((14, 11, 17, 13), (17, 18, 12, 15)) == (17,)
    assert candidate((14, 9, 16, 17), (21, 18, 19, 17)) == (17,)
    assert candidate((7, 7, 13, 8), (17, 17, 9, 16)) == ()
    assert candidate((11, 10, 11, 12), (18, 20, 18, 16)) == ()
    assert candidate((8, 8, 18, 15), (18, 19, 16, 16)) == (18,)
    assert candidate((6, 10, 15, 18), (12, 13, 11, 16)) == ()
    assert candidate((13, 12, 15, 14), (17, 17, 11, 14)) == (14,)
    assert candidate((14, 17, 18, 18), (22, 12, 9, 18)) == (18,)
    assert candidate((10, 16, 14, 9), (13, 20, 19, 8)) == ()
    assert candidate((7, 9, 10, 15), (21, 12, 13, 16)) == ()
    assert candidate((6, 8, 12, 14), (17, 10, 14, 11)) == (14,)
    assert candidate((7, 10, 10, 12), (21, 17, 18, 17)) == ()
    assert candidate((12, 12, 13, 18), (14, 17, 16, 15)) == ()
    assert candidate((13, 7, 17, 11), (18, 20, 9, 10)) == ()
    assert candidate((10, 11, 14, 13), (16, 19, 9, 13)) == (13,)
    assert candidate((8, 17, 15, 10), (19, 12, 9, 14)) == ()
    assert candidate((9, 10, 13, 8), (14, 10, 19, 17)) == (10,)
    assert candidate((11, 14, 17, 10), (15, 15, 10, 11)) == (10, 11)

if __name__ == '__main__':
    check(similar_elements)