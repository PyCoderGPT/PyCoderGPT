from case_MBPP_409 import remove_nested


def check(candidate):
    assert candidate((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
    assert candidate((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)
    assert candidate((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)
    assert candidate((5, 6, 12, (3, 10), 7)) == (5, 6, 12, 7)
    assert candidate((5, 7, 8, (2, 6), 7)) == (5, 7, 8, 7)
    assert candidate((4, 5, 4, (1, 4), 12)) == (4, 5, 4, 12)
    assert candidate((5, 2, 11, (4, 1), 7)) == (5, 2, 11, 7)
    assert candidate((6, 8, 3, (2, 8), 7)) == (6, 8, 3, 7)
    assert candidate((3, 8, 9, (5, 1), 7)) == (3, 8, 9, 7)
    assert candidate((5, 9, 6, (1, 10), 9)) == (5, 9, 6, 9)
    assert candidate((6, 3, 7, (9, 9), 14)) == (6, 3, 7, 14)
    assert candidate((6, 8, 8, (3, 10), 7)) == (6, 8, 8, 7)
    assert candidate((6, 4, 10, (5, 6), 8)) == (6, 4, 10, 8)
    assert candidate((6, 9, 4, (6, 4), 11)) == (6, 9, 4, 11)
    assert candidate((6, 1, 9, (3, 9), 12)) == (6, 1, 9, 12)
    assert candidate((1, 1, 11, (6, 1), 13)) == (1, 1, 11, 13)
    assert candidate((1, 6, 9, (9, 2), 11)) == (1, 6, 9, 11)
    assert candidate((6, 10, 2, (1, 4), 14)) == (6, 10, 2, 14)
    assert candidate((5, 6, 2, (7, 2), 9)) == (5, 6, 2, 9)
    assert candidate((2, 1, 7, (7, 10), 5)) == (2, 1, 7, 5)
    assert candidate((2, 6, 8, (7, 5), 5)) == (2, 6, 8, 5)
    assert candidate((6, 3, 10, (1, 6), 13)) == (6, 3, 10, 13)
    assert candidate((4, 9, 3, (8, 6), 10)) == (4, 9, 3, 10)
    assert candidate((5, 9, 9, (2, 4), 5)) == (5, 9, 9, 5)
    assert candidate((3, 4, 7, (9, 6), 11)) == (3, 4, 7, 11)
    assert candidate((3, 7, 12, (6, 4), 10)) == (3, 7, 12, 10)
    assert candidate((2, 3, 6, (7, 9), 11)) == (2, 3, 6, 11)
    assert candidate((3, 10, 5, (7, 7), 15)) == (3, 10, 5, 15)
    assert candidate((6, 8, 6, (7, 7), 15)) == (6, 8, 6, 15)
    assert candidate((3, 7, 3, (8, 9), 13)) == (3, 7, 3, 13)
    assert candidate((1, 2, 9, (3, 1), 11)) == (1, 2, 9, 11)
    assert candidate((3, 7, 2, (4, 8), 5)) == (3, 7, 2, 5)
    assert candidate((3, 10, 10, (4, 4), 6)) == (3, 10, 10, 6)
    assert candidate((2, 5, 3, (2, 11), 10)) == (2, 5, 3, 10)
    assert candidate((2, 2, 8, (3, 10), 13)) == (2, 2, 8, 13)
    assert candidate((2, 6, 12, (1, 2), 9)) == (2, 6, 12, 9)
    assert candidate((3, 8, 7, (6, 2), 16)) == (3, 8, 7, 16)
    assert candidate((4, 11, 9, (2, 4), 12)) == (4, 11, 9, 12)
    assert candidate((4, 2, 10, (7, 4), 14)) == (4, 2, 10, 14)
    assert candidate((3, 3, 8, (8, 5), 16)) == (3, 3, 8, 16)
    assert candidate((6, 3, 6, (3, 9), 8)) == (6, 3, 6, 8)
    assert candidate((4, 7, 12, (10, 6), 8)) == (4, 7, 12, 8)
    assert candidate((5, 9, 5, (6, 10), 8)) == (5, 9, 5, 8)
    assert candidate((7, 2, 13, (5, 8), 11)) == (7, 2, 13, 11)
    assert candidate((1, 3, 9, (3, 2), 16)) == (1, 3, 9, 16)
    assert candidate((6, 7, 6, (3, 2), 14)) == (6, 7, 6, 14)
    assert candidate((5, 8, 6, (8, 6), 13)) == (5, 8, 6, 13)
    assert candidate((4, 6, 4, (10, 11), 6)) == (4, 6, 4, 6)
    assert candidate((2, 11, 8, (6, 7), 15)) == (2, 11, 8, 15)
    assert candidate((1, 7, 13, (7, 6), 11)) == (1, 7, 13, 11)
    assert candidate((5, 10, 9, (4, 10), 11)) == (5, 10, 9, 11)
    assert candidate((4, 5, 13, (9, 3), 14)) == (4, 5, 13, 14)
    assert candidate((1, 11, 7, (9, 6), 12)) == (1, 11, 7, 12)
    assert candidate((1, 2, 4, (2, 9), 15)) == (1, 2, 4, 15)
    assert candidate((2, 8, 3, (9, 7), 6)) == (2, 8, 3, 6)
    assert candidate((4, 6, 6, (10, 3), 14)) == (4, 6, 6, 14)
    assert candidate((5, 10, 5, (4, 7), 9)) == (5, 10, 5, 9)
    assert candidate((4, 6, 3, (10, 5), 12)) == (4, 6, 3, 12)
    assert candidate((3, 11, 3, (3, 10), 10)) == (3, 11, 3, 10)
    assert candidate((1, 11, 12, (10, 11), 8)) == (1, 11, 12, 8)
    assert candidate((7, 10, 4, (9, 10), 12)) == (7, 10, 4, 12)
    assert candidate((2, 3, 11, (5, 4), 15)) == (2, 3, 11, 15)
    assert candidate((7, 8, 11, (6, 6), 10)) == (7, 8, 11, 10)
    assert candidate((1, 7, 12, (1, 10), 8)) == (1, 7, 12, 8)
    assert candidate((3, 8, 11, (5, 10), 12)) == (3, 8, 11, 12)
    assert candidate((4, 11, 8, (3, 10), 13)) == (4, 11, 8, 13)
    assert candidate((1, 11, 4, (2, 4), 12)) == (1, 11, 4, 12)
    assert candidate((4, 11, 5, (3, 7), 15)) == (4, 11, 5, 15)
    assert candidate((7, 6, 6, (7, 2), 8)) == (7, 6, 6, 8)
    assert candidate((7, 8, 7, (3, 12), 9)) == (7, 8, 7, 9)
    assert candidate((7, 8, 7, (7, 5), 7)) == (7, 8, 7, 7)
    assert candidate((1, 2, 8, (6, 7), 16)) == (1, 2, 8, 16)
    assert candidate((8, 9, 6, (2, 9), 16)) == (8, 9, 6, 16)
    assert candidate((8, 12, 4, (7, 3), 9)) == (8, 12, 4, 9)
    assert candidate((1, 8, 10, (2, 3), 15)) == (1, 8, 10, 15)
    assert candidate((5, 6, 9, (11, 9), 16)) == (5, 6, 9, 16)
    assert candidate((6, 4, 8, (1, 5), 15)) == (6, 4, 8, 15)
    assert candidate((6, 2, 4, (9, 11), 11)) == (6, 2, 4, 11)
    assert candidate((1, 7, 6, (10, 9), 16)) == (1, 7, 6, 16)
    assert candidate((6, 12, 13, (10, 12), 14)) == (6, 12, 13, 14)
    assert candidate((3, 4, 6, (7, 7), 16)) == (3, 4, 6, 16)
    assert candidate((5, 9, 4, (9, 9), 13)) == (5, 9, 4, 13)
    assert candidate((2, 11, 10, (9, 12), 12)) == (2, 11, 10, 12)
    assert candidate((6, 2, 5, (7, 8), 17)) == (6, 2, 5, 17)
    assert candidate((1, 11, 11, (6, 13), 9)) == (1, 11, 11, 9)
    assert candidate((7, 3, 10, (11, 3), 8)) == (7, 3, 10, 8)
    assert candidate((5, 9, 7, (2, 8), 17)) == (5, 9, 7, 17)
    assert candidate((3, 11, 4, (4, 10), 10)) == (3, 11, 4, 10)
    assert candidate((4, 12, 11, (3, 12), 9)) == (4, 12, 11, 9)
    assert candidate((6, 10, 5, (1, 6), 8)) == (6, 10, 5, 8)
    assert candidate((6, 8, 13, (7, 10), 13)) == (6, 8, 13, 13)
    assert candidate((5, 11, 13, (5, 8), 9)) == (5, 11, 13, 9)
    assert candidate((3, 5, 9, (9, 8), 10)) == (3, 5, 9, 10)
    assert candidate((1, 10, 13, (9, 4), 13)) == (1, 10, 13, 13)
    assert candidate((3, 9, 14, (9, 5), 12)) == (3, 9, 14, 12)
    assert candidate((3, 3, 7, (11, 12), 16)) == (3, 3, 7, 16)
    assert candidate((7, 2, 4, (1, 3), 7)) == (7, 2, 4, 7)
    assert candidate((8, 11, 11, (1, 6), 17)) == (8, 11, 11, 17)
    assert candidate((6, 12, 12, (5, 5), 17)) == (6, 12, 12, 17)
    assert candidate((5, 6, 6, (4, 11), 11)) == (5, 6, 6, 11)
    assert candidate((5, 12, 4, (6, 10), 7)) == (5, 12, 4, 7)
    assert candidate((7, 12, 14, (6, 10), 8)) == (7, 12, 14, 8)

if __name__ == '__main__':
    check(remove_nested)